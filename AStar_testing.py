from collections import namedtuple
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
    return [Coords(y - 1, x, z + 1),
            Coords(y, x + 1, z + 1),
            Coords(y + 1, x, z + 1),
            Coords(y, x - 1, z + 1),
            Coords(y, x, z + 1)]  # wait action


def neighbor_cells(_map, current_pos, closed_list, robot):
    return [target_pos for target_pos in surround_area(current_pos)
            if (is_not_wall(target_pos, _map) and
                not is_in_list(closed_list, target_pos) and
                is_not_crossed(current_pos, target_pos, robot))]


def is_not_wall(_position, _map):
    height = len(_map)
    width = len(_map[0])
    y = _position.y
    x = _position.x
    return 0 <= y < height and 0 <= x < width and not _map[y][x]


def is_in_list(list, pos):
    for item in list:
        if is_same_pos(item, pos):
            return True
    return False


def is_same_pos(a, b):
    return a.y == b.y and a.x == b.x and a.z == b.z


def is_not_crossed(current_pos, target_pos, this_robot):
    z = target_pos.z
    for robot in robots:
        if robot == this_robot:
            break  # Only check robots with higher priority

        if z < len(robot.path):
            point = robot.path[z]
        else:
            point = robot.path[-1]  # Wait at last cell

        if is_same_pos(Coords(point.y, point.x, z), target_pos):
            return False

        if z < len(robot.path) and point.parent:
            if (is_same_pos(point.parent, Coords(target_pos.y, target_pos.x, target_pos.z - 1)) and
                is_same_pos(point, Coords(current_pos.y, current_pos.x, current_pos.z + 1))):
                return False

    return True


def reconstruct_path(current_pos):
    path = []
    while current_pos.parent:
        path.append(current_pos)
        current_pos = current_pos.parent
    path.reverse()
    return path


def find_node(cell, list):
    for item in list:
        if is_same_pos(item, cell):
            return item
    return None


def calc_heuristic(a, b):
    return abs(b.y - a.y) + abs(b.x - a.x)


def search(grid, robot):
    openlist = []
    closedlist = []
    openlist.append(robot.path[0])  # start node

    while openlist:
        current_pos = min(openlist, key=lambda o: (o.score, o.h_cost))
        openlist.remove(current_pos)
        closedlist.append(current_pos)

        for target_pos in neighbor_cells(grid, current_pos, closedlist, robot):

            if target_pos.y == robot.dst.y and target_pos.x == robot.dst.x:
                end = Node(*target_pos)
                end.parent = current_pos
                return reconstruct_path(end)

            new_g_cost = current_pos.g_cost + (0.5 if target_pos.y == current_pos.y and target_pos.x == current_pos.x else 1)

            if is_in_list(openlist, target_pos):
                node = find_node(target_pos, openlist)
                if new_g_cost >= node.g_cost:
                    continue
            else:
                node = Node(*target_pos)
                openlist.append(node)
                node.h_cost = calc_heuristic(node, robot.dst)

            node.g_cost = new_g_cost
            node.score = node.g_cost + node.h_cost
            node.parent = current_pos

    return []


# MAIN
if __name__ == '__main__':
    robots = []
    bots = []

    # Fixed start and goal positions (non-random)
    startNodes = [ [10, 0], [20, 0], [30, 0], [40, 0], [10, 16], [20, 16], [30, 16], [40, 16] ]
    goalNodes  = [ [10, 16], [20, 16], [30, 16], [40, 16], [10, 0], [20, 0], [30, 0], [40, 0] ]

    for i in range(len(startNodes)):
        start = Node(startNodes[i][0], startNodes[i][1])
        goal = Node(goalNodes[i][0], goalNodes[i][1])
        bot = Robot(f'R{i}', start, goal)
        bot.path = [start]  # Initialize path with start
        bots.append(bot)

    for robot in bots:
        print(f'Computing {robot.name} ...')
        path = search(grid, robot)
        for point in path:
            robot.path.append(point)
        robots.append(robot)

    visualize(grid, robots)
    outlinePath(grid, robots)
