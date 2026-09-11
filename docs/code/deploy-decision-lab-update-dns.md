# deploy/decision-lab-update-dns

Updates Duck DNS from the server’s outward-facing IPv4 address without embedding the token in the repository.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1 | Selects a POSIX shell interpreter when the installed script is executed directly. |
| 2 | Exits on an unhandled command failure or unset variable. |
| 4-9 | Calls Duck DNS over IPv4 with connection/total timeouts. token@ reads the token from its protected file; empty ip asks the service to detect the address. Captures the response without printing the credential. |
| 11-16 | Only literal OK counts as success. Other responses write a generic failure to stderr and return exit code 1 for systemd. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1 | Selects a POSIX shell interpreter when the installed script is executed directly. |
| 2 | 2 | Exits on an unhandled command failure or unset variable. |
| 3 | 3 | Blank separator; no execution. |
| 4 | 4-9 | Calls Duck DNS over IPv4 with connection/total timeouts. token@ reads the token from its protected file; empty ip asks the service to detect the address. Captures the response without printing the credential. |
| 5 | 4-9 | Calls Duck DNS over IPv4 with connection/total timeouts. token@ reads the token from its protected file; empty ip asks the service to detect the address. Captures the response without printing the credential. |
| 6 | 4-9 | Calls Duck DNS over IPv4 with connection/total timeouts. token@ reads the token from its protected file; empty ip asks the service to detect the address. Captures the response without printing the credential. |
| 7 | 4-9 | Calls Duck DNS over IPv4 with connection/total timeouts. token@ reads the token from its protected file; empty ip asks the service to detect the address. Captures the response without printing the credential. |
| 8 | 4-9 | Calls Duck DNS over IPv4 with connection/total timeouts. token@ reads the token from its protected file; empty ip asks the service to detect the address. Captures the response without printing the credential. |
| 9 | 4-9 | Calls Duck DNS over IPv4 with connection/total timeouts. token@ reads the token from its protected file; empty ip asks the service to detect the address. Captures the response without printing the credential. |
| 10 | 10 | Blank separator; no execution. |
| 11 | 11-16 | Only literal OK counts as success. Other responses write a generic failure to stderr and return exit code 1 for systemd. |
| 12 | 11-16 | Only literal OK counts as success. Other responses write a generic failure to stderr and return exit code 1 for systemd. |
| 13 | 11-16 | Only literal OK counts as success. Other responses write a generic failure to stderr and return exit code 1 for systemd. |
| 14 | 11-16 | Only literal OK counts as success. Other responses write a generic failure to stderr and return exit code 1 for systemd. |
| 15 | 11-16 | Only literal OK counts as success. Other responses write a generic failure to stderr and return exit code 1 for systemd. |
| 16 | 11-16 | Only literal OK counts as success. Other responses write a generic failure to stderr and return exit code 1 for systemd. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  #!/bin/sh
   2  set -eu
   3  
   4  result="$(curl -4 --fail --silent --show-error \
   5      --connect-timeout 10 --max-time 30 \
   6      --get 'https://www.duckdns.org/update' \
   7      --data-urlencode 'domains=function-optimization' \
   8      --data-urlencode 'token@/etc/decision-lab/duckdns-token' \
   9      --data-urlencode 'ip=')"
  10  
  11  if [ "$result" = "OK" ]; then
  12      echo "Duck DNS update succeeded."
  13  else
  14      echo "Duck DNS update failed." >&2
  15      exit 1
  16  fi
```
