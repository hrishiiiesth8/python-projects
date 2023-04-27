import turtle
import pandas as pd

ALIGNMENT = "center"
FONT = ("Arial", 8, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("states.csv")
list_of_states = data["state"].tolist()
guessed_till_now = []

while len(guessed_till_now) < 50:
    answer = screen.textinput(title=f"{len(guessed_till_now)}/50 guessed correctly.", prompt="What's another state "
                                                                                             "name? ").title()

    if answer == "Exit":
        missing_ones = [states for states in list_of_states if states not in guessed_till_now]
        dictionary = {
                    "Not Guessed": missing_ones
                }
        nd = pd.DataFrame(dictionary)
        nd.to_csv("remind_these_next_time.csv")
        break

    if answer in list_of_states:
        guessed_till_now.append(answer)
        state_row = data[data["state"] == answer]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_row.x), int(state_row.y))
        t.write(answer, align=ALIGNMENT, font=FONT)
