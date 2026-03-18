# bio-engine-simulation
Biological simulation for game systems (oxygen, respiration, performance)
# Bio Engine Simulation

## Overview
This project proposes a biological simulation model for game systems,
replacing traditional HP-based mechanics with dynamic physiological states.

## Motivation
Conventional game systems often rely on simplified HP mechanics,
which fail to capture realistic biological responses.

For example:
- A headshot is often treated as just "high damage" instead of functional failure
- Neck injuries do not affect breathing
- Environmental factors like pressure rarely influence the player

This project aims to model the player as a biological system rather than a simple health value.

---

## Core Concept

The system is structured into three layers:

### 1. Neural System (Function Layer)
Represents the player's functional abilities:

- Physical performance
- Decision-making ability
- Reaction speed

This layer directly affects gameplay experience.

---

### 2. Damage System (Structural Layer)
Represents physical damage to the body:

- Damaged body parts (head, neck, torso, etc.)
- Severity of injury

This layer acts as the source of constraints on the system.

---

### 3. Metabolic System (Sustain Layer)
Represents life-supporting processes:

- Respiration
- Oxygen transport
- Energy generation and consumption

This layer maintains the internal state required for survival.

---

## System Interaction

The layers interact as follows:

Damage (Structure)  
→ affects Metabolism (Oxygen / Energy)  
→ limits Neural performance (Reaction / Movement)

This creates a chain of causality instead of a single HP value.

---

## Example Mechanics

- Neck injury → reduced respiration → lower oxygen → slower movement
- High activity → increased energy consumption → fatigue
- Low pressure environment → reduced oxygen intake → performance drop

---

## Model (Prototype)

Oxygen dynamics:

dO/dt = R - cP

Performance:

P = P_max * O

---

## Features (Planned)

- Body-part based damage system
- Oxygen-dependent performance
- Energy and fatigue simulation
- Environmental interaction (pressure, gas)
- Magic interaction with biological states

---

## Future Work

- Neural delay model
- Blood flow simulation
- Internal organ damage system