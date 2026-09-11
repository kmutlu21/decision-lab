# deploy/decision-lab-dns.timer

Schedules the one-shot DNS update at boot and periodically afterward.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1-2 | Describes the timer independently of the service it triggers. |
| 4-7 | Schedules an update 30 seconds after boot and then 5 minutes after the service's last activation. This is not a permanent IP reservation. |
| 9-10 | Allows systemctl enable to hook the timer into timers.target. Actual firing can be affected by normal systemd timing and network availability. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1-2 | Describes the timer independently of the service it triggers. |
| 2 | 1-2 | Describes the timer independently of the service it triggers. |
| 3 | 3 | Blank separator; no execution. |
| 4 | 4-7 | Schedules an update 30 seconds after boot and then 5 minutes after the service's last activation. This is not a permanent IP reservation. |
| 5 | 4-7 | Schedules an update 30 seconds after boot and then 5 minutes after the service's last activation. This is not a permanent IP reservation. |
| 6 | 4-7 | Schedules an update 30 seconds after boot and then 5 minutes after the service's last activation. This is not a permanent IP reservation. |
| 7 | 4-7 | Schedules an update 30 seconds after boot and then 5 minutes after the service's last activation. This is not a permanent IP reservation. |
| 8 | 8 | Blank separator; no execution. |
| 9 | 9-10 | Allows systemctl enable to hook the timer into timers.target. Actual firing can be affected by normal systemd timing and network availability. |
| 10 | 9-10 | Allows systemctl enable to hook the timer into timers.target. Actual firing can be affected by normal systemd timing and network availability. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  [Unit]
   2  Description=Update Decision Lab DNS after boot and periodically
   3  
   4  [Timer]
   5  OnBootSec=30s
   6  OnUnitActiveSec=5min
   7  Unit=decision-lab-dns.service
   8  
   9  [Install]
  10  WantedBy=timers.target
```
