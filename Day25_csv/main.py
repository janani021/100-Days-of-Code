import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_s = len(data[data["Primary Fur Color"] == "Gray"])
red_s = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_s = len(data[data["Primary Fur Color"] == "Black"])
dict = {
    "Fur Colour " : ["Gray", "Cinnamon" , "Black"],
    "Count": [grey_s,red_s,black_s]
}
dict_df = pd.DataFrame(dict)
dict_df.to_csv("Count of squirrels.csv")
