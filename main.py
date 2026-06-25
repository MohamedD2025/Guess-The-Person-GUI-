import turtle,pandas as pd,time

screen=turtle.Screen()
screen.title("Where Is The Person")
screen.bgpic("PEOPLE.gif")
screen.setup(width=1697,height=927)
screen.tracer(0)


data=pd.read_csv("coords.csv")
people=data.person.to_list()
guessed=set()
unguessed=set()

while len(guessed)<10:
    screen.update()
    answer=screen.textinput(title=f"You Guessed: {len(guessed)} / 10",prompt="Enter a Name of Person and Hit [Enter]: ").title().strip()

    if not answer:
        continue

    if answer in people:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        person_x=data[data.person==answer]["x"].item()
        person_y=data[data.person==answer]["y"].item()

        t.goto(x=person_x,y=person_y)
        t.pencolor("blue")
        t.write(answer,font=("Courier",12,"bold"))
        screen.update()
        guessed.add(answer)
        
        if len(guessed)==10:
            time.sleep(2)

    elif answer =="Exit":
        for person in people:
            if person not in guessed:
                unguessed.add(person)

        pd.DataFrame(unguessed).to_csv("wrong_answers.csv")
        break



