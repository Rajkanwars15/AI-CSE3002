def is_valid_assignment(region, color, assignment, graph):
    # Check if the assigned color is valid for the given region
    for neighbor in graph[region]:
        # Loop through neighboring regions
        if neighbor in assignment and assignment[neighbor] == color:
            # If a neighboring region has the same color, return False
            return False
    return True

def map_coloring(graph, colors, assignment={}):
    # if all regions have been assigned colors, return the assignment
    if len(assignment) == len(graph):
        return assignment

    # Select an unassigned region from the graph
    region = next(iter([r for r in graph if r not in assignment]))

    # Try each available color for the selected region
    for color in colors:
        # Check if the current color is valid for the selected region
        if is_valid_assignment(region, color, assignment, graph):
            # If the color is valid, assign it to the region and recursively call the function
            assignment[region] = color
            result = map_coloring(graph, colors, assignment)
            if result is not None:
                # If a valid assignment is found in the recursion, return it
                return result
            # If the assignment was not successful, backtrack by removing the color from the current region
            assignment.pop(region, None)

    # If no valid assignment is found, return None
    return None

if __name__ == "__main__":
    # Example usage
    # Define the map as a graph with regions (nodes) as keys and their neighboring regions (nodes) as values
    map_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'E', 'F'],
        'D': ['B', 'C', 'F'],
        'E': ['C', 'F'],
        'F': ['C', 'D', 'E']
    }

    # Define available colors
    colors = ['Red', 'Green', 'Blue']

    # Solve the map coloring problem
    result = map_coloring(map_graph, colors)

    if result is not None:
        print("Map coloring solution:")
        for region, color in result.items():
            print(f"{region}: {color}")
    else:
        print("No solution found.")
