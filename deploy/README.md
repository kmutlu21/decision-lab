# AWS deployment

Live application: https://function-optimization.duckdns.org

## Architecture

An Ubuntu 24.04 EC2 instance runs:
- Caddy as a system service, providing HTTPS and forwarding requests to the API.
- A Docker Compose API container running FastAPI and PyTorch.
- A PostgreSQL container with a persistent Docker volume.
- A systemd timer that updates Duck DNS after boot and every five minutes.

The API binds to 127.0.0.1:8000. PostgreSQL has no published host port.
The EC2 security group permits public HTTP/HTTPS on ports 80/443.
SSH on port 22 is restricted to the administrator's IP address.

## Configuration files

- compose.yaml: application, database, mounts, and restart policies.
- deploy/Caddyfile: HTTPS hostname and reverse proxy.
- deploy/decision-lab-update-dns: Duck DNS update script.
- deploy/decision-lab-dns.service: one-shot update service.
- deploy/decision-lab-dns.timer: update schedule.

The DNS script must be installed at /usr/local/bin/decision-lab-update-dns
with executable permissions. The service and timer belong in
/etc/systemd/system/. The Caddyfile belongs in /etc/caddy/Caddyfile.

After installing or changing systemd files, run:
    sudo systemctl daemon-reload
    sudo systemctl enable --now decision-lab-dns.timer

Validate the Caddyfile before reloading Caddy.

## Private prerequisites

This repository alone does not contain the research data or trained models.
A deployment requires authorized copies of data/raw and the three model
artifacts checked by setup_docker.py.

Generate the server database password with setup_docker.py.
Keep .env private with mode 600.

Store the Duck DNS token separately at:
    /etc/decision-lab/duckdns-token

The token directory must be accessible only to root, and the token file
must have mode 600. Never commit credentials, private keys, raw research
data, or model artifacts.

The container runs as UID 10001. On this server, read access to the
mounted data and models was granted with:
    sudo setfacl -R -m u:10001:rX data/raw models

## Validation performed

- SQL inference verification passed for 36 prefixes across 12
  session/game combinations, with maximum prediction difference 0.
- The replay and predictions were checked through an SSH tunnel.
- Public HTTPS access worked.
- After an EC2 stop/start, both containers became healthy, Caddy was
  active, and the DNS updater successfully registered the new IP.
- The HTTPS health endpoint returned status ok and database connected.

These checks verify deployment and inference consistency. They do not
constitute a new evaluation of predictive accuracy or a load test.

## Pause and resume

To pause, select the instance in the AWS EC2 console and choose
Instance state > Stop instance. Do not terminate it.

Stopping EC2 makes the site unavailable. Retained storage continues
consuming credits; stopping is not a zero-storage-cost mode.

To resume, choose Instance state > Start instance.
Docker and Caddy start automatically. The DNS timer updates the
hostname to the new public IP. Allow several minutes for startup
and DNS caches to refresh.

The URL stays the same:
    https://function-optimization.duckdns.org

Avoid stopping or removing the containers before stopping EC2:
unless-stopped preserves a manually stopped container's state.
Never use docker compose down --volumes on this deployment;
that would remove its database volume.

## Troubleshooting

On the server:
    sudo docker compose ps
    sudo systemctl is-active caddy
    sudo journalctl -u decision-lab-dns.service -b --no-pager -n 20
    curl --fail http://127.0.0.1:8000/health

If SSH no longer connects after restarting EC2, use its current
public IPv4 address from the AWS console.
