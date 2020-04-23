# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
data = pd.read_csv(path)

data = data.rename(columns={'Total':'Total_Medals'})

print(data.head())
#Code starts here



# --------------
#Code starts here





data["Better_Event"] = np.where(data["Total_Summer"]>data["Total_Winter"], "Summer", "Winter")

data["Better_Event"] = np.where(data["Total_Summer"]==data["Total_Winter"], "Both", data["Better_Event"])

better_event = data["Better_Event"].value_counts().reset_index().iloc[0,0]

print(better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

last_row = top_countries.shape[0]
top_countries = top_countries.drop(last_row-1, axis=0)

def top_ten(variable1, variable2):
    country_list = []
    temp = list(variable1.nlargest(10, variable2)["Country_Name"])
    country_list.extend(temp)
    return country_list 

top_10_summer = top_ten(top_countries,"Total_Summer")
top_10_winter = top_ten(top_countries, "Total_Winter")
top_10 = top_ten(top_countries, "Total_Medals")

common = list(set(top_10) & set(top_10_summer) & set(top_10_winter))


# --------------
#Code starts here

winter_df = data[data["Country_Name"].isin(top_10_winter)]
summer_df = data[data["Country_Name"].isin(top_10_summer)]
top_df = data[data['Country_Name'].isin(top_10)]

summer_df.plot(kind="bar", x="Country_Name", y="Total_Summer")
winter_df.plot(kind="bar", x="Country_Name", y="Total_Winter")


# --------------
#Code starts here

summer_df["Golden_Ratio"] = summer_df["Gold_Summer"] / summer_df["Total_Summer"]

summer_country_gold_index = summer_df["Golden_Ratio"].idxmax()
summer_country_gold = summer_df["Country_Name"][summer_country_gold_index]
summer_max_ratio = summer_df["Golden_Ratio"].max()

print(summer_country_gold, summer_max_ratio)

winter_df["Golden_Ratio"] = winter_df["Gold_Winter"] / winter_df["Total_Winter"]
winter_country_gold_index = winter_df["Golden_Ratio"].idxmax()
winter_country_gold = winter_df["Country_Name"][winter_country_gold_index]
winter_max_ratio = winter_df["Golden_Ratio"].max()

print(winter_country_gold, winter_max_ratio)


top_df["Golden_Ratio"] = top_df["Gold_Total"] / top_df["Total_Medals"]
top_country_gold_index = top_df["Golden_Ratio"].idxmax()
top_country_gold = top_df["Country_Name"][top_country_gold_index]
top_max_ratio = top_df["Golden_Ratio"].max()

print(winter_country_gold, winter_max_ratio)




# --------------
#Code starts here

data_1 = data.drop(data.shape[0]-1, axis=0)

data_1["Total_Points"] = 3*data_1["Gold_Total"] + 2*data_1["Silver_Total"] + 1*data_1["Bronze_Total"]

most_points = data_1["Total_Points"].max()
best_country_index = data_1["Total_Points"].idxmax()
best_country = data_1.iloc[best_country_index]["Country_Name"]


# --------------
#Code starts here

best = data[data["Country_Name"] == best_country]

best = best.loc[:, ["Gold_Total", "Silver_Total", "Bronze_Total"]]

best.plot.bar(stacked=True)

plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation=45)
plt.show()


