# replay.html

Contains all production HTML, CSS and browser JavaScript. It requests historical JSON from FastAPI and draws SVG, without a frontend framework.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1-6 | Sets standards mode, English language, UTF-8, viewport sizing, browser title and the page description. |
| 7 | Begins inline CSS; no separate CSS build or downloaded UI framework is required. |
| 8 | Base styles define page widths, controls, panels, metric grids, chart/legend, results and responsive rules. Includes some unused styles left from earlier UI versions. Later declarations override earlier ones through CSS cascade. |
| 10 | Embeds DecisionPixel as a base64 font so headings render without a separate network fetch. This long payload is font data, not executable JavaScript or model parameters. |
| 11-17 | Overrides base colors, gradients, pixel headings, panels and controls with the final retro theme. |
| 18 | Legacy outcome-shell styles remain but the current results use a dialog rather than that former wrapper. |
| 19-20 | Styles the forecast panel and STOP/CONTINUE indicators, including the CSS stop-sign shape. |
| 21-23 | Styles metrics, chart, legends, axes explanation and result cards. Teammate colors are overridden to orange later. |
| 24-26 | Defines a glowing star and the fading upward sample-cost animation. |
| 27-28 | Adjusts mobile sizes and reduces animations when the viewer requests reduced motion. |
| 30 | Includes older legend-checkbox rules and intermediate model colors. Current legends are spans, so checkbox selectors no longer apply; later ice-blue styling wins. |
| 31-33 | Styles the persistent result button and scrollable native dialog with a backdrop, focus controls and reduced-motion handling. |
| 35-36 | Sets final slightly larger typography and ice-blue prediction styling. Mobile SVG text remains larger in viewBox coordinates. |
| 38-39 | Styles the references disclosure and sets chart aspect ratio 900/580. References remain collapsed because HTML omits the open attribute. |
| 40-42 | Ends styling/head metadata and begins the visible page body. |
| 43 | Provides Kaan's byline, the two central questions, business framing and concise experiment counts. These are static labels, not data queries. |
| 44-49 | Defines disabled initial session/game/player/round controls and live status regions; initialization fills choices from API responses. |
| 50-52 | Begins the main replay panel, adds analyst landscape reveal and a concise token/competition explanation. |
| 53 | Adds a collapsible headphone-company analogy, plus own-test count, remaining-budget bar, own-best metric and display clock. |
| 54-60 | Creates the empty accessible SVG with a 900×580 coordinate system and passive legend. JavaScript fills the SVG and hides inapplicable scenario legend entries. |
| 61 | Retains hidden teammate/opponent score panels for compatibility with existing JavaScript element references. Their values update but are not visible panels. |
| 62-63 | Adds current-event text, replay controls, slider and end-of-timeline results button. |
| 67 | Closes the main replay panel before the model section. |
| 69-70 | Defines opt-in model comparison fields and a concise method disclosure. UI claims summarize saved training choices; this file performs no training or threshold fitting. |
| 71-75 | Defines the result dialog and collapsed research section with five coauthored works, then closes the page content and links API docs. Manuscript statuses are author-supplied. |
| 76-80 | Starts JavaScript; provides the element lookup helper and session date/display-name maps. |
| 81-82 | Maps game numbers to sharing explanations and names the four selection controls. |
| 83-85 | Initializes request-generation counters, animation deadlines, timeline state, cancellation controller, prediction/result caches and playback timer. |
| 86 | Formats a normalized fraction as a one-decimal percentage for display. |
| 87 | Creates HTML elements using textContent for text, avoiding HTML interpretation of API-provided strings. |
| 88 | Creates SVG elements in the SVG namespace and sets supplied attributes/text. |
| 89 | Reads the four current selector values into query parameter names expected by FastAPI. |
| 90 | Fetches same-origin JSON with URLSearchParams and an abort signal. On HTTP failure, prefers a plain server detail string and otherwise reports status. |
| 91 | Updates page status and its error styling. |
| 92 | Replaces select options from value/label pairs; browser DOM construction is separate from API fetching. |
| 93 | Filters /rounds results for the selected player to populate their round choices. |
| 94 | Stops the playback interval and resets the Play label. |
| 95 | Invalidates pending result responses, closes the dialog and clears the result cache when replay selection/frame changes. |
| 96-99 | Starts a new selection load, cancels older requests, clears cached state and disables controls while data is loading. |
| 100-102 | On session/game changes, fetches /rounds and rebuilds participant/round menus; on player changes, only updates round choices. Rejects an empty selection. |
| 103-109 | Fetches /replay-story, ignores stale responses, stores the full permitted timeline and renders its initial frame. Recoverable errors restore selection controls. |
| 110 | Moves the visible-event count within valid bounds, invalidates frame-specific predictions/results and triggers animation only for one-step forward moves. |
| 111-114 | Derives visible own/mate events and their separate best samples. One replay frame is a merged event, not necessarily an own test. |
| 115-117 | Computes own token spending and displays metrics. Earlier teammate timestamps show Before first test, not a negative clock. |
| 118-121 | Updates scenario-specific teammate/rival values, including the legacy hidden panels. Rival x is never supplied or drawn. |
| 122 | Describes the latest visible event and its sample cost in an accessible status region. |
| 123-124 | Enables rewind/advance controls according to frame position and unlocks results only after the visible historical stream ends. |
| 125 | Allows the model toggle after three OWN samples. It does not yet display an x comparison until own test 4 is revealed. |
| 126-130 | Displays only a prediction matching the last revealed own event and current frame; shows probability, thresholded action and percentage-point x error. |
| 131-133 | Draws the chart and schedules a model lookup after rendering when at least four own events are visible. predictionKey prevents repeated requests from the render loop. |
| 134-137 | Returns null for mismatched/early comparisons; otherwise error = 100 × absolute(predicted normalized x minus actual normalized x). It is not uncertainty or relative percentage error. |
| 138-142 | Clears and describes the SVG, determines visible/landscape y limits and obtains the allowed competitor score. Y limits can change as more observations are revealed. |
| 143 | Maps normalized x to 76..866 and y values to 450..110. Separate text rows above/below this rectangle prevent annotation/axis collisions. |
| 144 | Updates the competitor legend with the most recent visible benchmark when permitted. |
| 145-146 | Draws 21 vertical and 9 horizontal mesh lines with stronger major lines. |
| 147-149 | Draws both axes, ticks and percentage labels. The x title is at y560, below the error bracket at y518. |
| 150-151 | Draws the optional objective curve and red dashed rival-best horizontal line. Neither is an LSTM y-head prediction. |
| 152-158 | Finds the highest sampled landscape point, builds a 10-vertex star, adds accessibility text and puts its label at fixed y55. This sampled peak is approximate. |
| 159 | Draws the actual-vs-predicted x distance at y518 with caps and a label at y503. It omits the graphical bracket for an out-of-domain predicted x; numeric error still exists. |
| 160 | Draws an ice-blue dashed vertical x prediction with its label at y85, separate from the star label at y55. Out-of-range predictions are reported without clipping. |
| 161 | Draws own circles and teammate squares; the latest event is gold and slightly larger. Each marker carries readable player/step/coordinate accessibility text. The always-true filter is a remnant of removed layer controls. |
| 162 | Adds a ring around the focal player's own best sampled point, which may differ from the team's visible best used in model features. |
| 163 | Draws the transient token-cost text near the current point when a one-event forward animation is active. |
| 164-165 | Adds an initial prompt if there are no revealed tests/curve and ends the draw function. |
| 166-169 | Loads a comparison only from own test 4 onward; captures version, frame and generation, and requests after_step = current own step minus one. |
| 170-175 | Reuses per-round cached predictions or calls /predict; ignores stale responses and labels the observed next sample as CONTINUE. Renders either the matched result or a recoverable error. |
| 176-180 | Pauses replay, requests final outcomes once at timeline end and reopens cached results on subsequent clicks. Displays win/loss only for consistent complete records. |
| 181-183 | Builds both team's player cards, budgets and payoff. Payoff displays zero decimals but its tooltip preserves the underlying value; missing records are labeled. |
| 184-185 | On a current results-request error, restores the button and reports it; stale/aborted results do not overwrite a new selection. |
| 186-191 | Optionally compares the stop decision at the final own prefix, including an exactly-three-own-test round. No next-position error is computed after stopping; prediction failure does not hide recorded outcomes. |
| 192 | Closes the terminal-stop helper. |
| 193 | Connects selection changes to the appropriate reload behavior. |
| 194 | Connects Next, Previous, Reset and slider controls; manual actions pause automatic playback first. |
| 195 | Advances one merged event immediately and then every second until the end. This is a playback pace, not the original physical sampling speed. |
| 196 | Toggles model comparison while invalidating in-flight results and wires the final-results button. |
| 197 | Fetches a 1000-point landscape only on demand, caches it for the selection and ignores stale responses; reveal controls glow and redraw. |
| 198 | Bootstraps the page by loading sessions, selecting February 18 when present and loading its first available round. There is no offline fetch shim in production. |
| 199 | Closes the JavaScript, page body and document. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1-6 | Sets standards mode, English language, UTF-8, viewport sizing, browser title and the page description. |
| 2 | 1-6 | Sets standards mode, English language, UTF-8, viewport sizing, browser title and the page description. |
| 3 | 1-6 | Sets standards mode, English language, UTF-8, viewport sizing, browser title and the page description. |
| 4 | 1-6 | Sets standards mode, English language, UTF-8, viewport sizing, browser title and the page description. |
| 5 | 1-6 | Sets standards mode, English language, UTF-8, viewport sizing, browser title and the page description. |
| 6 | 1-6 | Sets standards mode, English language, UTF-8, viewport sizing, browser title and the page description. |
| 7 | 7 | Begins inline CSS; no separate CSS build or downloaded UI framework is required. |
| 8 | 8 | Base styles define page widths, controls, panels, metric grids, chart/legend, results and responsive rules. Includes some unused styles left from earlier UI versions. Later declarations override earlier ones through CSS cascade. |
| 9 | 9 | Blank separator; no execution. |
| 10 | 10 | Embeds DecisionPixel as a base64 font so headings render without a separate network fetch. This long payload is font data, not executable JavaScript or model parameters. |
| 11 | 11-17 | Overrides base colors, gradients, pixel headings, panels and controls with the final retro theme. |
| 12 | 11-17 | Overrides base colors, gradients, pixel headings, panels and controls with the final retro theme. |
| 13 | 11-17 | Overrides base colors, gradients, pixel headings, panels and controls with the final retro theme. |
| 14 | 11-17 | Overrides base colors, gradients, pixel headings, panels and controls with the final retro theme. |
| 15 | 11-17 | Overrides base colors, gradients, pixel headings, panels and controls with the final retro theme. |
| 16 | 11-17 | Overrides base colors, gradients, pixel headings, panels and controls with the final retro theme. |
| 17 | 11-17 | Overrides base colors, gradients, pixel headings, panels and controls with the final retro theme. |
| 18 | 18 | Legacy outcome-shell styles remain but the current results use a dialog rather than that former wrapper. |
| 19 | 19-20 | Styles the forecast panel and STOP/CONTINUE indicators, including the CSS stop-sign shape. |
| 20 | 19-20 | Styles the forecast panel and STOP/CONTINUE indicators, including the CSS stop-sign shape. |
| 21 | 21-23 | Styles metrics, chart, legends, axes explanation and result cards. Teammate colors are overridden to orange later. |
| 22 | 21-23 | Styles metrics, chart, legends, axes explanation and result cards. Teammate colors are overridden to orange later. |
| 23 | 21-23 | Styles metrics, chart, legends, axes explanation and result cards. Teammate colors are overridden to orange later. |
| 24 | 24-26 | Defines a glowing star and the fading upward sample-cost animation. |
| 25 | 24-26 | Defines a glowing star and the fading upward sample-cost animation. |
| 26 | 24-26 | Defines a glowing star and the fading upward sample-cost animation. |
| 27 | 27-28 | Adjusts mobile sizes and reduces animations when the viewer requests reduced motion. |
| 28 | 27-28 | Adjusts mobile sizes and reduces animations when the viewer requests reduced motion. |
| 29 | 29 | Blank separator; no execution. |
| 30 | 30 | Includes older legend-checkbox rules and intermediate model colors. Current legends are spans, so checkbox selectors no longer apply; later ice-blue styling wins. |
| 31 | 31-33 | Styles the persistent result button and scrollable native dialog with a backdrop, focus controls and reduced-motion handling. |
| 32 | 31-33 | Styles the persistent result button and scrollable native dialog with a backdrop, focus controls and reduced-motion handling. |
| 33 | 31-33 | Styles the persistent result button and scrollable native dialog with a backdrop, focus controls and reduced-motion handling. |
| 34 | 34 | Blank separator; no execution. |
| 35 | 35-36 | Sets final slightly larger typography and ice-blue prediction styling. Mobile SVG text remains larger in viewBox coordinates. |
| 36 | 35-36 | Sets final slightly larger typography and ice-blue prediction styling. Mobile SVG text remains larger in viewBox coordinates. |
| 37 | 37 | Blank separator; no execution. |
| 38 | 38-39 | Styles the references disclosure and sets chart aspect ratio 900/580. References remain collapsed because HTML omits the open attribute. |
| 39 | 38-39 | Styles the references disclosure and sets chart aspect ratio 900/580. References remain collapsed because HTML omits the open attribute. |
| 40 | 40-42 | Ends styling/head metadata and begins the visible page body. |
| 41 | 40-42 | Ends styling/head metadata and begins the visible page body. |
| 42 | 40-42 | Ends styling/head metadata and begins the visible page body. |
| 43 | 43 | Provides Kaan's byline, the two central questions, business framing and concise experiment counts. These are static labels, not data queries. |
| 44 | 44-49 | Defines disabled initial session/game/player/round controls and live status regions; initialization fills choices from API responses. |
| 45 | 44-49 | Defines disabled initial session/game/player/round controls and live status regions; initialization fills choices from API responses. |
| 46 | 44-49 | Defines disabled initial session/game/player/round controls and live status regions; initialization fills choices from API responses. |
| 47 | 44-49 | Defines disabled initial session/game/player/round controls and live status regions; initialization fills choices from API responses. |
| 48 | 44-49 | Defines disabled initial session/game/player/round controls and live status regions; initialization fills choices from API responses. |
| 49 | 44-49 | Defines disabled initial session/game/player/round controls and live status regions; initialization fills choices from API responses. |
| 50 | 50-52 | Begins the main replay panel, adds analyst landscape reveal and a concise token/competition explanation. |
| 51 | 50-52 | Begins the main replay panel, adds analyst landscape reveal and a concise token/competition explanation. |
| 52 | 50-52 | Begins the main replay panel, adds analyst landscape reveal and a concise token/competition explanation. |
| 53 | 53 | Adds a collapsible headphone-company analogy, plus own-test count, remaining-budget bar, own-best metric and display clock. |
| 54 | 54-60 | Creates the empty accessible SVG with a 900×580 coordinate system and passive legend. JavaScript fills the SVG and hides inapplicable scenario legend entries. |
| 55 | 54-60 | Creates the empty accessible SVG with a 900×580 coordinate system and passive legend. JavaScript fills the SVG and hides inapplicable scenario legend entries. |
| 56 | 54-60 | Creates the empty accessible SVG with a 900×580 coordinate system and passive legend. JavaScript fills the SVG and hides inapplicable scenario legend entries. |
| 57 | 54-60 | Creates the empty accessible SVG with a 900×580 coordinate system and passive legend. JavaScript fills the SVG and hides inapplicable scenario legend entries. |
| 58 | 54-60 | Creates the empty accessible SVG with a 900×580 coordinate system and passive legend. JavaScript fills the SVG and hides inapplicable scenario legend entries. |
| 59 | 54-60 | Creates the empty accessible SVG with a 900×580 coordinate system and passive legend. JavaScript fills the SVG and hides inapplicable scenario legend entries. |
| 60 | 54-60 | Creates the empty accessible SVG with a 900×580 coordinate system and passive legend. JavaScript fills the SVG and hides inapplicable scenario legend entries. |
| 61 | 61 | Retains hidden teammate/opponent score panels for compatibility with existing JavaScript element references. Their values update but are not visible panels. |
| 62 | 62-63 | Adds current-event text, replay controls, slider and end-of-timeline results button. |
| 63 | 62-63 | Adds current-event text, replay controls, slider and end-of-timeline results button. |
| 64 | 64 | Blank separator; no execution. |
| 65 | 65 | Blank separator; no execution. |
| 66 | 66 | Blank separator; no execution. |
| 67 | 67 | Closes the main replay panel before the model section. |
| 68 | 68 | Blank separator; no execution. |
| 69 | 69-70 | Defines opt-in model comparison fields and a concise method disclosure. UI claims summarize saved training choices; this file performs no training or threshold fitting. |
| 70 | 69-70 | Defines opt-in model comparison fields and a concise method disclosure. UI claims summarize saved training choices; this file performs no training or threshold fitting. |
| 71 | 71-75 | Defines the result dialog and collapsed research section with five coauthored works, then closes the page content and links API docs. Manuscript statuses are author-supplied. |
| 72 | 71-75 | Defines the result dialog and collapsed research section with five coauthored works, then closes the page content and links API docs. Manuscript statuses are author-supplied. |
| 73 | 71-75 | Defines the result dialog and collapsed research section with five coauthored works, then closes the page content and links API docs. Manuscript statuses are author-supplied. |
| 74 | 71-75 | Defines the result dialog and collapsed research section with five coauthored works, then closes the page content and links API docs. Manuscript statuses are author-supplied. |
| 75 | 71-75 | Blank separator; no execution. |
| 76 | 76-80 | Starts JavaScript; provides the element lookup helper and session date/display-name maps. |
| 77 | 76-80 | Starts JavaScript; provides the element lookup helper and session date/display-name maps. |
| 78 | 76-80 | Starts JavaScript; provides the element lookup helper and session date/display-name maps. |
| 79 | 76-80 | Starts JavaScript; provides the element lookup helper and session date/display-name maps. |
| 80 | 76-80 | Starts JavaScript; provides the element lookup helper and session date/display-name maps. |
| 81 | 81-82 | Maps game numbers to sharing explanations and names the four selection controls. |
| 82 | 81-82 | Maps game numbers to sharing explanations and names the four selection controls. |
| 83 | 83-85 | Initializes request-generation counters, animation deadlines, timeline state, cancellation controller, prediction/result caches and playback timer. |
| 84 | 83-85 | Initializes request-generation counters, animation deadlines, timeline state, cancellation controller, prediction/result caches and playback timer. |
| 85 | 83-85 | Initializes request-generation counters, animation deadlines, timeline state, cancellation controller, prediction/result caches and playback timer. |
| 86 | 86 | Formats a normalized fraction as a one-decimal percentage for display. |
| 87 | 87 | Creates HTML elements using textContent for text, avoiding HTML interpretation of API-provided strings. |
| 88 | 88 | Creates SVG elements in the SVG namespace and sets supplied attributes/text. |
| 89 | 89 | Reads the four current selector values into query parameter names expected by FastAPI. |
| 90 | 90 | Fetches same-origin JSON with URLSearchParams and an abort signal. On HTTP failure, prefers a plain server detail string and otherwise reports status. |
| 91 | 91 | Updates page status and its error styling. |
| 92 | 92 | Replaces select options from value/label pairs; browser DOM construction is separate from API fetching. |
| 93 | 93 | Filters /rounds results for the selected player to populate their round choices. |
| 94 | 94 | Stops the playback interval and resets the Play label. |
| 95 | 95 | Invalidates pending result responses, closes the dialog and clears the result cache when replay selection/frame changes. |
| 96 | 96-99 | Starts a new selection load, cancels older requests, clears cached state and disables controls while data is loading. |
| 97 | 96-99 | Starts a new selection load, cancels older requests, clears cached state and disables controls while data is loading. |
| 98 | 96-99 | Starts a new selection load, cancels older requests, clears cached state and disables controls while data is loading. |
| 99 | 96-99 | Starts a new selection load, cancels older requests, clears cached state and disables controls while data is loading. |
| 100 | 100-102 | On session/game changes, fetches /rounds and rebuilds participant/round menus; on player changes, only updates round choices. Rejects an empty selection. |
| 101 | 100-102 | On session/game changes, fetches /rounds and rebuilds participant/round menus; on player changes, only updates round choices. Rejects an empty selection. |
| 102 | 100-102 | On session/game changes, fetches /rounds and rebuilds participant/round menus; on player changes, only updates round choices. Rejects an empty selection. |
| 103 | 103-109 | Fetches /replay-story, ignores stale responses, stores the full permitted timeline and renders its initial frame. Recoverable errors restore selection controls. |
| 104 | 103-109 | Fetches /replay-story, ignores stale responses, stores the full permitted timeline and renders its initial frame. Recoverable errors restore selection controls. |
| 105 | 103-109 | Fetches /replay-story, ignores stale responses, stores the full permitted timeline and renders its initial frame. Recoverable errors restore selection controls. |
| 106 | 103-109 | Fetches /replay-story, ignores stale responses, stores the full permitted timeline and renders its initial frame. Recoverable errors restore selection controls. |
| 107 | 103-109 | Fetches /replay-story, ignores stale responses, stores the full permitted timeline and renders its initial frame. Recoverable errors restore selection controls. |
| 108 | 103-109 | Fetches /replay-story, ignores stale responses, stores the full permitted timeline and renders its initial frame. Recoverable errors restore selection controls. |
| 109 | 103-109 | Fetches /replay-story, ignores stale responses, stores the full permitted timeline and renders its initial frame. Recoverable errors restore selection controls. |
| 110 | 110 | Moves the visible-event count within valid bounds, invalidates frame-specific predictions/results and triggers animation only for one-step forward moves. |
| 111 | 111-114 | Derives visible own/mate events and their separate best samples. One replay frame is a merged event, not necessarily an own test. |
| 112 | 111-114 | Derives visible own/mate events and their separate best samples. One replay frame is a merged event, not necessarily an own test. |
| 113 | 111-114 | Derives visible own/mate events and their separate best samples. One replay frame is a merged event, not necessarily an own test. |
| 114 | 111-114 | Derives visible own/mate events and their separate best samples. One replay frame is a merged event, not necessarily an own test. |
| 115 | 115-117 | Computes own token spending and displays metrics. Earlier teammate timestamps show Before first test, not a negative clock. |
| 116 | 115-117 | Computes own token spending and displays metrics. Earlier teammate timestamps show Before first test, not a negative clock. |
| 117 | 115-117 | Computes own token spending and displays metrics. Earlier teammate timestamps show Before first test, not a negative clock. |
| 118 | 118-121 | Updates scenario-specific teammate/rival values, including the legacy hidden panels. Rival x is never supplied or drawn. |
| 119 | 118-121 | Updates scenario-specific teammate/rival values, including the legacy hidden panels. Rival x is never supplied or drawn. |
| 120 | 118-121 | Updates scenario-specific teammate/rival values, including the legacy hidden panels. Rival x is never supplied or drawn. |
| 121 | 118-121 | Updates scenario-specific teammate/rival values, including the legacy hidden panels. Rival x is never supplied or drawn. |
| 122 | 122 | Describes the latest visible event and its sample cost in an accessible status region. |
| 123 | 123-124 | Enables rewind/advance controls according to frame position and unlocks results only after the visible historical stream ends. |
| 124 | 123-124 | Enables rewind/advance controls according to frame position and unlocks results only after the visible historical stream ends. |
| 125 | 125 | Allows the model toggle after three OWN samples. It does not yet display an x comparison until own test 4 is revealed. |
| 126 | 126-130 | Displays only a prediction matching the last revealed own event and current frame; shows probability, thresholded action and percentage-point x error. |
| 127 | 126-130 | Displays only a prediction matching the last revealed own event and current frame; shows probability, thresholded action and percentage-point x error. |
| 128 | 126-130 | Displays only a prediction matching the last revealed own event and current frame; shows probability, thresholded action and percentage-point x error. |
| 129 | 126-130 | Displays only a prediction matching the last revealed own event and current frame; shows probability, thresholded action and percentage-point x error. |
| 130 | 126-130 | Displays only a prediction matching the last revealed own event and current frame; shows probability, thresholded action and percentage-point x error. |
| 131 | 131-133 | Draws the chart and schedules a model lookup after rendering when at least four own events are visible. predictionKey prevents repeated requests from the render loop. |
| 132 | 131-133 | Draws the chart and schedules a model lookup after rendering when at least four own events are visible. predictionKey prevents repeated requests from the render loop. |
| 133 | 131-133 | Draws the chart and schedules a model lookup after rendering when at least four own events are visible. predictionKey prevents repeated requests from the render loop. |
| 134 | 134-137 | Returns null for mismatched/early comparisons; otherwise error = 100 × absolute(predicted normalized x minus actual normalized x). It is not uncertainty or relative percentage error. |
| 135 | 134-137 | Returns null for mismatched/early comparisons; otherwise error = 100 × absolute(predicted normalized x minus actual normalized x). It is not uncertainty or relative percentage error. |
| 136 | 134-137 | Returns null for mismatched/early comparisons; otherwise error = 100 × absolute(predicted normalized x minus actual normalized x). It is not uncertainty or relative percentage error. |
| 137 | 134-137 | Returns null for mismatched/early comparisons; otherwise error = 100 × absolute(predicted normalized x minus actual normalized x). It is not uncertainty or relative percentage error. |
| 138 | 138-142 | Clears and describes the SVG, determines visible/landscape y limits and obtains the allowed competitor score. Y limits can change as more observations are revealed. |
| 139 | 138-142 | Clears and describes the SVG, determines visible/landscape y limits and obtains the allowed competitor score. Y limits can change as more observations are revealed. |
| 140 | 138-142 | Clears and describes the SVG, determines visible/landscape y limits and obtains the allowed competitor score. Y limits can change as more observations are revealed. |
| 141 | 138-142 | Clears and describes the SVG, determines visible/landscape y limits and obtains the allowed competitor score. Y limits can change as more observations are revealed. |
| 142 | 138-142 | Clears and describes the SVG, determines visible/landscape y limits and obtains the allowed competitor score. Y limits can change as more observations are revealed. |
| 143 | 143 | Maps normalized x to 76..866 and y values to 450..110. Separate text rows above/below this rectangle prevent annotation/axis collisions. |
| 144 | 144 | Updates the competitor legend with the most recent visible benchmark when permitted. |
| 145 | 145-146 | Draws 21 vertical and 9 horizontal mesh lines with stronger major lines. |
| 146 | 145-146 | Draws 21 vertical and 9 horizontal mesh lines with stronger major lines. |
| 147 | 147-149 | Draws both axes, ticks and percentage labels. The x title is at y560, below the error bracket at y518. |
| 148 | 147-149 | Draws both axes, ticks and percentage labels. The x title is at y560, below the error bracket at y518. |
| 149 | 147-149 | Draws both axes, ticks and percentage labels. The x title is at y560, below the error bracket at y518. |
| 150 | 150-151 | Draws the optional objective curve and red dashed rival-best horizontal line. Neither is an LSTM y-head prediction. |
| 151 | 150-151 | Draws the optional objective curve and red dashed rival-best horizontal line. Neither is an LSTM y-head prediction. |
| 152 | 152-158 | Finds the highest sampled landscape point, builds a 10-vertex star, adds accessibility text and puts its label at fixed y55. This sampled peak is approximate. |
| 153 | 152-158 | Finds the highest sampled landscape point, builds a 10-vertex star, adds accessibility text and puts its label at fixed y55. This sampled peak is approximate. |
| 154 | 152-158 | Finds the highest sampled landscape point, builds a 10-vertex star, adds accessibility text and puts its label at fixed y55. This sampled peak is approximate. |
| 155 | 152-158 | Finds the highest sampled landscape point, builds a 10-vertex star, adds accessibility text and puts its label at fixed y55. This sampled peak is approximate. |
| 156 | 152-158 | Finds the highest sampled landscape point, builds a 10-vertex star, adds accessibility text and puts its label at fixed y55. This sampled peak is approximate. |
| 157 | 152-158 | Finds the highest sampled landscape point, builds a 10-vertex star, adds accessibility text and puts its label at fixed y55. This sampled peak is approximate. |
| 158 | 152-158 | Finds the highest sampled landscape point, builds a 10-vertex star, adds accessibility text and puts its label at fixed y55. This sampled peak is approximate. |
| 159 | 159 | Draws the actual-vs-predicted x distance at y518 with caps and a label at y503. It omits the graphical bracket for an out-of-domain predicted x; numeric error still exists. |
| 160 | 160 | Draws an ice-blue dashed vertical x prediction with its label at y85, separate from the star label at y55. Out-of-range predictions are reported without clipping. |
| 161 | 161 | Draws own circles and teammate squares; the latest event is gold and slightly larger. Each marker carries readable player/step/coordinate accessibility text. The always-true filter is a remnant of removed layer controls. |
| 162 | 162 | Adds a ring around the focal player's own best sampled point, which may differ from the team's visible best used in model features. |
| 163 | 163 | Draws the transient token-cost text near the current point when a one-event forward animation is active. |
| 164 | 164-165 | Adds an initial prompt if there are no revealed tests/curve and ends the draw function. |
| 165 | 164-165 | Adds an initial prompt if there are no revealed tests/curve and ends the draw function. |
| 166 | 166-169 | Loads a comparison only from own test 4 onward; captures version, frame and generation, and requests after_step = current own step minus one. |
| 167 | 166-169 | Loads a comparison only from own test 4 onward; captures version, frame and generation, and requests after_step = current own step minus one. |
| 168 | 166-169 | Loads a comparison only from own test 4 onward; captures version, frame and generation, and requests after_step = current own step minus one. |
| 169 | 166-169 | Loads a comparison only from own test 4 onward; captures version, frame and generation, and requests after_step = current own step minus one. |
| 170 | 170-175 | Reuses per-round cached predictions or calls /predict; ignores stale responses and labels the observed next sample as CONTINUE. Renders either the matched result or a recoverable error. |
| 171 | 170-175 | Reuses per-round cached predictions or calls /predict; ignores stale responses and labels the observed next sample as CONTINUE. Renders either the matched result or a recoverable error. |
| 172 | 170-175 | Reuses per-round cached predictions or calls /predict; ignores stale responses and labels the observed next sample as CONTINUE. Renders either the matched result or a recoverable error. |
| 173 | 170-175 | Reuses per-round cached predictions or calls /predict; ignores stale responses and labels the observed next sample as CONTINUE. Renders either the matched result or a recoverable error. |
| 174 | 170-175 | Reuses per-round cached predictions or calls /predict; ignores stale responses and labels the observed next sample as CONTINUE. Renders either the matched result or a recoverable error. |
| 175 | 170-175 | Reuses per-round cached predictions or calls /predict; ignores stale responses and labels the observed next sample as CONTINUE. Renders either the matched result or a recoverable error. |
| 176 | 176-180 | Pauses replay, requests final outcomes once at timeline end and reopens cached results on subsequent clicks. Displays win/loss only for consistent complete records. |
| 177 | 176-180 | Pauses replay, requests final outcomes once at timeline end and reopens cached results on subsequent clicks. Displays win/loss only for consistent complete records. |
| 178 | 176-180 | Pauses replay, requests final outcomes once at timeline end and reopens cached results on subsequent clicks. Displays win/loss only for consistent complete records. |
| 179 | 176-180 | Pauses replay, requests final outcomes once at timeline end and reopens cached results on subsequent clicks. Displays win/loss only for consistent complete records. |
| 180 | 176-180 | Pauses replay, requests final outcomes once at timeline end and reopens cached results on subsequent clicks. Displays win/loss only for consistent complete records. |
| 181 | 181-183 | Builds both team's player cards, budgets and payoff. Payoff displays zero decimals but its tooltip preserves the underlying value; missing records are labeled. |
| 182 | 181-183 | Builds both team's player cards, budgets and payoff. Payoff displays zero decimals but its tooltip preserves the underlying value; missing records are labeled. |
| 183 | 181-183 | Builds both team's player cards, budgets and payoff. Payoff displays zero decimals but its tooltip preserves the underlying value; missing records are labeled. |
| 184 | 184-185 | On a current results-request error, restores the button and reports it; stale/aborted results do not overwrite a new selection. |
| 185 | 184-185 | On a current results-request error, restores the button and reports it; stale/aborted results do not overwrite a new selection. |
| 186 | 186-191 | Optionally compares the stop decision at the final own prefix, including an exactly-three-own-test round. No next-position error is computed after stopping; prediction failure does not hide recorded outcomes. |
| 187 | 186-191 | Optionally compares the stop decision at the final own prefix, including an exactly-three-own-test round. No next-position error is computed after stopping; prediction failure does not hide recorded outcomes. |
| 188 | 186-191 | Optionally compares the stop decision at the final own prefix, including an exactly-three-own-test round. No next-position error is computed after stopping; prediction failure does not hide recorded outcomes. |
| 189 | 186-191 | Optionally compares the stop decision at the final own prefix, including an exactly-three-own-test round. No next-position error is computed after stopping; prediction failure does not hide recorded outcomes. |
| 190 | 186-191 | Optionally compares the stop decision at the final own prefix, including an exactly-three-own-test round. No next-position error is computed after stopping; prediction failure does not hide recorded outcomes. |
| 191 | 186-191 | Optionally compares the stop decision at the final own prefix, including an exactly-three-own-test round. No next-position error is computed after stopping; prediction failure does not hide recorded outcomes. |
| 192 | 192 | Closes the terminal-stop helper. |
| 193 | 193 | Connects selection changes to the appropriate reload behavior. |
| 194 | 194 | Connects Next, Previous, Reset and slider controls; manual actions pause automatic playback first. |
| 195 | 195 | Advances one merged event immediately and then every second until the end. This is a playback pace, not the original physical sampling speed. |
| 196 | 196 | Toggles model comparison while invalidating in-flight results and wires the final-results button. |
| 197 | 197 | Fetches a 1000-point landscape only on demand, caches it for the selection and ignores stale responses; reveal controls glow and redraw. |
| 198 | 198 | Bootstraps the page by loading sessions, selecting February 18 when present and loading its first available round. There is no offline fetch shim in production. |
| 199 | 199 | Closes the JavaScript, page body and document. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  <!doctype html>
   2  <html lang="en">
   3  <head>
   4  <meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
   5  <title>Decision Lab | Competition replay</title>
   6  <meta name="description" content="Explore how teams choose what to test and when to stop. Replay a real experiment and compare held-out machine-learning predictions with recorded decisions.">
   7  <style>
   8  :root{color-scheme:dark;font-family:system-ui,-apple-system,'Segoe UI',sans-serif;font-size:16px;background:#0c1420;color:#e7eff5;--mint:#63ebbc;--blue:#6ebeff;--gold:#ffc86a;--red:#ff8f98;--muted:#a7bac9;--line:#334656;--panel:#142230}*{box-sizing:border-box}body{margin:0}button,input,select{font:inherit}button,select{color:inherit;background:#1b2d3e;border:1px solid #526a7c;border-radius:3px;padding:10px 13px}button{cursor:pointer;font-weight:650}button:hover:enabled{background:#2d4557}button:disabled{opacity:.45;cursor:default}button.primary{color:#0c1420;background:var(--mint);border-color:var(--mint)}:focus-visible{outline:3px solid var(--gold);outline-offset:4px}a{color:var(--mint)}main,header,footer{max-width:1260px;margin:auto;padding:24px}.brand,.eyebrow,h1,h2,h3,.metric strong,.verdict{font-family:ui-monospace,Consolas,monospace}.brand{letter-spacing:.15em;text-transform:uppercase;color:var(--mint);font-weight:800;font-size:14px}.brand span{color:var(--muted);letter-spacing:0;margin-left:16px}header{padding-bottom:10px}h1{font-size:clamp(26px,3.1vw,38px);max-width:1000px;line-height:1.22;margin:18px 0 12px;letter-spacing:-.035em}header p{color:#bdccd8;line-height:1.65;max-width:960px;margin:0}main{padding-top:16px}.panel{background:var(--panel);border:1px solid var(--line);border-top:3px solid #496276;padding:22px;margin-bottom:20px;box-shadow:4px 4px 0 #070d15}.selectors{display:grid;grid-template-columns:1fr 1.6fr 1fr 1fr;gap:18px}label{font-size:14px;font-weight:650}select{display:block;width:100%;margin-top:8px}.scenario{margin:18px 0 8px;line-height:1.55;color:var(--blue)}.status,.note{color:var(--muted);font-size:14px;line-height:1.6;margin:10px 0 0}.error{color:var(--red)}h2{font-size:20px;margin:0}h3{font-size:17px}.topline{display:flex;justify-content:space-between;align-items:center;gap:15px;flex-wrap:wrap}.topline label{display:flex;align-items:center;gap:9px}input[type=checkbox]{accent-color:var(--mint);width:19px;height:19px}.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:20px 0}.metric{padding:14px;background:#0c1926;border:1px solid #2b4051;position:relative}.metric span{display:block;font-size:14px;color:var(--muted)}.metric strong{display:block;font-size:25px;margin-top:8px;color:var(--mint)}.metric progress{width:100%;height:5px;accent-color:var(--mint);display:block;margin-top:9px}.coin{position:absolute;right:15px;top:8px;background:var(--gold);color:#17140d;border-radius:30px;padding:4px 8px;font-family:monospace;font-weight:bold;animation:spend 1.4s ease-out forwards;pointer-events:none}@keyframes spend{to{transform:translateY(-45px);opacity:0}}.arena{display:grid;grid-template-columns:minmax(0,1fr) 210px;gap:20px}.chart{width:100%;display:block;background:#0c1926;border:1px solid #2b4051}svg text{font-family:system-ui,sans-serif;fill:#b7cad8;font-size:14px}.scorebox{background:#0c1926;border:1px solid #2b4051;padding:15px;margin-bottom:12px}.scorebox strong{display:block;font-family:monospace;font-size:25px;margin:9px 0;color:var(--gold)}.scorebox .note{margin-top:4px}.eyebrow{font-size:14px;color:var(--muted);text-transform:uppercase;letter-spacing:.04em}.legend{display:flex;flex-wrap:wrap;gap:18px;font-size:14px;color:var(--muted);margin:12px 0 18px}.key{width:10px;height:10px;display:inline-block;background:var(--mint);margin-right:6px;border-radius:50%}.key.mate{background:var(--blue)}.key.latest{background:var(--gold)}.key.best{background:transparent;border:2px solid var(--mint);width:14px;height:14px}.key.pred{background:#d9a1ff;border-radius:0;width:3px;height:14px}.controls{display:flex;gap:10px;flex-wrap:wrap;align-items:center}.controls input{flex:1;min-width:130px;accent-color:var(--mint)}.forecast{margin-top:20px;border:1px solid #67547c;background:#1b2033;padding:18px}.forecastgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:16px}.forecastgrid span{font-size:14px;color:var(--muted);display:block}.forecastgrid strong{display:block;font-size:22px;margin-top:7px}.resultteams{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:20px}.team{border:1px solid var(--line);padding:16px;background:#0c1926}.team.win{border-top:4px solid var(--mint)}.team.loss{border-top:4px solid var(--red)}.badge{font-size:14px;padding:4px 8px;color:var(--mint);border:1px solid currentColor}.loss .badge{color:var(--red)}.verdict{font-size:clamp(23px,3vw,32px);margin:15px 0;color:var(--mint)}.verdict.loss{color:var(--red)}.flash{animation:announce 1.1s ease-out}@keyframes announce{from{background:#526249}to{background:transparent}}.tablewrap{overflow:auto}table{border-collapse:collapse;width:100%;font-variant-numeric:tabular-nums}th,td{border-bottom:1px solid #2d4354;padding:12px 9px;text-align:right;white-space:nowrap;font-size:14px}th{color:var(--muted);font-weight:600}th:first-child,td:first-child{text-align:left}.team dl{display:grid;grid-template-columns:1fr auto;margin:10px 0;padding:10px 0;border-bottom:1px solid var(--line);font-size:14px;gap:7px}.team dt{color:var(--muted)}.team dd{margin:0;text-align:right}.history{max-height:300px}summary{cursor:pointer;font-weight:650}.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0)}[hidden]{display:none!important}footer{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;font-size:14px;color:var(--muted);padding-top:0}@media(max-width:900px){.arena{grid-template-columns:1fr}.side{display:grid;grid-template-columns:1fr 1fr;gap:12px}.scorebox{margin:0}.forecastgrid{grid-template-columns:1fr 1fr}}@media(max-width:600px){header,main,footer{padding:16px}.panel{padding:14px}.selectors{grid-template-columns:1fr 1fr;gap:12px}.metrics{grid-template-columns:1fr 1fr}.metric strong{font-size:22px}.resultteams{grid-template-columns:1fr}.brand span{display:block;margin:7px 0 0}.controls button{padding:10px}.side{grid-template-columns:1fr}.legend{gap:12px}}@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;scroll-behavior:auto!important}}
   9  
  10  @font-face{font-family:DecisionPixel;src:url(data:font/ttf;base64,[font bytes omitted in guide]) format('truetype');font-display:swap}
  11  :root{background:#242763;color:#f4f4ff;--mint:#64f7d1;--blue:#baadff;--muted:#ced4f3;--panel:#34488c;--line:#718be2;--gold:#ffe28a;--red:#ffa0b5}
  12  body{background:radial-gradient(ellipse at 8% 0%,#4e4592 0%,transparent 50%),linear-gradient(135deg,#25275f,#243974);min-height:100vh}
  13  header .brand,h2,.eyebrow,.verdict{font-family:DecisionPixel,monospace;font-weight:400;letter-spacing:.035em;line-height:1.65}
  14  h1{font-family:DecisionPixel,monospace;font-weight:400;letter-spacing:0;line-height:1.45;font-size:clamp(23px,2.65vw,34px);max-width:1120px;color:#fff4cd;text-shadow:3px 3px 0 #171e54}
  15  header p{color:#edf0ff;max-width:1000px;font-size:17px}header .brand span{font-family:system-ui,sans-serif}.facts{display:flex;gap:14px;flex-wrap:wrap;margin-top:18px;font-family:monospace;font-size:15px;color:#abffe4}.facts span{color:#a59bff}
  16  .panel{background:#344889;border:2px solid #7894e9;border-top:4px solid #a6baff;border-radius:0;box-shadow:6px 6px 0 #141d49}.scenario{color:#deedff}.note,.status{color:#d1dbf7}
  17  select,button{background:#26376d;border:2px solid #9db1ff;border-radius:0;box-shadow:3px 3px 0 #172452}button:hover:enabled{background:#435ca0}button.primary{box-shadow:4px 4px 0 #147e77}select{box-shadow:2px 2px 0 #172452}
  18  .outcome-shell{border-top-color:#ffc5ec}.outcome-shell h2{color:#ffd7f4}.outcome-shell #results{margin:16px 0 0;box-shadow:none;background:#2b3c79;border:0;padding:0}.outcome-shell #results .eyebrow{display:none}
  19  .forecast{margin:0 0 20px;border:2px solid #b19af7;border-top:4px solid #d2bfff;background:#3f418b;padding:20px;box-shadow:6px 6px 0 #141d49}.forecast h2{color:#e5d9ff}.forecastgrid{padding:14px;background:#2b3474;border:1px solid #8c83d6}.forecastgrid span{color:#d2dcff}.forecastgrid strong{color:#fff5d1}
  20  .action-stop,.action-continue{display:inline-flex!important;align-items:center;gap:10px;font-family:monospace;font-weight:900}.action-stop{color:#ffb6c6!important}.action-stop::before{content:'STOP';font:700 9px system-ui;background:#eb4169;color:white;width:34px;height:34px;display:inline-grid;place-items:center;clip-path:polygon(29% 0,71% 0,100% 29%,100% 71%,71% 100%,29% 100%,0 71%,0 29%)}.action-continue{color:#64f7d1!important}.action-continue::before{content:'➜';font-size:32px}
  21  .metrics .metric{background:#25356e;border:1px solid #6e8acf}.metric span{color:#d5ddfb}.metric strong{color:#a3ffe1}.arena{grid-template-columns:minmax(0,1fr)}.chart{background:#1c2e64;border:2px solid #6482cb}svg text{fill:#e2e9ff}.key{width:16px;height:16px;vertical-align:middle}.key.mate{border-radius:0;background:#c7a2ff}.key.latest{background:#ffe28a}.key.best{width:20px;height:20px}.key.rival{width:28px;height:0;border-top:3px dashed #ff7f96;border-radius:0;background:transparent}.legend{color:#e2e6ff;gap:20px;font-size:15px}
  22  .revealgroup{display:flex;flex-direction:column;gap:6px}.revealgroup span{font-size:14px;color:#d4dcff}.analogy{margin-top:14px;background:#293a79;padding:12px 16px;border-left:4px solid #75efdc}.analogy summary{color:#b6ffee}.analogy p{line-height:1.65;max-width:930px;margin-bottom:0}.model-details{font-size:14px;line-height:1.6;color:#d1dbf7;margin-top:10px}.model-details p{max-width:950px}
  23  .team{background:#25356c;border:1px solid #7692d8}.team dt{color:#d7e1ff}.team h3{color:#fff3cd}.badge{font-family:monospace;font-weight:800}.verdict{font-size:clamp(22px,3vw,32px)}th{color:#d6e1ff}th,td{border-bottom-color:#647bc0}footer{color:#d0d8f5}
  24  .optimum{filter:drop-shadow(0 0 5px #f7c944)}.glow{animation:peakglow 1.5s ease-out}.sample-cost{paint-order:stroke;stroke:#1c2e64;stroke-width:4;animation:samplecost 1.45s ease-out forwards;pointer-events:none}
  25  @keyframes peakglow{0%{filter:drop-shadow(0 0 2px #ffdc64);opacity:.3}40%{filter:drop-shadow(0 0 18px #ffdc64);opacity:1}100%{filter:drop-shadow(0 0 5px #ffdc64)}}
  26  @keyframes samplecost{0%{opacity:1;transform:translateY(0)}65%{opacity:1}100%{opacity:0;transform:translateY(-26px)}}
  27  @media(max-width:650px){.forecastgrid{grid-template-columns:1fr 1fr}.forecast{padding:14px}h2{font-size:17px}.facts{gap:8px;font-size:14px}.chart{min-height:270px}svg text{font-size:18px}.sample-cost{font-size:24px!important}.legend{font-size:14px;gap:12px}}
  28  @media(prefers-reduced-motion:reduce){.sample-cost{animation:none;opacity:0}.glow{animation:none}}
  29  
  30  h1{font-size:clamp(21px,2.4vw,31px);line-height:1.55}.legend label{display:inline-flex;align-items:center;gap:8px;cursor:pointer;padding:8px 10px;background:#283770;border:1px solid #8c9dde;font-size:14px;min-height:44px}.legend input{accent-color:#64f7d1;width:18px;height:18px}.legend .key{width:20px;height:20px;margin:0}.legend .key.mate{background:#ffad55}.legend .key.rival{width:28px;height:0}.legend .key.pred{width:7px;height:22px;background:#fff;border:2px solid #fa58d4}.legend label:has(input:not(:checked)){opacity:.6}.legend .key.best{width:23px;height:23px}.forecast{border-color:#fa91dc;border-top-color:#ffd8f5;background:#34377b}.forecast h2{color:#ffe2f8}
  31  #finish{border-color:#ffc86a;color:#fff1c8;margin-left:auto}.result-ready{animation:result-ready 1.5s ease-out 2}@keyframes result-ready{50%{box-shadow:0 0 0 4px #ffda7955;background:#6c4d70}}
  32  #results{color:#f4f4ff;background:#283a77;border:3px solid #a3b8ff;border-top:5px solid #ffe28a;padding:24px;max-width:1000px;width:calc(100% - 32px);max-height:85vh;overflow:auto;box-shadow:10px 10px 0 #101945}#results::backdrop{background:#0e1647c9;backdrop-filter:blur(4px)}.dialog-close{display:flex;justify-content:flex-end}.dialog-close button{border-color:#d6c5ff}.forecast{margin-top:20px}.forecastgrid strong{overflow-wrap:anywhere;font-size:20px}#preverror{font-size:18px}.controls{row-gap:14px}
  33  @media(prefers-reduced-motion:reduce){.result-ready{animation:none}}
  34  
  35  :root{font-size:17px}header p{font-size:18px}.note,.status,label,.eyebrow,th,td,.legend label,.model-details,.revealgroup span{font-size:15px}.metric span,.forecastgrid span,.team dl{font-size:15px}.legend{font-size:16px}.legend>span{display:inline-flex;align-items:center;gap:8px}.legend .key.pred{border:0;border-left:3px dashed #b6f0ff;background:transparent;width:5px;height:23px;filter:drop-shadow(0 0 4px #8edfff)}.ice-glow{filter:drop-shadow(0 0 3px #8edfff)}.forecast{border-color:#a7e9ff;border-top-color:#d2f5ff}.forecast h2{color:#d8f7ff}.final-stop{margin:14px 0;padding:14px;border:1px solid #9cdeee;color:#d8f7ff;background:#22396b;font-size:16px;line-height:1.6}
  36  svg text{font-size:15px}@media(max-width:650px){svg text{font-size:18px}}
  37  
  38  .references{margin-top:24px}.references>p{line-height:1.65;max-width:1050px;color:#e1e9ff}.references article{padding:18px 0;border-top:1px solid #7b91d0}.references h3{font:650 18px/1.5 system-ui,sans-serif;margin:0 0 8px}.references h3 a{color:#b8eeff;text-underline-offset:4px}.references .citation{font-size:15px;line-height:1.65;margin:0;color:#e4eaff;overflow-wrap:anywhere}.research-topic{font-size:15px;color:#b7ffe5;margin:8px 0 0;line-height:1.5}.legend>span{padding:4px 0}.chart{aspect-ratio:900/580}
  39  .references summary{cursor:pointer;font-size:20px;font-weight:750;line-height:1.5}.references summary:focus-visible{outline:2px solid #b6f0ff;outline-offset:6px}.references h2{font-size:19px;margin-top:24px}
  40  </style>
  41  </head>
  42  <body>
  43  <header><div class="brand">Decision Lab <span>by Kaan Mutlu</span></div><h1>How do teams explore under uncertainty?<br>When should they stop testing and commit?</h1><p>In product development, every experiment costs resources, and competitors keep searching. Follow real players in a lab competition, then see whether deep learning predicts their next move.</p><div class="facts">3 sessions <span>•</span> 4 sharing scenarios <span>•</span> 2-player teams</div></header>
  44  <main>
  45  <section class="panel" aria-label="Choose a recorded round"><div class="selectors">
  46  <label>Session<select id="session" disabled></select></label>
  47  <label>Information sharing<select id="game" disabled><option value="1">No sharing</option><option value="2">Teammate sharing</option><option value="3">Competitor scores</option><option value="4">Both</option></select></label>
  48  <label>Player<select id="participant" disabled></select></label><label>Round<select id="round" disabled></select></label>
  49  </div><p id="scenario" class="scenario"></p><p id="status" class="status" role="status">Loading recorded sessions...</p></section>
  50  <section class="panel" aria-label="Competition replay">
  51  <div class="topline"><h2>Follow the search</h2><div class="revealgroup"><label><input id="reveal" type="checkbox" disabled>Reveal landscape</label><span>Players could not see this curve or its peak.</span></div></div>
  52  <p class="note">Each test costs 10 tokens. Your team wins by finding a better-performing design than the opposing team.</p>
  53  <details class="analogy"><summary>What do the axes mean?</summary><p>Think of competing headphone companies: <b>x</b> is a noise-cancellation setting, and <b>y</b> is the listening-quality score discovered by testing it. Your colleague can share settings and results; a rival may publish a score without revealing its settings. This is a business analogy for the experiment.</p></details><div class="metrics"><div class="metric"><span>Selected player's tests</span><strong id="count">Not started</strong></div><div class="metric" id="budgetbox"><span>Selected player's tokens left</span><strong id="budget">200</strong><progress id="budgetbar" max="200" value="200" aria-label="Selected player's remaining budget"></progress></div><div class="metric"><span>Selected player's best performance</span><strong id="best">Not sampled</strong></div><div class="metric"><span>Time since first own sample</span><strong id="elapsed">Not started</strong></div></div>
  54  <div class="arena"><div><svg id="chart" class="chart" viewBox="0 0 900 580" role="img" aria-label="Recorded tests across the design range"></svg><div class="legend" aria-label="Chart layers">
  55  <span><i class="key"></i>Selected player</span>
  56  <span id="matelegend"><i class="key mate"></i>Teammate</span>
  57  <span id="opplegend"><i class="key rival"></i><span id="opplegendtext">Competitor best</span></span>
  58  <span id="predlegend"><i class="key pred"></i>Model comparison</span>
  59  <span><i class="key best"></i>Own best</span>
  60  </div></div>
  61  <aside class="side" hidden><div class="scorebox"><div class="eyebrow">Teammate</div><strong id="matebest">Hidden</strong><p id="matenote" class="note"></p></div><div class="scorebox"><div class="eyebrow">Competitor best</div><strong id="oppbest">Hidden</strong><p id="oppnote" class="note"></p></div></aside></div>
  62  <p id="eventstatus" class="status" aria-live="polite">Press Play or Next decision to follow the search.</p>
  63  <div class="controls" style="margin-top:14px"><button id="reset" disabled>Reset</button><button id="back" disabled>Previous</button><button id="play" class="primary" disabled>Play</button><button id="next" disabled>Next decision</button><label class="sr" for="step">Replay event</label><input id="step" type="range" min="0" max="1" value="0" disabled><button id="finish" disabled aria-haspopup="dialog">Round results</button></div><p id="finishnote" class="note">Round results unlock when the visible search ends.</p>
  64  
  65  
  66  
  67  </section>
  68  
  69  <div class="forecast"><div class="topline"><h2>Can the model anticipate this player?</h2><button id="predictToggle" disabled aria-expanded="false" aria-controls="predictionPanel">Show model prediction</button></div><p class="note">Reveal each prediction alongside the action it was made for.</p>
  70  <div id="predictionPanel" hidden><p id="modelstatus" class="status" role="status"></p><div class="forecastgrid"><div><span>Predicted choice</span><strong id="px">Pending</strong></div><div><span>Stopping probability</span><strong id="stopscore">Pending</strong></div><div><span>Predicted action</span><strong id="action">Pending</strong><span id="threshold"></span></div><div><span>Position error</span><strong id="preverror">No comparison yet</strong></div></div><details class="model-details"><summary>How the prediction works</summary><p>An LSTM learns dependencies across the sequence of tests. We use 5-fold cross-validation and each player-round's held-out model. A per-scenario cutoff maximizes F1, balancing precision and recall for stopping. Predictions use the history available before the displayed action, starting after 3 own tests. Stopping includes submission and timeout.</p></details></div></div>
  71  <dialog id="results" aria-labelledby="resulttitle"><form method="dialog" class="dialog-close"><button aria-label="Close round results">Close ✕</button></form><div class="eyebrow">Round complete</div><h2 id="resulttitle" class="verdict" tabindex="-1"></h2><div id="finalStop" class="final-stop" hidden></div><div id="resultteams" class="resultteams"></div><p id="resultnote" class="note"></p></dialog><details class="panel references"><summary>Research and publications</summary><p>Our team's work explores design choices under uncertainty, rational benchmarks and models of observed behavior.</p><h2>Published and accepted</h2><article><h3><a href="https://par.nsf.gov/biblio/10710525" target="_blank" rel="noopener noreferrer">Information Sharing in Design Teams under Competition: Effect on Decision Quality and Search Efficiency</a></h3><p class="citation">Javadpour, N., Mutlu, K., Sha, Z., &amp; Bayrak, A. E. <i>ASME Journal of Mechanical Design</i>. Accepted, in press.</p></article>
  72  <article><h3><a href="https://doi.org/10.1017/pds.2025.10039" target="_blank" rel="noopener noreferrer">A Quantitative Analysis of Rational Decisions Under Uncertainty in Engineering Systems Design</a></h3><p class="citation">Mutlu, K., Javadpour, N., Sha, Z., &amp; Bayrak, A. E. (2025). <i>Proceedings of the Design Society</i>, 5, 249–258. DOI: 10.1017/pds.2025.10039.</p><p class="research-topic">Human search compared with a Bayesian expected-utility benchmark.</p></article>
  73  <article><h3><a href="https://doi.org/10.1115/DETC2025-169672" target="_blank" rel="noopener noreferrer">Impact of Information Sharing Between Members in Design Teams Under Competition in Unknown Design Space Exploration</a></h3><p class="citation">Javadpour, N., Mutlu, K., Sha, Z., &amp; Bayrak, A. E. (2025). <i>Proceedings of the ASME 2025 IDETC-CIE</i>, V03BT03A029. DOI: 10.1115/DETC2025-169672.</p><p class="research-topic">How sharing information changes search, performance and resource use.</p></article><h2>Manuscripts</h2><article><h3>Predicting Designers’ Search Behavior and Stopping Decisions Under Competition with Sequence Learning</h3><p class="citation">Mutlu, K., Javadpour, N., Sha, Z., &amp; Bayrak, A. E. Manuscript in development.</p><p class="research-topic">Multi-task LSTM modeling of sequential next-action, outcome and stopping behavior.</p></article>
  74  <article><h3>Quantifying Bounded Rationality and Robustness in Design Decisions under Competition</h3><p class="citation">Mutlu, K., Javadpour, N., Sha, Z., &amp; Bayrak, A. E. <i>Design Science</i>. Revision under review.</p><p class="research-topic">Gaussian-process and Bayesian-optimization modeling of sequential decisions under uncertainty.</p></article></details></main><footer><span>Recorded human decisions. Served by a deployed machine-learning application.</span><a href="/docs">Explore the API</a></footer>
  75  
  76  <script>
  77  'use strict';
  78  const $=id=>document.getElementById(id);
  79  const dates={feb18:'February 18, 2026',feb20:'February 20, 2026',march6:'March 6, 2025'};
  80  const labels={march6:'Session 1',feb18:'Session 2',feb20:'Session 3'};
  81  const scenarios={1:'You see only your own tests. Your teammate and competitors work out of sight.',2:'You see what your teammate tested and how it performed, like sharing internal R&D results.',3:'You see competitors\' best performance, but not how they achieved it, like a rival\'s product benchmark without its engineering details.',4:'Share your team\'s experiments while tracking competitors\' performance. Their design settings remain hidden.'};
  82  const picks=['session','game','participant','round'];
  83  let predictionGeneration=0,resultGeneration=0,resultsCache=null;
  84  let animationFrame=-1, animationUntil=0, peakGlowUntil=0;
  85  let rows=[],story=null,shown=0,version=0,controller=null,timer=null,curve=null,predictOn=false,predictions=new Map(),predictionKey='',current=null,previous=null,modelMessage='',resultRequest=false;
  86  const pct=v=>(v*100).toFixed(1)+'%';
  87  const el=(tag,cls,text)=>{const n=document.createElement(tag);if(cls)n.className=cls;if(text!==undefined)n.textContent=text;return n;};
  88  const svg=(tag,attrs={},text)=>{const n=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attrs).forEach(([k,v])=>n.setAttribute(k,v));if(text!==undefined)n.textContent=text;return n;};
  89  function params(){return {session_id:$('session').value,game_number:$('game').value,participant_id:$('participant').value,round_number:$('round').value};}
  90  async function get(path,p={},signal=controller?.signal){const r=await fetch(path+'?'+new URLSearchParams(p),{signal});if(!r.ok){let d;try{d=(await r.json()).detail;}catch{}throw Error(typeof d==='string'?d:`Request failed (${r.status}).`);}return r.json();}
  91  function setStatus(text,error=false){$('status').textContent=text;$('status').classList.toggle('error',error);}
  92  function options(id,choices){$(id).replaceChildren(...choices.map(([value,label])=>{const o=el('option','',label);o.value=value;return o;}));}
  93  function roundOptions(){options('round',rows.filter(r=>r.participant_id===Number($('participant').value)).map(r=>[r.round_number,`Round ${r.round_number}`]));}
  94  function pause(){clearInterval(timer);timer=null;$('play').textContent='Play';}
  95  function clearResults(){resultGeneration++;$('finalStop').hidden=true;$('finalStop').textContent='';if($('results').open)$('results').close();$('resultteams').replaceChildren();resultRequest=false;resultsCache=null;$('finish').textContent='Round results';$('finish').classList.remove('result-ready');}
  96  async function load(refresh=false,participant=false){
  97   predictionGeneration++;animationFrame=-1;peakGlowUntil=0;const ticket=++version;controller?.abort();controller=new AbortController();pause();story=null;curve=null;shown=0;current=null;previous=null;predictionKey='';predictions.clear();clearResults();
  98   picks.concat(['reset','back','play','next','step','reveal','predictToggle','finish']).forEach(id=>$(id).disabled=true);$('reveal').checked=false;$('chart').replaceChildren();$('predictionPanel').hidden=true;
  99   $('count').textContent='Loading';$('best').textContent='Loading';$('budget').textContent='Loading';$('elapsed').textContent='Loading';$('matebest').textContent='Loading';$('oppbest').textContent='Loading';$('eventstatus').textContent='';setStatus('Loading recorded decisions...');
 100   try{
 101    if(refresh){rows=await get('/rounds',{session_id:$('session').value,game_number:$('game').value});if(ticket!==version)return;options('participant',[...new Set(rows.map(r=>r.participant_id))].map(p=>[p,`Player ${p}`]));roundOptions();}else if(participant)roundOptions();
 102    if(!$('round').value)throw Error('No recorded rounds for this selection.');
 103    const result=await get('/replay-story',params());if(ticket!==version)return;
 104    if(!result.events?.length)throw Error('No recorded events for this selection.');
 105    story=result;$('step').max=story.events.length;$('scenario').textContent=scenarios[$('game').value];
 106    setStatus(`${labels[$('session').value]} | ${dates[$('session').value]} | Player ${$('participant').value} | Round ${$('round').value}. Press Play or Next decision.`);
 107    picks.concat(['reveal','predictToggle']).forEach(id=>$(id).disabled=false);render();
 108   }catch(e){if(e.name==='AbortError'||ticket!==version)return;setStatus(e.message,true);picks.forEach(id=>$(id).disabled=false);}
 109  }
 110  function advance(n,animate=false){if(!story)return;predictionGeneration++;predictionKey='';current=null;previous=null;const old=shown;shown=Math.max(0,Math.min(n,story.events.length));if(shown!==old)clearResults();animationFrame=animate&&shown===old+1?shown:-1;animationUntil=Date.now()+1450;render();}
 111  function render(){
 112   if(!story)return;
 113   const visible=story.events.slice(0,shown),last=visible.at(-1),own=visible.filter(e=>e.role==='own'),mate=visible.filter(e=>e.role==='teammate'),lastOwn=own.at(-1),g=Number($('game').value);
 114   const best=own.reduce((a,b)=>!a||b.quality_fraction>a.quality_fraction?b:a,null),mateBest=mate.reduce((a,b)=>!a||b.quality_fraction>a.quality_fraction?b:a,null);
 115   const spent=own.length*story.rules.sample_cost,left=story.rules.initial_tokens-spent;
 116   $('count').textContent=`${own.length} / ${story.events.filter(e=>e.role==='own').length}`;$('budget').textContent=`${left} tokens`;$('budgetbar').value=left;$('best').textContent=best?pct(best.quality_fraction):'Not sampled';
 117   $('elapsed').textContent=last?(last.seconds_since_first_own_sample<0?'Before first test':`${last.seconds_since_first_own_sample.toFixed(0)} s`):'Not started';
 118   $('matelegend').hidden=![2,4].includes(g);$('matebest').textContent=[2,4].includes(g)?(mateBest?pct(mateBest.quality_fraction):'Not sampled'):'Hidden';
 119   $('matenote').textContent=[2,4].includes(g)?(mate.length?`Player ${mate.at(-1).participant_id}: ${mate.length} tests; ${story.rules.initial_tokens-mate.length*story.rules.sample_cost} tokens left, calculated from visible tests.`:(story.teammate_record_available?'Shared tests will appear as the replay advances.':'No teammate sample record is available.')):'This scenario does not share teammate tests.';
 120   $('oppbest').textContent=[3,4].includes(g)?(last?.opponent_best_quality!=null?pct(last.opponent_best_quality):'Not observed'):'Hidden';
 121   $('oppnote').textContent=[3,4].includes(g)?(story.opponent_scores_available?'Recorded competitor benchmark. Design settings are hidden.':'Competitor score history is unavailable in this record.'):'This scenario does not share competitor scores.';
 122   $('eventstatus').textContent=last?`Player ${last.participant_id} ${last.role==='own'?'(selected player)':'(teammate)'} tested setting ${pct(last.position_fraction)}. Performance: ${pct(last.quality_fraction)}. Cost: ${story.rules.sample_cost} tokens.`:'Press Play or Next decision to follow the search.';
 123   $('step').value=shown;$('step').disabled=false;$('reset').disabled=$('back').disabled=!shown;$('next').disabled=$('play').disabled=shown===story.events.length;$('finish').disabled=shown!==story.events.length||resultRequest;$('finish').classList.toggle('result-ready',shown===story.events.length&&!resultsCache);
 124   $('finishnote').textContent=shown===story.events.length?'Search ended. Open Round results to see both teams and their budgets.':'Round results unlock when the visible search ends.';
 125   const unlocked=own.length>=3;$('predictToggle').disabled=!unlocked;$('predictionPanel').hidden=!predictOn;$('predictToggle').textContent=!unlocked?`Observe 3 own tests (${Math.min(own.length,3)}/3)`:(predictOn?'Hide model comparison':'Show model comparison');$('predictToggle').setAttribute('aria-expanded',String(predictOn));
 126   const compared=lastOwn;const forecast=predictOn&&previousError(current,compared)!==null&&predictionKey===`${version}:${shown}`?current:null;
 127   const prev=forecast;
 128   $('px').textContent=forecast?pct(forecast.predicted_position_fraction):'Not available';$('stopscore').textContent=forecast?pct(forecast.stop_probability):'Not available';$('action').textContent=forecast?(forecast.predicted_action==='stop'?'STOP':'CONTINUE'):'Not available';$('action').className=forecast?(forecast.predicted_action==='stop'?'action-stop':'action-continue'):'';$('threshold').textContent=forecast?`Stop cutoff: ${pct(forecast.stop_threshold)}`:'';
 129   $('preverror').textContent=prev?`${previousError(prev,compared).toFixed(1)} pp (test ${compared.step_number-1} → ${compared.step_number})`:'No comparison yet';
 130   $('modelstatus').textContent=own.length<4?`The first comparison appears with own test 4 (${own.length}/4).`:modelMessage||'Loading the matching prediction...';
 131   draw(visible,last,best,forecast,prev,compared);$('predlegend').hidden=false;
 132   if(predictOn&&lastOwn?.step_number>=4)queueMicrotask(loadPrediction);
 133  }
 134  function previousError(pred,event){
 135   if(!pred?.available||event?.role!=='own'||event.step_number<4||pred.after_step!==event.step_number-1)return null;
 136   return Math.abs(pred.predicted_position_fraction-event.position_fraction)*100;
 137  }
 138  function draw(visible,last,best,forecast,prev,compared){
 139   const chart=$('chart'),land=$('reveal').checked&&curve?curve.curve:[];
 140   chart.replaceChildren(svg('title',{},'Design tests and predicted next setting'),svg('desc',{},`${visible.length} recorded tests revealed. Focus a marker to read its player, choice and performance.`));
 141   const values=visible.map(e=>e.quality_fraction).concat(land.map(e=>e.quality_fraction)),lo=Math.min(0,...values),hi=Math.max(1,...values,last?.opponent_best_quality||0)*1.16;
 142   const rival=[3,4].includes(Number($('game').value))?last?.opponent_best_quality:null;
 143   const X=x=>76+x*790,Y=y=>450-(y-lo)/(hi-lo)*340;
 144   $('opplegend').hidden=![3,4].includes(Number($('game').value));$('opplegendtext').textContent=rival==null?'Competitor best so far':`Competitor best so far: ${pct(rival)}`;
 145   for(let i=0;i<=20;i++){const x=76+i*790/20;chart.append(svg('line',{x1:x,x2:x,y1:110,y2:450,stroke:i%5===0?'#6a84bb':'#47649e','stroke-width':i%5===0?1.1:.65,'stroke-opacity':.7}));}
 146   for(let i=0;i<=8;i++){const y=110+i*340/8;chart.append(svg('line',{x1:76,x2:866,y1:y,y2:y,stroke:i%2===0?'#6a84bb':'#47649e','stroke-width':i%2===0?1.1:.65,'stroke-opacity':.7}));}
 147   chart.append(svg('line',{x1:76,x2:76,y1:110,y2:450,stroke:'#d3e7ff','stroke-width':2}),svg('line',{x1:76,x2:866,y1:450,y2:450,stroke:'#d3e7ff','stroke-width':2}));
 148   for(let i=0;i<=4;i++){const y=lo+(hi-lo)*i/4;chart.append(svg('line',{x1:70,x2:76,y1:Y(y),y2:Y(y),stroke:'#d3e7ff','stroke-width':2}),svg('line',{x1:X(i/4),x2:X(i/4),y1:450,y2:457,stroke:'#d3e7ff','stroke-width':2}),svg('text',{x:65,y:Y(y)+5,'text-anchor':'end'},`${Math.round(y*100)}%`),svg('text',{x:X(i/4),y:476,'text-anchor':'middle'},`${i*25}%`));}
 149   chart.append(svg('text',{x:76,y:27},'Performance (% of round maximum)'),svg('text',{x:470,y:560,'text-anchor':'middle'},'Design choice (% of available range)'));
 150   if(land.length)chart.append(svg('polyline',{points:land.map(p=>`${X(p.position_fraction)},${Y(p.quality_fraction)}`).join(' '),fill:'none',stroke:'#8195a8','stroke-width':2}));
 151   if(rival!=null&&true){chart.append(svg('line',{x1:76,x2:866,y1:Y(rival),y2:Y(rival),stroke:'#ff7f96','stroke-width':3,'stroke-dasharray':'12 7'}));}
 152   if(land.length){
 153    const peak=land.reduce((a,b)=>b.quality_fraction>a.quality_fraction?b:a),cx=X(peak.position_fraction),cy=Y(peak.quality_fraction);
 154    const points=Array.from({length:10},(_,i)=>{const a=-Math.PI/2+i*Math.PI/5,r=i%2?10:22;return `${cx+Math.cos(a)*r},${cy+Math.sin(a)*r}`;}).join(' ');
 155    const star=svg('polygon',{points,fill:'#ffdf75',stroke:'#fff6cc','stroke-width':2,class:Date.now()<peakGlowUntil?'optimum glow':'optimum',tabindex:0});
 156    star.append(svg('title',{},'Best possible performance: estimated peak of the revealed curve. This was hidden from players.'));chart.append(star);
 157    chart.append(svg('text',{x:470,y:55,'text-anchor':'middle',style:'fill:#ffdf75;font-weight:700'},'★ Best possible performance'));
 158   }
 159   if(prev&&compared){const a=prev.predicted_position_fraction,b=compared.position_fraction;if(a>=0&&a<=1){chart.append(svg('line',{x1:X(a),x2:X(b),y1:518,y2:518,stroke:'#b6f0ff','stroke-width':5,class:'ice-glow'}));[a,b].forEach(x=>chart.append(svg('line',{x1:X(x),x2:X(x),y1:511,y2:525,stroke:'#b6f0ff','stroke-width':3})));chart.append(svg('text',{x:Math.max(140,Math.min(790,X((a+b)/2))),y:503,'text-anchor':'middle',style:'fill:#c9f5ff;font-weight:700'},`Test ${compared.step_number}: ${previousError(prev,compared).toFixed(1)} pp error`));}}
 160   if(forecast){const x=forecast.predicted_position_fraction;if(x>=0&&x<=1){chart.append(svg('line',{x1:X(x),x2:X(x),y1:110,y2:450,stroke:'#b6f0ff','stroke-width':3.5,'stroke-dasharray':'11 7',class:'ice-glow'}),svg('text',{x:Math.max(145,Math.min(790,X(x))),y:85,'text-anchor':'middle',style:'fill:#cdf6ff;font-weight:800'},`Prediction for test ${forecast.after_step+1}`));}else{$('modelstatus').textContent+=' Predicted setting is outside the allowed range; its value is shown without clipping.';}}
 161   visible.filter(e=>e.role==='own'?true:true).forEach(e=>{const size=e===last?10:7.5;const attrs={fill:e===last?'#ffe28a':e.role==='own'?'#64f7d1':'#ffad55',stroke:'#172763','stroke-width':2.5,tabindex:0};const point=e.role==='teammate'?svg('rect',{...attrs,x:X(e.position_fraction)-size,y:Y(e.quality_fraction)-size,width:2*size,height:2*size}):svg('circle',{...attrs,cx:X(e.position_fraction),cy:Y(e.quality_fraction),r:size});const desc=`Player ${e.participant_id}, test ${e.step_number}: setting ${pct(e.position_fraction)}, performance ${pct(e.quality_fraction)}`;point.setAttribute('aria-label',desc);point.append(svg('title',{},desc));chart.append(point);});
 162   if(best&&true)chart.append(svg('circle',{cx:X(best.position_fraction),cy:Y(best.quality_fraction),r:14,fill:'none',stroke:'#63ebbc','stroke-width':2}));
 163   if(last&&(last.role==='own'?true:true)&&animationFrame===shown&&Date.now()<animationUntil){const tx=Math.max(140,Math.min(800,X(last.position_fraction))),ty=Math.max(135,Y(last.quality_fraction)-28);const cost=svg('text',{x:tx,y:ty,'text-anchor':'middle',class:'sample-cost',style:`fill:${last.role==='own'?'#64f7d1':'#ffbd75'};font-weight:800;font-size:20px`},`−${story.rules.sample_cost} tokens`);chart.append(cost);}
 164   if(!visible.length&&!land.length)chart.append(svg('text',{x:470,y:205,'text-anchor':'middle'},'Every test reveals a little more. Press Play to begin.'));
 165  }
 166  async function loadPrediction(){
 167   const event=story?.events.slice(0,shown).filter(e=>e.role==='own').at(-1);if(!predictOn||!event||event.step_number<4)return;
 168   const key=`${version}:${shown}`;if(predictionKey===key)return;predictionKey=key;current=null;previous=null;modelMessage='Loading the matching prediction...';
 169   const generation=++predictionGeneration,ticket=version,frame=shown,signal=controller.signal,p=params(),step=event.step_number-1;
 170   try{let value=predictions.get(step);if(!value){value=await get('/predict',{...p,after_step:step},signal);if(ticket===version)predictions.set(step,value);}
 171    if(ticket!==version||shown!==frame||!predictOn||generation!==predictionGeneration)return;
 172    current=value;modelMessage=value.available?`Before test ${event.step_number}: model predicted ${value.predicted_action.toUpperCase()}. Actual: CONTINUE.`:value.reason;
 173    render();
 174   }catch(e){if(e.name==='AbortError'||ticket!==version||shown!==frame||generation!==predictionGeneration)return;modelMessage=e.message;render();}
 175  }
 176  async function revealResults(){
 177   pause();if(!story||shown!==story.events.length||resultRequest)return;if(resultsCache){$('results').showModal();showFinalStop(version,resultGeneration);return;}resultRequest=true;$('finish').disabled=true;const ticket=version,resultTicket=++resultGeneration;
 178   try{const r=await get('/replay-results',params());if(ticket!==version||resultTicket!==resultGeneration)return;
 179    resultsCache=r;resultRequest=false;$('finish').disabled=false;$('finish').classList.remove('result-ready');const own=r.teams[0],valid=r.outcome_consistent;$('finish').textContent=valid?(own.won?'Team won · View results':'Team lost · View results'):'View recorded results';
 180    $('resulttitle').textContent=valid?(own.won?'Your team won':'Your team lost'):'Recorded round results';$('resulttitle').className=`verdict flash${valid&&!own.won?' loss':''}`;
 181    $('resultteams').replaceChildren(...r.teams.map(t=>{const card=el('div',`team ${t.won===true?'win':t.won===false?'loss':''}`),heading=el('div','topline');heading.append(el('h3','',t.label),el('span','badge',t.won===true?'Won':t.won===false?'Lost':'Outcome unavailable'));card.append(heading);
 182     t.players.forEach(p=>{card.append(el('h3','',`Player ${p.participant_id}${p.selected?' (selected player)':''}`));const dl=el('dl');[['Best performance',pct(p.best_quality)],['Tests taken',p.samples],['Tokens spent',p.tokens_spent],['Tokens remaining',p.tokens_remaining],['Final recorded payoff',p.recorded_payoff==null?'Unavailable':`${p.recorded_payoff.toFixed(0)} tokens`]].forEach(([k,v])=>{const value=el('dd','',v);if(k==='Final recorded payoff'&&p.recorded_payoff!=null)value.setAttribute('title',`Recorded value: ${p.recorded_payoff} tokens`);dl.append(el('dt','',k),value);});card.append(dl);});if(t.players.length<2)card.append(el('p','note','A player record is missing. No result is inferred for that player.'));return card;}));
 183    $('resultnote').textContent=valid?'':'Incomplete records or conflicting outcome flags.';$('results').showModal();$('resulttitle').focus();showFinalStop(ticket,resultTicket);
 184   }catch(e){if(e.name!=='AbortError'&&ticket===version&&resultTicket===resultGeneration){setStatus(e.message,true);resultRequest=false;$('finish').disabled=false;}}
 185  }
 186  async function showFinalStop(ticket,resultTicket){
 187   if(!predictOn){$('finalStop').hidden=true;return;}const own=story.events.filter(e=>e.role==='own'),last=own.at(-1);if(!last||last.step_number<3)return;
 188   try{let pred=predictions.get(last.step_number);if(!pred){pred=await get('/predict',{...params(),after_step:last.step_number});if(ticket===version)predictions.set(last.step_number,pred);}
 189   if(ticket!==version||resultTicket!==resultGeneration||!predictOn||!pred.available)return;
 190   $('finalStop').hidden=false;$('finalStop').textContent=`Final stopping prediction: ${pred.predicted_action.toUpperCase()} (${pct(pred.stop_probability)} stop probability). Recorded: search ended.`;
 191   }catch{ /* Recorded outcomes remain usable if model comparison is unavailable. */ }
 192  }
 193  picks.forEach(id=>$(id).onchange=()=>load(id==='session'||id==='game',id==='participant'));
 194  $('next').onclick=()=>{pause();advance(shown+1,true);};$('back').onclick=()=>{pause();advance(shown-1);};$('reset').onclick=()=>{pause();advance(0);};$('step').oninput=()=>{pause();advance(Number($('step').value));};
 195  $('play').onclick=()=>{if(timer){pause();return;}$('play').textContent='Pause';advance(shown+1,true);if(shown===story.events.length){pause();return;}timer=setInterval(()=>{advance(shown+1,true);if(shown===story.events.length)pause();},1000);};
 196  function togglePrediction(){if($('predictToggle').disabled)return;predictionGeneration++;predictOn=!predictOn;predictionKey='';current=null;previous=null;modelMessage='';render();}$('predictToggle').onclick=togglePrediction;$('finish').onclick=revealResults;
 197  $('reveal').onchange=async()=>{if(!$('reveal').checked||curve){if($('reveal').checked)peakGlowUntil=Date.now()+1600;render();return;}const ticket=version;$('reveal').disabled=true;try{const result=await get('/landscape',{session_id:$('session').value,game_number:$('game').value,round_number:$('round').value,points:1000});if(ticket!==version)return;curve=result;peakGlowUntil=Date.now()+1600;render();}catch(e){if(e.name!=='AbortError'&&ticket===version){$('reveal').checked=false;setStatus(e.message,true);}}finally{if(ticket===version)$('reveal').disabled=false;}};
 198  (async()=>{try{const sessions=await get('/sessions');options('session',sessions.map(s=>[s.session_id,labels[s.session_id]||s.session_id]));if(sessions.some(s=>s.session_id==='feb18'))$('session').value='feb18';await load(true);}catch(e){setStatus(e.message,true);}})();
 199  </script></body></html>
```
