# 3D Graphics Project

> A faithful recreation of the 1980 Atari arcade classic, rebuilt in Python with OpenGL and computer graphics techniques. 

---

## Screenshots

*coming soon*

---

## Overview

This project recreates *Atari Battlezone*, the pioneering 1980 first-person tank shooter, using Python and OpenGL. It features retro wireframe 3D graphics, enemy tanks with autonomous AI, procedurally generated terrain, and arcade-style gameplay, exploring real-time 3D graphics. The game starts with a difficulty menu, then places you in a first-person battlefield where you navigate, aim, shoot, and survive waves of enemies across multiple levels, using pygame for the window/event loop and PyOpenGL for rendering.

---

## Technical Highlights & Features

- **First-person wireframe rendering** — retro vector-style 3D visuals inspired by the original  
- **Tank controls** — smooth forward, backward, and turning movement  
- **Shooting mechanics** — projectile firing with raycasting-based hit detection, blocked by obstacles  
- **Raycasting** — line-of-sight detection for enemy attacks with proper obstruction handling  
- **Enemy AI** — three distinct types using state machines  
  - Guard: patrol → attack → return  
  - Hunter: approach → charge  
  - Sniper: advance → hold → retreat  
- **Pathfinding** — positional correction-based avoidance prevents overlap while blending with target-seeking  
- **Procedural world generation** — randomized obstacles and enemies scaled by level and difficulty  
- **Difficulty system** — Easy, Normal, and Hard with scaling enemy count and damage  
- **HUD & game states** — score, lives, scope indicator, plus menu, gameplay, and game-over screens
  
---

## Project Structure

- `main.py` starts the game
- `engine/` contains window setup, configuration, and launch logic
- `objects/` contains the player, enemy, bullet, world, and game state classes
- `render/` contains OpenGL drawing code for the world, HUD, menu, and overlays
- `math3d/` contains raycasting, collision, and pathfinding helpers
- `game_ai/` contains enemy behavior logic
- `models/` stores the tank model assets used by the renderer
  
---

## Enemy Types

| Type | Behavior | Dominant In |
|------|----------|-------------|
| **Guard** | Patrols a fixed area, attacks when player enters range | Easy |
| **Hunter** | Aggressively chases and closes to point-blank range | Normal |
| **Sniper** | Keeps distance, retreats when approached, fires from afar | Hard |

Enemy spawn ratios shift by difficulty:

| Difficulty | Guard | Hunter | Sniper |
|------------|-------|--------|--------|
| Easy | 60% | 30% | 10% |
| Normal | 30% | 40% | 30% |
| Hard | 10% | 40% | 50% |

---

## 🚀 Getting Started

### Requirements

- Python 3.10+
- PyOpenGL
- pygame or GLFW (for windowing)

### Install

```bash
pip install PyOpenGL PyOpenGL_accelerate pygame
```

### Run

```bash
python main.py
```

---

## Controls

| Key | Action |
|-----|--------|
| `W` | Move forward |
| `S` | Move backward |
| `A` | Rotate left |
| `D` | Rotate right |
| `Q` | Aim left |
| `E` | Aim right |
| `Space` | Shoot |
| `Esc` | Quit |

---

## References

- [Atari Battlezone (1980)](https://en.wikipedia.org/wiki/Battlezone_(1980_video_game))
- [Computer Graphics — CMPUT 411, University of Alberta](https://apps.ualberta.ca/catalogue/course/cmput/411)
- [Tank STL/OBJ Model — Thingiverse](https://www.thingiverse.com/thing:3695414)
- [OpenGL Documentation](https://www.opengl.org/documentation/)

*Inspired by the original Atari Battlezone © 1980 Atari Inc.*
