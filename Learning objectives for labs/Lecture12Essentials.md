### Fundamental Topics First‑Year Engineering Students Should Master — Lecture 12

*Difficulty ratings: 1 = easiest, 3 = most challenging*

1. Creating structures — **Difficulty: 1**
   - Construct scalar and nonscalar structures with dot notation and `struct`; know valid field-name rules and inspect type with `isstruct`.
   - *Simple struct/dot syntax and isstruct checks; low conceptual load.*

2. Accessing and assigning fields — **Difficulty: 1**
   - Read/write fields with `s.field` and nested fields `s.sub.field`; guard against missing fields using `isfield` before access.
   - *Basic field access s.field; guarding with isfield is straightforward.*

3. Structure arrays and indexing — **Difficulty: 2**
   - Build and index arrays of structs (`s(1)`, `s(2).field`), extract fields across elements and understand when results are numeric arrays vs cell arrays.
   - *Understanding when field extraction yields numeric vs cell arrays and indexing nuances adds modest complexity.*

4. Dynamic field names and programmatic creation — **Difficulty: 2**
   - Use `s.(fname)` to create/access fields programmatically, validate names with `isvarname`/`namelengthmax`, and generate fields in loops safely.
   - *s.(fname) is simple syntactically but requires careful name validation and loop logic.*

5. Converting between containers (struct, cell, table) — **Difficulty: 2**
   - Convert with `fieldnames`, `struct2cell`, `cell2struct`, `struct2table`, `table2struct`; understand ordering and dimensional implications.
   - *Multiple conversion functions exist; ordering/dimensional implications need attention.*

6. Common structure utilities — **Difficulty: 1**
   - Use `fieldnames`, `isfield`, `rmfield`, `orderfields` to query/manipulate structure metadata and layout programmatically.
   - *fieldnames, isfield, rmfield, orderfields are straightforward APIs to learn.*

7. Passing and returning structures in functions — **Difficulty: 2**
   - Accept structs as inputs/outputs, support optional fields, validate with `isstruct`/`isfield`, and document expected field names/types.
   - *Function I/O and optional-field validation introduce moderate design considerations.*

8. Efficient preallocation and bulk assignment — **Difficulty: 2**
   - Preallocate structure arrays (e.g., `s(n) = struct(...)`) and assign fields without growing arrays in loops to avoid performance penalties.
   - *Preallocation pattern s(n)=struct(...) is essential for performance and requires discipline.*

9. Logical selection and aggregation from struct data — **Difficulty: 2**
   - Build masks from fields (e.g., `[s.value] > thr`), use `arrayfun`/`cellfun` for elementwise operations, and select elements by condition.
   - *Building masks ([s.value] > thr) and using arrayfun/cellfun require careful use to avoid type/shape surprises.*

10. Designing nested/hierarchical data layouts — **Difficulty: 3**
    - Model hierarchical data with nested structs, traverse or flatten nested fields for processing, and evaluate when tables or classes are more appropriate.
    - *Modeling choices, traversal/flattening logic, and when to prefer tables/classes demand design judgment.*

11. Robustness and edge‑case handling — **Difficulty: 3**
    - Handle empty structs, missing or heterogeneous fields defensively (defaults, validation), and write tests that compare structures reliably (consider `isequal`/custom comparison).
    - *Handling empty/heterogeneous/missing fields, defaults, and reliable comparisons (isequal/custom) is subtle and critical.*
