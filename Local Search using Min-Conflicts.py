# Category 7: Constraint Satisfaction Problem
# Problem 3: Local Search using Min-Conflicts

import random

map_graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

colors = ["Red", "Green", "Blue", "Yellow"]


def count_conflicts(region, color, assignment):

    conflicts = 0

    for neighbour in map_graph[region]:

        if assignment[neighbour] == color:
            conflicts += 1

    return conflicts


def find_conflicting_regions(assignment):

    conflicts = []

    for region in map_graph:

        if count_conflicts(
            region,
            assignment[region],
            assignment
        ) > 0:

            conflicts.append(region)

    return conflicts


def min_conflicts(max_steps=100):

    assignment = {}

    for region in map_graph:
        assignment[region] = random.choice(colors)

    print("\nInitial Assignment:")

    for region, color in assignment.items():
        print(region, "->", color)

    for step in range(max_steps):

        conflicting_regions = find_conflicting_regions(
            assignment
        )

        if not conflicting_regions:
            print("\nSolution found in", step, "steps.")
            return assignment

        region = random.choice(conflicting_regions)

        best_colors = []
        minimum_conflicts = float("inf")

        for color in colors:

            conflicts = count_conflicts(
                region,
                color,
                assignment
            )

            if conflicts < minimum_conflicts:
                minimum_conflicts = conflicts
                best_colors = [color]

            elif conflicts == minimum_conflicts:
                best_colors.append(color)

        selected_color = random.choice(best_colors)

        assignment[region] = selected_color

        print(
            "Step", step + 1,
            ":", region,
            "->", selected_color
        )

    return None


print("================================")
print("      LOCAL SEARCH FOR CSP")
print("       MIN-CONFLICTS")
print("================================")

solution = min_conflicts()

if solution:

    print("\nFinal Solution:")

    for region, color in solution.items():
        print(region, "->", color)

else:
    print("\nNo solution found.")
