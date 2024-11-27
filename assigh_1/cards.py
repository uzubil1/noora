class Card:
    pass
    def __init__(a_card, rank, suit):
        a_card.rank = rank
        a_card.suit = suit

class Flippable:
    def __init__(a_card, flipped, card):
        a_card.flipped = flipped
        a_card.card = card

class Board:
    def __init__(a_card, rows, cols):
        a_card.board = [[Flippable(False, Card(1, "GCIS")) for _ in range(cols)] for _ in range(rows)]

    def print_board(a_card):
        for row in a_card.board:
            for flippable in row:
                print(f"Card: {flippable.card.rank} of {flippable.card.suit}, Flipped: {flippable.flipped}")

# Create a 3x3 board
board = Board(3, 3)

# Change the rank of the card at row 2, column 1
board.board[2][1].card.rank = 12

# Print the updated board
board.print_board()
