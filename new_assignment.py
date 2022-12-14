import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def urban_data():
    urban_data = pd.read_csv("urban_electric.csv",skiprows=4)
    return urban_data;

def rural_data():
    rural_data = pd.read_csv("rural_electric.csv",skiprows=4)
    return rural_data;

def cleanfuel_rural():
    cleanfuel_rural_data = pd.read_csv("clean_fuel_rural.csv",skiprows=4)
    return cleanfuel_rural_data;

def cleanfuel_urban():
    fuel_urban_data = pd.read_csv("cleanfuel_urban.csv",skiprows=4)
    return fuel_urban_data;

def renewable_consumption():
    renewable_energy = pd.read_csv("renewable_consumption.csv",skiprows=4)
    return renewable_energy;

def climate_change():
    climate_change_data = pd.read_csv("climate_change.csv",skiprows=4)
    return climate_change_data;    

# Side to side bar plot
plt.figure(figsize=(10,4))
urban_values = urban_data()
val = urban_values.transpose()
sorted_data = urban_values.iloc[1:7]
countries = sorted_data["Country Name"]
sorted_year = sorted_data.iloc[:,59]
rural_values = rural_data()
rural_value_sorted = rural_values.iloc[1:7]
rural_year_value = rural_value_sorted.iloc[:,59]
x = np.arange(len(countries))
plt.bar(x-0.15, sorted_year, width = 0.3, label = "Urban")
plt.bar(x+0.15, rural_year_value,  width = 0.3, label = "Rural")
plt.xticks(x,countries,rotation = 70, horizontalalignment = "center", fontsize = 18)
plt.yticks(fontsize = 18)
plt.title("Access to Electricity Urban/Rural \n (% of Urban/Rural population)", fontsize = 18)
plt.xlabel("Countries", fontsize = 18)
plt.ylabel("% of population", fontsize = 18)
plt.legend()
plt.savefig("bar_plot_two.png",bbox_inches='tight')
plt.show()

# Line plot
plt.figure(figsize=(10,4))
cleanfuel_rural_data = cleanfuel_rural()
cleanfuel_transposed_rural = cleanfuel_rural_data.transpose()
cleanfuel_sorted_rural = cleanfuel_rural_data.iloc[1:7]
cleanfuel_countries = cleanfuel_sorted_rural["Country Name"]
cleanfuel_sorted_year = cleanfuel_sorted_rural.iloc[:,59]
fuel_urban = cleanfuel_urban()
fuel_urban_transposed = fuel_urban.transpose()
fuel_urban_sorted = fuel_urban.iloc[1:7]
fuel_urban_countries = fuel_urban_sorted["Country Name"]
fuel_urban_year = fuel_urban_sorted.iloc[:,59]
plt.plot(fuel_urban_countries, fuel_urban_year, label = "Urban", marker = 'o')
plt.plot(cleanfuel_countries, cleanfuel_sorted_year, label = "Rural", marker = 'o')
plt.xticks(rotation = 70, horizontalalignment = "center", fontsize = 18)
plt.yticks(fontsize = 18)
plt.title("Access to clean fuels and technologies for cooking, Urban/Rural \n (% of Urban/Rural population)", fontsize = 18)
plt.xlabel("Countries", fontsize = 18)
plt.ylabel("% of rural population", fontsize = 18)
plt.legend()
plt.savefig("line_plot_two.png", bbox_inches='tight')
plt.show()

# single bar plot - Renewable Energy consumption for Afghanistan
renewable_data = renewable_consumption()
years = ['2009','2010','2011','2012','2013','2014']
values = renewable_data[['Country Name','2009','2010','2011','2012','2013','2014']]
values_sorted = values.iloc[2]
values_sorted_year = values_sorted[1:]
df = pd.DataFrame({'Year': years, 'Renewable Energy Consumption':[values_sorted_year[0],
                                            values_sorted_year[1],
                                            values_sorted_year[2],
                                            values_sorted_year[3],
                                            values_sorted_year[4],
                                            values_sorted_year[5]]})
print(df)
renewable_mean = df.mean()
print(renewable_mean)
ren_describe = df.describe()
print(ren_describe)
ax = df.plot.bar(x = 'Year',
                 y = 'Renewable Energy Consumption',
                 title = 'Renewable Energy Consumption of Afghanistan during 2009-2014 \n (% of total final energy consumption)',
                 color = [(250/255,188/255,42/255)],
                 rot = 0)
ax.set_ylabel("Energy Consumption")


# Heatmap for Australia
plt.figure(figsize=(12,8))
climate_data = climate_change()
data_sorted = climate_data.loc[(climate_data["Country Name"] == "Australia") | 
                               (climate_data["Country Name"] == "Albania")]
print(data_sorted)
data_sorted_new = data_sorted.loc[(data_sorted["Indicator Name"] == "Population, total") |
                                  (data_sorted["Indicator Name"] == "CO2 emissions (kt)") |
                                  (data_sorted["Indicator Name"] == "Energy use (kg of oil equivalent per capita)") |
                                  (data_sorted["Indicator Name"] == "Total greenhouse gas emissions (kt of CO2 equivalent)")]
print(data_sorted_new)
data_final = data_sorted_new[['Country Name','Indicator Name','2004','2005','2006',
                              '2007','2008','2009','2010','2011','2012','2013','2014']]
print(data_final)
data_sortedby_country = data_final.loc[data_final["Country Name"] == "Australia"]
data_final_transpose = data_sortedby_country.transpose()
print(data_final_transpose.iloc[1:,1:])
aus_data = data_final_transpose.iloc[1:]
print(x)
aus_data_to_csv = aus_data.to_csv('australia.csv')
aus_data_read = pd.read_csv("australia.csv",skiprows=1)
aus_data_final = aus_data_read[['Population, total','CO2 emissions (kt)',
       'Energy use (kg of oil equivalent per capita)',
       'Total greenhouse gas emissions (kt of CO2 equivalent)']]
sns.set(font_scale=2.5)
sns.heatmap(data = aus_data_final.corr(), annot = True, cmap = 'mako', center = 0)
plt.title("Australia")
plt.savefig("heatmap1.png", bbox_inches='tight')
plt.show()

# Heatmap for Albania
plt.figure(figsize=(12,8))
albania_data = data_final.loc[data_final["Country Name"] == "Albania"]
albania_data_transpose = albania_data.transpose()
alb_data = albania_data_transpose.iloc[1:]
print(alb_data)
alb_data_to_csv = alb_data.to_csv('albania.csv')
alb_data_read = pd.read_csv("albania.csv",skiprows = 1)
alb_data_read_sorted = alb_data_read[['Population, total','CO2 emissions (kt)',
       'Energy use (kg of oil equivalent per capita)',
       'Total greenhouse gas emissions (kt of CO2 equivalent)']]
sns.heatmap(data = alb_data_read_sorted.corr(), annot = True, cmap = 'rocket', center = 0)
plt.title("Albania")
plt.savefig("heatmap2.png", bbox_inches='tight')
plt.show()












