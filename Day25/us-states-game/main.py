from turtle import Turtle, Screen
import pandas as pd


screen = Screen()
screen.title("U.S State Game")
image = "Day25/us-states-game/blank_states_img.gif"
screen.addshape(image)
t = Turtle()
t.shape(image)
data = pd.read_csv("Day25/us-states-game/50_states.csv")
answer = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states Correct",
                                    prompt="what's another state's name:").title()
    if answer_state == "Exit":
        missing_states = [state for state in answer if state not in guessed_states ]
        # missing_states = []
        # for state in answer:
        #   if state not in guessed_states:
        #     missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("Day25/us-states-game/states_to_learn.csv")
        break

    if answer_state in answer:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        place = data[data["state"] == answer_state]
        t.goto(place["x"].item(), place["y"].item())
        t.write(place["state"].item())
        