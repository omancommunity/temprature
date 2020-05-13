import pandas as pd
import numpy as np
import re
import datetime

# we are interested only in two col date/time and temperature
# there are two type of parsing date  date_parser/parser_date
COLUMNS = [
    "date_full_with_time",
    "temp_dry_in_c"
]

# make sure to - parse date - formate so you can search and modify later
# for example date_parser / dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
# parser_date = ['date_full_with_time']
# https://stackoverflow.com/questions/17465045/can-pandas-automatically-recognize-dates/17468012
# The pandas.datetime class is now deprecated.
# Import from datetime instead (GH30610)
# https://pandas.pydata.org/docs/whatsnew/v1.0.0.html
# so we will Import from datetime instead


dateparse = lambda x: datetime.datetime.strptime(x, '%d/%m/%Y %H:%M')
# 01/01/2011 1:00
# make sure date time format as csv file %d/%m/%Y %H:%M as our example
df = pd.read_csv('salalah.csv',
                 usecols=COLUMNS,
                 parse_dates=['date_full_with_time'],
                 date_parser=dateparse)

# Down was easy to calculate but there were missing data in csv between 2013/2014/2012

# df = df.set_index(['date_full_with_time'])
# df_2011 = df.loc['01/01/2011 1:00':'31/12/2011 0:00']
# period = len(df_2011.loc['01/01/2011 1:00':'01/01/2011 23:00'])
# df['date_full_with_time'] = pd.date_range('01/01/2011 1:00', periods=period, freq='H')
# df = df.set_index(['date_full_with_time'])
# print(df.loc['01/01/2011 1:00':'31/12/2011 0:00'])


# 2012 data


df = df.set_index(['date_full_with_time'])
df_2011 = df.loc['01/01/2011 1:00':'31/12/2011 0:00']
df_2012 = df.loc['01/01/2012 1:00':'31/12/2012 0:00']
df_2013 = df.loc['01/01/2013 1:00':'31/12/2013 0:00']
df_2014 = df.loc['01/01/2014 1:00':'31/12/2014 0:00']

"""
2011
"""
# keep in mind high/low higher
# temperature and low temperature and not median
print(
    '2011 High temp :{0} and 2011 Low temp :{1}'.format(
        df_2011['temp_dry_in_c'].max(),
        df_2011['temp_dry_in_c'].min())
)
# median
print('2011 Median temp :{0}'.format(
    df_2011['temp_dry_in_c'].median())
)

"""
2012
"""
# keep in mind high/low higher
# temperature and low temperature and not median
print(
    '2012 High temp :{0} and 2012 Low temp :{1}'.format(
        df_2012['temp_dry_in_c'].max(),
        df_2012['temp_dry_in_c'].min())
)
# median
print('2012 Median temp :{0}'.format(
    df_2012['temp_dry_in_c'].median())
)

"""
2013
"""
# keep in mind high/low higher
# temperature and low temperature and not median
print(
    '2013 High temp :{0} and 2013 Low temp :{1}'.format(
        df_2013['temp_dry_in_c'].max(),
        df_2013['temp_dry_in_c'].min())
)
# median
print('2013 Median temp :{0}'.format(
    df_2013['temp_dry_in_c'].median())
)

"""
2014
"""
# keep in mind high/low higher
# temperature and low temperature and not median
print(
    '2014 High temp :{0} and 2014 Low temp :{1}'.format(
        df_2014['temp_dry_in_c'].max(),
        df_2014['temp_dry_in_c'].min())
)
# median
print('2014 Median temp :{0}'.format(
    df_2014['temp_dry_in_c'].median())
)

# Temperature for 4 years max/min
print('{0} the median (normal) Temperature'
      ' for 4 year \nand max :{1},'
      ' \nand min: {2}'
      .format(((df_2011['temp_dry_in_c'].median()+
                df_2012['temp_dry_in_c'].median()+
                df_2013['temp_dry_in_c'].median()+
                df_2014['temp_dry_in_c'].median())/4),
              (
                      (df_2011['temp_dry_in_c'].max() +
                       df_2012['temp_dry_in_c'].max() +
                       df_2013['temp_dry_in_c'].max() +
                       df_2014['temp_dry_in_c'].max()) / 4),
              (
                            (df_2011['temp_dry_in_c'].min() +
                             df_2012['temp_dry_in_c'].min() +
                             df_2013['temp_dry_in_c'].min() +
                             df_2014['temp_dry_in_c'].min()) / 4)
              )
      )

# you can also use np.median(YOUR CALCULATION) FOR SIMPLICITY
