import turtle
import pandas
screen=turtle.Screen()
screen.title("US States game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed=[]
while len(guessed)<50:
    answer_state=screen.textinput(title=f"{len(guessed)}/50 States Correct",prompt="what's another states name ?").title()
    print(answer_state)
    if answer_state=="Exit":
        missing_states=[]
        for i in all_states:
            if i not in guessed:
                missing_states.append(i)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("missing_state.csv")
        break
    if answer_state in all_states:
        guessed.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)

screen.exitonclick()



