### Fundamental Topics First‑Year Engineering Students Should Master — Lecture 14

*Difficulty ratings: 1 = easiest, 3 = most challenging*

1. Cell Array Construction — **Difficulty: 1**
   - Create cell arrays with {} and the cell function, preallocate for performance, and use cells to hold heterogeneous types/sizes.
   - *Basic syntax ({}, cell) and preallocation patterns; straightforward once heterogeneity concept is clear.*

2. Indexing Cells: Contents vs Containers — **Difficulty: 2**
   - Distinguish parentheses () for cell slices and curly braces {} for contents; extract and assign single elements, subarrays, and nested cells correctly.
   - *Distinguishing () vs {} and correct extraction/assignment is a common source of confusion.*

3. Dynamic and Programmatic Cell Access — **Difficulty: 2**
   - Use dynamic indexing (C{idx}), comma‑separated lists to unpack multiple cells, and programmatically build arrays from compatible cell contents.
   - *Comma‑separated lists and programmatic unpacking require attention to output shapes and compatibility.*

4. Cell‑Array Utilities and Conversions — **Difficulty: 2**
   - Apply cellfun, celldisp, cell2mat, num2cell, and mat2cell to process, summarize, and convert between cell and ordinary array representations.
   - *cellfun, cell2mat, mat2cell are powerful but demand careful handling of element types/sizes.*

5. Passing Cells To/From Functions — **Difficulty: 2**
   - Accept and return cell arrays, handle variable numbers of outputs with comma‑separated lists, and document expected cell shapes/types for robust APIs.
   - *Varargout/varargin and comma‑separated lists introduce API design considerations and edge cases.*

6. Categorical Arrays: Creation and Inspection — **Difficulty: 2**
   - Create categorical arrays from text or factors, inspect category levels, and understand ordered vs unordered behavior for comparisons and grouping.
   - *Creating and inspecting categories is easy; understanding ordered vs unordered semantics adds nuance.*

7. Managing Categories: Reorder, Merge, Missing — **Difficulty: 3**
   - Rename/add/remove/reorder categories, handle undefined/missing category values, and control underlying levels using categorical options.
   - *Renaming/reordering/merging categories and handling missing levels can be subtle and important for analysis correctness.*

8. Table Construction and Basic Manipulation — **Difficulty: 1**
   - Build tables from arrays/cells/variables, name variables, add/remove columns and rows, and query table size and variable types.
   - *Building tables and basic column/row operations are API‑centric and easy to learn.*

9. Extracting Data From Tables — **Difficulty: 2**
   - Index tables by variable name or position; extract variables as arrays, cell arrays, or sub‑tables using dot notation, (), and {} appropriately.
   - *Multiple indexing methods (dot, (), {}) produce different types; correct extraction requires attention.*

10. Grouping, Aggregation, and Joins With Tables — **Difficulty: 3**
    - Use groupsummary, rowfun, varfun for aggregation and join/innerjoin/outerjoin to combine tabular datasets for relational operations.
    - *Groupwise summaries and joins involve relational thinking and careful treatment of keys, missing values, and result shapes.*

11. Import/Export Workflows and Choosing Containers — **Difficulty: 3**
    - Import/export data with readtable/writetable/datastore patterns, connect conceptually to external data stores, and choose between table, cell, categorical (or struct) for downstream analysis.
    - *Deciding between tables/cells/categoricals, and designing robust import/export flows for downstream analysis requires broader data‑engineering judgment.*
