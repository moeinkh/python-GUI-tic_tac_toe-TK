from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('بازی دوز') 

# func for show board game
def game():
    global buttons

    # for players name
    header_frame = Frame(root)
    header_frame.grid(row=0)
    name_label_1 = Label(header_frame, text='بازیکن 1', font=('vazir', 12, 'bold'), padx=5)
    name_label_2 = Label(header_frame, text='بازیکن 2', font=('vazir', 12, 'bold'), padx=5)
    name_label_1.grid(row=0, column=0)
    name_label_2.grid(row=0, column=1)

    # to record points
    points_frame = Frame(root)
    points_frame.grid(row=1)
    points_label_1 = Label(points_frame, text=f'{point_player[0]}', font=('vazir', 12, 'bold'), padx=35)
    points_label_2 = Label(points_frame, text=f'{point_player[1]}', font=('vazir', 12, 'bold'), padx=35)
    points_label_1.grid(row=0, column=0)
    points_label_2.grid(row=0, column=1)

    # board game
    game_frame = Frame(root)
    game_frame.grid(row=2)
    buttons = []
    counter = 0
    for row in range(1, 4):
        for column in range(1, 4):
            index = counter
            buttons.append(index)
            buttons[index] = Button(game_frame, width=15, height=7, command=lambda x=f'{index}':press_button(x))
            buttons[index].grid(row=row, column=column)
            counter += 1

# global var for functions
global turn, buttons, point_list, point_player

# func for reset game
def reset():
    global turn, point_list
    point_list = ['', '', '', '', '', '', '', '', '']
    turn = 'X'
    game()

# func for check draw
def check_draw():
    if '' not in point_list:
        messagebox.showinfo("پایان بازی", "بازی مساوی شد")
        reset()


# func to check winner
def check_winner():
    if point_list[0] == point_list[1] == point_list[2] and point_list[0]:
        show_winner(point_list[0])
    elif point_list[3] == point_list[4] == point_list[5] and point_list[3]:
        show_winner(point_list[3])
    elif point_list[6] == point_list[7] == point_list[8] and point_list[6]:
        show_winner(point_list[6])
    elif point_list[0] == point_list[3] == point_list[6] and point_list[0]:
        show_winner(point_list[0])
    elif point_list[1] == point_list[4] == point_list[7] and point_list[1]:
        show_winner(point_list[1])
    elif point_list[2] == point_list[5] == point_list[8] and point_list[2]:
        show_winner(point_list[2])
    elif point_list[0] == point_list[4] == point_list[8] and point_list[0]:
        show_winner(point_list[0])
    elif point_list[2] == point_list[4] == point_list[6] and point_list[2]:
        show_winner(point_list[2])
    else:
        check_draw()

point_player = [0, 0]
# func for show winner(who winner?)
def show_winner(winner):
    if winner == 'X':
        point_player[0] += 1
        messagebox.showinfo("پایان بازی", "بازیکن 1 برنده شد")
        reset()
    else:
        point_player[1] += 1
        messagebox.showinfo("پایان بازی", "بازیکن 2 برنده شد")
        reset()

turn = 'X'
point_list = ['', '', '', '', '', '', '', '', '']
# func to press button
def press_button(btn):
    global turn
    btn = int(btn)
    if point_list[btn] == '':
        if turn == 'X':
            buttons[btn]['bg'] = 'green'
            buttons[btn]['fg'] = 'white'
            buttons[btn]['text'] = 'X'
            point_list[btn] = turn
            turn = 'O'
        elif turn == 'O':
            buttons[btn]['bg'] = 'red'
            buttons[btn]['fg'] = 'white'
            buttons[btn]['text'] = 'O'
            point_list[btn] = turn
            turn = 'X'
    check_winner()     

# call game func for run game
game()

root.mainloop()