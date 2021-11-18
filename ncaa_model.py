# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 14:24:49 2021

@author: Matthew Connealy
"""

import pandas as pd

# total_stats = pd.read_csv("C:\\Users\\mattc\\Sports Betting\\Data\\NBA\\2020 NBA total stats.txt")

ncaa_school_stats = pd.read_csv("E:\\Sports-Betting-Models\\Data\\NBA\\2020-21 ncaa basketball school stats.txt")

select_data = ncaa_school_stats[['School', 'Tm', 'Opp', 'FGA', 'FTA', 'ORB', 'TOV']]
select_data.loc['avg'] = select_data.mean()


select_data['pos'] = select_data.apply(lambda row: row.FGA - row.ORB + row.TOV + row.FTA * 0.475, axis=1) # 0.4 for NBA
select_data['OE'] = select_data.apply(lambda row: (row.Tm / row.pos) * 100, axis=1) # offensive efficiency
select_data['DE'] = select_data.apply(lambda row: (row.Opp / row.pos) * 100, axis=1) # defensive effenciency

print(select_data['OE'].mean())
print(select_data['DE'].mean())


# ivy league did not play, drop them from analysis
select_data = select_data.dropna()

select_data.loc['avg', 'OE'] = select_data['OE'].mean()