import time


def state_to_tuple(state):
    return tuple(map(int, state))


def tuple_to_state(matrix):
    return list(matrix)


def get_moves(state):
    index = state.index(0)
    row, col = divmod(index, 3)
    moves = []

    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    for move, (dr, dc) in directions.items():
        nr, nc = row + dr, col + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_state = list(state)
            new_index = nr * 3 + nc
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            moves.append((move, tuple(new_state)))

    return moves


def dfs(start_state, goal_state):
    stack = [(start_state, [])]
    visited = set()
    nodes_visited = 0

    while stack:
        state, path = stack.pop()
        nodes_visited += 1

        if state == goal_state:
            return path, nodes_visited

        if state in visited:
            continue

        visited.add(state)

        for move, next_state in get_moves(state):
            stack.append((next_state, path + [move]))

    return None, nodes_visited


def main():
    start_state = input("Enter start State: ")
    goal_state = input("Enter goal State: ")

    start_tuple = state_to_tuple(start_state)
    goal_tuple = state_to_tuple(goal_state)

    print("-----------------")
    print("DFS Algorithm")
    print("-----------------")

    start_time = time.time()
    solution_path, nodes_visited = dfs(start_tuple, goal_tuple)
    end_time = time.time()

    if solution_path:
        print("Time taken:", end_time - start_time, "seconds")
        print("Path Cost:", len(solution_path))
        print("No of Nodes Visited:", nodes_visited)

        current_state = start_tuple
        for move in solution_path:
            for m, new_state in get_moves(current_state):
                if m == move:
                    current_state = new_state
                    break
            for i in range(0, 9, 3):
                print(' '.join(map(str, current_state[i:i + 3])))
            print("------")
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
