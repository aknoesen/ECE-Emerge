### Fundamental Topics First‑Year Engineering Students Should Master — Lecture 16

*Difficulty ratings: 1 = easiest, 3 = most challenging*

1. Row and Column Vectors, Orientation, and Sizes — **Difficulty: 1**
   - Construct row/column vectors, transpose between them, and inspect orientation/emptiness with `size`, `length`, and `isempty`.
   - *Basic construction and inspection (size, length, isempty) are straightforward.*

2. Vector Arithmetic and Elementwise Operations — **Difficulty: 1**
   - Perform vector addition/subtraction, scalar scaling, and elementwise ops using `.*`, `./`, `.^`; understand scalar broadcasting vs. incompatible sizes.
   - *Simple elementwise syntax (.*, ./, .^) and scalar broadcasting; mainly syntactic to learn.*

3. Inner (Dot) and Outer Products — **Difficulty: 2**
   - Compute dot products with `dot` or matrix multiplication, and form outer products (v * w.') to produce matrices; relate to projections and component coupling.
   - *Conceptually simple but requires attention to shapes and interpretation (projections vs. rank‑1 matrices).*

4. Vector Norms and Measures — **Difficulty: 1**
   - Use `norm(v,1)`, `norm(v,2)`, `norm(v,Inf)`, `numel`/`length` to quantify magnitude and errors and compare vectors via norms.
   - *Using norm and interpreting common norms is routine; little API complexity.*

5. Matrix Creation, Shape, and Indexing — **Difficulty: 2**
   - Build matrices with brackets and `zeros`, `ones`, `eye`, `diag`; query dimensions and index using linear and row/column subscripts correctly.
   - *Basic constructors are easy; indexing subtleties and linear vs subscript indexing need care.*

6. Transpose vs Conjugate Transpose — **Difficulty: 2**
   - Use `.'` for nonconjugate transpose and `'` for conjugate transpose; apply appropriately for real vs complex data and track dimension changes.
   - *Syntax is trivial (.' vs ') but understanding conjugation effects for complex data is important.*

7. Matrix Multiplication and Elementwise Matrix Ops — **Difficulty: 2**
   - Compute linear-algebraic products with `*` and elementwise operations with `.*`, `./`, `.^`; ensure dimension compatibility for each operation.
   - *Distinguishing * vs .* and ensuring dimension compatibility is a common source of errors.*

8. Special Square Matrices and Basic Properties — **Difficulty: 2**
   - Construct `eye`, `diag`, test symmetry, compute `det` and `trace`, and recognize implications of singular vs nonsingular matrices.
   - *Constructing eye/diag and computing det/trace is easy; numerical issues (singularity) add nuance.*

9. Elementary Row Operations and Elementary Matrices — **Difficulty: 3**
   - Perform row operations, represent simple operations via elementary matrices, and observe effects on row structure and determinants.
   - *Mapping operations to elementary matrices and understanding determinant effects require linear‑algebra insight.*

10. Solving Linear Systems with Backslash — **Difficulty: 3**
    - Solve `A\b` for square/invertible, overdetermined (least squares), and underdetermined systems; avoid explicit inverses and interpret solver diagnostics.
    - *A\b is simple to use, but interpreting behavior for singular/ill‑conditioned, over/underdetermined systems and avoiding explicit inverses is subtle.*

11. Triangular Systems and Forward/Backward Substitution — **Difficulty: 2**
    - Identify lower/upper triangular matrices, solve triangular systems efficiently (MATLAB backslash), and implement forward/back substitution for practice and verification.
    - *Conceptually straightforward and efficiently handled by backslash; implementing substitutions for pedagogy needs careful indexing.*
