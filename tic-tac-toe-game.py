from tkinter import *
import random


def next_turn(row, col):
    global player

    if game_btns[row][col]['text'] == "" and check_winner() is False:
        game_btns[row][col]['text'] = player

        if check_winner() is False:
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + " turn"))
        elif check_winner() == "tie":
            label.config(text="Tie, No Winner!")
        else:
            label.config(text=(player + " wins!"))


def check_winner():
    # Check rows for a winner
    for row in range(3):
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] != "":
            highlight_winning_cells(row, 0, row, 1, row, 2)
            return game_btns[row][0]['text']

    # Check columns for a winner
    for col in range(3):
        if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] != "":
            highlight_winning_cells(0, col, 1, col, 2, col)
            return game_btns[0][col]['text']

    # Check diagonals for a winner
    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != "":
        highlight_winning_cells(0, 0, 1, 1, 2, 2)
        return game_btns[0][0]['text']
    elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != "":
        highlight_winning_cells(0, 2, 1, 1, 2, 0)
        return game_btns[0][2]['text']

    # Check for a tie
    if not check_empty_spaces():
        return "tie"
    else:
        return False


def highlight_winning_cells(r1, c1, r2, c2, r3, c3):
    game_btns[r1][c1].config(bg="green")
    game_btns[r2][c2].config(bg="green")
    game_btns[r3][c3].config(bg="green")


def check_empty_spaces():
    for row in range(3):
        for col in range(3):
            if game_btns[row][col]['text'] == "":
                return True
    return False


def start_new_game():
    global player

    player = random.choice(players)
    label.config(text=(player + " turn"))

    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text="", bg="SystemButtonFace")


# Initialize the main window
window = Tk()
window.title("Tic Tac Toe Game")

players = ["x", "o"]
player = random.choice(players)

game_btns = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

label = Label(text=(player + " turn"), font=("Arial", 40))
label.pack(side="top")

restart_btn = Button(text="Restart", font=("Arial", 20), command=start_new_game)
restart_btn.pack(side="top")

btns_frame = Frame(window)
btns_frame.pack()

for row in range(3):
    for col in range(3):
        game_btns[row][col] = Button(btns_frame, text="", font=("Arial", 50), width=4, height=1,
                                     command=lambda row=row, col=col: next_turn(row, col))
        game_btns[row][col].grid(row=row, column=col)

window.mainloop()