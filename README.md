# AI-Robot-Path-Planning
Developed an AI robot path planning system using the A* heuristic algorithm. Optimized obstacle avoidance and shortest path detection by combining cost functions and heuristic estimates, enabling efficient and intelligent robot navigation across complex environments.

Overview
This project implements an AI-based robot path planning system using the A* (A-star) heuristic algorithm. The system efficiently finds the shortest and safest path from a start to a goal position while avoiding obstacles and prioritizing critical paths based on assigned priorities.

Features
Efficient shortest path computation using A* heuristic search

Non-collision handling to avoid obstacles

Priority-based navigation to prefer higher priority routes or targets

Real-time path visualization

Flexible for different environment setups

Algorithm
The A* algorithm uses:

G-cost: Cost from the start node to the current node

H-cost: Heuristic estimate from the current node to the goal

F-cost: F = G + H

Additional Conditions Implemented:
Non-Collision: Robot checks for obstacle-free paths during expansion.

Priority-Based Movement: Nodes are given priority values; higher-priority nodes are explored first when F-costs are equal.
