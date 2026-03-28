### Fundamental Topics First‑Year Engineering Students Should Master — Lecture 10

*Difficulty ratings: 1 = easiest, 3 = most challenging*

1. Creating and distinguishing text types — **Difficulty: 1**
   - Create string scalars/arrays and character vectors; test types with isstring/ischar/isStringScalar.
   - *Basic constructors and type tests; straightforward API.*

2. Text concatenation and appending — **Difficulty: 1**
   - Combine text using +, append, strcat, and char-array bracket concatenation; know resulting types and behaviors.
   - *Simple operations, but watch resulting type (string vs char).*

3. Converting between text and numeric/container types — **Difficulty: 2**
   - Convert with string/char/cellstr, parse numbers with str2double/sscanf, and format numbers with num2str/sprintf robustly.
   - *Requires careful choice of conversion/format functions and error handling.*

4. Measuring and validating text objects — **Difficulty: 1**
   - Use strlength, numel and type checks to measure and validate text shape and scalar/array status.
   - *Simple size/type queries and scalar vs array checks.*

5. Case, whitespace, and character property handling — **Difficulty: 1**
   - Normalize and trim text with lower/upper/strtrim and test character classes with isstrprop/isletter/isspace.
   - *Direct functions (lower/upper/strtrim/isstrprop) with low conceptual load.*

6. Text comparison and logical masks — **Difficulty: 2**
   - Compare and match text using ==, strcmp/strcmpi, contains, startsWith, endsWith, matches to produce logical masks.
   - *Multiple APIs (==, strcmp, contains) and type differences add modest complexity.*

7. Finding and locating substrings — **Difficulty: 2**
   - Locate substrings with strfind/contains/matches and use resulting indices or logicals to extract or index parts.
   - *Several similar functions produce different output shapes/types; need attention.*

8. Extracting, replacing, and editing text — **Difficulty: 2**
   - Extract with extractBetween/Before/After and modify with replace/replaceBetween/strrep while preserving desired output types.
   - *Numerous specialized functions; choosing the right one and preserving types is moderately tricky.*

9. Splitting, joining, and tokenization — **Difficulty: 2**
   - Tokenize text with split/strsplit and reassemble tokens with join/strjoin; convert between token lists and delimited strings.
   - *Token/list conversions and delimiter edge cases require care.*

10. Pattern matching and regular expressions — **Difficulty: 3**
    - Build and apply patterns using contains/matches or regexp/regexpi for complex find/extract/replace operations.
    - *regexp usage and crafting patterns are powerful but conceptually and syntactically challenging.*

11. Robust formatting and parsing of text data — **Difficulty: 3**
    - Format values with sprintf/compose and parse structured text with sscanf/textscan; handle invalid or mixed-type inputs safely.
    - *Designing tolerant parsing/formatting for mixed or invalid data requires careful validation and error handling.*
