# Category 7: Constraint Satisfaction Problem
# Problem 2: Crypt-Arithmetic
def is_valid_assignment(assignment):

    if assignment["S"] == 0 or assignment["M"] == 0:
        return False

    send = (
        assignment["S"] * 1000 +
        assignment["E"] * 100 +
        assignment["N"] * 10 +
        assignment["D"]
    )

    more = (
        assignment["M"] * 1000 +
        assignment["O"] * 100 +
        assignment["R"] * 10 +
        assignment["E"]
    )

    money = (
        assignment["M"] * 10000 +
        assignment["O"] * 1000 +
        assignment["N"] * 100 +
        assignment["E"] * 10 +
        assignment["Y"]
    )

    return send + more == money


def solve_cryptarithm():

    letters = ["S", "E", "N", "D", "M", "O", "R", "Y"]

    assignment = {}
    used_digits = set()

    def assign_letter(index):

        if index == len(letters):
            return is_valid_assignment(assignment)

        letter = letters[index]

        for digit in range(10):

            if digit in used_digits:
                continue

            if letter in ["S", "M"] and digit == 0:
                continue

            assignment[letter] = digit
            used_digits.add(digit)

            if assign_letter(index + 1):
                return True

            del assignment[letter]
            used_digits.remove(digit)

        return False

    if assign_letter(0):
        return assignment

    return None


print("================================")
print("     CRYPT-ARITHMETIC")
print("================================")

solution = solve_cryptarithm()

if solution:

    print("\nSolution:")

    for letter in sorted(solution):
        print(letter, "=", solution[letter])

    send = (
        solution["S"] * 1000 +
        solution["E"] * 100 +
        solution["N"] * 10 +
        solution["D"]
    )

    more = (
        solution["M"] * 1000 +
        solution["O"] * 100 +
        solution["R"] * 10 +
        solution["E"]
    )

    money = (
        solution["M"] * 10000 +
        solution["O"] * 1000 +
        solution["N"] * 100 +
        solution["E"] * 10 +
        solution["Y"]
    )

    print("\nEquation:")
    print(" ", send)
    print("+", more)
    print("------")
    print(money)

else:
    print("No solution exists.")
