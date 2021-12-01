from main import EightPuzzle
import cProfile
import pstats

board = [[8, 7, 4],
         [1, 6, 0],
         [3, 2, 5]]

board2 = [[1, 2, 3],
          [4, 0, 6],
          [7, 5, 8]]

board3 = [[0, 8, 7],
          [6, 5, 4],
          [3, 2, 1]]

board4 = [[8, 4, 5],
          [6, 7, 2],
          [0, 1, 3]]

board5 = [[8, 6, 7],
          [2, 5, 4],
          [3, 0, 1]]

board6 = [[6, 5, 7],
          [8, 5, 0],
          [3, 2, 1]]

board7 = [[1, 2, 3],
          [4, 5, 0],
          [7, 8, 6]]

board8 = [[1, 2, 3],
          [4, 0, 5],
          [7, 8, 6]]

board9 = [[1, 4, 7],
          [2, 5, 8],
          [3, 6, 0]]

board10 = [[3, 6, 0],
           [2, 5, 8],
           [1, 4, 7]]

eight_puzzle_ideal = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 0]]

fifteen_puzzle_idea = [[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12],
                       [13, 14, 15, 0]]

fifteen_puzzle_board = [[12, 13, 4, 14],
                        [0, 11, 1, 6],
                        [10, 9, 8, 3],
                        [5, 7, 15, 2]]

puzzle24 = [[5, 10, 15, 20, 24],
            [4, 12, 7, 8, 9],
            [3, 13, 14, 19, 23],
            [2, 0, 17, 18, 22],
            [1, 6, 11, 16, 21]]

ideal24 = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 0]]


def main():
    with cProfile.Profile() as pr:
        new_puzzle = EightPuzzle(puzzle24, ideal24)
        new_puzzle.best_first_search()

        for move in new_puzzle.give_path():
            print(*move, sep="\n")
            print("=" * 20)

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.dump_stats(filename="needs_profiling.prof")


if __name__ == "__main__":
    main()
