from collections import namedtuple
from pprint import pprint

from map import grid
from robot import Robot
from visualization import visualize, outlinePath


class Node:
    def __init__(self, y, x, z=0):
        self.y = y
        self.x = x
        self.z = z
        self.g_cost = 0
        self.h_cost = 0
        self.score = 0
        self.parent = None

    def __repr__(self):
        return f'({self.y} {self.x} {self.z})'


Coords = namedtuple('Coords', 'y x z')


def surround_area(current_pos):
    y, x, z = current_pos.y, current_pos.x, current_pos.z
    return [
        Coords(y - 1, x, z + 1),
        Coords(y, x + 1, z + 1),
        Coords(y + 1, x, z + 1),
        Coords(y, x - 1, z + 1),
        Coords(y, x, z + 1),  # stay in place
    ]


def neighbor_cells(_map, current_pos, closed_list, robot):
    return [
        target_pos for target_pos in surround_area(current_pos)
        if is_not_wall(target_pos, _map)
        and not is_in_list(closed_list, target_pos)
        and is_not_crossed(current_pos, target_pos, robot)
    ]


def is_not_wall(pos, _map):
    height, width = len(_map), len(_map[0])
    return 0 <= pos.y < height and 0 <= pos.x < width and not _map[pos.y][pos.x]


def is_in_list(lst, pos):
    return any(is_same_pos(item, pos) for item in lst)


def is_same_pos(a, b):
    return a.y == b.y and a.x == b.x and a.z == b.z


def is_not_crossed(current_pos, target_pos, this_robot):
    z = target_pos.z
    for robot in robots:
        if robot == this_robot:
            continue

        point = robot.path[z] if z < len(robot.path) else robot.path[-1]

        # Prevent collision at same time
        if is_same_pos(Coords(point.y, point.x, z), target_pos):
            return False

        # Prevent "swap positions" (x-cross)
        if z < len(robot.path):
            if is_x_crossed(target_pos, current_pos, point):
                return False

    return True


def is_x_crossed(target_pos, current_pos, point):
    return (
        is_same_pos(point.parent, Coords(target_pos.y, target_pos.x, target_pos.z - 1))
        and is_same_pos(point, Coords(current_pos.y, current_pos.x, current_pos.z + 1))
    )


def reconstruct_path(current_pos):
    path = []
    while current_pos.parent:
        path.append(current_pos)
        current_pos = current_pos.parent
    return path[::-1]


def find_node(cell, lst):
    for item in lst:
        if is_same_pos(item, cell):
            return item
    return None


def calc_heuristic(a, b):
    base = abs(b.y - a.y) + abs(b.x - a.x)
    for robot in robots:
        if len(robot.path) > a.z:
            future = robot.path[a.z]
            if (future.y, future.x) == (a.y, a.x):
                base += 3  # Congestion penalty
    return base


def search(grid, robot):
    openlist = [robot.path[0]]
    closedlist = []

    z_max = max([len(robo.path) for robo in robots] + [0]) - 1

    while openlist:
        current_pos = min(openlist, key=lambda o: (o.score, o.h_cost))
        openlist.remove(current_pos)
        closedlist.append(current_pos)

        for target_pos in neighbor_cells(grid, current_pos, closedlist, robot):
            if target_pos.z >= z_max and target_pos.y == robot.dst.y and target_pos.x == robot.dst.x:
                end = Node(*target_pos)
                end.parent = current_pos
                return reconstruct_path(end)

            new_g_cost = current_pos.g_cost + (
                0.5 if target_pos.y == current_pos.y and target_pos.x == current_pos.x else 1
            )

            node = find_node(target_pos, openlist)
            if node and new_g_cost >= node.g_cost:
                continue

            if not node:
                node = Node(*target_pos)
                openlist.append(node)
                node.h_cost = calc_heuristic(node, robot.dst)

            node.g_cost = new_g_cost
            node.score = node.g_cost + node.h_cost
            node.parent = current_pos

    return []


if __name__ == '__main__':
    m, n = len(grid) - 1, len(grid[0]) - 1
    robots = []
    bots = []

    startNodes = [[9, 1], [39, 3], [33, 5], [24, 7], [15, 9], [16, 11], [10, 13], [14, 15], [35, 16]]
    goalNodes = [[1,2 ], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]]

    for i in range(8):
        src = Node(startNodes[i][0], startNodes[i][1])
        dst = Node(goalNodes[i][0], goalNodes[i][1])
        bots.append(Robot(f'R{i}', src, dst))

    bots.sort(key=lambda r: abs(r.dst.y - r.src.y) + abs(r.dst.x - r.src.x), reverse=True)

    for i, robot in enumerate(bots):
        robot.path = [Node(robot.src.y, robot.src.x, z=i * 2)]

    for robot in bots:
        print('Computing', robot.name, '...')
        path = search(grid, robot)
        robot.path.extend(path)
        robots.append(robot)

    
    visualize(grid, robots)
    outlinePath(grid, robots)
