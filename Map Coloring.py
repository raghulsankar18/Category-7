# Category 7: Constraint Satisfaction Problem
# Problem 1: Map Coloring

map_graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

colors = ["Red", "Green", "Blue", "Yellow"]


def is_safe(region, color, assignment):
    for neighbour in map_graph[region]:
        if neighbour in assignment:
            if assignment[neighbour] == color:
                return False
    return True


def solve_map_coloring(assignment):

    if len(assignment) == len(map_graph):
        return True

    for region in map_graph:

        if region not in assignment:

            for color in colors:

                if is_safe(region, color, assignment):

                    assignment[region] = color

                    print("Assigned", color, "to", region)

                    if solve_map_coloring(assignment):
                        return True

                    print("Backtracking from", region)
                    del assignment[region]

            return False

    return False


print("================================")
print("       MAP COLORING")
print("================================")

assignment = {}

if solve_map_coloring(assignment):

    print("\nFinal Solution:")

    for region, color in assignment.items():
        print(region, "->", color)

else:
    print("No solution exists.")
