### Fundamental Topics First‑Year Engineering Students Should Master — Lecture 3

*Difficulty ratings: 1 = easiest, 3 = most challenging*

1. Elementwise arithmetic on vectors — **Difficulty: 1**
   - Perform +, -, .*, ./, .^ on vectors; understand elementwise vs matrix operations and size compatibility.
   - *Basic syntax (.* ./ .^) and size checks; simple once elementwise vs matrix distinction is shown.*

2. Elementwise relational operations — **Difficulty: 1**
   - Compare vectors with <, >, <=, >=, ==, ~= to produce logical masks for further processing.
   - *Straightforward application of comparison operators to vectors.*

3. Elementwise logical operations and mask combination — **Difficulty: 2**
   - Combine logical vectors with &, |, ~, xor; use parentheses to control precedence.
   - *Requires understanding operator precedence and correct use of parentheses with logical operators.*

4. Logical (mask) indexing and modification — **Difficulty: 2**
   - Select, assign, and remove elements using logical masks; ensure masks match vector length and understand assignment behavior.
   - *Powerful but can be subtle (mask shape, assignment effects), so moderate difficulty.*

5. Common vector functions and shape-aware usage — **Difficulty: 2**
   - Use sum, prod, cumsum, diff, conv (and FFT when appropriate); know input/output shapes and interpretations.
   - *Familiar functions (sum, diff, cumsum) are simple, but shape/output awareness adds complexity.*

6. Aggregation and cumulative operations — **Difficulty: 1**
   - Compute totals, running sums, products, differences, and understand when to use cumulative vs global aggregates.
   - *Conceptually simple (total vs running); mostly API familiarity.*

7. Numeric utilities and elementwise transforms — **Difficulty: 1**
   - Apply round, floor, ceil, mod/rem, and elementwise mathematical transforms reliably to vectors.
   - *Routine elementwise math and rounding functions; low conceptual load.*

8. Complex‑valued vectors and basic statistics — **Difficulty: 3**
   - Handle complex data (real, imag, abs, angle), compute mean/median/std, and interpret results for vector data.
   - *Complex handling (phase, magnitude) plus statistical interpretation is more challenging for beginners.*

9. Random number generation and reproducibility — **Difficulty: 2**
   - Generate pseudorandom vectors with rng control for reproducible experiments and tests.
   - *RNG usage is simple, but reproducibility (rng seeds, repeatable experiments) introduces subtlety.*

10. Basic audio/vector signal handling — **Difficulty: 3**
    - Read/process 1‑D signals: normalization, RMS, trimming, simple filtering, and maintain sampling‑rate awareness.
    - *Involves signal concepts (sampling rate, normalization, filtering) beyond basic vector ops.*

11. Simple 2‑D plotting of 1‑D data — **Difficulty: 1**
    - Visualize vectors with plot/stem, label axes/titles, add legends for multiple series, and save figures programmatically.
    - *Basic plotting and labeling; low difficulty once plotting functions are demonstrated.*
