# list, list, int, int, int, matrix
def waterJugSolver(jug1, jug2, aim, amt1, amt2, visited):
    # Check if the desired amount of water has been reached
    # This is the base case of the recursion
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print(f"({amt1}, {amt2})")
        return True
    # Check if the current state has already been visited
    # This is to avoid infinite recursion and improve efficiency
    if visited[amt1][amt2] == False:
        # Mark the current state as visited
        # This is to avoid visiting the same state again
        visited[amt1][amt2] = True
        print(f"({amt1}, {amt2})")
        # Try all possible moves
        # This is to explore all possible ways to reach the desired amount of water
        return (waterJugSolver(jug1, jug2, aim, 0, amt2, visited) or  # Empty jug1
                waterJugSolver(jug1, jug2, aim, amt1, 0, visited) or  # Empty jug2
                waterJugSolver(jug1, jug2, aim, jug1, amt2, visited) or  # Fill jug1
                waterJugSolver(jug1, jug2, aim, amt1, jug2, visited) or  # Fill jug2
                waterJugSolver(jug1, jug2, aim,
                               amt1 + min(amt2, (jug1 - amt1)),
                               amt2 - min(amt2, (jug1 - amt1)), visited) or  # Pour from jug2 to jug1
                waterJugSolver(jug1, jug2, aim,
                               amt1 - min(amt1, (jug2 - amt2)),
                               amt2 + min(amt1, (jug2 - amt2)), visited))  # Pour from jug1 to jug2
    else:
        return False


# Take user input for the capacities of the two jugs
jug1 = int(input("Enter the capacity of jug 1: "))
jug2 = int(input("Enter the capacity of jug 2: "))

aim = 2  # Desired amount of water
visited = [[False for i in range(10000)] for j in range(10000)]  # Matrix to keep track of visited states
print(waterJugSolver(jug1, jug2, aim, 0, 0, visited))  # Call the function with initial amounts of water set to 0
#  time & space complexity O(jug1 * jug2) to explore and store all possible states (jug1 + 1) * (jug2 + 1).
