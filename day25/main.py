import pandas as pd
import turtle
'''
with open("weather_data.csv") as data_file:

    
    tenperature = []
    data = data_file.readlines()
    print(data)


df = pd.read_csv('weather_data.csv')
temp_list = df['temp'].to_list()

df['F'] = df.temp * 9/5 + 32

df['temp'].max() 
day = df[df.day =='Monday']
#print(df['temp'].max())
print(day)
# print(df)

df = pd.DataFrame(data_dic)


df = pd.read_csv('100days/bin/day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gre_s = len(df[df["Primary Fur Color"] == "Gray"])
red_s = len(df[df["Primary Fur Color"] == "Cinnamon"])
black_s = len(df[df["Primary Fur Color"] == "Black"])

print(gre_s)
print(red_s)
print(black_s)


data_dict = {
            "Fur Color": ["Gray", "Cinnamon", "Black"],
            "Count" : [gre_s, red_s, black_s]
}

df_data = pd.DataFrame(data_dict)
print(data_dict)

'''
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df_location = pd.read_csv('50_states.csv')
all_states = df_location.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answwer_state = screen.textinput(title=f"{len(guessed_states)} / 50 states correct", prompt="What's another state's name?")


def guess(state):
    
   if answwer_state is all_states:
      guessed_states.append(answwer_state)
      t = turtle.Turtle()
      t.hideturtle()
      t.penup()
      state_data = df_location[df_location.state == answwer_state]
      t.goto(state_data.x.items(), state_data.y.item())
      t.write(answwer_state)

guess(answwer_state)


screen.exitonclick()