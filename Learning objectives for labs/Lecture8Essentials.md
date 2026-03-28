### Fundamental Topics First‑Year Engineering Students Should Master — Lecture 8

*Difficulty ratings: 1 = easiest, 3 = most challenging*

1. 1‑D Interpolation Fundamentals — **Difficulty: 2**
   - Use interp1 with appropriate methods ('linear','spline','pchip') to evaluate functions between sampled points and choose method for smoothness vs local accuracy.
   - *API use is simple, but choosing methods (linear vs spline vs pchip) and understanding tradeoffs requires judgment.*

2. Extrapolation Handling and Domain Guards — **Difficulty: 3**
   - Detect out‑of‑range query points and handle extrapolation by specifying methods/values or by precluding/outlining safe behavior for queries outside data range.
   - *Detecting/mitigating out‑of‑range behavior and specifying safe policies is subtle and important for robustness.*

3. Polynomial Fitting and Limitations — **Difficulty: 3**
   - Fit polynomials with polyfit/polyval, inspect high‑degree instability (Runge phenomenon), and prefer lower‑order or piecewise/local interpolants when appropriate.
   - *Fitting is straightforward, but recognizing Runge instability and when to avoid high‑degree fits needs deeper numerical insight.*

4. Linear Least Squares Regression — **Difficulty: 2**
   - Formulate and solve overdetermined linear models using backslash (or normal equations), compute residuals, and evaluate predictive performance on test data.
   - *Formulation and solution with backslash are routine; model validation and overfitting considerations add complexity.*

5. Nonlinear Curve Fitting Basics — **Difficulty: 3**
   - Fit nonlinear models using nlinfit/lsqcurvefit or custom optimizers, provide sensible initial guesses, and assess fit quality via residual norms and diagnostic plots.
   - *Requires familiarity with optimizer behavior, initial guesses, and diagnostic assessment — higher conceptual and practical difficulty.*

6. Numerical Integration: Functions — **Difficulty: 2**
   - Integrate continuous functions numerically with integral (and integral2), set tolerances, and handle singularities or improper integrals by splitting domains or transformations.
   - *Using integral/integral2 is direct, but handling singularities and tolerance settings requires care.*

7. Numerical Integration: Discrete Data — **Difficulty: 1**
   - Integrate sampled data with trapz and compute cumulative integrals with cumtrapz; account for nonuniform spacing and sampling resolution effects.
   - *trapz and cumtrapz usage is straightforward; main concerns are spacing and interpretation.*

8. Numerical Differentiation and Finite Differences — **Difficulty: 3**
   - Compute derivatives from discrete samples using forward/central/backward differences and gradient; understand sensitivity to step size and noise amplification.
   - *Noise amplification and step‑size tradeoffs make stable numerical differentiation challenging.*

9. Root Finding for Scalar Equations — **Difficulty: 2**
   - Find zeros with fzero and implement safeguarded Newton–Raphson iterations (derivative or finite‑difference derivative, tolerances, max iterations).
   - *fzero is easy to use; implementing safeguarded Newton methods and ensuring convergence needs more care.*

10. Solving Nonlinear Systems (Vector Roots) — **Difficulty: 3**
    - Use fsolve for systems of nonlinear equations, supply reasonable initial guesses, interpret solver outputs and convergence diagnostics, and recognize nonuniqueness issues.
    - *fsolve and multi‑variable root finding require good initial guesses, solver tuning, and interpreting convergence — higher difficulty.*

11. Validation, Error Quantification, and Tolerance Selection — **Difficulty: 3**
    - Quantify absolute/relative errors, set meaningful tolerances for solvers/integrators/differentiation, and design tests that compare results within specified tolerances (abs(a-b) ≤ tol).
    - *Choosing meaningful absolute/relative tolerances and designing tolerant tests requires numerical judgment and experience.*
