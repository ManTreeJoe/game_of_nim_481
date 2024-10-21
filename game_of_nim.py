from games import *

class GameOfNim(Game):

    def __init__(self, board=[3, 1]): #Initialize the game with the given board position.
        self.initial = GameState(
            to_move=0,  # Start with player 0 (MAX)
            utility=0,  # Utility is 0 at the start of the game
            board=board,  # Initial board configuration
            moves=self.make_moves(board)  # Generate valid moves based on the board
        )
        self.player = 0  # Start with player 0 (MAX)

    def make_moves(self, board): #Make valid moves logic
        moves = []
        for r, objects in enumerate(board):
            for n in range(1, objects + 1):
                moves.append((r, n))
        return moves

    def actions(self, state):
        return state.moves

    def result(self, state, move):
        r, n = move
        new_board = state.board[:]
        new_board[r] -= n
        new_state = GameState(
            to_move=1 - state.to_move,  # Switch turns
            utility=0,  # The utility will still be 0 unless it's a terminal state
            board=new_board,
            moves=self.make_moves(new_board)  # Generate new moves for the updated board
        )
        return new_state

    def utility(self, state, player): #Return the value to player 1 for win -1 for loss 0 otherwise.
        if self.terminal_test(state):
            return -1 if state.to_move == player else 1
        return 0

    def terminal_test(self, state): #If no objects are left the state is terminal
        return all(objects == 0 for objects in state.board)

    def display(self, state):
        board = state.board
        print("board: ", board)


if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1])  # Creating the game instance
    print(nim.initial.board)  # Output: [0, 5, 3, 1]
    print(nim.actions(nim.initial))  # Output: [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)]
    print(nim.result(nim.initial, (1, 3)))  # Apply a move (1, 3)

    # Play the game
    utility = nim.play_game(alpha_beta_player, query_player)  # Computer moves first
    if utility < 0:
        print("MIN won the game")
    else:
        print("MAX won the game")
