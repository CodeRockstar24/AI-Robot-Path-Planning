# AI-Robot-Path-Planning
Developed an AI robot path planning system using the A* heuristic algorithm. Optimized obstacle avoidance and shortest path detection by combining cost functions and heuristic estimates, enabling efficient and intelligent robot navigation across complex environments.

Overview
This project implements an AI-based robot path planning system using the A* (A-star) heuristic algorithm. The system efficiently finds the shortest and safest path from a start to a goal position while avoiding obstacles and prioritizing critical paths based on assigned priorities.

Features
1. Efficient shortest path computation using A* heuristic search

2. Non-collision handling to avoid obstacles

3. Priority-based navigation to prefer higher priority routes or targets

4. Real-time path visualization

5. Flexible for different environment setups
   

The A* algorithm uses:

1 -G-cost: Cost from the start node to the current node

2- H-cost: Heuristic estimate from the current node to the goal

3- F-cost: F = G + H


Additional Conditions Implemented:
1* Non-Collision: Robot checks for obstacle-free paths during expansion.

2* Priority-Based Movement: Nodes are given priority values; higher-priority nodes are explored first when F-costs are equal.
