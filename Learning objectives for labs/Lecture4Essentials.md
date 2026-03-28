### Fundamental Topics First‑Year Engineering Students Should Master — Lecture 4

*Difficulty ratings: 1 = easiest, 3 = most challenging*

1. Creating and inspecting 2D arrays (matrices) — **Difficulty: 1**
   - Construct matrices, use size/ndims/numel, and understand MATLAB's column‑major memory layout.
   - *Basic construction and querying (size, ndims, numel); memory layout concept is introductory.*

2. Element access and assignment with (row,col) indexing — **Difficulty: 1**
   - Read and write individual entries using A(i,j); handle out‑of‑range errors.
   - *Simple syntax A(i,j) and bounds checking; fundamental skill.*

3. Linear indexing and conversions — **Difficulty: 2**
   - Use A(k) and A(:), convert between linear and subscript indices with sub2ind/ind2sub, and reason about linearized ordering.
   - *Linear vs subscript indexing and sub2ind/ind2sub require conceptual mapping to column‑major order.*

4. Row/column slicing with the colon operator — **Difficulty: 1**
   - Select full rows/columns and ranges (A(:,j), A(i,:), A(i,1:3)) and know how returned shapes differ.
   - *Common operations (A(:,j), A(i,:), ranges) with predictable shapes; low difficulty.*

5. Concatenation of matrices — **Difficulty: 2**
   - Join arrays horizontally [A,B] and vertically [A;B], and ensure dimension compatibility.
   - *Straightforward syntax, but dimension compatibility errors are a common stumbling block.*

6. Multi‑element indexing with integer index vectors — **Difficulty: 2**
   - Index submatrices or arbitrary element sets via A(rows,cols), including repeated and reordered indices.
   - *Reordering/repeating indices is powerful but requires careful attention to dimensions and results.*

7. Logical masks for selection and assignment — **Difficulty: 2**
   - Build logical arrays (A > v, A==v) and use them to extract or assign elements; understand column‑major extraction order.
   - *Useful but subtle (mask shape, assignment semantics, extraction order); moderate difficulty.*

8. Constructing logical index expressions — **Difficulty: 2**
   - Combine relational and logical operators to form masks for conditional selection and modification.
   - *Combining relational/logical operators to form masks needs precision and parentheses for clarity.*

9. Using end in index expressions — **Difficulty: 1**
   - Use end to write size‑robust slices (A(end,:), A(1:end-1,end)) and avoid hard‑coding dimensions.
   - *Small but very useful feature for size‑robust code; low conceptual load.*

10. Reshaping and linear view operations — **Difficulty: 2**
    - Change shapes safely with reshape, flatten with A(:), and be aware of how transpose (.' vs ') affects layout and conjugation.
    - *reshape, A(:), and transpose differences can be nonintuitive; watch element ordering and conjugation.*

11. Safe shape manipulation and error avoidance — **Difficulty: 2**
    - Use size/length to guide operations, check compatibility before concatenation/indexing, and prefer clear, robust indexing patterns.
    - *Defensive checks (size, length) and compatibility reasoning are essential practice, moderate difficulty.*
