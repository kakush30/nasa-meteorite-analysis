# Nasa Meteorite Analysis

This analysis is based on NASA's Meteorite Dataset, which is downloaded from [here](https://data.nasa.gov/view/ak9y-cwf9). In this analysis is done on classes of Meteorite, weight of meteorites & analysis of how many events happened in 10 years period in past 200 years. 

#### Number of recordings grouped by recclass

As there are various classes reported in Datasets, that is same but reported in Capital letters & Small. For removing this ambiguity I changed all classes to small letters. This is the sample result.

![1st img](https://raw.githubusercontent.com/kakush30/nasa-meteorite-analysis/master/img/result_1.png)

#### Heaviest and Lightest Meteorite landing recorded

As there are some meteorites that are reported as 0 g, for analysis of heaviest and lightest meteorites I removed those datasets.
The results as following 
(60000000.0, 0.01, 13283.615209542177)

The heaviest Meteorite is of `60000000 g` and lightest as `0.01 `g, and the average is `13283.61 g`

#### Number of recordings per 10 year period

There is a recording of year 2101, which is not possible, so I removed that data from dataset for year based analysis.

In ascending order
` year
(1727, 1737]        0
(1687, 1697]        1
(1697, 1707]        1
(1757, 1767]        1
(1707, 1717]        2
(1717, 1727]        2
(1737, 1747]        2
(1747, 1757]        5
(1777, 1787]        6
(1767, 1777]        7
(1787, 1797]       10
(1797, 1807]       18
(1827, 1837]       27
(1807, 1817]       28
(1817, 1827]       32
(1837, 1847]       54
(1847, 1857]       65
(1857, 1867]       80
(1867, 1877]       94
(1877, 1887]      116
(1887, 1897]      125
(1897, 1907]      146
(1907, 1917]      149
(1917, 1927]      157
(1947, 1957]      221
(1937, 1947]      230
(1927, 1937]      263
(1957, 1967]      307
(1967, 1977]     1785
(2007, 2017]     4417
(1977, 1987]     7698
(1987, 1997]     9663
(1997, 2007]    19691`

For descending order
`year
(1997, 2007]    19691
(1987, 1997]     9663
(1977, 1987]     7698
(2007, 2017]     4417
(1967, 1977]     1785
(1957, 1967]      307
(1927, 1937]      263
(1937, 1947]      230
(1947, 1957]      221
(1917, 1927]      157
(1907, 1917]      149
(1897, 1907]      146
(1887, 1897]      125
(1877, 1887]      116
(1867, 1877]       94
(1857, 1867]       80
(1847, 1857]       65
(1837, 1847]       54
(1817, 1827]       32
(1807, 1817]       28
(1827, 1837]       27
(1797, 1807]       18
(1787, 1797]       10
(1767, 1777]        7
(1777, 1787]        6
(1747, 1757]        5
(1737, 1747]        2
(1717, 1727]        2
(1707, 1717]        2
(1757, 1767]        1
(1697, 1707]        1
(1687, 1697]        1
(1727, 1737]        0`

#### Analysis of past 100 years

![img2](https://raw.githubusercontent.com/kakush30/nasa-meteorite-analysis/master/img/100_years.png)

Yes the technologies advance, the number of events of meteorite strikes that reported increased with each passing year. 

#### Average mass of meteorites in recorded data

The average mass of meteorites is `13283.61 g`

#### Alternative ways to do Analysis

Beside from CSV analysis, the larger analysis can be done by importing JSON supplied data into MongoDB. MongoDB support various operations that cant be done by Pandas Library. 

Example of MongoDB driven Analysis:https://github.com/kakush30/Project-3-Data-Wrangling-with-MongoDB
