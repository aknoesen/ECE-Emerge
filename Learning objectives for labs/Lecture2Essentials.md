### Fundamental Topics First‑Year Engineering Students Should Master — Lecture 2

*Difficulty ratings: 1 = easiest, 3 = most challenging*

1. Logical scalars and boolean variables — **Difficulty: 1**
   - Create, assign, and inspect logical true/false values; store and use them in the workspace.
   - *Basic creation/inspection; minimal conceptual overhead.*

2. Relational operators for comparisons — **Difficulty: 1**
   - Use <, >, <=, >=, ==, ~= to compare scalars and obtain logical results.
   - *Straightforward operator use on scalars.*

3. Logical operators and compound tests — **Difficulty: 2**
   - Combine conditions with &, |, ~, xor and understand operator precedence and parentheses.
   - *Requires understanding operator precedence and short‑circuiting nuances.*

4. Elementwise logical operations on arrays — **Difficulty: 2**
   - Apply relational and logical operators to vectors/matrices to produce logical arrays of the same shape.
   - *Applies relational logic to arrays; students must track shapes and elementwise semantics.*

5. Row and column vector concepts — **Difficulty: 1**
   - Create row vs column vectors, query size/length/numel, and understand how orientation affects operations.
   - *Simple construction and size queries; orientation concept is basic.*

6. Vector construction methods — **Difficulty: 1**
   - Build vectors using literals, concatenation, colon notation, and linspace for evenly spaced values.
   - *Literal, colon, linspace are low‑complexity tools.*

7. Integer (subscript) indexing of arrays — **Difficulty: 2**
   - Select, reorder, and repeat elements using numeric index vectors; handle bounds and index order.
   - *Needs careful handling of bounds, ordering, and common indexing mistakes.*

8. Logical (mask) indexing of arrays — **Difficulty: 2**
   - Use logical masks to extract, modify, or remove elements; ensure mask dimensions match the array.
   - *Powerful but subtle (mask shape must match, results may reshape), so moderate difficulty.*

9. Resizing and assignment to arrays — **Difficulty: 2**
   - Grow or shrink vectors via indexed assignment (including use of end), and understand implicit filling/expansion behavior.
   - *Implicit growth and use of end can confuse beginners and cause performance issues.*

10. Array creation utilities — **Difficulty: 1**
    - Use zeros, ones, rand, eye, and similar constructors appropriately for initialization and testing.
    - *API familiarity; low conceptual difficulty.*

11. Numeric comparison nuances and tolerances — **Difficulty: 3**
    - Compare floating‑point arrays with tolerances (abs(a-b) ≤ tol), and convert/orient between row and column forms as needed.
