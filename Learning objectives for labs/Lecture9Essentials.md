### Fundamental Topics First‑Year Engineering Students Should Master — Lecture 9

*Difficulty ratings: 1 = easiest, 3 = most challenging*

1. Creating Figures and Basic UI Components — **Difficulty: 2**
   - Programmatically create figures and add basic UI controls (buttons, labels, sliders); set and query common properties (Position, String, Value).
   - *API is straightforward but requires understanding properties and coordinate positioning.*

2. Message and Alert Dialogs — **Difficulty: 1**
   - Display informational, warning, and error dialogs (msgbox/warndlg/errordlg or uialert) and handle user acknowledgement flow.
   - *Simple functions with predictable behavior; low conceptual load.*

3. Collecting and Validating User Input — **Difficulty: 2**
   - Request input via inputdlg or edit fields, convert/validate types and ranges, and provide clear feedback for invalid entries.
   - *Input parsing and clear validation/feedback add modest complexity.*

4. Converting Scripts to Simple Interactive Apps — **Difficulty: 2**
   - Turn procedural scripts into Live Script apps or simple GUIs that run predictably and update outputs in sequence.
   - *Conceptually simple, but requires restructuring code and managing UI flow.*

5. Event‑Driven Callbacks — **Difficulty: 3**
   - Write callbacks for UI components that execute on user interaction and correctly access inputs and update outputs.
   - *Moving from procedural to event‑driven thinking and correct callback design is challenging for beginners.*

6. State Management Across Callbacks — **Difficulty: 3**
   - Share and persist state safely between callbacks using guidata/app properties/handles rather than globals.
   - *Proper sharing/persistence (guidata/app properties) without globals needs careful design.*

7. Dynamic UI Updates and Control Flow — **Difficulty: 2**
   - Enable/disable controls, update labels/plots/tables dynamically, and reflect internal state changes immediately in the UI.
   - *Enabling/disabling and reflecting state is practical but requires attention to timing and consistency.*

8. Embedding and Updating Plots and Tables — **Difficulty: 2**
   - Place axes and uitable components in GUIs, update their data from callbacks, and coordinate interactions (selection, zoom) with other components.
   - *Updating UI axes/uitable from callbacks is routine but requires correct data binding and redraw handling.*

9. Input Validation and Immediate User Feedback — **Difficulty: 2**
   - Implement validation within callbacks, give immediate feedback (highlight, dialogs), and prevent invalid operations through UI gating.
   - *Implementing robust, responsive validation inside callbacks is important and moderately tricky.*

10. App Designer Basics and Component APIs — **Difficulty: 2**
    - Build small apps in App Designer, wire ValueChangedFcn/Callback handlers, and use component properties consistently from design and code views.
    - *App Designer simplifies many tasks; learning its component API and callback wiring is a moderate step.*

11. Timers, Asynchronous Tasks, and Clean Cancellation — **Difficulty: 3**
    - Use timers or background/asynchronous patterns for periodic or long‑running tasks, provide progress feedback, and implement safe cancellation/cleanup.
    - *Concurrency, background tasks, progress reporting, and safe cancellation are advanced and error‑prone.*
