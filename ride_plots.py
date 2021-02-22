import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_day(row):
    return int(row.split(' ')[0].split('-')[2])

def get_plot(df):
    df['DAY'] = df['CREATED'].apply(lambda row: get_day(row))
    df.sort_values('DAY', inplace=True)
    return df['DAY'].value_counts().sort_index(axis=0)

def get_ride_plot(year):
    dfA = pd.read_csv(f'RidesWithTripClassA{year}.csv')
    dfB = pd.read_csv(f'RidesWithTripClassB{year}.csv')
    dfC = pd.read_csv(f'RidesWithTripClassC{year}.csv')

    tripA = 'Trip starts and ends on campus'
    tripB = 'Trip starts on campus and ends off campus'
    tripC = 'Trip starts off campus and ends on campus'
    dict = {tripA: get_plot(dfA), tripB: get_plot(dfB), tripC: get_plot(dfC)}
    data = pd.DataFrame(dict)
    ax = data.plot(kind='bar', stacked=True, rot=0, figsize=(8,5))
    dir = 'upper right' if year == 2020 else 'upper left'
    ax.legend(loc=dir)
    plt.xlabel(f'Day of October {year}')
    plt.ylabel('Number of Rides')
    plt.title('Number of Rides per Trip Class')
    sns.despine()
    plt.tight_layout()
    plt.show()

get_ride_plot(2019)