import pandas as pd
import matplotlib.pyplot as plt


def main_data():
    ''' Reading data from the dataset '''
    
    # reading data from csv file using pandas
    # returing the data
    data_values = pd.read_csv("fsa_list.csv")
    return data_values;
    

def lineChartValues():
    ''' Extracting the data for line plot '''
    
    # calling the main function to get the dataset
    f = main_data()
    
    # extracting year from date
    f['year'] = pd.DatetimeIndex(f['PeriodEnd']).year
    
    # extracting food safety values and animal welfare values seperately and returning it
    food_safety = f.loc[f["Area"] == "food hygiene / safety"]
    animal_welfare = f.loc[(f["Area"] == "animal welfare") |
                           (f["Area"] == "animal welfare / cattle id / abp")]
    return food_safety,animal_welfare;


def groupBarChartValues():
    ''' setting the data for side by side bar chart '''
    
    # getting values from each column of the dataset
    x_years = food_safety_val["year"]
    y_values1 = food_safety_val["NumberOfCasesCommenced"]
    y_values2 = food_safety_val["NumberOfSuccessfulCases"]
    return x_years,y_values1,y_values2; 


def pieChartValues():
    ''' setting the values for pie chart '''
    
    # getting values from columns and returning it
    total_fines = food_safety_val["TotalFines"]
    years = food_safety_val["year"]
    return total_fines, years;


    

plt.figure()
# calling the line chart function to get the values 
food_safety_val, animal_val = lineChartValues()
# 1st argument is the x-axis which is year
# 2nd argument is the y-axis total cost
plt.plot(food_safety_val["year"], food_safety_val["TotalCosts"], marker = 'o', label = "Food Safety")
plt.plot(animal_val["year"], animal_val["TotalCosts"], marker = 'o', label = "Animal Welfare")
# general matters
plt.legend()
plt.title("Food Hygiene / Safety & Animal Welfare")
plt.xlabel("Year")
plt.ylabel("Total cost")
plt.savefig("line_plot.png")
plt.show()


plt.figure(figsize=(10,8))
# calling the bar plot function to get the values
x_years, y_values1, y_values2 = groupBarChartValues()
# 1st argument 0.2 offset to the left and right (first 10 years)
# 2nd argument is the height of bars of first 10 years
# width in units of the x-axis
plt.bar(x_years[:10]-0.2, y_values1[:10], width = 0.5, label = "No Of Cases")
plt.bar(x_years[:10]+0.2, y_values2[:10], width = 0.5, label = "No Of Successful Cases")
# general matters
plt.title("Food Hygiene / Safety Cases")
plt.xlabel("year")
plt.ylabel("No of cases")
plt.legend()
plt.savefig("bar_plot.png")
plt.show()

plt.figure()
# calling the pie chart function to get the values
total_fines, years = pieChartValues()
# values of latest 7 years from the dataset
# autopct for dispalying values in percentage
plt.pie(total_fines[10:], autopct='%.0f%%', labels = years[10:])
# general matters
plt.title("Food Hygiene / Safety Total Fines Imposed") 
plt.savefig("pie_plot.png") 
plt.show()

    