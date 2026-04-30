# TTS Performance Instructions
**Target engine:** OpenAI `gpt-4o-mini-tts` (instructable)
**Voice:** `ash` (baritone, warm, mature American male — closest match to a 57-year-old preventive cardiologist)
**Fallback voice:** `onyx` (deeper, slightly more formal — try if `ash` reads too young)

---

## Instructions payload (pass to `instructions` field)

```
Voice: Dr. Marcus Thompson, a 57-year-old preventive cardiologist in Boston. Warm but not saccharine. Clinical but not cold. He is recording a personal voice message to his patient between appointments — this is not a broadcast, not a podcast. It is one person talking to one person.

Affect: Steady, grounded, emotionally intelligent. He likes this patient and is quietly pleased by how dedicated they are, but he does not perform warmth. The warmth is in the pacing and the breath, not in the vowels.

Tone: Mid-chest resonance, relaxed register. Never the "news anchor" voice. Never the "reassuring doctor" voice. A real doctor speaking to a real person he respects.

Pacing: Conversational with deliberate variation. He SLOWS DOWN for the important medical information (diagnoses, numbers, recommendations) and speeds up through transitions and throat-clearing. The worst possible read is an even pace — it must breathe and vary. Natural pauses between clauses. Audible inhales before landing important beats.

Emotion by section:
- Opening acknowledgment ("You're already on a great path"): sincere, quietly moved. He means it.
- Philosophy framing ("Sometimes we shift, sometimes we monitor"): teaching register, unhurried, like describing a craft.
- The folksy closer of the philosophy ("if it ain't broke, we don't fix it"): small smile in the voice, but contained.
- Clinical findings (ATM variant, ApoB, Lp(a)): direct, unhurried, zero alarm. He is not dramatizing cancer or cardiovascular risk — these are clinical nouns delivered as information.
- Statin conversation: calm acknowledgment of patient skepticism, then confident recommendation.
- RHR + imaging: curious and generous — "you're probably just fit, but let's confirm."
- Pancreatic MRI: matter-of-fact proactive surveillance, not fear-based.
- Closing ("I'm going to keep you doing great"): quiet conviction, not slogan. 
- Final line ("Take care of yourself, Jason"): slightly slower, a small warmth on the name, then stop. Do not flourish.

Delivery texture: Permit soft mouth sounds, audible breaths, small natural hesitations. This is a phone recording in a quiet office — not a scrubbed studio master. Do not over-articulate. Let consonants soften where a real speaker's would.

Absolute rules:
- Do NOT smile through the read. Do not lean on a "friendly announcer" affect.
- Do NOT dramatize any medical term.
- Do NOT accelerate into the final line — decelerate into it.
- Numbers should land clean and unhurried: "twelve weeks" gets a tiny beat before and after.
- The em-dashes in the script represent genuine thoughtful pauses, not punctuation rhythm.
```

---

## Generation parameters

```python
model="gpt-4o-mini-tts"
voice="ash"           # try "onyx" if too young
response_format="mp3"
speed=1.0             # do NOT accelerate — the script is paced for natural delivery
instructions=<payload above>
input=<script from dr-thompson-transcript.txt>
```

---

## Notes on why `gpt-4o-mini-tts` for this test

This is the one major engine we haven't tried yet. Its selling point is **free-form natural-language performance direction** — the same way you'd brief a voice actor. Inworld bakes voice behavior into fixed presets; ElevenLabs v3 uses inline `[emotion]` tags that fight clean prose. OpenAI's model accepts prose direction.

The voices themselves score lower than Inworld/Eleven on Arena ELO blind tests, but **Arena tests don't measure directed-read-with-context-instructions** — they test stock voice quality. This engine's ceiling is different from its baseline.

The experiment: can a less-natural voice *directed specifically* beat a more-natural voice with no direction? If yes, we've found the missing lever. If no, we have our answer — voice cloning is the only path.
