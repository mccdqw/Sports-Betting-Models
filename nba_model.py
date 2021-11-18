# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 12:19:26 2021

@author: mattc
"""

import pandas as pd

# total_stats = pd.read_csv("C:\\Users\\mattc\\Sports Betting\\Data\\NBA\\2020 NBA total stats.txt")

ncaa_school_stats = pd.read_csv("C:\\Users\\mattc\\Sports Betting\\Data\\NBA\\2020-21 ncaa basketball school stats.txt")
# ncaa_school_stats.drop(columns=['Rk', 'G', 'W', 'L', 'W-L%', 'SRS', 'SOS', 'Unnamed: 8', 'W.1'
                                #, 'L.1', 'Unnamed: 11', ])
select_data = ncaa_school_stats[['Tm.', 'Opp.', 'FGA', 'FTA', 'ORB', 'TOV']]
select_data.loc['avg'] = select_data.mean()
