import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("India States Game")
image = "india_map.gif"
screen.addshape(image)
turtle.shape(image)

#def mouse_click_coords(x ,y):
#   print(x, y)
#turtle.onscreenclick(mouse_click_coords)

data = pd.read_csv("india_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 38:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/37 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.pensize(10)
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

#turtle.mainloop()