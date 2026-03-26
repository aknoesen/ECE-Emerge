# EEC1 Lab Conversion — To-Do List
*Generated 2026-03-25 after Labs 4–8 batch conversion*

## Action Items by Lab

### Lab 4
- [ ] **Duplicate `rl-setup` figure:** Two different circuits share `\label{fig:rl-setup}` in `Lab4Instructions.tex` — both currently render to `rl-setup-1.png`. If they should look visually distinct in the HTML, create a second rendered PNG with a unique name and update the Markdown reference.

### Lab 5
- [ ] **Verify subfigure PNG:** Check that `media/fig_01-1.png` visually shows both Circuit 1 and Circuit 2 side by side as intended.
- [ ] **Clean source typo:** Stray Unicode bullet `●` at line 153 of `Lab5Instructions.tex` before `\prelabdeliverable{0}{...}` — copy-paste artifact, safe to delete.

### Lab 6
- [ ] **Add missing figure:** `\ref{fig:powerconnection}` is referenced in Section 2 (Connecting DC Power) but no figure is defined in `Lab6Instructions.tex`. Placeholder "Figure 1" is in the HTML. Likely candidates already in `Labs/Lab 6 & 7 Operational Amplifiers/Media/`:
  - `LM6134BreadboardSupply.png`
  - `MarkUpL61324Power.png`
  Add the correct image to the .tex source and re-run conversion.

### Lab 7
- [ ] **Verify HTML output path:** Agent reported writing HTML to a path with `Knoosen` (double-o). Confirm `Lab7Instructions.html` is at `Lab Manuals/Lab7/htmlconversion/` under the correct `Knoesen` spelling.

### Lab 8
- [ ] **Renumber duplicate prelab deliverable:** `\prelabdeliverable{1}` is used twice in `Lab8Instructions.tex` — once in Section 1 (reflection) and again in Section 2 (INA gain selection). The Submission Instructions box says "Prelab Deliverables 2–6 (Design Document)" suggesting Section 2 deliverables should be numbered #2–#6. Fix in source .tex and re-run conversion.

---

## All Labs — General
- [ ] Open each HTML file in a browser and do a visual spot-check (images centered, math renders, blockquotes styled, tables formatted)
