import csv
import matplotlib.pyplot as plt
import numpy as np

filename = "IHME_USA_LIFE_EXPECTANCY_1985_2010.csv"

dict_category = {}
def get_data(state, county):
    with open('Life/IHME_USA_LIFE_EXPECTANCY_1985_2010.csv', newline = '') as csvfile:
        d_reader= csv.DictReader(csvfile)
        dict_category['Year'] = []
        dict_category['Female life expectancy (national, years)'] = []
        dict_category['Female life expectancy (state, years)'] = []
        dict_category['Female life expectancy (years)'] = []
        dict_category['Male life expectancy (years)'] = []
        dict_category['Male life expectancy (national, years)'] = []
        dict_category['Male life expectancy (state, years)'] = []
        for row in d_reader:
            if row['State'] == state and row['County'] == county:
                dict_category['Year'].append(row['Year'])
                dict_category['Female life expectancy (years)'].append(row['Female life expectancy (years)'])
                dict_category['Female life expectancy (national, years)'].append(row['Female life expectancy (national, years)'])
                dict_category['Female life expectancy (state, years)'].append(row['Female life expectancy (state, years)'])
                dict_category['Male life expectancy (national, years)'].append(row['Male life expectancy (national, years)'])
                dict_category['Male life expectancy (years)'].append(row['Male life expectancy (years)'])
                dict_category['Male life expectancy (state, years)'].append(row['Male life expectancy (state, years)'])
    return dict_category


def worst_county(year):
    # return (state, county)
    with open('Life/IHME_USA_LIFE_EXPECTANCY_1985_2010.csv', newline = '') as csvfile:
        reader= csv.DictReader(csvfile)
        # establishing the categories and dictionary and basis
        for row in reader:
            if int(row['Year']) == year:
                dict_category = row
                break
        # then you parse through that specific year
        for row in reader:
            if int(row['Year']) == year:
                if (float(row['Female life expectancy (years)']) + float(row['Male life expectancy (years)']))/2 < (float(dict_category['Female life expectancy (years)']) + float(dict_category['Male life expectancy (years)']))/2:
                    dict_category = row
        # ok so now i'm assuming you need to get the values of all those FUCKING data for the specific female/male life expectancies ew.
        with open('Life/IHME_USA_LIFE_EXPECTANCY_1985_2010.csv', newline = '') as csvfile:
            d_reader= csv.DictReader(csvfile)
            dict_category['Year'] = []
            dict_category['Female life expectancy (years)'] = []
            dict_category['Male life expectancy (years)'] = []
            for row in d_reader:
                if row['State'] == dict_category['State'] and row['County'] == dict_category['County']:
                    dict_category['Year'].append(row['Year'])
                    dict_category['Female life expectancy (years)'].append(row['Female life expectancy (years)'])
                    dict_category['Male life expectancy (years)'].append(row['Male life expectancy (years)'])
    return (dict_category['State'], dict_category['County'])

def plotdata(state, county):
    """
    PNG Files
    Legend per six data types w/ separate color for gender & separate symbol for county/state/national
    x-axis: years
    y-axis: life expectancy
    title: xxx <COUNTY> county, yyy <STATE>: life expectancy
    """
    values = get_data(state, county)
    x = np.arange(1985, 2011)
    plt.plot(x, values['Female life expectancy (years)'], 'r', label = 'Female life expectancy')
    plt.plot(x, values['Female life expectancy (national, years)'], 'b', label = 'National Female life expectancy')
    plt.plot(x, values['Female life expectancy (state, years)'], 'g', label = 'State Female life expectancy')
    plt.plot(x, values['Male life expectancy (years)'], 'y', label = 'Male life expectancy')
    plt.plot(x, values['Male life expectancy (national, years)'], 'c', label = 'National Male life expectancy')
    plt.plot(x, values['Male life expectancy (state, years)'], 'm', label = 'State Male life expectancy')
    title = county + ' , ' + state + ': life expectancy'
    plt.title(title)
    plt.ylabel('life expectancy')
    plt.xlabel('years')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad = 0.)
    pngtitle = state + "_" + county +".png"
    plt.savefig(pngtitle)
    plt.show()
    pass

if __name__ == "__main__":
    state, county = worst_county(1985)
    plotdata(state, county)