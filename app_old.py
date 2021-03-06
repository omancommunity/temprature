from typing import List, Any, Union

import pandas as pd
import numpy as np
import re

COLUMNS = [
    "date_full_with_time",
    "temp_dry_in_c"
]

# import csv file
df = pd.read_csv('salalah.csv',
                 usecols=COLUMNS)

# print(df)


# get higher and minimum value based on csv (dataframe) max & min
# keep in mind this solution is not ok especially as
# data here taken 24 time per day please keep reading down
print('maxmium temp: {}'.format(df['temp_dry_in_c'].max()))
print('minimum temp: {}'.format(df['temp_dry_in_c'].min()))

# split (ready csv file) into seprate files every file for one year in out folder
# 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12
# YEAR_ = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
# another solution is by year as data appear to be started from 01/01/2011 to 01/01/2015
# another important thing that every temp. taking 24 time per day
# it is important here to take sum of 24 reading thin divided by 24 to get
# the accurate reading in day except in 01/01/2015 it token once only
# use simple loop here is taking much time please use function within pandas
YEAR_ = [
    # year 1
    '01/01/2011',
    '31/12/2011',
    # year 2
    '01/01/2012',
    '31/12/2012',
    # year 3
    '01/01/2013',
    '31/12/2013',
    # year 4
    '01/01/2014',
    '31/12/2014',
    # year 5 will not be added in this example
    '01/01/2015']
__YEAR_ = [
    # year 1
    '2011',
    # year 2
    '2012',
    # year 3
    '2013',
    # year 4
    '2014',
    # year 5 will not be added in this example
    '2015']

# for col in df.date_full_with_time:

# year one all date with 2011
year_one = df[df['date_full_with_time'].str.contains(__YEAR_[0])]

# year one all date with 2012
year_two = df[df['date_full_with_time'].str.contains(__YEAR_[1])]

# year one all date with 2013
year_three = df[df['date_full_with_time'].str.contains(__YEAR_[2])]

# year one all date with 2014
year_four = df[df['date_full_with_time'].str.contains(__YEAR_[3])]


# export data to new csv for each year
year_one.to_csv('out/year_one_.csv' , index=0)
year_two.to_csv('out/year_two_.csv')
year_three.to_csv('out/year_three_.csv')
year_four.to_csv('out/year_four_.csv')



# year one high/low temprature
print('maxmium temp in year one: {}'.format(year_one['temp_dry_in_c'].max()))
print('minimum temp in year one: {}'.format(year_one['temp_dry_in_c'].min()))


# year two high/low temprature
print('maxmium temp in year two: {}'.format(year_two['temp_dry_in_c'].max()))
print('minimum temp in year two: {}'.format(year_two['temp_dry_in_c'].min()))

# year three high/low temprature
print('maxmium temp in year three: {}'.format(year_three['temp_dry_in_c'].max()))
print('minimum temp in year three: {}'.format(year_three['temp_dry_in_c'].min()))

# year four high/low temprature
print('maxmium temp in year four: {}'.format(year_four['temp_dry_in_c'].max()))
print('minimum temp in year four: {}'.format(year_four['temp_dry_in_c'].min()))



total_high_temp  = ((year_one['temp_dry_in_c'].max() + year_two['temp_dry_in_c'].max() + year_three['temp_dry_in_c'].max() + year_four['temp_dry_in_c'].max()) / 4)
total_low_temp  = ((year_one['temp_dry_in_c'].min() + year_two['temp_dry_in_c'].min() + year_three['temp_dry_in_c'].min() + year_four['temp_dry_in_c'].min()) / 4)
# year all year high/low temprature

print('\n\n\n\n Please check result above if you \n '
      'just grab max and min temp directly without \n '
      'divide data directly above first two result ..\n')

print('maxmium temp in all four year: {}'.format(total_high_temp))
print('minimum temp in all four year: {}'.format(total_low_temp))



# after split years now take reading of 24 time per day and then rewrite the sum result again

# here you will jump every 24 row for learn only
# splii =  year_one_.iloc[::24, :]


# STILL  NOT FINISH 



