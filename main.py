from queue import PriorityQueue as pqueue


class EightPuzzle:
    def __init__(self, board: list, goal_state: list[list]) -> None:
        self.board = board
        self.open_list: pqueue = pqueue()
        self.closed_list: list = []
        self._goal_state: list[list] = goal_state
        self._shape: tuple = (len(self.board), len(self.board[0]))
        self._moves: list[tuple] = []
        self.count = 0

    def get_heuristic(self, board_config: list) -> int:
        heuristic: int = 0

        for i in range(0, self._shape[0]):
            for j in range(0, self._shape[0]):
                if board_config[i][j] != self._goal_state[i][j]:
                    heuristic += 1
        return heuristic

    def get_exact_moves(self, position: tuple) -> list[tuple]:
        i, j = position
        total_moves: list[tuple] = [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]
        legal_moves: list[tuple] = []

        for move in total_moves:
            predicate1 = (move[0] > -1) and (move[0] < self._shape[0])
            predicate2 = (move[1] > -1) and (move[1] < self._shape[1])

            if predicate1 and predicate2:
                legal_moves.append(move)

        return legal_moves

    def get_position(self, board_config: list) -> tuple:
        for i in range(0, self._shape[0]):
            for j in range(0, self._shape[0]):
                if board_config[i][j] == 0:

                    return (i, j)

    def get_children(self, board_config: list) -> list:
        children: list = []
        children_heuristics: list = []
        position: tuple = self.get_position(board_config)
        swap_candidates: list = self.get_exact_moves(position)
        i, j = position

        for newi, newj in swap_candidates:
            copy_matrix = [row[:] for row in board_config]
            copy_matrix[i][j], copy_matrix[newi][newj] = copy_matrix[newi][newj], copy_matrix[i][j]
            children.append(copy_matrix)

        for child in children:
            children_heuristics.append(self.get_heuristic(child))

        return (children, children_heuristics)

    def give_path(self) -> list[list]:
        path: list[list] = []

        last_parent: list[list] = self._moves[-1][0]
        path.append(last_parent)

        for pair in reversed(self._moves):
            if last_parent in pair[1]:
                last_parent = pair[0]
                path.append(last_parent)

        return reversed(path)

    def best_first_search(self) -> None:
        initial_heuristic: int = self.get_heuristic(self.board)
        self.open_list.put((initial_heuristic, self.board))
        self._moves.append(([], self.board))

        while not self.open_list.empty():
            new_board: list[list] = self.open_list.get()[1]

            if new_board == self._goal_state:
                return

            children, children_heuristic = self.get_children(new_board)
            self._moves.append((new_board, children))

            for child, child_heuristic in list(zip(children, children_heuristic)):

                if child not in self.closed_list:
                    self.closed_list.append(child)
                    self.open_list.put((child_heuristic, child))
