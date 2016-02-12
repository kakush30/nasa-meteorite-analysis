import numpy as np
import pandas
from ggplot1 import *

def no_of_recordings_gouped_by_reclass(filename):
    
    df = pandas.read_csv(filename)
    # NO. of Recording by RecClass
    # Changed to small letters, as there same classes described in capital and small letter
    pivot = pandas.tools.pivot.pivot_table(df,values = 'id', columns = df['recclass'].str.lower() ,aggfunc='count')
    return pivot
    

def max_min(filename):
    df = pandas.read_csv(filename)
    # Those which are greater than 0 g
    df = df[df['mass (g)'] > 0]   
    max_value = df['mass (g)'].max()     
    min_value = df['mass (g)'].min()
    avg_value = df['mass (g)'].mean()
    return max_value,min_value,avg_value


    
def year_range(filename):
    
    df = pandas.read_csv(filename)
    # Extracting year from DateTime
    df['year'] = (pandas.to_datetime(df['year'], coerce=True))
    df['year'] = df['year'].dt.year
    
    # Removing year 2101, as it is impossibe that this year exist presently 
    df = df[df['year']<2017]
    pivot = pandas.tools.pivot.pivot_table(df,values = 'id', columns = pandas.cut(df['year'], np.arange(1687, 2013+10, 10)) ,aggfunc='count')
    
    #Ascending.
    pivot_ascending = pivot.order(ascending=True)
    
    #Descending
    pivot_decending = pivot.order(ascending=False)
    
    # Plotting Data for last 100 years
    pivot_plot1 = pivot[23:33]
    plot = ggplot(pivot_plot1,aes(x = pivot_plot1.index, y = pivot_plot1.values)) +\
           geom_bar(stat='identity') +\
           ggtitle('Years') + xlab('Years') + ylab('No. of Meteorite strike') + \
           theme(axis_text_x  = element_text(angle = 45, hjust = 1))

    return pivot,pivot_ascending,pivot_decending,plot
    
    

    
if __name__ == '__main__':
    
    print no_of_recordings_gouped_by_reclass('Meteorite_Landings.csv')
    print max_min('Meteorite_Landings.csv')   
    print year_range('Meteorite_Landings.csv')   