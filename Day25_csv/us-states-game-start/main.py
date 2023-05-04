import turtle
import pandas as pd
screen=turtle.Screen()
screen.title("US States")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states=pd.read_csv("50_states.csv")
state=states.state.to_list()
guessed_state=[]
while(len(guessed_state)<50):
    answer=screen.textinput(f"{len(guessed_state)}/50 Correct","Whats another state?")
    if answer == "exit":
        missing_states=[]
        for states in state:
            if states not in guessed_state:
                missing_states.append(states)
        break
    if answer in state:
        guessed_state.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        location = states[states.state == answer]
        t.goto(int(location.x),int(location.y))
        t.write(answer)

missing_states= pd.DataFrame(missing_states)
missing_states.to_csv("StatesToLearn.csv")

screen.exitonclick()