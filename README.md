## 🎮 3D Graphics Project (OpenGL)

**Goal:** Rebuild Atari Battlezone or create a similar project

**Tech Stack:** Python, OpenGL

**Features:**

* First-person view with retro-style wireframe graphics
* Tank movement & shooting mechanics
* Procedural terrain generation
* Multiple enemies with simple AI (chase/fire)
* HUD with lives, and score
* Game loop with win/lose conditions

---

### ✅ Workflow & Milestones Checklist

#### MVP 1: Basic Framework & Movement
- [x] Set up Python and OpenGL development environment
- [x] Create window and rendering context
- [x] Implement first-person camera controls (look & move)
- [x] Render simple wireframe objects (e.g., tank model placeholder)
- [x] Basic tank movement mechanics (forward, backward, turn)

#### MVP 2: Shooting & Enemy Basics
- [x] Implement shooting mechanics (projectiles firing)
- [x] Create simple enemy models (wireframe)
- [x] Implement maual basic enemy movement (similar to player)
- [x] Generate multiple enemies at random locations
- [x] Scope detects when enemy in line and changes
- [x] Collision detection for projectiles and enemies

#### MVP 3: Game, Effects & Gameplay
- [x] Add HUD elements (score display, lives counter, etc.)  
- [x] Implement win/lose conditions  
- [x] Smoothen player and bullet movements
- [x] Add game state system (menu, playing, game over) 
- [x] Raytracing hindered by obstacles (leaving for easy testing)

#### MVP 4: Enemy AI & Finishing Touches 
- [x] Border handling and hit signs
- [x] Make enemy behavior autonomous (AI patrol or attack)
  - [x] snipers/hiders (hides and keeps distance then snipes from afar) (majority in hard mode, minority in easy)
  - [x] aggresive/hunters (hunt you from the jump and chases you relentlessly) (majority in medium mode)
  - [x] patrollers/guards (circles a certain area till you're in range then attacks) (majority in easy mode, minority in hard)
- [ ] Enemies should avoid obstacles and other enemies (replace move foward with pathfinding) + raytracing for enemy shooting
- [ ] Finishing touches + UPD readme with pictures (mountains maybe)

---

### 📚 References

**OpenGL & Game Dev Tutorials**

* [Computer Graphics Basics and OpenGL](https://apps.ualberta.ca/catalogue/course/cmput/411)
* [Tank STL and OBJ Model](https://www.thingiverse.com/thing:3695414)
