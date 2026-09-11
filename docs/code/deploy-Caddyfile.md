# deploy/Caddyfile

Connects the public hostname to the API bound on the EC2 host.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1 | Configures the function-optimization.duckdns.org site. Host installation and DNS must already exist; this file alone does not launch Caddy. |
| 2 | Forwards incoming requests to the host's loopback API port 8000. The API container maps this port through Compose. |
| 3 | Closes the site block. The active copy is /etc/caddy/Caddyfile, not automatically this repository template. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1 | Configures the function-optimization.duckdns.org site. Host installation and DNS must already exist; this file alone does not launch Caddy. |
| 2 | 2 | Forwards incoming requests to the host's loopback API port 8000. The API container maps this port through Compose. |
| 3 | 3 | Closes the site block. The active copy is /etc/caddy/Caddyfile, not automatically this repository template. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  function-optimization.duckdns.org {
   2      reverse_proxy 127.0.0.1:8000
   3  }
```
