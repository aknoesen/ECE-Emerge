### Fundamental Topics First‑Year Engineering Students Should Master — Lecture 5

*Difficulty ratings: 1 = easiest, 3 = most challenging*

1. Inspecting Array Dimensions and Sizes — **Difficulty: 1**
   - Use size, ndims, numel, length and compare shapes (isequal(size(A),[m n])) to write size‑robust code.
   - *API familiarity and simple checks; low conceptual load.*

2. Creating Common Matrices — **Difficulty: 1**
   - Construct zeros, ones, eye, diag, and sample/magic matrices; understand default numeric class and types.
   - *Straightforward constructor functions and basic types.*

3. Concatenation and Block Construction — **Difficulty: 2**
   - Concatenate arrays horizontally and vertically ([A,B], [A;B]); check and resolve shape compatibility issues.
   - *Simple syntax but frequent dimension‑mismatch errors require attention.*

4. Replication and Tiling — **Difficulty: 2**
   - Use repmat and implicit expansion to replicate rows/columns and tile arrays for broadcasting or repeated patterns.
   - *repmat and implicit expansion are easy to use but require shape reasoning.*

5. Reshaping and Permuting Arrays — **Difficulty: 2**
   - Change array shape with reshape, transpose (.'), and permute while preserving element count and respecting column‑major order.
   - *reshape/permute are conceptually trickier due to column‑major ordering.*

6. Linear Indexing and find — **Difficulty: 2**
   - Linearize with A(:), use A(k), and locate elements with find; convert between linear and subscripts with sub2ind/ind2sub.
   - *A(:), find, and sub2ind/ind2sub need mapping between linear and subscript views.*

7. Logical Masking and Element Selection — **Difficulty: 2**
   - Build masks via relational expressions and is* functions (isnan, isfinite, ismissing); extract and assign using logical indexing.
   - *Powerful but subtle; mask shapes and NaN/missing handling can confuse beginners.*

8. Combining Masks and Logical Functions — **Difficulty: 2**
   - Combine masks with &, |, ~ and use logical helpers to implement conditional selection/cleansing of data.
   - *Requires careful use of logical operators and parentheses for correct masks.*

9. Sorting and Reordering Data — **Difficulty: 2**
   - Sort along dimensions with sort and sortrows, obtain permutation indices, and apply them to reorder rows/columns consistently.
   - *sort/sortrows plus applying permutation indices is straightforward but error‑prone in practice.*

10. Elementwise Operations and Implicit Expansion — **Difficulty: 2**
    - Perform .*, ./, .^ and exploit implicit expansion rules; diagnose and fix size incompatibility errors.
    - *Elementwise ops are basic; implicit expansion introduces occasional nonobvious behavior.*

11. Array Manipulation Utilities and Reduction Functions — **Difficulty: 2**
    - Use utilities (flipud/fliplr, circshift, padding techniques) and reduction functions (sum, mean, max, min, cumsum, diff) with dimension arguments; interpret output shapes.
    - *Many small APIs to learn and dimension arguments to manage; moderate difficulty.*
