# objectives.py

One source of truth for the two mathematical landscapes and their normalization maximum.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Symbols

| Symbol | Lines |
|---|---|
| `evaluate` | 8-13 |
| `estimate_maximum` | 16-26 |

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1-6 | Imports vectorized NumPy evaluation and bounded scalar minimization; names the historical estimation procedure for auditability. |
| 8-10 | Gaussian family: sum three a_i * exp(-b_i * (x-c_i)^2) terms. x may be a scalar or array. |
| 11-13 | Cauchy family: sum three a_i / ((x-b_i)^2+c_i) terms; reject unknown family names. |
| 16-19 | Defines maximum estimation by minimizing the negative objective. It is a numerical estimate, not a proof of global optimality. |
| 20 | Evaluates 10,000 evenly spaced domain points, including endpoints, to reduce the risk of missing a sharp peak. |
| 21 | Also evaluates a 200-point grid to preserve the original preprocessing recipe; seed_max is not actually passed as an optimizer seed. |
| 22 | Runs one bounded scalar minimization over the full interval; a multimodal function does not guarantee its result is the global optimum. |
| 23-26 | Takes the largest candidate from both grids and the optimizer, rejects nonfinite/nonpositive values and returns a float. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1-6 | Imports vectorized NumPy evaluation and bounded scalar minimization; names the historical estimation procedure for auditability. |
| 2 | 1-6 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 3 | 1-6 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 4 | 1-6 | Blank separator; no execution. |
| 5 | 1-6 | Imports vectorized NumPy evaluation and bounded scalar minimization; names the historical estimation procedure for auditability. |
| 6 | 1-6 | Blank separator; no execution. |
| 7 | 7 | Blank separator; no execution. |
| 8 | 8-10 | Function declaration: this body runs when called, not at declaration time. |
| 9 | 8-10 | Conditional branch: determines which following statements run. |
| 10 | 8-10 | Return: sends this result to the caller and ends this invocation. |
| 11 | 11-13 | Conditional branch: determines which following statements run. |
| 12 | 11-13 | Return: sends this result to the caller and ends this invocation. |
| 13 | 11-13 | Failure path: interrupts normal execution with the stated exception. |
| 14 | 14 | Blank separator; no execution. |
| 15 | 15 | Blank separator; no execution. |
| 16 | 16-19 | Function declaration: this body runs when called, not at declaration time. |
| 17 | 16-19 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 18 | 16-19 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 19 | 16-19 | Defines maximum estimation by minimizing the negative objective. It is a numerical estimate, not a proof of global optimality. |
| 20 | 20 | Evaluates 10,000 evenly spaced domain points, including endpoints, to reduce the risk of missing a sharp peak. |
| 21 | 21 | Also evaluates a 200-point grid to preserve the original preprocessing recipe; seed_max is not actually passed as an optimizer seed. |
| 22 | 22 | Runs one bounded scalar minimization over the full interval; a multimodal function does not guarantee its result is the global optimum. |
| 23 | 23-26 | Takes the largest candidate from both grids and the optimizer, rejects nonfinite/nonpositive values and returns a float. |
| 24 | 23-26 | Conditional branch: determines which following statements run. |
| 25 | 23-26 | Failure path: interrupts normal execution with the stated exception. |
| 26 | 23-26 | Return: sends this result to the caller and ends this invocation. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  """Objective families and normalization shared by the importer and API."""
   2  import numpy as np
   3  from scipy.optimize import minimize_scalar
   4  
   5  MAXIMUM_METHOD = 'default_model_grid10000_grid200_bounded_v1'
   6  
   7  
   8  def evaluate(x, family, parameters):
   9      if family == 'gaussian':
  10          return sum(parameters[f'a_{i}'] * np.exp(-parameters[f'b_{i}'] * (x - parameters[f'c_{i}']) ** 2) for i in range(1, 4))
  11      if family == 'cauchy':
  12          return sum(parameters[f'a_{i}'] / ((x - parameters[f'b_{i}']) ** 2 + parameters[f'c_{i}']) for i in range(1, 4))
  13      raise ValueError(f'Unknown objective family: {family}')
  14  
  15  
  16  def estimate_maximum(family, parameters, xmin, xmax):
  17      # Reproduce save_sequences_delta_default.py's numerical procedure.
  18      # This is an estimate, not a guarantee of the exact global optimum.
  19      negative = lambda x: -evaluate(x, family, parameters)
  20      grid = np.array([evaluate(x, family, parameters) for x in np.linspace(xmin, xmax, 10000)])
  21      seed_max = max(-negative(x) for x in np.linspace(xmin, xmax, 200))
  22      result = minimize_scalar(negative, bounds=(xmin, xmax), method='bounded')
  23      maximum = float(max(grid.max(), seed_max, -result.fun))
  24      if not np.isfinite(maximum) or maximum <= 0:
  25          raise ValueError('Normalization requires a finite positive maximum.')
  26      return maximum
```
