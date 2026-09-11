# deploy/decision-lab-dns.service

Defines a one-shot system service for the installed DNS updater.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1-4 | Names the unit and requests ordering after network-online.target. This ordering does not guarantee external connectivity will succeed. |
| 6-8 | Runs the installed /usr/local/bin script once. No User is specified, so a system unit runs as root and can read the root-protected token. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1-4 | Names the unit and requests ordering after network-online.target. This ordering does not guarantee external connectivity will succeed. |
| 2 | 1-4 | Names the unit and requests ordering after network-online.target. This ordering does not guarantee external connectivity will succeed. |
| 3 | 1-4 | Names the unit and requests ordering after network-online.target. This ordering does not guarantee external connectivity will succeed. |
| 4 | 1-4 | Names the unit and requests ordering after network-online.target. This ordering does not guarantee external connectivity will succeed. |
| 5 | 5 | Blank separator; no execution. |
| 6 | 6-8 | Runs the installed /usr/local/bin script once. No User is specified, so a system unit runs as root and can read the root-protected token. |
| 7 | 6-8 | Runs the installed /usr/local/bin script once. No User is specified, so a system unit runs as root and can read the root-protected token. |
| 8 | 6-8 | Runs the installed /usr/local/bin script once. No User is specified, so a system unit runs as root and can read the root-protected token. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  [Unit]
   2  Description=Update Decision Lab Duck DNS address
   3  Wants=network-online.target
   4  After=network-online.target
   5  
   6  [Service]
   7  Type=oneshot
   8  ExecStart=/usr/local/bin/decision-lab-update-dns
```
