# feature_math.py

Implements the fixed 14-column event representation shared by offline parity checking and live inference. No training or future targets are created here.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Symbols

| Symbol | Lines |
|---|---|
| `parse_opponent_timeline` | 12-29 |
| `compute_opp_best_at_time` | 32-43 |
| `build_sequences` | 47-258 |

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1-10 | Imports numerical tools, defines teammate visibility for games 2/4 and opponent visibility for games 3/4, and sets a 120-second normalization cap. |
| 12-24 | Parses a JSON opponent export or returns an empty timeline when JSON parsing fails. The prose claim about all malformed payloads is broader than the shape validation actually implemented. |
| 25-29 | Flattens opponent samples to timestamp and performance only, deliberately ignoring opponent x, then sorts timestamps. |
| 32-43 | Scans opponent scores through the supplied event time, starting best at zero and breaking at the first future entry. Earlier negative scores would not lower this initial best. |
| 47-56 | Groups events by session/game/round and reads that round's domain, objective maximum and sharing flags. |
| 57-65 | Groups by team and parses the first nonmissing opponent payload once for all focal players in the group. |
| 66-70 | Selects one focal player and builds its own event dictionaries ordered by own step. |
| 71-78 | Adds other same-group players as teammate events only when sharing is enabled. Despite an older comment, teammate samples do not enter own spread statistics. |
| 79-90 | Merges streams by timestamp and puts own events first on exact ties. The current condition accepts one own event; the old two-event comment describes training, not this runtime behavior. |
| 90-96 | Keeps current payoff/win as metadata only and fetches prior-round outcome inputs. At runtime the current outcome metadata is supplied as zero. |
| 98-102 | Sets the time origin to the EARLIEST MERGED own/teammate timestamp. round_start_ts is a misleading name: no actual round-start timestamp is read. |
| 104-115 | Initializes output lists, running best, 200-token own budget and own-only spread histories. |
| 117-133 | Initializes previous-event quantities and the own non-improvement counter. First-event deltas default to zero. |
| 135-138 | Processes events in order and normalizes x by domain width and y by the stored estimated objective maximum. |
| 139-143 | Reads the best BEFORE this event. If no best location exists, uses the current x as its initial reference. |
| 145-153 | Opponent gap is opponent best minus the updated visible best when context exists. It can be NEGATIVE when ahead; the comment claiming zero when leading is inaccurate. |
| 155-160 | Subtracts 10 tokens only for OWN events; teammate events cost the focal player nothing. Divides remaining own budget by 200. |
| 162-169 | Computes absolute x/y distance to the best AFTER including this event. Best position changes only for strict performance improvement. |
| 170-174 | Computes nonnegative improvement relative to the pre-event visible best. |
| 176-181 | Any improvement resets stagnation; an own non-improvement increments it. Each stagnant own sample contributes 10/200 = 0.05. |
| 183-185 | Clamps elapsed time divided by 120 into [0,1], using the earliest merged event origin, not actual remaining round time. |
| 187-194 | Updates population standard deviations using only focal-player x and y samples. Fewer than two own observations gives zero spread. |
| 196-205 | Computes seven changes relative to the immediately previous MERGED event, which may belong to a teammate. |
| 207-209 | Starts the fixed feature vector. Column order is part of the saved model contract and cannot be reordered without changing its meaning. |
| 210 | Column 0: change in normalized x since the previous merged event, zero at the first event. |
| 211 | Column 1: change in normalized observed performance since the previous merged event. |
| 212 | Column 2: own-event flag, 1 for the focal player and 0 for teammate; also used by verifiers to identify eligible output steps. |
| 213 | Column 3: fraction of the focal player's 200-token budget remaining after this event. |
| 214 | Column 4: change in opponent gap, not the absolute opponent gap. |
| 215 | Column 5: change in x distance from the updated visible best location. |
| 216 | Column 6: change in performance distance from the updated visible best value. |
| 217 | Column 7: nonnegative improvement over the preceding visible best. |
| 218 | Column 8: change in own x population standard deviation. |
| 219 | Column 9: change in own normalized-performance population standard deviation. |
| 220 | Column 10: own non-improvement count scaled by 10/200. |
| 221 | Column 11: elapsed fraction since the earliest merged event, capped at 120 seconds. |
| 222 | Column 12: previous available round's win flag, constant over this sequence. |
| 223 | Column 13: previous available round's recorded payoff divided by 200, also constant. |
| 224 | Closes the appended 14-column feature row. |
| 226-230 | Stores absolute normalized current x/y separately so inference can turn delta-head outputs into absolute predictions. |
| 232-239 | Advances all previous-event state for the next merged event, including teammate events. |
| 241-243 | Updates raw running-best state only after calculations needing the previous best are complete. |
| 245-253 | Builds metadata including focal/team/opponent identity and priors. A teammate ID of -1 means no teammate event was available in this sequence. |
| 254-258 | Converts features/current coordinates to float32 arrays and returns the list of focal-player sequences. No labels or fold allocation are calculated. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1-10 | Imports numerical tools, defines teammate visibility for games 2/4 and opponent visibility for games 3/4, and sets a 120-second normalization cap. |
| 2 | 1-10 | Imports numerical tools, defines teammate visibility for games 2/4 and opponent visibility for games 3/4, and sets a 120-second normalization cap. |
| 3 | 1-10 | Imports numerical tools, defines teammate visibility for games 2/4 and opponent visibility for games 3/4, and sets a 120-second normalization cap. |
| 4 | 1-10 | Imports numerical tools, defines teammate visibility for games 2/4 and opponent visibility for games 3/4, and sets a 120-second normalization cap. |
| 5 | 1-10 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 6 | 1-10 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 7 | 1-10 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 8 | 1-10 | Blank separator; no execution. |
| 9 | 1-10 | Imports numerical tools, defines teammate visibility for games 2/4 and opponent visibility for games 3/4, and sets a 120-second normalization cap. |
| 10 | 1-10 | Imports numerical tools, defines teammate visibility for games 2/4 and opponent visibility for games 3/4, and sets a 120-second normalization cap. |
| 11 | 11 | Blank separator; no execution. |
| 12 | 12-24 | Function declaration: this body runs when called, not at declaration time. |
| 13 | 12-24 | Parses a JSON opponent export or returns an empty timeline when JSON parsing fails. The prose claim about all malformed payloads is broader than the shape validation actually implemented. |
| 14 | 12-24 | Parses a JSON opponent export or returns an empty timeline when JSON parsing fails. The prose claim about all malformed payloads is broader than the shape validation actually implemented. |
| 15 | 12-24 | Parses a JSON opponent export or returns an empty timeline when JSON parsing fails. The prose claim about all malformed payloads is broader than the shape validation actually implemented. |
| 16 | 12-24 | Parses a JSON opponent export or returns an empty timeline when JSON parsing fails. The prose claim about all malformed payloads is broader than the shape validation actually implemented. |
| 17 | 12-24 | Parses a JSON opponent export or returns an empty timeline when JSON parsing fails. The prose claim about all malformed payloads is broader than the shape validation actually implemented. |
| 18 | 12-24 | Blank separator; no execution. |
| 19 | 12-24 | Parses a JSON opponent export or returns an empty timeline when JSON parsing fails. The prose claim about all malformed payloads is broader than the shape validation actually implemented. |
| 20 | 12-24 | Parses a JSON opponent export or returns an empty timeline when JSON parsing fails. The prose claim about all malformed payloads is broader than the shape validation actually implemented. |
| 21 | 12-24 | Parses a JSON opponent export or returns an empty timeline when JSON parsing fails. The prose claim about all malformed payloads is broader than the shape validation actually implemented. |
| 22 | 12-24 | Conditional branch: determines which following statements run. |
| 23 | 12-24 | Exception-control block: separates normal work, error handling and cleanup. |
| 24 | 12-24 | Exception-control block: separates normal work, error handling and cleanup. |
| 25 | 25-29 | Flattens opponent samples to timestamp and performance only, deliberately ignoring opponent x, then sorts timestamps. |
| 26 | 25-29 | Loop: repeats the following operations for the stated elements/condition. |
| 27 | 25-29 | Loop: repeats the following operations for the stated elements/condition. |
| 28 | 25-29 | Flattens opponent samples to timestamp and performance only, deliberately ignoring opponent x, then sorts timestamps. |
| 29 | 25-29 | Return: sends this result to the caller and ends this invocation. |
| 30 | 30 | Blank separator; no execution. |
| 31 | 31 | Blank separator; no execution. |
| 32 | 32-43 | Function declaration: this body runs when called, not at declaration time. |
| 33 | 32-43 | Scans opponent scores through the supplied event time, starting best at zero and breaking at the first future entry. Earlier negative scores would not lower this initial best. |
| 34 | 32-43 | Scans opponent scores through the supplied event time, starting best at zero and breaking at the first future entry. Earlier negative scores would not lower this initial best. |
| 35 | 32-43 | Scans opponent scores through the supplied event time, starting best at zero and breaking at the first future entry. Earlier negative scores would not lower this initial best. |
| 36 | 32-43 | Scans opponent scores through the supplied event time, starting best at zero and breaking at the first future entry. Earlier negative scores would not lower this initial best. |
| 37 | 32-43 | Scans opponent scores through the supplied event time, starting best at zero and breaking at the first future entry. Earlier negative scores would not lower this initial best. |
| 38 | 32-43 | Scans opponent scores through the supplied event time, starting best at zero and breaking at the first future entry. Earlier negative scores would not lower this initial best. |
| 39 | 32-43 | Scans opponent scores through the supplied event time, starting best at zero and breaking at the first future entry. Earlier negative scores would not lower this initial best. |
| 40 | 32-43 | Loop: repeats the following operations for the stated elements/condition. |
| 41 | 32-43 | Conditional branch: determines which following statements run. |
| 42 | 32-43 | Conditional branch: determines which following statements run. |
| 43 | 32-43 | Return: sends this result to the caller and ends this invocation. |
| 44 | 44 | Blank separator; no execution. |
| 45 | 45 | Blank separator; no execution. |
| 46 | 46 | Blank separator; no execution. |
| 47 | 47-56 | Function declaration: this body runs when called, not at declaration time. |
| 48 | 47-56 | Groups events by session/game/round and reads that round's domain, objective maximum and sharing flags. |
| 49 | 47-56 | Loop: repeats the following operations for the stated elements/condition. |
| 50 | 47-56 | Groups events by session/game/round and reads that round's domain, objective maximum and sharing flags. |
| 51 | 47-56 | Groups events by session/game/round and reads that round's domain, objective maximum and sharing flags. |
| 52 | 47-56 | Groups events by session/game/round and reads that round's domain, objective maximum and sharing flags. |
| 53 | 47-56 | Groups events by session/game/round and reads that round's domain, objective maximum and sharing flags. |
| 54 | 47-56 | Groups events by session/game/round and reads that round's domain, objective maximum and sharing flags. |
| 55 | 47-56 | Groups events by session/game/round and reads that round's domain, objective maximum and sharing flags. |
| 56 | 47-56 | Groups events by session/game/round and reads that round's domain, objective maximum and sharing flags. |
| 57 | 57-65 | Loop: repeats the following operations for the stated elements/condition. |
| 58 | 57-65 | Groups by team and parses the first nonmissing opponent payload once for all focal players in the group. |
| 59 | 57-65 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 60 | 57-65 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 61 | 57-65 | Groups by team and parses the first nonmissing opponent payload once for all focal players in the group. |
| 62 | 57-65 | Conditional branch: determines which following statements run. |
| 63 | 57-65 | Groups by team and parses the first nonmissing opponent payload once for all focal players in the group. |
| 64 | 57-65 | Conditional branch: determines which following statements run. |
| 65 | 57-65 | Groups by team and parses the first nonmissing opponent payload once for all focal players in the group. |
| 66 | 66-70 | Loop: repeats the following operations for the stated elements/condition. |
| 67 | 66-70 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 68 | 66-70 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 69 | 66-70 | Selects one focal player and builds its own event dictionaries ordered by own step. |
| 70 | 66-70 | Selects one focal player and builds its own event dictionaries ordered by own step. |
| 71 | 71-78 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 72 | 71-78 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 73 | 71-78 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 74 | 71-78 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 75 | 71-78 | Adds other same-group players as teammate events only when sharing is enabled. Despite an older comment, teammate samples do not enter own spread statistics. |
| 76 | 71-78 | Conditional branch: determines which following statements run. |
| 77 | 71-78 | Adds other same-group players as teammate events only when sharing is enabled. Despite an older comment, teammate samples do not enter own spread statistics. |
| 78 | 71-78 | Adds other same-group players as teammate events only when sharing is enabled. Despite an older comment, teammate samples do not enter own spread statistics. |
| 79 | 79-90 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 80 | 79-90 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 81 | 79-90 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 82 | 79-90 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 83 | 79-90 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 84 | 79-90 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 85 | 79-90 | Merges streams by timestamp and puts own events first on exact ties. The current condition accepts one own event; the old two-event comment describes training, not this runtime behavior. |
| 86 | 79-90 | Merges streams by timestamp and puts own events first on exact ties. The current condition accepts one own event; the old two-event comment describes training, not this runtime behavior. |
| 87 | 79-90 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 88 | 79-90 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 89 | 79-90 | Conditional branch: determines which following statements run. |
| 90 | 90-96 | Keeps current payoff/win as metadata only and fetches prior-round outcome inputs. At runtime the current outcome metadata is supplied as zero. |
| 91 | 90-96 | Keeps current payoff/win as metadata only and fetches prior-round outcome inputs. At runtime the current outcome metadata is supplied as zero. |
| 92 | 90-96 | Blank separator; no execution. |
| 93 | 90-96 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 94 | 90-96 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 95 | 90-96 | Keeps current payoff/win as metadata only and fetches prior-round outcome inputs. At runtime the current outcome metadata is supplied as zero. |
| 96 | 90-96 | Keeps current payoff/win as metadata only and fetches prior-round outcome inputs. At runtime the current outcome metadata is supplied as zero. |
| 97 | 97 | Blank separator; no execution. |
| 98 | 98-102 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 99 | 98-102 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 100 | 98-102 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 101 | 98-102 | Sets the time origin to the EARLIEST MERGED own/teammate timestamp. round_start_ts is a misleading name: no actual round-start timestamp is read. |
| 102 | 98-102 | Sets the time origin to the EARLIEST MERGED own/teammate timestamp. round_start_ts is a misleading name: no actual round-start timestamp is read. |
| 103 | 103 | Blank separator; no execution. |
| 104 | 104-115 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 105 | 104-115 | Initializes output lists, running best, 200-token own budget and own-only spread histories. |
| 106 | 104-115 | Initializes output lists, running best, 200-token own budget and own-only spread histories. |
| 107 | 104-115 | Initializes output lists, running best, 200-token own budget and own-only spread histories. |
| 108 | 104-115 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 109 | 104-115 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 110 | 104-115 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 111 | 104-115 | Initializes output lists, running best, 200-token own budget and own-only spread histories. |
| 112 | 104-115 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 113 | 104-115 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 114 | 104-115 | Initializes output lists, running best, 200-token own budget and own-only spread histories. |
| 115 | 104-115 | Initializes output lists, running best, 200-token own budget and own-only spread histories. |
| 116 | 116 | Blank separator; no execution. |
| 117 | 117-133 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 118 | 117-133 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 119 | 117-133 | Initializes previous-event quantities and the own non-improvement counter. First-event deltas default to zero. |
| 120 | 117-133 | Initializes previous-event quantities and the own non-improvement counter. First-event deltas default to zero. |
| 121 | 117-133 | Initializes previous-event quantities and the own non-improvement counter. First-event deltas default to zero. |
| 122 | 117-133 | Initializes previous-event quantities and the own non-improvement counter. First-event deltas default to zero. |
| 123 | 117-133 | Initializes previous-event quantities and the own non-improvement counter. First-event deltas default to zero. |
| 124 | 117-133 | Initializes previous-event quantities and the own non-improvement counter. First-event deltas default to zero. |
| 125 | 117-133 | Initializes previous-event quantities and the own non-improvement counter. First-event deltas default to zero. |
| 126 | 117-133 | Blank separator; no execution. |
| 127 | 117-133 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 128 | 117-133 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 129 | 117-133 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 130 | 117-133 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 131 | 117-133 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 132 | 117-133 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 133 | 117-133 | Initializes previous-event quantities and the own non-improvement counter. First-event deltas default to zero. |
| 134 | 134 | Blank separator; no execution. |
| 135 | 135-138 | Loop: repeats the following operations for the stated elements/condition. |
| 136 | 135-138 | Processes events in order and normalizes x by domain width and y by the stored estimated objective maximum. |
| 137 | 135-138 | Processes events in order and normalizes x by domain width and y by the stored estimated objective maximum. |
| 138 | 135-138 | Processes events in order and normalizes x by domain width and y by the stored estimated objective maximum. |
| 139 | 139-143 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 140 | 139-143 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 141 | 139-143 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 142 | 139-143 | Reads the best BEFORE this event. If no best location exists, uses the current x as its initial reference. |
| 143 | 139-143 | Reads the best BEFORE this event. If no best location exists, uses the current x as its initial reference. |
| 144 | 144 | Blank separator; no execution. |
| 145 | 145-153 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 146 | 145-153 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 147 | 145-153 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 148 | 145-153 | Conditional branch: determines which following statements run. |
| 149 | 145-153 | Opponent gap is opponent best minus the updated visible best when context exists. It can be NEGATIVE when ahead; the comment claiming zero when leading is inaccurate. |
| 150 | 145-153 | Opponent gap is opponent best minus the updated visible best when context exists. It can be NEGATIVE when ahead; the comment claiming zero when leading is inaccurate. |
| 151 | 145-153 | Opponent gap is opponent best minus the updated visible best when context exists. It can be NEGATIVE when ahead; the comment claiming zero when leading is inaccurate. |
| 152 | 145-153 | Conditional branch: determines which following statements run. |
| 153 | 145-153 | Opponent gap is opponent best minus the updated visible best when context exists. It can be NEGATIVE when ahead; the comment claiming zero when leading is inaccurate. |
| 154 | 154 | Blank separator; no execution. |
| 155 | 155-160 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 156 | 155-160 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 157 | 155-160 | Conditional branch: determines which following statements run. |
| 158 | 155-160 | Subtracts 10 tokens only for OWN events; teammate events cost the focal player nothing. Divides remaining own budget by 200. |
| 159 | 155-160 | Subtracts 10 tokens only for OWN events; teammate events cost the focal player nothing. Divides remaining own budget by 200. |
| 160 | 155-160 | Subtracts 10 tokens only for OWN events; teammate events cost the focal player nothing. Divides remaining own budget by 200. |
| 161 | 161 | Blank separator; no execution. |
| 162 | 162-169 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 163 | 162-169 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 164 | 162-169 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 165 | 162-169 | Computes absolute x/y distance to the best AFTER including this event. Best position changes only for strict performance improvement. |
| 166 | 162-169 | Computes absolute x/y distance to the best AFTER including this event. Best position changes only for strict performance improvement. |
| 167 | 162-169 | Blank separator; no execution. |
| 168 | 162-169 | Computes absolute x/y distance to the best AFTER including this event. Best position changes only for strict performance improvement. |
| 169 | 162-169 | Computes absolute x/y distance to the best AFTER including this event. Best position changes only for strict performance improvement. |
| 170 | 170-174 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 171 | 170-174 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 172 | 170-174 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 173 | 170-174 | Computes nonnegative improvement relative to the pre-event visible best. |
| 174 | 170-174 | Computes nonnegative improvement relative to the pre-event visible best. |
| 175 | 175 | Blank separator; no execution. |
| 176 | 176-181 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 177 | 176-181 | Conditional branch: determines which following statements run. |
| 178 | 176-181 | Any improvement resets stagnation; an own non-improvement increments it. Each stagnant own sample contributes 10/200 = 0.05. |
| 179 | 176-181 | Conditional branch: determines which following statements run. |
| 180 | 176-181 | Any improvement resets stagnation; an own non-improvement increments it. Each stagnant own sample contributes 10/200 = 0.05. |
| 181 | 176-181 | Any improvement resets stagnation; an own non-improvement increments it. Each stagnant own sample contributes 10/200 = 0.05. |
| 182 | 182 | Blank separator; no execution. |
| 183 | 183-185 | Clamps elapsed time divided by 120 into [0,1], using the earliest merged event origin, not actual remaining round time. |
| 184 | 183-185 | Clamps elapsed time divided by 120 into [0,1], using the earliest merged event origin, not actual remaining round time. |
| 185 | 183-185 | Clamps elapsed time divided by 120 into [0,1], using the earliest merged event origin, not actual remaining round time. |
| 186 | 186 | Blank separator; no execution. |
| 187 | 187-194 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 188 | 187-194 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 189 | 187-194 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 190 | 187-194 | Conditional branch: determines which following statements run. |
| 191 | 187-194 | Updates population standard deviations using only focal-player x and y samples. Fewer than two own observations gives zero spread. |
| 192 | 187-194 | Updates population standard deviations using only focal-player x and y samples. Fewer than two own observations gives zero spread. |
| 193 | 187-194 | Updates population standard deviations using only focal-player x and y samples. Fewer than two own observations gives zero spread. |
| 194 | 187-194 | Updates population standard deviations using only focal-player x and y samples. Fewer than two own observations gives zero spread. |
| 195 | 195 | Blank separator; no execution. |
| 196 | 196-205 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 197 | 196-205 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 198 | 196-205 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 199 | 196-205 | Computes seven changes relative to the immediately previous MERGED event, which may belong to a teammate. |
| 200 | 196-205 | Computes seven changes relative to the immediately previous MERGED event, which may belong to a teammate. |
| 201 | 196-205 | Computes seven changes relative to the immediately previous MERGED event, which may belong to a teammate. |
| 202 | 196-205 | Computes seven changes relative to the immediately previous MERGED event, which may belong to a teammate. |
| 203 | 196-205 | Computes seven changes relative to the immediately previous MERGED event, which may belong to a teammate. |
| 204 | 196-205 | Computes seven changes relative to the immediately previous MERGED event, which may belong to a teammate. |
| 205 | 196-205 | Computes seven changes relative to the immediately previous MERGED event, which may belong to a teammate. |
| 206 | 206 | Blank separator; no execution. |
| 207 | 207-209 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 208 | 207-209 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 209 | 207-209 | Starts the fixed feature vector. Column order is part of the saved model contract and cannot be reordered without changing its meaning. |
| 210 | 210 | Column 0: change in normalized x since the previous merged event, zero at the first event. |
| 211 | 211 | Column 1: change in normalized observed performance since the previous merged event. |
| 212 | 212 | Column 2: own-event flag, 1 for the focal player and 0 for teammate; also used by verifiers to identify eligible output steps. |
| 213 | 213 | Column 3: fraction of the focal player's 200-token budget remaining after this event. |
| 214 | 214 | Column 4: change in opponent gap, not the absolute opponent gap. |
| 215 | 215 | Column 5: change in x distance from the updated visible best location. |
| 216 | 216 | Column 6: change in performance distance from the updated visible best value. |
| 217 | 217 | Column 7: nonnegative improvement over the preceding visible best. |
| 218 | 218 | Column 8: change in own x population standard deviation. |
| 219 | 219 | Column 9: change in own normalized-performance population standard deviation. |
| 220 | 220 | Column 10: own non-improvement count scaled by 10/200. |
| 221 | 221 | Column 11: elapsed fraction since the earliest merged event, capped at 120 seconds. |
| 222 | 222 | Column 12: previous available round's win flag, constant over this sequence. |
| 223 | 223 | Column 13: previous available round's recorded payoff divided by 200, also constant. |
| 224 | 224 | Closes the appended 14-column feature row. |
| 225 | 225 | Blank separator; no execution. |
| 226 | 226-230 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 227 | 226-230 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 228 | 226-230 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 229 | 226-230 | Stores absolute normalized current x/y separately so inference can turn delta-head outputs into absolute predictions. |
| 230 | 226-230 | Stores absolute normalized current x/y separately so inference can turn delta-head outputs into absolute predictions. |
| 231 | 231 | Blank separator; no execution. |
| 232 | 232-239 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 233 | 232-239 | Advances all previous-event state for the next merged event, including teammate events. |
| 234 | 232-239 | Advances all previous-event state for the next merged event, including teammate events. |
| 235 | 232-239 | Advances all previous-event state for the next merged event, including teammate events. |
| 236 | 232-239 | Advances all previous-event state for the next merged event, including teammate events. |
| 237 | 232-239 | Advances all previous-event state for the next merged event, including teammate events. |
| 238 | 232-239 | Advances all previous-event state for the next merged event, including teammate events. |
| 239 | 232-239 | Advances all previous-event state for the next merged event, including teammate events. |
| 240 | 240 | Blank separator; no execution. |
| 241 | 241-243 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 242 | 241-243 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 243 | 241-243 | Conditional branch: determines which following statements run. |
| 244 | 244 | Blank separator; no execution. |
| 245 | 245-253 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 246 | 245-253 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 247 | 245-253 | Builds metadata including focal/team/opponent identity and priors. A teammate ID of -1 means no teammate event was available in this sequence. |
| 248 | 245-253 | Builds metadata including focal/team/opponent identity and priors. A teammate ID of -1 means no teammate event was available in this sequence. |
| 249 | 245-253 | Builds metadata including focal/team/opponent identity and priors. A teammate ID of -1 means no teammate event was available in this sequence. |
| 250 | 245-253 | Builds metadata including focal/team/opponent identity and priors. A teammate ID of -1 means no teammate event was available in this sequence. |
| 251 | 245-253 | Builds metadata including focal/team/opponent identity and priors. A teammate ID of -1 means no teammate event was available in this sequence. |
| 252 | 245-253 | Builds metadata including focal/team/opponent identity and priors. A teammate ID of -1 means no teammate event was available in this sequence. |
| 253 | 245-253 | Builds metadata including focal/team/opponent identity and priors. A teammate ID of -1 means no teammate event was available in this sequence. |
| 254 | 254-258 | Converts features/current coordinates to float32 arrays and returns the list of focal-player sequences. No labels or fold allocation are calculated. |
| 255 | 254-258 | Converts features/current coordinates to float32 arrays and returns the list of focal-player sequences. No labels or fold allocation are calculated. |
| 256 | 254-258 | Converts features/current coordinates to float32 arrays and returns the list of focal-player sequences. No labels or fold allocation are calculated. |
| 257 | 254-258 | Converts features/current coordinates to float32 arrays and returns the list of focal-player sequences. No labels or fold allocation are calculated. |
| 258 | 254-258 | Return: sends this result to the caller and ends this invocation. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  """Feature calculation extracted from the original default preprocessing.
   2  The feature builder consumes event rows, an objective maximum and prior outcomes.
   3  It does not load pickles, train models, or calculate future targets.
   4  """
   5  import json
   6  import numpy as np
   7  import pandas as pd
   8  
   9  GAMES={g:{'has_teammate':g in (2,4),'has_opponent':g in (3,4)} for g in range(1,5)}
  10  TIME_CAP_S=120.0
  11  
  12  def parse_opponent_timeline(opp_results_json):
  13      """
  14      Decode the opponent group's results_data JSON (stored as a string of
  15      {pid: [[fx, x, ts], ...]}) into a flat (timestamp, fx_raw) list sorted
  16      in time order. Used downstream to compute the opponent's running-best
  17      curve at any query timestamp via compute_opp_best_at_time.
  18  
  19      Returns [] for missing or malformed payloads — callers check len() to
  20      decide whether comp_gap should default to 0.
  21      """
  22      if opp_results_json is None: return []
  23      try: rd = json.loads(opp_results_json)
  24      except: return []
  25      opp = []
  26      for pid_str, samples in rd.items():
  27          for s in samples: opp.append((s[2], float(s[0])))
  28      opp.sort(key=lambda x: x[0])
  29      return opp
  30  
  31  
  32  def compute_opp_best_at_time(opp_timeline, timestamp):
  33      """
  34      Linear scan to find the opponent's RUNNING-BEST fx as of `timestamp`.
  35      The timeline is presorted, so we can break out as soon as t > timestamp.
  36      Returns 0.0 if no opponent samples were observed by then (matches the
  37      way comp_gap is defined: opponent best is monotone-nondecreasing from 0).
  38      """
  39      best = 0.0
  40      for t, fx in opp_timeline:
  41          if t <= timestamp: best = max(best, fx)
  42          else: break
  43      return best
  44  
  45  
  46  
  47  def build_sequences(raw_df, true_max_lookup, prior_outcome):
  48      sequences=[]
  49      for (session,game_num,rnd), round_df in raw_df.groupby(['session','game_num','round']):
  50          game_cfg = GAMES[game_num]
  51          x_min_val = round_df['x_domain_min'].iloc[0]
  52          x_max_val = round_df['x_domain_max'].iloc[0]
  53          domain_width = x_max_val - x_min_val
  54          true_max = true_max_lookup[(session,game_num,rnd)]
  55          has_teammate = game_cfg['has_teammate']
  56          has_opponent = game_cfg['has_opponent']
  57          for gid, group_df in round_df.groupby('record_group_id'):
  58              players = sorted(group_df['participant_id'].unique())
  59              # Parse opponent timeline ONCE per group; reused across both focal
  60              # players in the group (in team games) since they share an opponent.
  61              opp_timeline = []
  62              if has_opponent:
  63                  opp_rd_row = group_df.dropna(subset=['opp_results_data'])
  64                  if len(opp_rd_row) > 0:
  65                      opp_timeline = parse_opponent_timeline(opp_rd_row.iloc[0]['opp_results_data'])
  66              for target_pid in players:
  67                  # Focal player's own samples (is_own=1) — these are the ones
  68                  # whose deltas the network will be trained to predict.
  69                  target_df = group_df[group_df['participant_id']==target_pid].sort_values('step')
  70                  target_samples = [{'x':float(r['x']),'fx':float(r['fx']),'timestamp':r['timestamp'],'is_own':1,'pid':target_pid} for _,r in target_df.iterrows()]
  71                  # Teammate's samples (is_own=0) only exist in G2/G4. The teammate
  72                  # influences the focal player's running-best and spread-of-own
  73                  # diagnostics, but the focal player's *targets* are computed
  74                  # only against their own next event.
  75                  mate_samples = []
  76                  if has_teammate:
  77                      mate_df = group_df[group_df['participant_id']!=target_pid].sort_values('step')
  78                      mate_samples = [{'x':float(r['x']),'fx':float(r['fx']),'timestamp':r['timestamp'],'is_own':0,'pid':int(r['participant_id'])} for _,r in mate_df.iterrows()]
  79                  # Merge the two streams and sort by timestamp. The (timestamp,
  80                  # -is_own) tie-break ensures that when an own and teammate event
  81                  # share a timestamp, the OWN event comes FIRST. This convention
  82                  # is mirrored exactly in deploy_success_model.py and the rollout
  83                  # simulators; if the order ever flips, deltas computed at tied
  84                  # timestamps will silently disagree across pipelines.
  85                  all_samples = target_samples + mate_samples
  86                  all_samples.sort(key=lambda s: (s['timestamp'], -s['is_own']))
  87                  # Need at least 2 own events to form a Δfx target between
  88                  # consecutive own samples (i.e. one event with a "next own").
  89                  if not target_samples: continue
  90                  payoff = target_df['payoff'].iloc[0]
  91                  is_win = target_df['is_win'].iloc[0]
  92      
  93                  # Pull this round's prior outcome for this participant. (0, 0)
  94                  # for round 1; the previous round's (is_win, payoff/200) otherwise.
  95                  prior_won, prior_payoff_frac = prior_outcome.get(
  96                      (session, game_num, rnd, int(target_pid)), (0.0, 0.0))
  97      
  98                  # round_start_ts is the timestamp of the FIRST event in the
  99                  # round — used to derive elapsed_s and time_frac. We take the
 100                  # earliest across all events in all_samples (own + teammate).
 101                  all_ts = [pd.to_datetime(s['timestamp']) for s in all_samples]
 102                  round_start_ts = min(all_ts)
 103      
 104                  # Per-sequence accumulators.
 105                  features = []
 106                  current_x_norms = []
 107                  current_fx_norms = []
 108                  # Running-best in raw units (best_y) and its x location (best_x);
 109                  # target_step_count tracks own samples only (for budget_frac);
 110                  # target_budget is the unspent token count.
 111                  best_y, best_x, target_step_count, target_budget = 0.0, None, 0, 200
 112                  # Spreads use only OWN samples; teammate samples don't enter the
 113                  # focal player's "exploration variance" estimate.
 114                  own_x_values = []
 115                  own_fx_values = []
 116      
 117                  # Previous-event scalars used for delta features. We initialize
 118                  # to None / 0 so the very first event's deltas are 0.
 119                  prev_x_norm = None
 120                  prev_fx_norm = None
 121                  prev_comp_gap = 0.0
 122                  prev_x_spread = 0.0
 123                  prev_y_spread = 0.0
 124                  prev_distance_to_best_x = 0.0
 125                  prev_distance_to_best_y = 0.0
 126      
 127                  # stagnation_steps counts the number of consecutive OWN events
 128                  # without improvement; it advances ONLY on own no-improvement
 129                  # events and resets to 0 whenever ANY event sets a new running
 130                  # best (own or teammate). It is then converted to fractional
 131                  # tokens (× 10 / 200) so that 0.05 means "the player has spent
 132                  # one own sample's worth of budget without improving".
 133                  stagnation_steps = 0
 134      
 135                  for i, sample in enumerate(all_samples):
 136                      x_raw, fx_raw = sample['x'], sample['fx']
 137                      x_norm = (x_raw - x_min_val) / domain_width
 138                      fx_norm = fx_raw / true_max
 139                      # best_y_norm / best_x_norm reflect the running-best BEFORE
 140                      # this event lands. Used to compute improvement and the
 141                      # opponent gap; we update them after the feature row is built.
 142                      best_y_norm = best_y/true_max if best_y>0 else 0.0
 143                      best_x_norm = (best_x-x_min_val)/domain_width if best_x is not None else x_norm
 144      
 145                      # comp_gap: how far ahead the opponent is at this event time,
 146                      # normalized to f*. Positive when the opponent is ahead, zero
 147                      # if we lead and we don't have visibility.
 148                      if has_opponent and opp_timeline:
 149                          opp_best = compute_opp_best_at_time(opp_timeline, sample['timestamp'])
 150                          opp_best_y_norm = opp_best/true_max
 151                          comp_gap = opp_best_y_norm - max(best_y_norm, fx_norm)
 152                      else:
 153                          comp_gap = 0.0
 154      
 155                      # Budget advances on OWN events only (teammate samples are
 156                      # paid by the teammate's budget, not the focal player's).
 157                      if sample['is_own']==1:
 158                          target_step_count += 1
 159                          target_budget = 200 - target_step_count*10
 160                      budget_frac = target_budget/200
 161      
 162                      # Distance-to-best is computed against the AFTER-this-event
 163                      # running best so it captures the move toward/away from the
 164                      # current peak (including this very sample).
 165                      updated_best_y_norm = max(best_y_norm, fx_norm)
 166                      updated_best_x_norm = x_norm if fx_raw>best_y else best_x_norm
 167      
 168                      distance_to_best_x = abs(x_norm - updated_best_x_norm)
 169                      distance_to_best_y = abs(fx_norm - updated_best_y_norm)
 170                      # Improvement is computed against the BEFORE-event best so
 171                      # that a sample which sets a new best fires a positive value;
 172                      # otherwise it is exactly 0. (Strictly nonneg by max(0, ·).)
 173                      prev_best_y_norm = best_y_norm
 174                      improvement = max(0.0, fx_norm - prev_best_y_norm)
 175      
 176                      # Stagnation counter logic — see big comment above the loop.
 177                      if improvement > 0:
 178                          stagnation_steps = 0
 179                      elif sample['is_own'] == 1:
 180                          stagnation_steps += 1
 181                      stagnation_frac = stagnation_steps * 10 / 200
 182      
 183                      ts = pd.to_datetime(sample['timestamp'])
 184                      elapsed_s = (ts - round_start_ts).total_seconds()
 185                      time_frac = min(max(elapsed_s / TIME_CAP_S, 0.0), 1.0)
 186      
 187                      # Spreads use only own samples and require >= 2 events to
 188                      # be defined; std() of a single value is 0 anyway, but we
 189                      # gate explicitly to keep the contract crisp.
 190                      if sample['is_own'] == 1:
 191                          own_x_values.append(x_norm)
 192                          own_fx_values.append(fx_norm)
 193                      x_spread = float(np.std(own_x_values)) if len(own_x_values) >= 2 else 0.0
 194                      y_spread = float(np.std(own_fx_values)) if len(own_fx_values) >= 2 else 0.0
 195      
 196                      # All seven delta features below are PER-EVENT deltas (i.e.
 197                      # they compare against the previous event in the merged
 198                      # stream, not the previous own event).
 199                      delta_x = (x_norm - prev_x_norm) if prev_x_norm is not None else 0.0
 200                      delta_fx = (fx_norm - prev_fx_norm) if prev_fx_norm is not None else 0.0
 201                      delta_comp_gap = comp_gap - prev_comp_gap
 202                      delta_distance_to_best_x = distance_to_best_x - prev_distance_to_best_x
 203                      delta_distance_to_best_y = distance_to_best_y - prev_distance_to_best_y
 204                      delta_spread_x = x_spread - prev_x_spread
 205                      delta_spread_y = y_spread - prev_y_spread
 206      
 207                      # 14-feature row, ORDER MUST MATCH downstream model and
 208                      # deploy/rollout mirrors. See top-of-file FEATURE ORDERING.
 209                      features.append([
 210                          delta_x,                    # 0
 211                          delta_fx,                   # 1
 212                          sample['is_own'],           # 2
 213                          budget_frac,                # 3
 214                          delta_comp_gap,             # 4
 215                          delta_distance_to_best_x,   # 5
 216                          delta_distance_to_best_y,   # 6
 217                          improvement,                # 7
 218                          delta_spread_x,             # 8
 219                          delta_spread_y,             # 9
 220                          stagnation_frac,            # 10
 221                          time_frac,                  # 11
 222                          prior_won,                  # 12  NEW (constant within round)
 223                          prior_payoff_frac,          # 13  NEW (constant within round)
 224                      ])
 225      
 226                      # Snapshot absolute coords at every event. Downstream
 227                      # (model_delta_default.py) adds dx_pred to current_x_norms[t]
 228                      # to recover absolute predictions for paper figures.
 229                      current_x_norms.append(x_norm)
 230                      current_fx_norms.append(fx_norm)
 231      
 232                      # Roll the previous-event scalars forward.
 233                      prev_x_norm = x_norm
 234                      prev_fx_norm = fx_norm
 235                      prev_comp_gap = comp_gap
 236                      prev_distance_to_best_x = distance_to_best_x
 237                      prev_distance_to_best_y = distance_to_best_y
 238                      prev_x_spread = x_spread
 239                      prev_y_spread = y_spread
 240      
 241                      # Update the running-best AFTER all features that depend on
 242                      # the pre-event best have been computed.
 243                      if fx_raw>best_y: best_y=fx_raw; best_x=x_raw
 244      
 245                  # Teammate id (only meaningful in G2/G4); -1 elsewhere. Useful
 246                  # downstream for fold construction and for joining back to logs.
 247                  mate_pid = mate_samples[0]['pid'] if has_teammate and mate_samples else -1
 248                  sequences.append({
 249                      'meta': {'session':session,'game_num':game_num,'round':rnd,'participant_id':target_pid,
 250                               'record_group_id':int(gid),'teammate_id':mate_pid,
 251                               'opponent_group_id':int(group_df['opponent_group_id'].iloc[0]),
 252                               'payoff':payoff,'is_win':is_win,'n_target_samples':len(target_samples),
 253                               'prior_won':prior_won,'prior_payoff_frac':prior_payoff_frac},
 254                      'features': np.array(features, dtype=np.float32),
 255                      'current_x_norms': np.array(current_x_norms, dtype=np.float32),
 256                      'current_fx_norms': np.array(current_fx_norms, dtype=np.float32),
 257                  })
 258      return sequences
```
