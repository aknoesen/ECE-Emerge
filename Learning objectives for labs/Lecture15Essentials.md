### Fundamental Topics First‑Year Engineering Students Should Master — Lecture 15

*Difficulty ratings: 1 = easiest, 3 = most challenging*

1. Scripts with Local Functions — **Difficulty: 1**
   - Place local functions at the end of a script, call them from the script body, and understand their scope is limited to the same file.
   - *Simple placement and call semantics; scope limited to file is straightforward.*

2. Functions with Subfunctions — **Difficulty: 2**
   - Define a primary function with subfunctions in the same file, pass data via arguments, and recognize each subfunction has its own workspace separate from the caller.
   - *Subfunction workspaces are separate; understanding call patterns and file organization requires attention.*

3. Nested Functions and Shared Workspace — **Difficulty: 3**
   - Use nested functions to share and modify variables in the parent function's workspace without explicit argument passing; understand lifetime and scope implications.
   - *Shared parent workspace and side effects are powerful but subtle for correct lifetime and mutation semantics.*

4. Anonymous Functions for Compact Behavior — **Difficulty: 1**
   - Create anonymous functions with `@` for short expressions and callbacks, capture external variables by value, and know they are limited to single expressions.
   - *Creating @ functions is syntactically simple; capture-by-value semantics are easy to learn.*

5. Function Handles and Higher‑Order Programming — **Difficulty: 2**
   - Create and pass function handles, store them in arrays/cells, invoke them directly or with `feval`, and use handles for callbacks, integrators, and customizable algorithms.
   - *Passing/storing/invoking handles is conceptually straightforward; using them in generic APIs takes practice.*

6. Workspaces and Variable Scope — **Difficulty: 3**
   - Distinguish base/script/function/nested workspaces; predict visibility and lifetime of variables created in scripts, functions, and nested contexts.
   - *Distinguishing base/script/function/nested scopes and predicting lifetime/visibility is a common source of confusion.*

7. Global Variables: Use and Alternatives — **Difficulty: 3**
   - Use `global` to share state across functions only when necessary, demonstrate risks (hidden state, side effects), and prefer passing arguments, handles, or `persistent` variables.
   - *Simple to use but designing safe alternatives (argument passing, handles, persistent) and understanding risks is advanced practice.*

8. Persistent Variables for Retained State — **Difficulty: 2**
   - Implement `persistent` to retain state between calls, initialize safely on first call, and provide explicit reset patterns to avoid stale or unsafe state.
   - *persistent is easy to declare; correct initialization, reset patterns, and avoiding stale state need care.*

9. Recursion and Termination Safeguards — **Difficulty: 2**
   - Write recursive functions with correct base case(s), monitor recursion depth, and include safeguards (max depth, input validation) to prevent runaway recursion.
   - *Writing recursive routines with base cases is basic; adding depth checks and robustness raises complexity modestly.*

10. Flexible Argument and Output Handling — **Difficulty: 2**
    - Use `nargin`, `nargout`, `varargin`, and `varargout` to accept optional inputs and return variable outputs; document and validate optional arguments robustly.
    - *Using nargin/nargout/varargin/varargout is routine API work; designing clear optional-argument behavior and validation requires thought.*

11. Defensive Function Design and Error Handling — **Difficulty: 3**
    - Validate input types/sizes/ranges, use `assert`/`error`/`warning` appropriately, signal clear error messages, and write tests for normal and edge cases to ensure robust behavior.
    - *Validating inputs, choosing appropriate assert/error/warning usage, and writing comprehensive tests for edge cases demand careful design and experience.*
