# import_data.py

Validates the 12 raw experiment exports and transactionally imports sessions, nonempty player-rounds and own sample events.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Symbols

| Symbol | Lines |
|---|---|
| `number` | 51-57 |
| `integer` | 60-64 |
| `sequence` | 67-79 |
| `read_exports` | 82-150 |
| `import_records` | 153-194 |
| `main` | 197-215 |

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1-20 | Explains the import entry point and imports safe JSON/literal parsing, dataframe readers and validation helpers. |
| 22-26 | Maps three session IDs to dates, domains and expected filenames. February uses [0,100]; March uses [-20,20]. |
| 27-31 | Creates experiment_sessions with its primary key and positive-width domain constraint. |
| 32-40 | Creates participant_rounds, a generated internal ID, session foreign key, group/outcome fields and a unique natural identity. |
| 41-48 | Creates ordered sample rows with required finite-value checks handled in Python, a round foreign key and unique own-step constraint. Timestamps carry no timezone. |
| 51-57 | Converts missing scalars to None and rejects nonfinite numeric values, keeping invalid data out of the database. |
| 60-64 | Accepts only a nonmissing exact integer. A value such as 1.5 is rejected rather than truncated. |
| 67-79 | Parses a list from JSON or ast.literal_eval, never eval. Blank/missing values become an empty sequence; other types are rejected. |
| 82-91 | Walks all sessions and four games, requiring exactly one matching export file, then loads CSV or Excel accordingly. |
| 92-97 | Finds game-specific sample columns using a regular expression and sorts round numbers numerically. |
| 98-105 | Initializes counts and constructs a symmetric mapping from each recorded group to its opponent. |
| 106-116 | Skips unused participant rows and empty sequences, while retaining all nonempty rounds including one-sample rounds. |
| 117-126 | Rejects duplicate identities, applies the original payoff fallback when payoff_float is missing/zero, and validates win flags. |
| 127-135 | Reads each [observed value, x, timestamp] triplet, numbers own steps starting at 1 and checks domain/value validity. |
| 136-142 | Rejects invalid or timezone-aware timestamps and decreasing own-event time; stores Python datetimes in original order. |
| 143-150 | Collects records and reports round/sample/empty counts before connecting to the database. |
| 153-162 | Imports psycopg only when writing, gets a private password and creates one transaction for this import stage. |
| 163-170 | Creates schema, takes a transaction-scoped advisory lock, and inserts or validates session metadata. Existing conflicts abort the transaction. |
| 171-184 | For existing participant-rounds, compares metadata and the complete ordered sample history. Identical data is skipped; mismatched data is never silently overwritten. |
| 185-194 | Inserts new parent rounds, reads generated IDs and batch-inserts child samples. Successful context-manager exit commits the transaction and then prints counts. |
| 197-207 | Parses command-line paths, database arguments and check-only. This importer's host/port/database/user defaults are CLI values, unlike some sibling scripts' PG environment defaults. |
| 208-215 | Validates raw files first; check-only makes no database connection. Otherwise writes transactionally, reporting failures with exit code 1. |
| 218-219 | Runs main only when invoked as a script, allowing the parsing helpers and schema to be imported safely elsewhere. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1-20 | Explains the import entry point and imports safe JSON/literal parsing, dataframe readers and validation helpers. |
| 2 | 1-20 | Blank separator; no execution. |
| 3 | 1-20 | Explains the import entry point and imports safe JSON/literal parsing, dataframe readers and validation helpers. |
| 4 | 1-20 | Explains the import entry point and imports safe JSON/literal parsing, dataframe readers and validation helpers. |
| 5 | 1-20 | Explains the import entry point and imports safe JSON/literal parsing, dataframe readers and validation helpers. |
| 6 | 1-20 | Blank separator; no execution. |
| 7 | 1-20 | Explains the import entry point and imports safe JSON/literal parsing, dataframe readers and validation helpers. |
| 8 | 1-20 | Explains the import entry point and imports safe JSON/literal parsing, dataframe readers and validation helpers. |
| 9 | 1-20 | Explains the import entry point and imports safe JSON/literal parsing, dataframe readers and validation helpers. |
| 10 | 1-20 | Explains the import entry point and imports safe JSON/literal parsing, dataframe readers and validation helpers. |
| 11 | 1-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 12 | 1-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 13 | 1-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 14 | 1-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 15 | 1-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 16 | 1-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 17 | 1-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 18 | 1-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 19 | 1-20 | Blank separator; no execution. |
| 20 | 1-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 21 | 21 | Blank separator; no execution. |
| 22 | 22-26 | Maps three session IDs to dates, domains and expected filenames. February uses [0,100]; March uses [-20,20]. |
| 23 | 22-26 | Maps three session IDs to dates, domains and expected filenames. February uses [0,100]; March uses [-20,20]. |
| 24 | 22-26 | Maps three session IDs to dates, domains and expected filenames. February uses [0,100]; March uses [-20,20]. |
| 25 | 22-26 | Maps three session IDs to dates, domains and expected filenames. February uses [0,100]; March uses [-20,20]. |
| 26 | 22-26 | Closes the multiline expression or payload begun above. |
| 27 | 27-31 | Creates experiment_sessions with its primary key and positive-width domain constraint. |
| 28 | 27-31 | Creates experiment_sessions with its primary key and positive-width domain constraint. |
| 29 | 27-31 | Creates experiment_sessions with its primary key and positive-width domain constraint. |
| 30 | 27-31 | Creates experiment_sessions with its primary key and positive-width domain constraint. |
| 31 | 27-31 | Creates experiment_sessions with its primary key and positive-width domain constraint. |
| 32 | 32-40 | Creates participant_rounds, a generated internal ID, session foreign key, group/outcome fields and a unique natural identity. |
| 33 | 32-40 | Creates participant_rounds, a generated internal ID, session foreign key, group/outcome fields and a unique natural identity. |
| 34 | 32-40 | Creates participant_rounds, a generated internal ID, session foreign key, group/outcome fields and a unique natural identity. |
| 35 | 32-40 | Creates participant_rounds, a generated internal ID, session foreign key, group/outcome fields and a unique natural identity. |
| 36 | 32-40 | Creates participant_rounds, a generated internal ID, session foreign key, group/outcome fields and a unique natural identity. |
| 37 | 32-40 | Creates participant_rounds, a generated internal ID, session foreign key, group/outcome fields and a unique natural identity. |
| 38 | 32-40 | Creates participant_rounds, a generated internal ID, session foreign key, group/outcome fields and a unique natural identity. |
| 39 | 32-40 | Creates participant_rounds, a generated internal ID, session foreign key, group/outcome fields and a unique natural identity. |
| 40 | 32-40 | Creates participant_rounds, a generated internal ID, session foreign key, group/outcome fields and a unique natural identity. |
| 41 | 41-48 | Creates ordered sample rows with required finite-value checks handled in Python, a round foreign key and unique own-step constraint. Timestamps carry no timezone. |
| 42 | 41-48 | Creates ordered sample rows with required finite-value checks handled in Python, a round foreign key and unique own-step constraint. Timestamps carry no timezone. |
| 43 | 41-48 | Creates ordered sample rows with required finite-value checks handled in Python, a round foreign key and unique own-step constraint. Timestamps carry no timezone. |
| 44 | 41-48 | Creates ordered sample rows with required finite-value checks handled in Python, a round foreign key and unique own-step constraint. Timestamps carry no timezone. |
| 45 | 41-48 | Creates ordered sample rows with required finite-value checks handled in Python, a round foreign key and unique own-step constraint. Timestamps carry no timezone. |
| 46 | 41-48 | Creates ordered sample rows with required finite-value checks handled in Python, a round foreign key and unique own-step constraint. Timestamps carry no timezone. |
| 47 | 41-48 | Creates ordered sample rows with required finite-value checks handled in Python, a round foreign key and unique own-step constraint. Timestamps carry no timezone. |
| 48 | 41-48 | Creates ordered sample rows with required finite-value checks handled in Python, a round foreign key and unique own-step constraint. Timestamps carry no timezone. |
| 49 | 49 | Blank separator; no execution. |
| 50 | 50 | Blank separator; no execution. |
| 51 | 51-57 | Function declaration: this body runs when called, not at declaration time. |
| 52 | 51-57 | Conditional branch: determines which following statements run. |
| 53 | 51-57 | Return: sends this result to the caller and ends this invocation. |
| 54 | 51-57 | Converts missing scalars to None and rejects nonfinite numeric values, keeping invalid data out of the database. |
| 55 | 51-57 | Conditional branch: determines which following statements run. |
| 56 | 51-57 | Failure path: interrupts normal execution with the stated exception. |
| 57 | 51-57 | Return: sends this result to the caller and ends this invocation. |
| 58 | 58 | Blank separator; no execution. |
| 59 | 59 | Blank separator; no execution. |
| 60 | 60-64 | Function declaration: this body runs when called, not at declaration time. |
| 61 | 60-64 | Accepts only a nonmissing exact integer. A value such as 1.5 is rejected rather than truncated. |
| 62 | 60-64 | Conditional branch: determines which following statements run. |
| 63 | 60-64 | Failure path: interrupts normal execution with the stated exception. |
| 64 | 60-64 | Return: sends this result to the caller and ends this invocation. |
| 65 | 65 | Blank separator; no execution. |
| 66 | 66 | Blank separator; no execution. |
| 67 | 67-79 | Function declaration: this body runs when called, not at declaration time. |
| 68 | 67-79 | Conditional branch: determines which following statements run. |
| 69 | 67-79 | Return: sends this result to the caller and ends this invocation. |
| 70 | 67-79 | Conditional branch: determines which following statements run. |
| 71 | 67-79 | Conditional branch: determines which following statements run. |
| 72 | 67-79 | Return: sends this result to the caller and ends this invocation. |
| 73 | 67-79 | Exception-control block: separates normal work, error handling and cleanup. |
| 74 | 67-79 | Parses a list from JSON or ast.literal_eval, never eval. Blank/missing values become an empty sequence; other types are rejected. |
| 75 | 67-79 | Exception-control block: separates normal work, error handling and cleanup. |
| 76 | 67-79 | Parses a list from JSON or ast.literal_eval, never eval. Blank/missing values become an empty sequence; other types are rejected. |
| 77 | 67-79 | Conditional branch: determines which following statements run. |
| 78 | 67-79 | Failure path: interrupts normal execution with the stated exception. |
| 79 | 67-79 | Return: sends this result to the caller and ends this invocation. |
| 80 | 80 | Blank separator; no execution. |
| 81 | 81 | Blank separator; no execution. |
| 82 | 82-91 | Function declaration: this body runs when called, not at declaration time. |
| 83 | 82-91 | Walks all sessions and four games, requiring exactly one matching export file, then loads CSV or Excel accordingly. |
| 84 | 82-91 | Walks all sessions and four games, requiring exactly one matching export file, then loads CSV or Excel accordingly. |
| 85 | 82-91 | Loop: repeats the following operations for the stated elements/condition. |
| 86 | 82-91 | Loop: repeats the following operations for the stated elements/condition. |
| 87 | 82-91 | Walks all sessions and four games, requiring exactly one matching export file, then loads CSV or Excel accordingly. |
| 88 | 82-91 | Conditional branch: determines which following statements run. |
| 89 | 82-91 | Failure path: interrupts normal execution with the stated exception. |
| 90 | 82-91 | Walks all sessions and four games, requiring exactly one matching export file, then loads CSV or Excel accordingly. |
| 91 | 82-91 | Walks all sessions and four games, requiring exactly one matching export file, then loads CSV or Excel accordingly. |
| 92 | 92-97 | Finds game-specific sample columns using a regular expression and sorts round numbers numerically. |
| 93 | 92-97 | Finds game-specific sample columns using a regular expression and sorts round numbers numerically. |
| 94 | 92-97 | Finds game-specific sample columns using a regular expression and sorts round numbers numerically. |
| 95 | 92-97 | Conditional branch: determines which following statements run. |
| 96 | 92-97 | Failure path: interrupts normal execution with the stated exception. |
| 97 | 92-97 | Finds game-specific sample columns using a regular expression and sorts round numbers numerically. |
| 98 | 98-105 | Loop: repeats the following operations for the stated elements/condition. |
| 99 | 98-105 | Initializes counts and constructs a symmetric mapping from each recorded group to its opponent. |
| 100 | 98-105 | Initializes counts and constructs a symmetric mapping from each recorded group to its opponent. |
| 101 | 98-105 | Initializes counts and constructs a symmetric mapping from each recorded group to its opponent. |
| 102 | 98-105 | Loop: repeats the following operations for the stated elements/condition. |
| 103 | 98-105 | Initializes counts and constructs a symmetric mapping from each recorded group to its opponent. |
| 104 | 98-105 | Initializes counts and constructs a symmetric mapping from each recorded group to its opponent. |
| 105 | 98-105 | Loop: repeats the following operations for the stated elements/condition. |
| 106 | 106-116 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 107 | 106-116 | Conditional branch: determines which following statements run. |
| 108 | 106-116 | Skips unused participant rows and empty sequences, while retaining all nonempty rounds including one-sample rounds. |
| 109 | 106-116 | Skips unused participant rows and empty sequences, while retaining all nonempty rounds including one-sample rounds. |
| 110 | 106-116 | Conditional branch: determines which following statements run. |
| 111 | 106-116 | Skips unused participant rows and empty sequences, while retaining all nonempty rounds including one-sample rounds. |
| 112 | 106-116 | Skips unused participant rows and empty sequences, while retaining all nonempty rounds including one-sample rounds. |
| 113 | 106-116 | Skips unused participant rows and empty sequences, while retaining all nonempty rounds including one-sample rounds. |
| 114 | 106-116 | Skips unused participant rows and empty sequences, while retaining all nonempty rounds including one-sample rounds. |
| 115 | 106-116 | Skips unused participant rows and empty sequences, while retaining all nonempty rounds including one-sample rounds. |
| 116 | 106-116 | Conditional branch: determines which following statements run. |
| 117 | 117-126 | Failure path: interrupts normal execution with the stated exception. |
| 118 | 117-126 | Rejects duplicate identities, applies the original payoff fallback when payoff_float is missing/zero, and validates win flags. |
| 119 | 117-126 | Rejects duplicate identities, applies the original payoff fallback when payoff_float is missing/zero, and validates win flags. |
| 120 | 117-126 | Rejects duplicate identities, applies the original payoff fallback when payoff_float is missing/zero, and validates win flags. |
| 121 | 117-126 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 122 | 117-126 | Conditional branch: determines which following statements run. |
| 123 | 117-126 | Rejects duplicate identities, applies the original payoff fallback when payoff_float is missing/zero, and validates win flags. |
| 124 | 117-126 | Rejects duplicate identities, applies the original payoff fallback when payoff_float is missing/zero, and validates win flags. |
| 125 | 117-126 | Conditional branch: determines which following statements run. |
| 126 | 117-126 | Failure path: interrupts normal execution with the stated exception. |
| 127 | 127-135 | Reads each [observed value, x, timestamp] triplet, numbers own steps starting at 1 and checks domain/value validity. |
| 128 | 127-135 | Loop: repeats the following operations for the stated elements/condition. |
| 129 | 127-135 | Conditional branch: determines which following statements run. |
| 130 | 127-135 | Failure path: interrupts normal execution with the stated exception. |
| 131 | 127-135 | Reads each [observed value, x, timestamp] triplet, numbers own steps starting at 1 and checks domain/value validity. |
| 132 | 127-135 | Reads each [observed value, x, timestamp] triplet, numbers own steps starting at 1 and checks domain/value validity. |
| 133 | 127-135 | Conditional branch: determines which following statements run. |
| 134 | 127-135 | Failure path: interrupts normal execution with the stated exception. |
| 135 | 127-135 | Reads each [observed value, x, timestamp] triplet, numbers own steps starting at 1 and checks domain/value validity. |
| 136 | 136-142 | Conditional branch: determines which following statements run. |
| 137 | 136-142 | Failure path: interrupts normal execution with the stated exception. |
| 138 | 136-142 | Rejects invalid or timezone-aware timestamps and decreasing own-event time; stores Python datetimes in original order. |
| 139 | 136-142 | Conditional branch: determines which following statements run. |
| 140 | 136-142 | Failure path: interrupts normal execution with the stated exception. |
| 141 | 136-142 | Rejects invalid or timezone-aware timestamps and decreasing own-event time; stores Python datetimes in original order. |
| 142 | 136-142 | Rejects invalid or timezone-aware timestamps and decreasing own-event time; stores Python datetimes in original order. |
| 143 | 143-150 | Collects records and reports round/sample/empty counts before connecting to the database. |
| 144 | 143-150 | Collects records and reports round/sample/empty counts before connecting to the database. |
| 145 | 143-150 | Collects records and reports round/sample/empty counts before connecting to the database. |
| 146 | 143-150 | Collects records and reports round/sample/empty counts before connecting to the database. |
| 147 | 143-150 | Collects records and reports round/sample/empty counts before connecting to the database. |
| 148 | 143-150 | Collects records and reports round/sample/empty counts before connecting to the database. |
| 149 | 143-150 | Collects records and reports round/sample/empty counts before connecting to the database. |
| 150 | 143-150 | Return: sends this result to the caller and ends this invocation. |
| 151 | 151 | Blank separator; no execution. |
| 152 | 152 | Blank separator; no execution. |
| 153 | 153-162 | Function declaration: this body runs when called, not at declaration time. |
| 154 | 153-162 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 155 | 153-162 | Imports psycopg only when writing, gets a private password and creates one transaction for this import stage. |
| 156 | 153-162 | Conditional branch: determines which following statements run. |
| 157 | 153-162 | Imports psycopg only when writing, gets a private password and creates one transaction for this import stage. |
| 158 | 153-162 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 159 | 153-162 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 160 | 153-162 | Imports psycopg only when writing, gets a private password and creates one transaction for this import stage. |
| 161 | 153-162 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 162 | 153-162 | Imports psycopg only when writing, gets a private password and creates one transaction for this import stage. |
| 163 | 163-170 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 164 | 163-170 | Creates schema, takes a transaction-scoped advisory lock, and inserts or validates session metadata. Existing conflicts abort the transaction. |
| 165 | 163-170 | Loop: repeats the following operations for the stated elements/condition. |
| 166 | 163-170 | Creates schema, takes a transaction-scoped advisory lock, and inserts or validates session metadata. Existing conflicts abort the transaction. |
| 167 | 163-170 | Creates schema, takes a transaction-scoped advisory lock, and inserts or validates session metadata. Existing conflicts abort the transaction. |
| 168 | 163-170 | Creates schema, takes a transaction-scoped advisory lock, and inserts or validates session metadata. Existing conflicts abort the transaction. |
| 169 | 163-170 | Conditional branch: determines which following statements run. |
| 170 | 163-170 | Failure path: interrupts normal execution with the stated exception. |
| 171 | 171-184 | For existing participant-rounds, compares metadata and the complete ordered sample history. Identical data is skipped; mismatched data is never silently overwritten. |
| 172 | 171-184 | Loop: repeats the following operations for the stated elements/condition. |
| 173 | 171-184 | For existing participant-rounds, compares metadata and the complete ordered sample history. Identical data is skipped; mismatched data is never silently overwritten. |
| 174 | 171-184 | For existing participant-rounds, compares metadata and the complete ordered sample history. Identical data is skipped; mismatched data is never silently overwritten. |
| 175 | 171-184 | For existing participant-rounds, compares metadata and the complete ordered sample history. Identical data is skipped; mismatched data is never silently overwritten. |
| 176 | 171-184 | For existing participant-rounds, compares metadata and the complete ordered sample history. Identical data is skipped; mismatched data is never silently overwritten. |
| 177 | 171-184 | Conditional branch: determines which following statements run. |
| 178 | 171-184 | For existing participant-rounds, compares metadata and the complete ordered sample history. Identical data is skipped; mismatched data is never silently overwritten. |
| 179 | 171-184 | For existing participant-rounds, compares metadata and the complete ordered sample history. Identical data is skipped; mismatched data is never silently overwritten. |
| 180 | 171-184 | For existing participant-rounds, compares metadata and the complete ordered sample history. Identical data is skipped; mismatched data is never silently overwritten. |
| 181 | 171-184 | Conditional branch: determines which following statements run. |
| 182 | 171-184 | Failure path: interrupts normal execution with the stated exception. |
| 183 | 171-184 | For existing participant-rounds, compares metadata and the complete ordered sample history. Identical data is skipped; mismatched data is never silently overwritten. |
| 184 | 171-184 | For existing participant-rounds, compares metadata and the complete ordered sample history. Identical data is skipped; mismatched data is never silently overwritten. |
| 185 | 185-194 | Inserts new parent rounds, reads generated IDs and batch-inserts child samples. Successful context-manager exit commits the transaction and then prints counts. |
| 186 | 185-194 | Inserts new parent rounds, reads generated IDs and batch-inserts child samples. Successful context-manager exit commits the transaction and then prints counts. |
| 187 | 185-194 | Inserts new parent rounds, reads generated IDs and batch-inserts child samples. Successful context-manager exit commits the transaction and then prints counts. |
| 188 | 185-194 | Inserts new parent rounds, reads generated IDs and batch-inserts child samples. Successful context-manager exit commits the transaction and then prints counts. |
| 189 | 185-194 | Inserts new parent rounds, reads generated IDs and batch-inserts child samples. Successful context-manager exit commits the transaction and then prints counts. |
| 190 | 185-194 | Inserts new parent rounds, reads generated IDs and batch-inserts child samples. Successful context-manager exit commits the transaction and then prints counts. |
| 191 | 185-194 | Inserts new parent rounds, reads generated IDs and batch-inserts child samples. Successful context-manager exit commits the transaction and then prints counts. |
| 192 | 185-194 | Inserts new parent rounds, reads generated IDs and batch-inserts child samples. Successful context-manager exit commits the transaction and then prints counts. |
| 193 | 185-194 | Inserts new parent rounds, reads generated IDs and batch-inserts child samples. Successful context-manager exit commits the transaction and then prints counts. |
| 194 | 185-194 | Inserts new parent rounds, reads generated IDs and batch-inserts child samples. Successful context-manager exit commits the transaction and then prints counts. |
| 195 | 195 | Blank separator; no execution. |
| 196 | 196 | Blank separator; no execution. |
| 197 | 197-207 | Function declaration: this body runs when called, not at declaration time. |
| 198 | 197-207 | Parses command-line paths, database arguments and check-only. This importer's host/port/database/user defaults are CLI values, unlike some sibling scripts' PG environment defaults. |
| 199 | 197-207 | Parses command-line paths, database arguments and check-only. This importer's host/port/database/user defaults are CLI values, unlike some sibling scripts' PG environment defaults. |
| 200 | 197-207 | Parses command-line paths, database arguments and check-only. This importer's host/port/database/user defaults are CLI values, unlike some sibling scripts' PG environment defaults. |
| 201 | 197-207 | Parses command-line paths, database arguments and check-only. This importer's host/port/database/user defaults are CLI values, unlike some sibling scripts' PG environment defaults. |
| 202 | 197-207 | Parses command-line paths, database arguments and check-only. This importer's host/port/database/user defaults are CLI values, unlike some sibling scripts' PG environment defaults. |
| 203 | 197-207 | Parses command-line paths, database arguments and check-only. This importer's host/port/database/user defaults are CLI values, unlike some sibling scripts' PG environment defaults. |
| 204 | 197-207 | Parses command-line paths, database arguments and check-only. This importer's host/port/database/user defaults are CLI values, unlike some sibling scripts' PG environment defaults. |
| 205 | 197-207 | Parses command-line paths, database arguments and check-only. This importer's host/port/database/user defaults are CLI values, unlike some sibling scripts' PG environment defaults. |
| 206 | 197-207 | Exception-control block: separates normal work, error handling and cleanup. |
| 207 | 197-207 | Parses command-line paths, database arguments and check-only. This importer's host/port/database/user defaults are CLI values, unlike some sibling scripts' PG environment defaults. |
| 208 | 208-215 | Conditional branch: determines which following statements run. |
| 209 | 208-215 | Validates raw files first; check-only makes no database connection. Otherwise writes transactionally, reporting failures with exit code 1. |
| 210 | 208-215 | Conditional branch: determines which following statements run. |
| 211 | 208-215 | Validates raw files first; check-only makes no database connection. Otherwise writes transactionally, reporting failures with exit code 1. |
| 212 | 208-215 | Exception-control block: separates normal work, error handling and cleanup. |
| 213 | 208-215 | Validates raw files first; check-only makes no database connection. Otherwise writes transactionally, reporting failures with exit code 1. |
| 214 | 208-215 | Validates raw files first; check-only makes no database connection. Otherwise writes transactionally, reporting failures with exit code 1. |
| 215 | 208-215 | Failure path: interrupts normal execution with the stated exception. |
| 216 | 216 | Blank separator; no execution. |
| 217 | 217 | Blank separator; no execution. |
| 218 | 218-219 | Conditional branch: determines which following statements run. |
| 219 | 218-219 | Runs main only when invoked as a script, allowing the parsing helpers and schema to be imported safely elsewhere. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  r"""Import the 12 original experiment exports into decision_lab.
   2  
   3  Run from VS Code (Windows):
   4    .\.venv\Scripts\python.exe import_data.py --check-only
   5    .\.venv\Scripts\python.exe import_data.py
   6  
   7  No model filtering/normalization is applied. Blank sequences are counted and
   8  skipped; one-sample rounds are retained. Original files remain untouched.
   9  Passwords are requested privately at runtime, never embedded in this script.
  10  """
  11  import argparse
  12  import ast
  13  import getpass
  14  import json
  15  import math
  16  import os
  17  from pathlib import Path
  18  import re
  19  
  20  import pandas as pd
  21  
  22  SESSIONS = {
  23      'feb18': ('2026-02-18', 0, 100, 'all_apps_wide-2026-02-18-{}.csv'),
  24      'feb20': ('2026-02-20', 0, 100, 'all_apps_wide-2026-02-20-{}.csv'),
  25      'march6': ('2025-03-06', -20, 20, 'Game {}.xlsx'),
  26  }
  27  SCHEMA = """
  28  CREATE TABLE IF NOT EXISTS experiment_sessions (
  29   session_id TEXT PRIMARY KEY, session_date DATE NOT NULL,
  30   x_min DOUBLE PRECISION NOT NULL, x_max DOUBLE PRECISION NOT NULL,
  31   CHECK (x_max > x_min));
  32  CREATE TABLE IF NOT EXISTS participant_rounds (
  33   participant_round_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  34   session_id TEXT NOT NULL REFERENCES experiment_sessions(session_id),
  35   participant_id INTEGER NOT NULL,
  36   game_number INTEGER NOT NULL CHECK(game_number BETWEEN 1 AND 4),
  37   round_number INTEGER NOT NULL CHECK(round_number > 0),
  38   group_id INTEGER, opponent_group_id INTEGER,
  39   recorded_payoff DOUBLE PRECISION, team_won BOOLEAN,
  40   UNIQUE(session_id, participant_id, game_number, round_number));
  41  CREATE TABLE IF NOT EXISTS samples (
  42   sample_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  43   participant_round_id BIGINT NOT NULL REFERENCES participant_rounds(participant_round_id),
  44   step_number INTEGER NOT NULL CHECK(step_number > 0),
  45   x_value DOUBLE PRECISION NOT NULL, observed_value DOUBLE PRECISION NOT NULL,
  46   sampled_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
  47   UNIQUE(participant_round_id, step_number));
  48  """
  49  
  50  
  51  def number(value):
  52      if value is None or pd.isna(value):
  53          return None
  54      result = float(value)
  55      if not math.isfinite(result):
  56          raise ValueError(f'Non-finite number: {value}')
  57      return result
  58  
  59  
  60  def integer(value):
  61      result = number(value)
  62      if result is None or result != int(result):
  63          raise ValueError(f'Expected an integer, got {value}')
  64      return int(result)
  65  
  66  
  67  def sequence(value):
  68      if value is None or (isinstance(value, float) and pd.isna(value)):
  69          return []
  70      if isinstance(value, str):
  71          if not value.strip():
  72              return []
  73          try:
  74              value = json.loads(value)
  75          except json.JSONDecodeError:
  76              value = ast.literal_eval(value)
  77      if not isinstance(value, (list, tuple)):
  78          raise ValueError('Expected a list of records')
  79      return value
  80  
  81  
  82  def read_exports(root):
  83      records, seen = [], set()
  84      total_empty = 0
  85      for session, (_, xmin, xmax, pattern) in SESSIONS.items():
  86          for game in range(1, 5):
  87              matches = list(root.rglob(pattern.format(game)))
  88              if len(matches) != 1:
  89                  raise ValueError(f'Expected exactly one {pattern.format(game)}; found {len(matches)}')
  90              path = matches[0]
  91              df = pd.read_csv(path) if path.suffix == '.csv' else pd.read_excel(path)
  92              columns = sorted(
  93                  (c for c in df.columns if re.fullmatch(rf'guess4{game}\.\d+\.player\.samples', c)),
  94                  key=lambda c: int(c.split('.')[1]))
  95              if not columns:
  96                  raise ValueError(f'No expected sample columns in {path.name}')
  97              nrounds = nsamples = empty = 0
  98              for column in columns:
  99                  prefix = column.removesuffix('.player.samples')
 100                  rnd = int(prefix.split('.')[1])
 101                  opponents = {}
 102                  for a, b in sequence(df[f'{prefix}.subsession.paired_groups'].iloc[0]):
 103                      opponents[integer(a)] = integer(b)
 104                      opponents[integer(b)] = integer(a)
 105                  for _, row in df.iterrows():
 106                      # Excel exports can include entirely unused participant rows.
 107                      if pd.isna(row['participant.id_in_session']):
 108                          continue
 109                      raw_samples = sequence(row[column])
 110                      if not raw_samples:
 111                          empty += 1
 112                          continue
 113                      pid = integer(row['participant.id_in_session'])
 114                      gid = integer(row[f'{prefix}.player.record_group_id'])
 115                      key = (session, pid, game, rnd)
 116                      if key in seen:
 117                          raise ValueError(f'Duplicate participant-round: {key}')
 118                      seen.add(key)
 119                      payoff = number(row.get(f'{prefix}.player.payoff_float'))
 120                      fallback = number(row.get(f'{prefix}.player.payoff'))
 121                      # Match the existing default preprocessing script's fallback.
 122                      if payoff in (None, 0) and fallback is not None:
 123                          payoff = fallback
 124                      won = number(row.get(f'{prefix}.group.is_win'))
 125                      if won not in (None, 0, 1):
 126                          raise ValueError(f'Unexpected win flag: {key}')
 127                      events = []
 128                      for step, sample in enumerate(raw_samples, 1):
 129                          if len(sample) != 3:
 130                              raise ValueError(f'Expected [value, x, timestamp]: {key}, step {step}')
 131                          value, x, time = sample
 132                          x, value = number(x), number(value)
 133                          if x is None or value is None or not xmin <= x <= xmax:
 134                              raise ValueError(f'Invalid sample values: {key}, step {step}')
 135                          timestamp = pd.Timestamp(time)
 136                          if pd.isna(timestamp) or timestamp.tzinfo is not None:
 137                              raise ValueError(f'Missing/timezone-aware timestamp: {key}, step {step}')
 138                          timestamp = timestamp.to_pydatetime()
 139                          if events and timestamp < events[-1][3]:
 140                              raise ValueError(f'Sample timestamps out of order: {key}')
 141                          events.append((step, x, value, timestamp))
 142                      records.append((key, (gid, opponents.get(gid), payoff,
 143                                           None if won is None else bool(won)), events))
 144                      nrounds += 1
 145                      nsamples += len(events)
 146              total_empty += empty
 147              print(f'{session:7} game {game}: {nrounds:4} rounds, {nsamples:5} samples; {empty} empty sequences')
 148      print(f'TOTAL: {len(records):,} rounds; {sum(len(r[2]) for r in records):,} samples')
 149      print(f'Empty sequences skipped: {total_empty}. One-sample rounds retained.')
 150      return records
 151  
 152  
 153  def import_records(records, args):
 154      import psycopg
 155      password = os.getenv('PGPASSWORD')
 156      if password is None:
 157          password = getpass.getpass(f'PostgreSQL password for {args.user}: ')
 158      # One transaction: either the entire import commits or none of it does.
 159      with psycopg.connect(host=args.host, port=args.port, dbname=args.database,
 160                           user=args.user, password=password, connect_timeout=10) as conn:
 161          with conn.cursor() as cur:
 162              cur.execute(SCHEMA)
 163              # Serialize concurrent runs of this importer.
 164              cur.execute('SELECT pg_advisory_xact_lock(20260908)')
 165              for session, (date, xmin, xmax, _) in SESSIONS.items():
 166                  cur.execute('INSERT INTO experiment_sessions VALUES (%s,%s,%s,%s) ON CONFLICT DO NOTHING',
 167                              (session, date, xmin, xmax))
 168                  cur.execute('SELECT session_date::text, x_min, x_max FROM experiment_sessions WHERE session_id=%s', (session,))
 169                  if cur.fetchone() != (date, xmin, xmax):
 170                      raise ValueError(f'Existing session metadata differs: {session}')
 171              added = unchanged = 0
 172              for key, metadata, events in records:
 173                  cur.execute('''SELECT participant_round_id, group_id, opponent_group_id,
 174                                 recorded_payoff, team_won FROM participant_rounds
 175                                 WHERE session_id=%s AND participant_id=%s AND game_number=%s AND round_number=%s''', key)
 176                  existing = cur.fetchone()
 177                  if existing:
 178                      round_id = existing[0]
 179                      cur.execute('''SELECT step_number, x_value, observed_value, sampled_at
 180                                     FROM samples WHERE participant_round_id=%s ORDER BY step_number''', (round_id,))
 181                      if tuple(existing[1:]) != metadata or cur.fetchall() != events:
 182                          raise ValueError(f'Existing data differs for {key}; refusing to overwrite it.')
 183                      unchanged += 1
 184                      continue
 185                  cur.execute('''INSERT INTO participant_rounds
 186                      (session_id, participant_id, game_number, round_number,
 187                       group_id, opponent_group_id, recorded_payoff, team_won)
 188                      VALUES (%s,%s,%s,%s,%s,%s,%s,%s) RETURNING participant_round_id''', key + metadata)
 189                  round_id = cur.fetchone()[0]
 190                  cur.executemany('''INSERT INTO samples
 191                      (participant_round_id, step_number, x_value, observed_value, sampled_at)
 192                      VALUES (%s,%s,%s,%s,%s)''', [(round_id,) + e for e in events])
 193                  added += 1
 194      print(f'COMMITTED: {added:,} new rounds; {unchanged:,} identical rounds already present.')
 195  
 196  
 197  def main():
 198      parser = argparse.ArgumentParser(description=__doc__)
 199      parser.add_argument('--raw-dir', type=Path, default=Path(__file__).resolve().parent / 'data' / 'raw')
 200      parser.add_argument('--check-only', action='store_true', help='Validate files without connecting to PostgreSQL')
 201      parser.add_argument('--host', default='localhost')
 202      parser.add_argument('--port', type=int, default=5432)
 203      parser.add_argument('--database', default='decision_lab')
 204      parser.add_argument('--user', default='postgres')
 205      args = parser.parse_args()
 206      try:
 207          records = read_exports(args.raw_dir)
 208          if args.check_only:
 209              print('Validation complete. No database changes made.')
 210          else:
 211              import_records(records, args)
 212      except Exception as exc:
 213          print(f'ERROR: {exc}')
 214          print('This run did not commit any database changes.')
 215          raise SystemExit(1)
 216  
 217  
 218  if __name__ == '__main__':
 219      main()
```
