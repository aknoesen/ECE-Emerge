# ECE Lab \#7: Operational Amplifiers: Part 2

**Department of Electrical and Computer Engineering**

**Spring 2025** *(Note: Acknowledgment: The lab was derived from [Simple Op Amps, For ADALM2000 by Doug Mercer](https://wiki.analog.com/university/courses/electronics/electronics-lab-1))*

---

## Overview

The purpose of Lab 7 is to:

- Implement and Experiment with Op-Amp Circuits:
  - Perform experiments involving basic operational amplifier (op-amp) circuits using negative feedback.
  - Become familiar with non-inverting amplifiers and inverting amplifiers.

- Understand the Characteristics of Op-Amps:
  - Learn about the defining properties of op-amps, including high input resistance, low output resistance, and large differential gain.
  - Understand how these characteristics make op-amps nearly ideal amplifiers and versatile building blocks in circuit applications.

---

## 1. Prelab Assignment

### 1.1 Reflective AI Exercise: Op-Amp Amplifier Configurations

**Objective:** Demonstrate understanding of how the same two Golden Rules produce two different amplifier configurations, and when each configuration is the right choice.

#### Part 1: Exploration

Example prompts are provided below. You may use them, adapt them, or write your own at the same level of specificity.

**Focus Area 1: Two Configurations, Two Golden Rules**

> *"I am an electrical engineering student preparing for a lab on op-amp amplifier circuits. Without deriving any formulas, can you explain what the two Golden Rules of an ideal op-amp force the circuit to do in an inverting amplifier configuration? Focus on what is happening physically at the inverting input terminal."*

Follow up with:

> *"Now apply the same Golden Rules to the non-inverting configuration. What is physically different at the input compared to the inverting case? Given that both configurations follow from identical rules, what accounts for the difference in how each one is used in practice?"*

**Focus Area 2: Gain-Bandwidth Product**

> *"I am using a real op-amp with a gain-bandwidth product of 1 MHz. Can you explain in physical terms what gain-bandwidth product means and why it exists as a constraint? If I configure this op-amp for a closed-loop gain of 10, what is the highest frequency at which it will still behave as expected?"*

Follow up with:

> *"If I increase the closed-loop gain to 100 using the same op-amp, what happens to the usable bandwidth? Describe what I would see on an oscilloscope if I drove this amplifier with a signal at a frequency above that limit."*

After completing both focus areas, connect them: the inverting and non-inverting configurations both have a closed-loop gain set by external resistors. Does the gain-bandwidth product constrain both configurations equally, or does the choice of configuration affect how that limit is encountered in practice?

#### Part 2: The Self-Test

Open Gemini and write your own quiz prompt targeting these two concepts. Your questions must involve explaining in physical terms, using the Golden Rules, why the two amplifier configurations behave differently, and predicting what happens to a real amplifier's output when the signal frequency or gain pushes against the gain-bandwidth product. Your prompt must explicitly instruct the AI not to ask questions that require algebraic derivations.

Apply the meta-prompt from *A Mind Worth Questioning* to evaluate and strengthen your draft, then run the quiz. Submit your original draft, the AI's critique, your revised prompt, and the full quiz transcript via the course submission app.

#### Part 3: Formal Reflection (150--250 words)

Your written synthesis must address all three of the following points:

- **The Link** -- How the same two Golden Rules produce two configurations with different input behavior, and what that difference means for how each is used in practice.
- **The Technical "Why"** -- Correct use of terms such as virtual ground, virtual short, closed-loop gain, or gain-bandwidth product.
- **The Lab Application** -- A specific Lab 7 measurement (either a gain deviation at high frequency or an output saturation event) that you can now explain using one of the real-device limits you explored.

> **Prelab Deliverable #1**
>
> Upload up to two screenshots capturing your Self-Test prompt-craft work (original draft prompt, the AI's critique, your revised prompt, and the quiz transcript) via the course submission app. Your name must be visible in each image before uploading.

> **Prelab Deliverable #2**
>
> Submit your formal written reflection (150--250 words, continuous prose) addressing all three points: The Link, The Technical "Why", and The Lab Application. Include your word count at the end. Submit via the course submission app.

---

## 2. Lab Procedure: Non-Inverting Amplifier

### 2.1 Background

The non-inverting amplifier configuration is shown in Figure 1. Like the unity-gain buffer (which is a special type of non-inverting amplifier, the feedback resistor is 0 Ohms), this circuit has the (usually) desirable property of high input resistance, so it is useful for buffering non-ideal sources:

<!-- CIRCUITIKZ FIGURE: Rendered from LaTeX source as media/non-inverting-amp-1.png -->
<img src="media/non-inverting-amp-1.png" alt="Circuit diagram of a non-inverting amplifier with a gain of 2. A sinusoidal voltage source connects from ground to the non-inverting input pin 3 of op-amp OA. The output at pin 1 is labeled Vout. A resistive feedback network sets the gain: a 1 kilohm resistor connects from the inverting input pin 2 node to ground, and a 1 kilohm feedback resistor connects from the same node up and across to the output, giving a closed-loop gain of 1 plus 1 kilohm divided by 1 kilohm, equal to 2. A 10 kilohm load resistor connects from the output node to ground." style="width: 60%; display: block; margin: 0 auto;" />

*Figure 1: Non-inverting amplifier with gain of 2. The 1 kΩ feedback and 1 kΩ ground resistors set the closed-loop gain to $1 + R_f/R_1 = 2$. The 10 kΩ resistor is the output load.*

#### Materials

- 2 1 kΩ resistors
- 1 10 kΩ resistor
- 1 LM6134 quad op-amp
- 2 0.1 μF capacitors

### 2.2 Hardware Setup

- Use the same +5 and -5 Volt connections to power as in Lab \#6.
- With the power turned off, modify your unity gain amplifier circuit of Lab \#6 as shown in Figure 1. Start with a feedback resistor of R = 1 kΩ.

> **IMPORTANT**
>
> **Leave the power supplies off. Get your setup checked off by TA or lab assistant before proceeding to the next step.**

- Turn on the power supplies and observe the current draw to be sure there are no accidental shorts.

### 2.3 Procedure

- Apply a 2 volt amplitude peak-to-peak, 1 kHz sine wave at the input, and display both input and output on the scope. Measure the voltage gain of this circuit, and compare to the theory discussed in class. Export a screenshot of the waveforms. An example is shown in Figure 2.

> **Lab Deliverable #4a**
>
> Screenshot of the oscilloscope display showing the input and output waveforms of the non-inverting amplifier with $R_2 = 1\,\text{k}\Omega$. Submit the image via the course submission app. Your name must be visible in the image before uploading.

> **Lab Deliverable #4b**
>
> Report the measured gain with $R_2 = 1\,\text{k}\Omega$ and compare it to the theoretical value. Submit via the course submission app.

<img src="media/noninverting_amp-waveform.png" alt="Scopy oscilloscope screenshot showing the input and output waveforms of a non-inverting amplifier with a gain of 2. Two sinusoidal waveforms are displayed: a purple Channel 2 input waveform and an orange Channel 1 output waveform. The orange output waveform has visibly larger amplitude than the purple input waveform, consistent with a gain of 2. Both waveforms are in phase with no observable phase shift, as expected for a non-inverting configuration. The time scale is 1 millisecond per division and the sample rate is 1600 samples at 100 kHz per 10 microseconds." style="width: 60%; display: block; margin: 0 auto;" />

*Figure 2: Example oscilloscope waveforms for the non-inverting amplifier. The orange Channel 1 output has twice the amplitude of the purple Channel 2 input with no phase shift, confirming a closed-loop gain of 2.*

- Increase the feedback resistor from 1 kΩ to about 5 kΩ. What is the measured gain now?

> **Lab Deliverable #4c**
>
> Report the measured gain with $R_2 \approx 5\,\text{k}\Omega$ and compare it to the theoretical value. Submit via the course submission app.

- Increase the feedback resistance further until the onset of clipping, that is, until the peaks of the output signal begin to be flattened due to output saturation. Record the value of resistance where this happens.

> **Lab Deliverable #4d**
>
> Record the feedback resistance at which the output begins to saturate (peaks begin to clip). Submit via the course submission app.

- Now increase the feedback resistance to 100 kΩ.

> **Lab Deliverable #4ei**
>
> Screenshot of the oscilloscope display showing the output waveform with the feedback resistor at 100 kΩ. Submit the image via the course submission app. Your name must be visible in the image before uploading.

> **Lab Deliverable #4eii**
>
> For a feedback resistance of 100 kΩ, describe and draw the input and output waveforms on a sheet of paper. Calculate the theoretical gain at this point. Calculate how small the input signal would have to be to keep the output level below 5 V. Try adjusting the waveform generator to this value and describe the output achieved. Photograph your completed work and submit the image via the course submission app. Your name must be visible in the photo.

The last step underscores an important consideration for high-gain amplifiers. High-gain necessarily implies a large output for a small input level. Sometimes this can lead to inadvertent saturation due to the amplification of some low-level noise or interference, for example the amplification of stray 60 Hz signals from power-lines that can sometimes be picked up. Amplifiers will amplify any signals at the input terminals, whether you want it or not.

---

## 3. Lab Procedure: Inverting Amplifier

### 3.1 Background

Figure 3 shows the conventional inverting amplifier configuration with a 10 kΩ "load" resistor at the output.

<!-- CIRCUITIKZ FIGURE: Rendered from LaTeX source as media/inverting-amp-1.png -->
<img src="media/inverting-amp-1.png" alt="Circuit diagram of an inverting amplifier with a gain of negative 4.7. The non-inverting input pin 3 of op-amp OA is connected directly to ground. A sinusoidal voltage source connects from ground through a 1 kilohm input resistor to the inverting input pin 2, which is the Vin node probed by Channel 2 oscilloscope to ground. A 4.7 kilohm feedback resistor connects from the inverting input node to the output pin 1, setting the closed-loop gain to negative 4.7 kilohm divided by 1 kilohm, equal to negative 4.7. The output pin 1 connects to Vout where Channel 1 oscilloscope probes to ground and a 10 kilohm load resistor connects to ground. The output is inverted and scaled by 4.7 relative to the input." style="width: 80%; display: block; margin: 0 auto;" />

*Figure 3: Inverting amplifier configuration with gain of $-R_f/R_{\text{in}} = -4.7\text{ k}\Omega / 1\text{ k}\Omega = -4.7$. The 10 kΩ resistor is the output load.*

### 3.2 Hardware Setup

- **Shut off the power supply before assembling a new circuit.**
- Assemble the inverting amplifier circuit shown in Figure 3 using 4.7 kΩ feedback resistor.
- Cut and bend the resistor leads as needed to keep them flat against the board surface, and use the shortest jumper wires for each connection. Remember, the breadboard gives you a lot of flexibility.

> **IMPORTANT**
>
> **Leave the power supplies off. Get your setup checked off by TA or lab assistant before proceeding to the next step.**

- After check-off, turn on the power supplies and observe the current draw to be sure there are no accidental shorts.

### 3.3 Procedure

- Adjust the waveform generator to produce a 2 volt amplitude peak-to-peak, 1 kHz sine wave at the input ($\text{V}_{\text{in}}$), and display both the input and output voltages on the oscilloscope.

An example of the expected waveforms is shown in Figure 4.

> **Lab Deliverable #5a**
>
> Screenshot of the oscilloscope display showing the input and output waveforms of the inverting amplifier. Submit the image via the course submission app. Your name must be visible in the image before uploading.

> **Lab Deliverable #5b**
>
> Record the measured voltage gain of the inverting amplifier ($R_f = 4.7\,\text{k}\Omega$) and compare it to the theoretical value. Submit via the course submission app.

<img src="media/inverting_amp-waveform.png" alt="Scopy oscilloscope screenshot showing the input and output waveforms of an inverting amplifier. Two sinusoidal waveforms are displayed: a purple Channel 2 input waveform with small amplitude and an orange Channel 1 output waveform with visibly larger amplitude. The orange output waveform is 180 degrees out of phase with the purple input, confirming the phase inversion of the inverting amplifier configuration. The amplitude ratio of approximately 4.7 to 1 is consistent with the expected gain of negative 4.7. The time scale is 1 millisecond per division and the sample rate is 1600 samples at 100 kHz per 10 microseconds." style="width: 60%; display: block; margin: 0 auto;" />

*Figure 4: Example oscilloscope waveforms for the inverting amplifier. The orange Channel 1 output is approximately 4.7 times larger in amplitude than the purple Channel 2 input and is inverted by 180°, confirming the expected gain of $-4.7$.*

### 3.4 Output Saturation

#### Procedure

- Now change the feedback resistor in Figure 3 from 4.7 kΩ to 10 kΩ. You do not have to switch off the power supply.
- Measure the gain now.

> **Lab Deliverable #5c**
>
> Record the measured gain with $R_f = 10\,\text{k}\Omega$ and compare it to the theoretical value. Submit via the course submission app.

- Slowly increase the amplitude of the input signal towards 2 volts until the output saturates.

> **Lab Deliverable #5d**
>
> Screenshot of the oscilloscope display showing the saturated output waveform. Note the positive and negative peak voltages at which saturation occurs. Submit the image via the course submission app. Your name must be visible in the image before uploading.

---

## 4. Lab Procedure: Summing Inverting Amplifier

The circuit of Figure 5 is a basic inverting amplifier with an additional input, called a "summing" amplifier. Using superposition we can show that $\text{V}_{\text{out}}$ is a linear sum of $\text{V}_{\text{in1}}$ and $\text{V}_{\text{in2}}$, each with their own unique gain or scale factor. In this experiment you will add two signals. One is a sinusoidal signal ($W1$) with no DC offset, and the second is a DC value ($W_2$). The output signal should be the result of the input signal $W1$ and the DC offset ($W_2$).

<!-- CIRCUITIKZ FIGURE: Rendered from LaTeX source as media/summing-amp-1.png -->
<img src="media/summing-amp-1.png" alt="Circuit diagram of an inverting summing amplifier with two weighted inputs. The non-inverting input pin 3 of op-amp OA is connected to ground. Signal generator W1 connects from ground through a 1 kilohm resistor to the inverting summing node at Vin1, giving a gain of negative 4.7. Signal generator W2 connects from ground through a 4.7 kilohm resistor to the same summing node at Vin2, giving a gain of negative 1. A 4.7 kilohm feedback resistor connects from the summing node to the output pin 1 labeled Vout. A 10 kilohm load resistor connects from the output to ground. The output voltage equals negative 4.7 times Vin1 minus Vin2." style="width: 80%; display: block; margin: 0 auto;" />

*Figure 5: Inverting summing amplifier configuration. Signal W1 is amplified by $-R_f/R_1 = -4.7$ and signal W2 by $-R_f/R_2 = -1$, giving $V_{\text{out}} = -4.7\,V_{\text{in1}} - V_{\text{in2}}$. The 10 kΩ resistor is the output load.*

### 4.1 Hardware Setup

- With the power turned off, modify your inverting amplifier circuit as shown in Figure 5. Check your connection to make sure it is connected correctly.
- Turn on the power supplies and observe the current draw to be sure there are no accidental shorts.

### 4.2 Procedure

- Use the first waveform generator (W1) to apply a sine wave $\text{V}_{\text{in1}}$, and the second waveform generator (W2) for $\text{V}_{\text{in2}}$ to apply a DC voltage.

- Apply a 1 volt amplitude peak-to-peak sine wave with no DC offset for $\text{V}_{\text{in1}}$ and 1 volt DC for $\text{V}_{\text{in2}}$.

- Observe and record the input/output waveforms on the oscilloscope screen. When used in this way, such a circuit could be called a level shifter.

> **Lab Deliverable #6a**
>
> Screenshot of the oscilloscope display showing the input and output waveforms of the level shifter. Submit the image via the course submission app. Your name must be visible in the image before uploading.

- Adjust the DC offset of waveform generator W1 ($\text{V}_{\text{in1}}$) until $\text{V}_{\text{out}}$ has zero DC component.

> **Lab Deliverable #6b**
>
> Estimate the required DC offset on W1 by observing the input waveform on the oscilloscope (note: it is not $V_{\text{in2}}$). Explain what you observe and why it makes sense. Submit via the course submission app.

- Reset the offset of waveform generator W1 to zero and apply a 2 volt amplitude peak-to-peak sine wave for $\text{V}_{\text{in1}}$. Increase the offset voltage of waveform generator W2, $\text{V}_{\text{in2}}$ slowly to 4V.

> **Lab Deliverable #6c**
>
> Record the DC voltage of $V_{\text{out}}$ when $V_{\text{in2}}$ reaches 4 V. Explain what you observe. Submit via the course submission app.

---

> **Self-Verification Checklist**
>
> Before leaving the lab, verify that you have collected all the necessary information to complete your post-lab report:
>
> - **4a:** Screenshot of non-inverting amplifier waveforms ($R_2 = 1\,\text{k}\Omega$).
> - **4b:** Measured gain with $R_2 = 1\,\text{k}\Omega$ and comparison to theory.
> - **4c:** Measured gain with $R_2 \approx 5\,\text{k}\Omega$ and comparison to theory.
> - **4d:** Feedback resistance at onset of output saturation.
> - **4ei:** Screenshot of output waveform with 100 kΩ feedback resistor.
> - **4eii:** Paper work: waveform sketch, theoretical gain calculation, minimum input amplitude, observation of adjusted output.
> - **5a:** Screenshot of inverting amplifier waveforms ($R_f = 4.7\,\text{k}\Omega$).
> - **5b:** Measured gain ($R_f = 4.7\,\text{k}\Omega$) and comparison to theory.
> - **5c:** Measured gain ($R_f = 10\,\text{k}\Omega$) and comparison to theory.
> - **5d:** Screenshot of saturated output with positive and negative peak voltages noted.
> - **6a:** Screenshot of level shifter input and output waveforms.
> - **6b:** Estimated DC offset on W1 and explanation.
> - **6c:** Recorded DC output voltage and explanation.

---

## 5. Post-Lab Analysis Report

### 5.1 Quantitative Analysis

> **Lab Deliverable #7b**
>
> Using the saturation voltages you recorded in Deliverable 5d, calculate the internal voltage drop between the supply rail ($\pm 5\,\text{V}$) and the actual output clipping level for both the positive and negative rails of the LM6134. Work on paper, showing all steps. Photograph your completed work and submit the image via the course submission app. Your name must be visible in the photo.

### 5.2 Discussion Questions

> **Lab Deliverable #7c**
>
> In the non-inverting amplifier (Experiment 4) and the inverting amplifier (Experiment 5), the gain was set by resistor ratios. Discuss: (1) why output saturation ultimately limits the useful operating range of any high-gain amplifier, and (2) how the gain-bandwidth product you calculated in the prelab would further restrict the amplifier if you increased the input frequency rather than the gain. Reference specific values from your prelab and in-lab measurements.
>
> You are encouraged to use an AI assistant to help structure your analysis or to clarify concepts such as op-amp gain-bandwidth product and output saturation. Ask it to explain, check your reasoning, or suggest a framework; then apply that framework to your own data. **The analysis you submit must be your own work: use AI as a thinking partner, not as a substitute for your own conclusions.**

> **IMPORTANT**
>
> Submit your completed work via the course submission app. All plots, images, data tables, and calculations must be clearly labeled and referenced in your post-lab report.
