#!/usr/bin/env python3
"""Generate Dr. Thompson voice with OpenAI gpt-4o-mini-tts + director's instructions."""
import os, sys, pathlib
from openai import OpenAI

INSTRUCTIONS = """Voice: Dr. Marcus Thompson, a 57-year-old preventive cardiologist in Boston. Warm but not saccharine. Clinical but not cold. He is recording a personal voice message to his patient between appointments — this is not a broadcast, not a podcast. It is one person talking to one person.

Affect: Steady, grounded, emotionally intelligent. He likes this patient and is quietly pleased by how dedicated they are, but he does not perform warmth. The warmth is in the pacing and the breath, not in the vowels.

Tone: Mid-chest resonance, relaxed register. Never the "news anchor" voice. Never the "reassuring doctor" voice. A real doctor speaking to a real person he respects.

Pacing: Conversational with deliberate variation. Slow down for important medical information (diagnoses, numbers, recommendations) and speed up through transitions. The worst possible read is an even pace — it must breathe and vary. Natural pauses between clauses. Audible inhales before landing important beats.

Emotion by section:
- Opening acknowledgment ("You're already on a great path"): sincere, quietly moved.
- Philosophy framing ("Sometimes we shift, sometimes we monitor"): teaching register, unhurried.
- The folksy closer ("if it ain't broke, we don't fix it"): small smile in the voice, contained.
- Clinical findings (ATM variant, ApoB, Lp(a)): direct, unhurried, zero alarm. Clinical nouns delivered as information.
- Statin conversation: calm acknowledgment of patient skepticism, then confident recommendation.
- RHR + imaging: curious and generous — "you're probably just fit, but let's confirm."
- Pancreatic MRI: matter-of-fact proactive surveillance, not fear-based.
- Closing ("I'm going to keep you doing great"): quiet conviction, not slogan.
- Final line ("Take care of yourself, Jason"): slightly slower, small warmth on the name, then stop. Do not flourish.

Delivery texture: Permit soft mouth sounds, audible breaths, small natural hesitations. This is a phone recording in a quiet office — not a scrubbed studio master. Do not over-articulate.

Absolute rules:
- Do NOT smile through the read.
- Do NOT dramatize any medical term.
- Do NOT accelerate into the final line — decelerate into it.
- Numbers land clean and unhurried.
- Em-dashes are genuine thoughtful pauses."""

script_path = pathlib.Path("/Users/jasonyim/Projects/MeridianPatient/assets/dr-thompson-transcript.txt")
script = script_path.read_text().strip()

client = OpenAI()
out_dir = pathlib.Path("/Users/jasonyim/Projects/MeridianPatient/assets/voice_ab_v2")

voice = sys.argv[1]
out_path = out_dir / f"openai-{voice}-directed.mp3"

print(f"Generating {voice}...")
with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice=voice,
    input=script,
    instructions=INSTRUCTIONS,
    response_format="mp3",
    speed=1.0,
) as response:
    response.stream_to_file(out_path)

print(f"Done: {out_path} ({out_path.stat().st_size} bytes)")
