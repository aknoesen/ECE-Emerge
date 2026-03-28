### Fundamental Topics First‑Year Engineering Students Should Master — Lecture 7

*Difficulty ratings: 1 = easiest, 3 = most challenging*

1. Class definition and basic constructor — **Difficulty: 2**
   - Create a classdef file and write a constructor that initializes object properties from inputs.
   - *Requires file structure and constructor pattern; straightforward but new syntax/concepts.*

2. Declaring and using properties — **Difficulty: 2**
   - Define properties, read/write them, and understand common attributes (e.g., Constant, Dependent).
   - *Basic declarations easy; attributes and validation add moderate complexity.*

3. Instance and static methods — **Difficulty: 2**
   - Implement instance methods that operate on object data and static methods callable without an object.
   - *Method syntax is simple; understanding when to use static vs instance is conceptual.*

4. Access control for encapsulation — **Difficulty: 3**
   - Apply Access attributes (public, protected, private) to restrict visibility and enforce encapsulation.
   - *Visibility rules and design choices (public/protected/private) require careful thinking.*

5. Getters and setters (property accessors) — **Difficulty: 3**
   - Implement set/get methods or Dependent properties to validate or transform values on assignment/read.
   - *Accessor semantics, return rules for value vs handle classes, and side effects are subtle.*

6. Handle vs value class semantics — **Difficulty: 3**
   - Understand reference (handle) vs value behavior, demonstrate assignment/copy differences, and implement cleanup for handles.
   - *Reference vs copy behavior causes common logic bugs; important and conceptually tricky.*

7. Simple operator overloading — **Difficulty: 2**
   - Overload at least one operator (e.g., plus, eq) to enable intuitive object operations and test expected results.
   - *Mechanical once pattern is clear, but testing and consistent semantics add effort.*

8. Designing stateful classes (mutating behavior) — **Difficulty: 3**
   - Build a class that manages internal state (e.g., seat reservation) with methods enforcing valid state transitions.
   - *Correct state transitions, invariants, and mutation handling are design‑heavy and error‑prone.*

9. Arrays of objects and indexing — **Difficulty: 2**
   - Create, index, and concatenate object arrays; understand how object arrays behave versus numeric arrays.
   - *Indexing is similar to arrays but object behavior (handle vs value) can introduce surprises.*

10. Inheritance and method overriding — **Difficulty: 3**
    - Subclass a superclass, override a method, and call superclass constructors/methods appropriately.
    - *Superclass/subclass interactions, constructor chaining, and correct overriding need careful design.*

11. Introspection, validation, and robustness — **Difficulty: 3**
    - Use type checks (isa), meta information for testing, validate inputs in constructors/methods, and ensure objects are save/load friendly.
    - *Meta‑programming, validation patterns, and save/load robustness require deeper API knowledge and defensive coding.*
