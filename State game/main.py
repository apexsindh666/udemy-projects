
import pandas
# with open("weather_data.csv") as datafile:
#     data=csv.reader(datafile)
#     temperature=[]
#     for i in data:
#         s=(i[1])
#         if s!="temp":
#             temperature.append(s)
#     print(temperature)
#
# d=pandas.read_csv("weather_data.csv")
# print(d["temp"].max())
# dic=d.to_dict()
# print(dic)

data=pandas.read_csv("sqdata.csv")
gray=len(data[data["Primary Fur Color"]=="Gray"])
red=len(data[data["Primary Fur Color"]=="Cinnamon"])
black=len(data[data["Primary Fur Color"]=="Black"])
d_dic={
    "Fur color":["gray","red","black"],
    "count":[gray,red,black]
}
df=pandas.DataFrame(d_dic)
print(df.to_csv("sq_count.csv"))
