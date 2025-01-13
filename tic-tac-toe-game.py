from tkinter import *
import random


def next_turn(row, col):
    global player
    if game_btns[row][col]['text'] == "" and check_winner() == False:
        if player == players[0]:
            game_btns[row][col]['text'] = player

            if check_winner() == False:
                player = players[1]
                label.config(text=(players[1] + " turn"))

            elif check_winner == True:
                label.config(text=(players[0] + " wins!"))

            elif check_winner == "tie":
                label.config(text="Tie, No Winner!")

        if player == players[1]:
            game_btns[row][col]['text'] = player

            if check_winner() == False:
                player = players[0]
                label.config(text=(players[0] + " turn"))

            elif check_winner == True:
                label.config(text=(players[1] + " wins!"))

            elif check_winner == "tie":
                label.config(text="Tie, No Winner!")


def check_winner():
    for row in range(3):
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text']:
            return True
        
    for col in range(3):
        if game_btns[col][0]['text'] == game_btns[col][1]['text'] == game_btns[col][2]['text']:
            return True
    
    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != "":
        return True
    elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != "":
        return True
    
    if check_empty_spaces() == False:
        for row in range(3):
            for col in range(3):
                game_btns[row][col].config(bg = 'red')
        return "tie"
    else:
        return False
    


def check_empty_spaces():
    ...

def start_new_game():
    ...

window = Tk()
window.title("Tic Tac Toe Game")

players = ["x", "o"]
player = random.choice(players)

game_btns = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

label = Label(text=(player + " turn"), font=("Arial", 40))
label.pack(side="top")

restart_btn = Button(text="Restart", font=("Arial", 20), command=start_new_game)
restart_btn.pack(side="top")

btns_frame = Frame(window)
btns_frame.pack()

for row in range(3):
    for col in range(3):
        game_btns[row][col] = Button(btns_frame, text="", font=("Arial", 50), width=4, height=1, command=lambda row=row, col=col: next_turn(row, col))
        game_btns[row][col].grid(row=row, column=col)

window.mainloop()
