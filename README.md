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

![Image Alt](https://github.com/CodeRockstar24/AI-Robot-Path-Planning/blob/79733c61c35aaa433fc9a96dcc09c31c8b7d8a71/Algorithm.png)

*** Priority Based Path Finding ***
![Image Alt](https://github.com/CodeRockstar24/AI-Robot-Path-Planning/blob/88ddf95786c3110d5cd0816a800f562f8f7542fc/Non%20Collision%20%2B%20Priority.png)


