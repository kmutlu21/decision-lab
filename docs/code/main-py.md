# main.py

Creates the FastAPI app, opens read-only database connections, exposes history and prediction endpoints, and registers the competition routes.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Symbols

| Symbol | Lines |
|---|---|
| `fetch` | 40-50 |
| `database_error` | 54-58 |
| `home` | 62-63 |
| `health` | 67-69 |
| `sessions` | 73-84 |
| `rounds` | 88-97 |
| `samples` | 101-145 |
| `get_function` | 148-158 |
| `landscape` | 162-181 |
| `predict` | 185-205 |

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1-8 | Module documentation describes direct Python startup; Docker instead imports main:app and supplies the password through its environment. |
| 9-20 | Imports database access, API validation/responses, numerical curve evaluation and the optional direct Uvicorn launcher. None of these imports trains the model. |
| 22-26 | Constructs the app and OpenAPI metadata. Version 0.5.0 remains in this deployed snapshot despite newer UI revisions. |
| 27-29 | Restricts session values, positive IDs and game numbers 1 through 4. FastAPI returns 422 for invalid query values. |
| 30-37 | Reads PG settings once when the module loads. localhost is the direct-run default; Compose supplies db as the network hostname. |
| 40-45 | Defines the shared SQL reader. The comment calls it a local first version, but this same implementation runs on AWS. |
| 46-50 | Opens a fresh read-only connection, executes SQL with a separate parameter tuple and returns dictionary rows. The context manager closes it even on exceptions; no connection pool exists. |
| 53-58 | Registers a PostgreSQL exception handler that returns a generic 503 response rather than leaking raw database errors to clients. |
| 61-63 | Serves replay.html relative to this Python file. This is the actual production page, not the bundled offline preview. |
| 66-69 | Checks SELECT 1 and reports database connectivity. This does not check schema completeness, trained artifacts, model accuracy or DNS. |
| 72-84 | Lists sessions with counts. LEFT JOIN keeps sessions with no records; DISTINCT prevents one round being counted repeatedly for its many samples. |
| 87-97 | Lists existing player-rounds for the selected session/game, counting samples and ordering choices for the browser menus. |
| 100-108 | Declares the own-sample endpoint and optional through_step. Display calculations here are separate from the 14-feature model builder. |
| 109-118 | Joins sample rows to their participant-round, filters the four identity fields and orders by own step. Missing history produces 404. |
| 119-125 | Optionally slices history and loads the objective scaling; initializes running-best and previous-position state. |
| 126-134 | Adds own running best, normalized x/y, change from the previous own x and seconds from the first own sample. These are display fields, not future labels. |
| 135-145 | Returns identity, explicit time reference, analyst normalization metadata and the enriched own samples. Current-round payoff/win are omitted. |
| 148-158 | Fetches the function for a session/game/round and joins session bounds. All players in that round use this stored function. Missing metadata yields 404. |
| 161-167 | Declares the full-curve reveal with 50 to 2000 plot points, default 500. The dense stored maximum is not recomputed here. |
| 168-172 | Samples the allowed x domain, evaluates the known objective and converts coordinates to normalized fractions. |
| 173-181 | Returns function metadata and JSON-friendly float points. This route deliberately reveals the full historical objective to the analyst. |
| 184-188 | Declares next-action inference. Imports the SQL prefix path lazily; after_step counts OWN tests, not all visible events. |
| 189-195 | Loads one prefix inside a repeatable-read, read-only transaction; closes SQL before inference; chooses the saved held-out model through the predictor singleton. |
| 196-205 | Maps missing round to 404, invalid step to 422, missing artifacts/dependencies to 503, and feature/artifact consistency failures to 409. |
| 210-212 | Injects app, fetch and get_function into replay_story.register_replay_routes. This adds two routes without a circular import back into main. |
| 214-222 | Only direct python main.py execution prompts for a password and starts loopback Uvicorn. Docker's python -m uvicorn main:app bypasses this block. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1-8 | Module documentation describes direct Python startup; Docker instead imports main:app and supplies the password through its environment. |
| 2 | 1-8 | Blank separator; no execution. |
| 3 | 1-8 | Module documentation describes direct Python startup; Docker instead imports main:app and supplies the password through its environment. |
| 4 | 1-8 | Module documentation describes direct Python startup; Docker instead imports main:app and supplies the password through its environment. |
| 5 | 1-8 | Module documentation describes direct Python startup; Docker instead imports main:app and supplies the password through its environment. |
| 6 | 1-8 | Module documentation describes direct Python startup; Docker instead imports main:app and supplies the password through its environment. |
| 7 | 1-8 | Module documentation describes direct Python startup; Docker instead imports main:app and supplies the password through its environment. |
| 8 | 1-8 | Module documentation describes direct Python startup; Docker instead imports main:app and supplies the password through its environment. |
| 9 | 9-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 10 | 9-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 11 | 9-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 12 | 9-20 | Blank separator; no execution. |
| 13 | 9-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 14 | 9-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 15 | 9-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 16 | 9-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 17 | 9-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 18 | 9-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 19 | 9-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 20 | 9-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 21 | 21 | Blank separator; no execution. |
| 22 | 22-26 | Constructs the app and OpenAPI metadata. Version 0.5.0 remains in this deployed snapshot despite newer UI revisions. |
| 23 | 22-26 | Constructs the app and OpenAPI metadata. Version 0.5.0 remains in this deployed snapshot despite newer UI revisions. |
| 24 | 22-26 | Constructs the app and OpenAPI metadata. Version 0.5.0 remains in this deployed snapshot despite newer UI revisions. |
| 25 | 22-26 | Constructs the app and OpenAPI metadata. Version 0.5.0 remains in this deployed snapshot despite newer UI revisions. |
| 26 | 22-26 | Closes the multiline expression or payload begun above. |
| 27 | 27-29 | Restricts session values, positive IDs and game numbers 1 through 4. FastAPI returns 422 for invalid query values. |
| 28 | 27-29 | Restricts session values, positive IDs and game numbers 1 through 4. FastAPI returns 422 for invalid query values. |
| 29 | 27-29 | Restricts session values, positive IDs and game numbers 1 through 4. FastAPI returns 422 for invalid query values. |
| 30 | 30-37 | Reads PG settings once when the module loads. localhost is the direct-run default; Compose supplies db as the network hostname. |
| 31 | 30-37 | Reads PG settings once when the module loads. localhost is the direct-run default; Compose supplies db as the network hostname. |
| 32 | 30-37 | Reads PG settings once when the module loads. localhost is the direct-run default; Compose supplies db as the network hostname. |
| 33 | 30-37 | Reads PG settings once when the module loads. localhost is the direct-run default; Compose supplies db as the network hostname. |
| 34 | 30-37 | Reads PG settings once when the module loads. localhost is the direct-run default; Compose supplies db as the network hostname. |
| 35 | 30-37 | Reads PG settings once when the module loads. localhost is the direct-run default; Compose supplies db as the network hostname. |
| 36 | 30-37 | Reads PG settings once when the module loads. localhost is the direct-run default; Compose supplies db as the network hostname. |
| 37 | 30-37 | Closes the multiline expression or payload begun above. |
| 38 | 38 | Blank separator; no execution. |
| 39 | 39 | Blank separator; no execution. |
| 40 | 40-45 | Function declaration: this body runs when called, not at declaration time. |
| 41 | 40-45 | Defines the shared SQL reader. The comment calls it a local first version, but this same implementation runs on AWS. |
| 42 | 40-45 | Blank separator; no execution. |
| 43 | 40-45 | Defines the shared SQL reader. The comment calls it a local first version, but this same implementation runs on AWS. |
| 44 | 40-45 | Defines the shared SQL reader. The comment calls it a local first version, but this same implementation runs on AWS. |
| 45 | 40-45 | Defines the shared SQL reader. The comment calls it a local first version, but this same implementation runs on AWS. |
| 46 | 46-50 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 47 | 46-50 | Opens a fresh read-only connection, executes SQL with a separate parameter tuple and returns dictionary rows. The context manager closes it even on exceptions; no connection pool exists. |
| 48 | 46-50 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 49 | 46-50 | Opens a fresh read-only connection, executes SQL with a separate parameter tuple and returns dictionary rows. The context manager closes it even on exceptions; no connection pool exists. |
| 50 | 46-50 | Return: sends this result to the caller and ends this invocation. |
| 51 | 51 | Blank separator; no execution. |
| 52 | 52 | Blank separator; no execution. |
| 53 | 53-58 | Decorator: attaches registration/metadata to the following function. |
| 54 | 53-58 | Function declaration: this body runs when called, not at declaration time. |
| 55 | 53-58 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 56 | 53-58 | Return: sends this result to the caller and ends this invocation. |
| 57 | 53-58 | Registers a PostgreSQL exception handler that returns a generic 503 response rather than leaking raw database errors to clients. |
| 58 | 53-58 | Registers a PostgreSQL exception handler that returns a generic 503 response rather than leaking raw database errors to clients. |
| 59 | 59 | Blank separator; no execution. |
| 60 | 60 | Blank separator; no execution. |
| 61 | 61-63 | Decorator: attaches registration/metadata to the following function. |
| 62 | 61-63 | Function declaration: this body runs when called, not at declaration time. |
| 63 | 61-63 | Return: sends this result to the caller and ends this invocation. |
| 64 | 64 | Blank separator; no execution. |
| 65 | 65 | Blank separator; no execution. |
| 66 | 66-69 | Decorator: attaches registration/metadata to the following function. |
| 67 | 66-69 | Function declaration: this body runs when called, not at declaration time. |
| 68 | 66-69 | Checks SELECT 1 and reports database connectivity. This does not check schema completeness, trained artifacts, model accuracy or DNS. |
| 69 | 66-69 | Return: sends this result to the caller and ends this invocation. |
| 70 | 70 | Blank separator; no execution. |
| 71 | 71 | Blank separator; no execution. |
| 72 | 72-84 | Decorator: attaches registration/metadata to the following function. |
| 73 | 72-84 | Function declaration: this body runs when called, not at declaration time. |
| 74 | 72-84 | Lists sessions with counts. LEFT JOIN keeps sessions with no records; DISTINCT prevents one round being counted repeatedly for its many samples. |
| 75 | 72-84 | Return: sends this result to the caller and ends this invocation. |
| 76 | 72-84 | Lists sessions with counts. LEFT JOIN keeps sessions with no records; DISTINCT prevents one round being counted repeatedly for its many samples. |
| 77 | 72-84 | Lists sessions with counts. LEFT JOIN keeps sessions with no records; DISTINCT prevents one round being counted repeatedly for its many samples. |
| 78 | 72-84 | Lists sessions with counts. LEFT JOIN keeps sessions with no records; DISTINCT prevents one round being counted repeatedly for its many samples. |
| 79 | 72-84 | Lists sessions with counts. LEFT JOIN keeps sessions with no records; DISTINCT prevents one round being counted repeatedly for its many samples. |
| 80 | 72-84 | Lists sessions with counts. LEFT JOIN keeps sessions with no records; DISTINCT prevents one round being counted repeatedly for its many samples. |
| 81 | 72-84 | Lists sessions with counts. LEFT JOIN keeps sessions with no records; DISTINCT prevents one round being counted repeatedly for its many samples. |
| 82 | 72-84 | Lists sessions with counts. LEFT JOIN keeps sessions with no records; DISTINCT prevents one round being counted repeatedly for its many samples. |
| 83 | 72-84 | Lists sessions with counts. LEFT JOIN keeps sessions with no records; DISTINCT prevents one round being counted repeatedly for its many samples. |
| 84 | 72-84 | Closes the multiline expression or payload begun above. |
| 85 | 85 | Blank separator; no execution. |
| 86 | 86 | Blank separator; no execution. |
| 87 | 87-97 | Decorator: attaches registration/metadata to the following function. |
| 88 | 87-97 | Function declaration: this body runs when called, not at declaration time. |
| 89 | 87-97 | Lists existing player-rounds for the selected session/game, counting samples and ordering choices for the browser menus. |
| 90 | 87-97 | Return: sends this result to the caller and ends this invocation. |
| 91 | 87-97 | Lists existing player-rounds for the selected session/game, counting samples and ordering choices for the browser menus. |
| 92 | 87-97 | Lists existing player-rounds for the selected session/game, counting samples and ordering choices for the browser menus. |
| 93 | 87-97 | Lists existing player-rounds for the selected session/game, counting samples and ordering choices for the browser menus. |
| 94 | 87-97 | Lists existing player-rounds for the selected session/game, counting samples and ordering choices for the browser menus. |
| 95 | 87-97 | Lists existing player-rounds for the selected session/game, counting samples and ordering choices for the browser menus. |
| 96 | 87-97 | Lists existing player-rounds for the selected session/game, counting samples and ordering choices for the browser menus. |
| 97 | 87-97 | Lists existing player-rounds for the selected session/game, counting samples and ordering choices for the browser menus. |
| 98 | 98 | Blank separator; no execution. |
| 99 | 99 | Blank separator; no execution. |
| 100 | 100-108 | Decorator: attaches registration/metadata to the following function. |
| 101 | 100-108 | Function declaration: this body runs when called, not at declaration time. |
| 102 | 100-108 | Declares the own-sample endpoint and optional through_step. Display calculations here are separate from the 14-feature model builder. |
| 103 | 100-108 | Declares the own-sample endpoint and optional through_step. Display calculations here are separate from the 14-feature model builder. |
| 104 | 100-108 | Declares the own-sample endpoint and optional through_step. Display calculations here are separate from the 14-feature model builder. |
| 105 | 100-108 | Blank separator; no execution. |
| 106 | 100-108 | Declares the own-sample endpoint and optional through_step. Display calculations here are separate from the 14-feature model builder. |
| 107 | 100-108 | Declares the own-sample endpoint and optional through_step. Display calculations here are separate from the 14-feature model builder. |
| 108 | 100-108 | Declares the own-sample endpoint and optional through_step. Display calculations here are separate from the 14-feature model builder. |
| 109 | 109-118 | Joins sample rows to their participant-round, filters the four identity fields and orders by own step. Missing history produces 404. |
| 110 | 109-118 | Joins sample rows to their participant-round, filters the four identity fields and orders by own step. Missing history produces 404. |
| 111 | 109-118 | Joins sample rows to their participant-round, filters the four identity fields and orders by own step. Missing history produces 404. |
| 112 | 109-118 | Joins sample rows to their participant-round, filters the four identity fields and orders by own step. Missing history produces 404. |
| 113 | 109-118 | Joins sample rows to their participant-round, filters the four identity fields and orders by own step. Missing history produces 404. |
| 114 | 109-118 | Joins sample rows to their participant-round, filters the four identity fields and orders by own step. Missing history produces 404. |
| 115 | 109-118 | Joins sample rows to their participant-round, filters the four identity fields and orders by own step. Missing history produces 404. |
| 116 | 109-118 | Joins sample rows to their participant-round, filters the four identity fields and orders by own step. Missing history produces 404. |
| 117 | 109-118 | Joins sample rows to their participant-round, filters the four identity fields and orders by own step. Missing history produces 404. |
| 118 | 109-118 | Conditional branch: determines which following statements run. |
| 119 | 119-125 | Failure path: interrupts normal execution with the stated exception. |
| 120 | 119-125 | Conditional branch: determines which following statements run. |
| 121 | 119-125 | Optionally slices history and loads the objective scaling; initializes running-best and previous-position state. |
| 122 | 119-125 | Optionally slices history and loads the objective scaling; initializes running-best and previous-position state. |
| 123 | 119-125 | Optionally slices history and loads the objective scaling; initializes running-best and previous-position state. |
| 124 | 119-125 | Optionally slices history and loads the objective scaling; initializes running-best and previous-position state. |
| 125 | 119-125 | Optionally slices history and loads the objective scaling; initializes running-best and previous-position state. |
| 126 | 126-134 | Adds own running best, normalized x/y, change from the previous own x and seconds from the first own sample. These are display fields, not future labels. |
| 127 | 126-134 | Adds own running best, normalized x/y, change from the previous own x and seconds from the first own sample. These are display fields, not future labels. |
| 128 | 126-134 | Loop: repeats the following operations for the stated elements/condition. |
| 129 | 126-134 | Adds own running best, normalized x/y, change from the previous own x and seconds from the first own sample. These are display fields, not future labels. |
| 130 | 126-134 | Adds own running best, normalized x/y, change from the previous own x and seconds from the first own sample. These are display fields, not future labels. |
| 131 | 126-134 | Adds own running best, normalized x/y, change from the previous own x and seconds from the first own sample. These are display fields, not future labels. |
| 132 | 126-134 | Adds own running best, normalized x/y, change from the previous own x and seconds from the first own sample. These are display fields, not future labels. |
| 133 | 126-134 | Adds own running best, normalized x/y, change from the previous own x and seconds from the first own sample. These are display fields, not future labels. |
| 134 | 126-134 | Adds own running best, normalized x/y, change from the previous own x and seconds from the first own sample. These are display fields, not future labels. |
| 135 | 135-145 | Returns identity, explicit time reference, analyst normalization metadata and the enriched own samples. Current-round payoff/win are omitted. |
| 136 | 135-145 | Returns identity, explicit time reference, analyst normalization metadata and the enriched own samples. Current-round payoff/win are omitted. |
| 137 | 135-145 | Return: sends this result to the caller and ends this invocation. |
| 138 | 135-145 | Returns identity, explicit time reference, analyst normalization metadata and the enriched own samples. Current-round payoff/win are omitted. |
| 139 | 135-145 | Returns identity, explicit time reference, analyst normalization metadata and the enriched own samples. Current-round payoff/win are omitted. |
| 140 | 135-145 | Returns identity, explicit time reference, analyst normalization metadata and the enriched own samples. Current-round payoff/win are omitted. |
| 141 | 135-145 | Returns identity, explicit time reference, analyst normalization metadata and the enriched own samples. Current-round payoff/win are omitted. |
| 142 | 135-145 | Returns identity, explicit time reference, analyst normalization metadata and the enriched own samples. Current-round payoff/win are omitted. |
| 143 | 135-145 | Returns identity, explicit time reference, analyst normalization metadata and the enriched own samples. Current-round payoff/win are omitted. |
| 144 | 135-145 | Returns identity, explicit time reference, analyst normalization metadata and the enriched own samples. Current-round payoff/win are omitted. |
| 145 | 135-145 | Closes the multiline expression or payload begun above. |
| 146 | 146 | Blank separator; no execution. |
| 147 | 147 | Blank separator; no execution. |
| 148 | 148-158 | Function declaration: this body runs when called, not at declaration time. |
| 149 | 148-158 | Fetches the function for a session/game/round and joins session bounds. All players in that round use this stored function. Missing metadata yields 404. |
| 150 | 148-158 | Fetches the function for a session/game/round and joins session bounds. All players in that round use this stored function. Missing metadata yields 404. |
| 151 | 148-158 | Fetches the function for a session/game/round and joins session bounds. All players in that round use this stored function. Missing metadata yields 404. |
| 152 | 148-158 | Fetches the function for a session/game/round and joins session bounds. All players in that round use this stored function. Missing metadata yields 404. |
| 153 | 148-158 | Fetches the function for a session/game/round and joins session bounds. All players in that round use this stored function. Missing metadata yields 404. |
| 154 | 148-158 | Fetches the function for a session/game/round and joins session bounds. All players in that round use this stored function. Missing metadata yields 404. |
| 155 | 148-158 | Fetches the function for a session/game/round and joins session bounds. All players in that round use this stored function. Missing metadata yields 404. |
| 156 | 148-158 | Conditional branch: determines which following statements run. |
| 157 | 148-158 | Failure path: interrupts normal execution with the stated exception. |
| 158 | 148-158 | Return: sends this result to the caller and ends this invocation. |
| 159 | 159 | Blank separator; no execution. |
| 160 | 160 | Blank separator; no execution. |
| 161 | 161-167 | Decorator: attaches registration/metadata to the following function. |
| 162 | 161-167 | Function declaration: this body runs when called, not at declaration time. |
| 163 | 161-167 | Declares the full-curve reveal with 50 to 2000 plot points, default 500. The dense stored maximum is not recomputed here. |
| 164 | 161-167 | Declares the full-curve reveal with 50 to 2000 plot points, default 500. The dense stored maximum is not recomputed here. |
| 165 | 161-167 | Blank separator; no execution. |
| 166 | 161-167 | Declares the full-curve reveal with 50 to 2000 plot points, default 500. The dense stored maximum is not recomputed here. |
| 167 | 161-167 | Declares the full-curve reveal with 50 to 2000 plot points, default 500. The dense stored maximum is not recomputed here. |
| 168 | 168-172 | Samples the allowed x domain, evaluates the known objective and converts coordinates to normalized fractions. |
| 169 | 168-172 | Samples the allowed x domain, evaluates the known objective and converts coordinates to normalized fractions. |
| 170 | 168-172 | Samples the allowed x domain, evaluates the known objective and converts coordinates to normalized fractions. |
| 171 | 168-172 | Samples the allowed x domain, evaluates the known objective and converts coordinates to normalized fractions. |
| 172 | 168-172 | Samples the allowed x domain, evaluates the known objective and converts coordinates to normalized fractions. |
| 173 | 173-181 | Returns function metadata and JSON-friendly float points. This route deliberately reveals the full historical objective to the analyst. |
| 174 | 173-181 | Return: sends this result to the caller and ends this invocation. |
| 175 | 173-181 | Returns function metadata and JSON-friendly float points. This route deliberately reveals the full historical objective to the analyst. |
| 176 | 173-181 | Returns function metadata and JSON-friendly float points. This route deliberately reveals the full historical objective to the analyst. |
| 177 | 173-181 | Returns function metadata and JSON-friendly float points. This route deliberately reveals the full historical objective to the analyst. |
| 178 | 173-181 | Returns function metadata and JSON-friendly float points. This route deliberately reveals the full historical objective to the analyst. |
| 179 | 173-181 | Returns function metadata and JSON-friendly float points. This route deliberately reveals the full historical objective to the analyst. |
| 180 | 173-181 | Loop: repeats the following operations for the stated elements/condition. |
| 181 | 173-181 | Closes the multiline expression or payload begun above. |
| 182 | 182 | Blank separator; no execution. |
| 183 | 183 | Blank separator; no execution. |
| 184 | 184-188 | Decorator: attaches registration/metadata to the following function. |
| 185 | 184-188 | Function declaration: this body runs when called, not at declaration time. |
| 186 | 184-188 | Declares next-action inference. Imports the SQL prefix path lazily; after_step counts OWN tests, not all visible events. |
| 187 | 184-188 | Declares next-action inference. Imports the SQL prefix path lazily; after_step counts OWN tests, not all visible events. |
| 188 | 184-188 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 189 | 189-195 | Exception-control block: separates normal work, error handling and cleanup. |
| 190 | 189-195 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 191 | 189-195 | Loads one prefix inside a repeatable-read, read-only transaction; closes SQL before inference; chooses the saved held-out model through the predictor singleton. |
| 192 | 189-195 | Loads one prefix inside a repeatable-read, read-only transaction; closes SQL before inference; chooses the saved held-out model through the predictor singleton. |
| 193 | 189-195 | Loads one prefix inside a repeatable-read, read-only transaction; closes SQL before inference; chooses the saved held-out model through the predictor singleton. |
| 194 | 189-195 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 195 | 189-195 | Return: sends this result to the caller and ends this invocation. |
| 196 | 196-205 | Exception-control block: separates normal work, error handling and cleanup. |
| 197 | 196-205 | Failure path: interrupts normal execution with the stated exception. |
| 198 | 196-205 | Exception-control block: separates normal work, error handling and cleanup. |
| 199 | 196-205 | Failure path: interrupts normal execution with the stated exception. |
| 200 | 196-205 | Exception-control block: separates normal work, error handling and cleanup. |
| 201 | 196-205 | Failure path: interrupts normal execution with the stated exception. |
| 202 | 196-205 | Exception-control block: separates normal work, error handling and cleanup. |
| 203 | 196-205 | Failure path: interrupts normal execution with the stated exception. |
| 204 | 196-205 | Exception-control block: separates normal work, error handling and cleanup. |
| 205 | 196-205 | Failure path: interrupts normal execution with the stated exception. |
| 206 | 206 | Blank separator; no execution. |
| 207 | 207 | Blank separator; no execution. |
| 208 | 208 | Blank separator; no execution. |
| 209 | 209 | Blank separator; no execution. |
| 210 | 210-212 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 211 | 210-212 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 212 | 210-212 | Injects app, fetch and get_function into replay_story.register_replay_routes. This adds two routes without a circular import back into main. |
| 213 | 213 | Blank separator; no execution. |
| 214 | 214-222 | Conditional branch: determines which following statements run. |
| 215 | 214-222 | Conditional branch: determines which following statements run. |
| 216 | 214-222 | Only direct python main.py execution prompts for a password and starts loopback Uvicorn. Docker's python -m uvicorn main:app bypasses this block. |
| 217 | 214-222 | Exception-control block: separates normal work, error handling and cleanup. |
| 218 | 214-222 | Only direct python main.py execution prompts for a password and starts loopback Uvicorn. Docker's python -m uvicorn main:app bypasses this block. |
| 219 | 214-222 | Exception-control block: separates normal work, error handling and cleanup. |
| 220 | 214-222 | Failure path: interrupts normal execution with the stated exception. |
| 221 | 214-222 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 222 | 214-222 | Only direct python main.py execution prompts for a password and starts loopback Uvicorn. Docker's python -m uvicorn main:app bypasses this block. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  """Decision Lab: local, read-only API for historical experimental records.
   2  
   3  Start with: python main.py
   4  Open: http://127.0.0.1:8000/docs
   5  The PostgreSQL password is prompted for and kept only in process memory.
   6  Optional DB settings: PGHOST, PGPORT, PGDATABASE, PGUSER, PGPASSWORD.
   7  Historical replay with held-out LSTM inference on PostgreSQL-built feature prefixes.
   8  """
   9  import getpass
  10  import os
  11  from typing import Annotated, Literal
  12  
  13  import psycopg
  14  from psycopg.rows import dict_row
  15  from fastapi import FastAPI, HTTPException, Query
  16  from fastapi.responses import JSONResponse, FileResponse
  17  from pathlib import Path
  18  import uvicorn
  19  import numpy as np
  20  from objectives import evaluate
  21  
  22  app = FastAPI(
  23      title='Decision Lab API',
  24      version='0.5.0',
  25      description='Explore historical decisions. Elapsed time starts at the first own sample, not the round start. Held-out LSTM predictions use PostgreSQL-built feature prefixes.',
  26  )
  27  Session = Literal['feb18', 'feb20', 'march6']
  28  PositiveInt = Annotated[int, Query(ge=1)]
  29  Game = Annotated[int, Query(ge=1, le=4)]
  30  DB_SETTINGS = {
  31      'host': os.getenv('PGHOST', 'localhost'),
  32      'port': os.getenv('PGPORT', '5432'),
  33      'dbname': os.getenv('PGDATABASE', 'decision_lab'),
  34      'user': os.getenv('PGUSER', 'postgres'),
  35      'password': os.getenv('PGPASSWORD'),
  36      'connect_timeout': 5,
  37  }
  38  
  39  
  40  def fetch(query, params=()):
  41      """Run a parameterized SELECT, return dictionaries, close the connection.
  42  
  43      A connection per request is sufficient for this local first version.
  44      A later deployment can use a connection pool and a dedicated DB role.
  45      """
  46      with psycopg.connect(**DB_SETTINGS, row_factory=dict_row) as conn:
  47          conn.read_only = True
  48          with conn.cursor() as cur:
  49              cur.execute(query, params)
  50              return cur.fetchall()
  51  
  52  
  53  @app.exception_handler(psycopg.Error)
  54  def database_error(request, exc):
  55      # Do not send raw connection details or database errors to the browser.
  56      return JSONResponse(status_code=503, content={
  57          'detail': 'Database request failed. Check PostgreSQL is running, connection settings, and that import_data.py and import_functions.py completed.'
  58      })
  59  
  60  
  61  @app.get('/')
  62  def home():
  63      return FileResponse(Path(__file__).resolve().parent / 'replay.html')
  64  
  65  
  66  @app.get('/health')
  67  def health():
  68      fetch('SELECT 1')
  69      return {'status': 'ok', 'database': 'connected'}
  70  
  71  
  72  @app.get('/sessions')
  73  def sessions():
  74      """List sessions and their imported round/sample counts."""
  75      return fetch('''
  76          SELECT e.session_id, e.session_date, e.x_min, e.x_max,
  77                 COUNT(DISTINCT r.participant_round_id) AS participant_rounds,
  78                 COUNT(s.sample_id) AS samples
  79          FROM experiment_sessions e
  80          LEFT JOIN participant_rounds r ON r.session_id = e.session_id
  81          LEFT JOIN samples s ON s.participant_round_id = r.participant_round_id
  82          GROUP BY e.session_id, e.session_date, e.x_min, e.x_max
  83          ORDER BY e.session_date
  84      ''')
  85  
  86  
  87  @app.get('/rounds')
  88  def rounds(session_id: Session, game_number: Game):
  89      """Find participants and recorded rounds for a session/game."""
  90      return fetch('''
  91          SELECT r.participant_id, r.round_number, COUNT(s.sample_id) AS sample_count
  92          FROM participant_rounds r
  93          JOIN samples s ON s.participant_round_id = r.participant_round_id
  94          WHERE r.session_id = %s AND r.game_number = %s
  95          GROUP BY r.participant_id, r.round_number
  96          ORDER BY r.participant_id, r.round_number
  97      ''', (session_id, game_number))
  98  
  99  
 100  @app.get('/samples')
 101  def samples(session_id: Session, game_number: Game, participant_id: PositiveInt,
 102              round_number: PositiveInt,
 103              through_step: Annotated[int | None, Query(ge=1)] = None):
 104      """Return own decisions in order, optionally stopping at a replay step.
 105  
 106      Running best and elapsed time only use the returned history. These are
 107      display calculations, not the LSTM's merged own/teammate feature builder.
 108      The final round payoff and winning status are deliberately not returned.
 109      """
 110      rows = fetch('''
 111          SELECT s.step_number, s.x_value, s.observed_value, s.sampled_at
 112          FROM samples s
 113          JOIN participant_rounds r ON r.participant_round_id = s.participant_round_id
 114          WHERE r.session_id = %s AND r.game_number = %s
 115            AND r.participant_id = %s AND r.round_number = %s
 116          ORDER BY s.step_number
 117      ''', (session_id, game_number, participant_id, round_number))
 118      if not rows:
 119          raise HTTPException(status_code=404, detail='No recorded samples for this participant-round.')
 120      if through_step is not None:
 121          rows = [row for row in rows if row['step_number'] <= through_step]
 122      function = get_function(session_id, game_number, round_number)
 123      xmin, xmax = function['x_min'], function['x_max']
 124      maximum = function['estimated_maximum']
 125      first_time = rows[0]['sampled_at']
 126      best = float('-inf')
 127      previous_x = None
 128      for row in rows:
 129          best = max(best, row['observed_value'])
 130          row['best_value_so_far'] = best
 131          row['position_fraction'] = (row['x_value'] - xmin) / (xmax - xmin)
 132          row['quality_fraction'] = row['observed_value'] / maximum
 133          row['best_quality_fraction_so_far'] = best / maximum
 134          row['change_in_x'] = None if previous_x is None else row['x_value'] - previous_x
 135          row['seconds_since_first_sample'] = (row['sampled_at'] - first_time).total_seconds()
 136          previous_x = row['x_value']
 137      return {
 138          'session_id': session_id, 'game_number': game_number,
 139          'participant_id': participant_id, 'round_number': round_number,
 140          'time_reference': 'first own recorded sample; not round start',
 141          'normalization': {'x_min': xmin, 'x_max': xmax, 'estimated_maximum': maximum,
 142                            'maximum_method': function['maximum_method'],
 143                            'perspective': 'analyst view; full objective used for scaling'},
 144          'samples': rows,
 145      }
 146  
 147  
 148  def get_function(session_id, game_number, round_number):
 149      rows = fetch("""
 150          SELECT f.function_family, f.parameters, f.estimated_maximum, f.maximum_method,
 151                 e.x_min, e.x_max
 152          FROM round_functions f
 153          JOIN experiment_sessions e ON e.session_id = f.session_id
 154          WHERE f.session_id=%s AND f.game_number=%s AND f.round_number=%s
 155      """, (session_id, game_number, round_number))
 156      if not rows:
 157          raise HTTPException(status_code=404, detail='Round function not found. Run import_functions.py and check the selected round.')
 158      return rows[0]
 159  
 160  
 161  @app.get('/landscape')
 162  def landscape(session_id: Session, game_number: Game, round_number: PositiveInt,
 163                points: Annotated[int, Query(ge=50, le=2000)] = 500):
 164      """Full objective for optional analyst reveal; not an LSTM input.
 165  
 166      Curve sampling is for plotting only. Normalization uses the stored
 167      maximum computed with the original model's denser numerical procedure.
 168      """
 169      function = get_function(session_id, game_number, round_number)
 170      x = np.linspace(function['x_min'], function['x_max'], points)
 171      y = evaluate(x, function['function_family'], function['parameters'])
 172      position = (x - function['x_min']) / (function['x_max'] - function['x_min'])
 173      quality = y / function['estimated_maximum']
 174      return {
 175          'session_id': session_id, 'game_number': game_number, 'round_number': round_number,
 176          **function,
 177          'perspective': 'analyst reveal; not necessarily visible to participants',
 178          'curve': [dict(x_value=float(xi), objective_value=float(yi),
 179                         position_fraction=float(pi), quality_fraction=float(qi))
 180                    for xi, yi, pi, qi in zip(x, y, position, quality)],
 181      }
 182  
 183  
 184  @app.get('/predict')
 185  def predict(session_id: Session, game_number: Game, participant_id: PositiveInt,
 186              round_number: PositiveInt, after_step: PositiveInt):
 187      """Build an observed event prefix from PostgreSQL and predict its next action."""
 188      from sql_runtime import load_prefix, MissingRound, InvalidStep
 189      try:
 190          with psycopg.connect(**DB_SETTINGS) as conn:
 191              conn.isolation_level = psycopg.IsolationLevel.REPEATABLE_READ
 192              conn.read_only = True
 193              seq, meta = load_prefix(conn, (session_id,game_number,round_number,participant_id), after_step)
 194          from inference import get_predictor
 195          return get_predictor().predict((session_id,game_number,round_number,participant_id),after_step,seq,meta)
 196      except MissingRound as exc:
 197          raise HTTPException(status_code=404,detail=str(exc))
 198      except InvalidStep as exc:
 199          raise HTTPException(status_code=422,detail=str(exc))
 200      except FileNotFoundError:
 201          raise HTTPException(status_code=503,detail='Missing original model weights or results in models/.')
 202      except ImportError:
 203          raise HTTPException(status_code=503,detail='Missing model/feature code or dependency. Check the update files.')
 204      except ValueError as exc:
 205          raise HTTPException(status_code=409,detail=str(exc))
 206  
 207  
 208  
 209  
 210  # Decision Lab competition replay routes
 211  from replay_story import register_replay_routes
 212  register_replay_routes(app, fetch, get_function)
 213  
 214  if __name__ == '__main__':
 215      if DB_SETTINGS['password'] is None:
 216          DB_SETTINGS['password'] = getpass.getpass(f"PostgreSQL password for {DB_SETTINGS['user']}: ")
 217      try:
 218          fetch('SELECT 1')
 219      except psycopg.Error:
 220          raise SystemExit('Could not connect. Check PostgreSQL is running and the password/settings are correct.')
 221      # Loopback binding: this learning server is accessible on your PC only.
 222      uvicorn.run(app, host='127.0.0.1', port=8000)
```
