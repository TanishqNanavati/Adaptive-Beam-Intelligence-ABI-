I am a 3rd year Computer Engineering student building a software-based project.

PROJECT TITLE:
AI-Assisted Signal Optimization for LEO Satellite-based 5G Non-Terrestrial Networks (NTN)

PROBLEM STATEMENT:
In 5G-enabled Non-Terrestrial Networks (NTN), Low Earth Orbit (LEO) satellites provide wide-area connectivity. However, due to satellite mobility, uneven user distribution, and limited beam coverage, many users experience poor signal strength.

Traditional static beam allocation methods do not adapt to dynamic user distribution, leading to inefficient coverage and poor quality of service.

OBJECTIVE:
Build a software simulation that models a satellite communication system and implements an optimization algorithm to improve signal coverage and efficiency.

WHAT I WANT TO BUILD:
A Python-based simulation where:
- Users are randomly distributed on a 2D grid
- A LEO satellite provides coverage
- Signal strength depends on distance
- A baseline model shows static/inefficient coverage
- An optimization algorithm improves coverage dynamically

EXPECTED OUTPUT:
- Visualization of users and satellite
- Signal strength plots / heatmaps
- Coverage comparison (before vs after optimization)
- Clear improvement metrics (coverage %, avg signal)

TECH STACK:
- Python
- NumPy
- Matplotlib
- (Optional) scikit-learn for clustering
- (Optional advanced) PyTorch for reinforcement learning

CONSTRAINTS:
- Must run on a normal laptop
- No hardware or real RF implementation
- Keep models simple but logically correct
- Code should be modular and well-structured

--------------------------------------------------

PROJECT DEVELOPMENT PHASES:

Phase 1: Environment Setup & User Simulation
- Create 2D grid
- Generate random users
- Plot users

Phase 2: Satellite Modeling
- Define satellite position (x, y, height)
- Add movement (optional simple path)

Phase 3: Distance & Signal Model
- Compute 3D distance
- Implement signal strength model (inverse square law)

Phase 4: Baseline Coverage System
- Fixed beam radius
- Identify covered users
- Compute basic metrics

Phase 5: Visualization & Metrics
- Scatter plots (users + satellite)
- Coverage stats
- Signal distribution

Phase 6: Optimization (Core Logic)
- Improve coverage using:
  - clustering (K-means) OR
  - heuristic logic (focus weak users)

Phase 7: Performance Comparison
- Before vs after optimization
- Graphs and improvements

Phase 8 (Advanced - Optional):
- Multiple satellites
- Reinforcement learning-based optimization
- Dynamic user movement

--------------------------------------------------

INSTRUCTIONS FOR YOU (AI):

1. Act as a mentor and guide me step-by-step through each phase.

2. Start with Phase 1 only.

3. For each phase:
   - First explain the concept in simple terms
   - Then explain what we will implement
   - Then provide clean, modular Python code
   - Then suggest how I should test it

4. After giving code:
   - Ask me if I have implemented it
   - Ask if I faced any errors
   - Wait for my confirmation before moving to next phase

5. Keep interaction active:
   - Ask small questions to check my understanding
   - Suggest small improvements
   - Help debug if I get stuck

6. Do NOT dump all phases at once.

7. Keep explanations beginner-friendly but technically correct.

8. Focus on building a real engineering-style project:
   - modular code
   - proper structure
   - reusable functions

--------------------------------------------------

