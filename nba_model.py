# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 12:19:26 2021

@author: mattc
"""

import pandas as pd

def aggregateAverages(df, raw_season):
    row = 0
    
    for i in df.index:
        team = df['Team'][i]
        
        
        if raw_season.empty:
            pass
        elif team != raw_season.loc[row, 'Team']:
            row += 1
            raw_season = raw_season.append({'Team': team, 'Games': 0, 'Wins': 0, 'Losses': 0,
                                    'Points': 0, 'Points Allowed': 0, 'FGM': 0, 'FGA': 0,
                                    '3PM': 0, '3PA': 0, 'FTA': 0, 'ORB': 0, 'DRB': 0,
                                    'TRB': 0, 'TOV': 0, 'oFGM': 0, 'oFGA': 0, 'o3PM': 0,
                                    'o3PA': 0, 'oFTA': 0, 'oORB': 0, 'oDRB': 0, 'oTRB': 0, 'oTOV': 0}, ignore_index=True)
        
        
        location = df['Loc'][i]
        win = df['Result'][i]
        
        pts = df['Points'][i]
        opts = df['O Points'][i]
        
        fgm = df['FGM'][i]
        fga = df['FGA'][i]
        
        p3m = df['3PM'][i]
        p3a = df['3PA'][i]
        if p3a == '':
            p3a = 0
        
        fta = df['FTA'][i]
        
        orb = df['ORB'][i]
        trb = df['TRB'][i]
        drb = trb - orb
        
        tov = df['TOV'][i]
        
        ofgm = df['oFGM'][i]
        ofga = df['oFGA'][i]
        
        op3m = df['o3PM'][i]
        op3a = df['o3PA'][i]
        
        ofta = df['FTA'][i]
        
        oorb = df['oORB'][i]
        otrb = df['oTRB'][i]
        odrb = otrb - oorb
        
        otov = df['oTOV'][i]
        
        if i == 0:
            raw_season = raw_season.append({'Team': team, 'Games': 0, 'Wins': 0, 'Losses': 0,
                                    'Points': 0, 'Points Allowed': 0, 'FGM': 0, 'FGA': 0,
                                    '3PM': 0, '3PA': 0, 'FTA': 0, 'ORB': 0, 'DRB': 0,
                                    'TRB': 0, 'TOV': 0, 'oFGM': 0, 'oFGA': 0, 'o3PM': 0,
                                    'o3PA': 0, 'oFTA': 0, 'oORB': 0, 'oDRB': 0, 'oTRB': 0, 'oTOV': 0}, ignore_index=True)
        
        #findTeam(row, raw_season, team)
        
        
        # row = findTeam(raw_season, team)
        
        #print(raw_season.loc[row, 'Games'])
        
        # raw_season['Team'] = team
        raw_season.loc[row, 'Games'] += 1
        
        if win == 'W':
            raw_season['Wins'] = raw_season['Wins'] + 1
        else:
            raw_season['Losses'] = raw_season['Losses'] + 1 
            
        raw_season['Points'] = raw_season['Points'] + pts
        raw_season['Points Allowed'] = raw_season['Points Allowed'] + opts
        
        raw_season['FGM'] = raw_season['FGM'] + fgm
        raw_season['FGA'] = raw_season['FGA'] + fga
        
        raw_season['3PM'] = raw_season['3PM'] + p3m
        try:
            raw_season['3PA'] = raw_season['3PA'] + int(p3a)
        except:
            print('e')
        
        raw_season['FTA'] = raw_season['FTA'] + fta
        
        raw_season['ORB'] = raw_season['ORB'] + orb
        raw_season['DRB'] = raw_season['DRB'] + drb
        raw_season['TRB'] = raw_season['TRB'] + trb
        
        raw_season['TOV'] = raw_season['TOV'] + tov
        
        raw_season['oFGM'] = raw_season['oFGM'] + ofgm
        raw_season['oFGA'] = raw_season['oFGA'] + ofga
        raw_season['o3PM'] = raw_season['o3PM'] + op3m
        raw_season['o3PA'] = raw_season['o3PA'] + op3a
        raw_season['oFTA'] = raw_season['oFTA'] + ofta
        raw_season['oORB'] = raw_season['oORB'] + oorb
        raw_season['oDRB'] = raw_season['oDRB'] + odrb
        raw_season['oTRB'] = raw_season['oTRB'] + otrb
        raw_season['oTOV'] = raw_season['oTOV'] + otov
        
    print(raw_season)
            

'''        
def findTeam(row, raw_season, team):
    if team != raw_season.loc[row, 'Team']: 
        raw_season = raw_season.append({'Team': team, 'Games': 0, 'Wins': 0, 'Losses': 0,
                                    'Points': 0, 'Points Allowed': 0, 'FGM': 0, 'FGA': 0,
                                    '3PM': 0, '3PA': 0, 'FTA': 0, 'ORB': 0, 'DRB': 0,
                                    'TRB': 0, 'TOV': 0, 'oFGM': 0, 'oFGA': 0, 'o3PM': 0,
                                    'o3PA': 0, 'oFTA': 0, 'oORB': 0, 'oDRB': 0, 'oTRB': 0, 'oTOV': 0}, ignore_index=True)
        return row_num + 1
    else:
        return row_num
'''


def main():
    df = pd.read_csv("E:\\Sports-Betting-Models\\Data\\NBA\\NBA Game Log by Team - Raw Log.csv")
    colum_names = ['Team', 'Games', 'Wins', 'Losses', 'Points', 'Points Allowed', 'FGM', 'FGA', '3PM', '3PA', 'FTA', 'ORB', 'DRB', 'TRB', 'TOV', 'oFGM', 'oFGA', 'o3PM', 'o3PA', 'oFTA', 'oORB', 'oDRB', 'oTRB', 'oTOV']
    
    raw_season = pd.DataFrame(columns = colum_names)
    aggregateAverages(df, raw_season)
    
    
if __name__ == "__main__":
    main()
        
    
