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
        
        raw_season.loc[row, 'Games'] += 1
        
        if win == 'W':
            raw_season.loc[row, 'Wins'] = raw_season.loc[row, 'Wins'] + 1
        else:
            raw_season.loc[row, 'Losses'] = raw_season.loc[row, 'Losses'] + 1 
            
        raw_season.loc[row, 'Points'] = raw_season.loc[row, 'Points'] + pts
        raw_season.loc[row, 'Points Allowed'] = raw_season.loc[row, 'Points Allowed'] + opts
        
        raw_season.loc[row, 'FGM'] = raw_season.loc[row, 'FGM'] + fgm
        raw_season.loc[row,'FGA'] = raw_season.loc[row,'FGA'] + fga
        
        raw_season.loc[row,'3PM'] = raw_season.loc[row,'3PM'] + p3m
        try:
            raw_season.loc[row,'3PA'] = raw_season.loc[row,'3PA'] + int(p3a)
        except:
            print('e')
        
        raw_season.loc[row,'FTA'] = raw_season.loc[row,'FTA'] + fta
        
        raw_season.loc[row,'ORB'] = raw_season.loc[row,'ORB'] + orb
        raw_season.loc[row,'DRB'] = raw_season.loc[row,'DRB'] + drb
        raw_season.loc[row,'TRB'] = raw_season.loc[row,'TRB'] + trb
        
        raw_season.loc[row,'TOV'] = raw_season.loc[row,'TOV'] + tov
        
        raw_season.loc[row,'oFGM'] = raw_season.loc[row,'oFGM'] + ofgm
        raw_season.loc[row,'oFGA'] = raw_season.loc[row,'oFGA'] + ofga
        raw_season.loc[row,'o3PM'] = raw_season.loc[row,'o3PM'] + op3m
        raw_season.loc[row,'o3PA'] = raw_season.loc[row,'o3PA'] + op3a
        raw_season.loc[row,'oFTA'] = raw_season.loc[row,'oFTA'] + ofta
        raw_season.loc[row,'oORB'] = raw_season.loc[row,'oORB'] + oorb
        raw_season.loc[row,'oDRB'] = raw_season.loc[row,'oDRB'] + odrb
        raw_season.loc[row,'oTRB'] = raw_season.loc[row,'oTRB'] + otrb
        raw_season.loc[row,'oTOV'] = raw_season.loc[row,'oTOV'] + otov
        
    print(raw_season)
    
def aggregateHomeAverages(df, raw_season):
    row = 0
    
    for i in df.index:
        team = df['Team'][i]
        if i == 0:
                raw_season = raw_season.append({'Team': team, 'Games': 0, 'Wins': 0, 'Losses': 0,
                                        'Points': 0, 'Points Allowed': 0, 'FGM': 0, 'FGA': 0,
                                        '3PM': 0, '3PA': 0, 'FTA': 0, 'ORB': 0, 'DRB': 0,
                                        'TRB': 0, 'TOV': 0, 'oFGM': 0, 'oFGA': 0, 'o3PM': 0,
                                        'o3PA': 0, 'oFTA': 0, 'oORB': 0, 'oDRB': 0, 'oTRB': 0, 'oTOV': 0}, ignore_index=True)
        location = df['Loc'][i]
        
        if raw_season.empty:
            pass
        elif team != raw_season.loc[row, 'Team']:
            row += 1
            raw_season = raw_season.append({'Team': team, 'Games': 0, 'Wins': 0, 'Losses': 0,
                                    'Points': 0, 'Points Allowed': 0, 'FGM': 0, 'FGA': 0,
                                    '3PM': 0, '3PA': 0, 'FTA': 0, 'ORB': 0, 'DRB': 0,
                                    'TRB': 0, 'TOV': 0, 'oFGM': 0, 'oFGA': 0, 'o3PM': 0,
                                    'o3PA': 0, 'oFTA': 0, 'oORB': 0, 'oDRB': 0, 'oTRB': 0, 'oTOV': 0}, ignore_index=True)
        
        if location == 'H':
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
            
            
            raw_season.loc[row, 'Games'] += 1
            
            if win == 'W':
                raw_season.loc[row, 'Wins'] = raw_season.loc[row, 'Wins'] + 1
            else:
                raw_season.loc[row, 'Losses'] = raw_season.loc[row, 'Losses'] + 1 
                
            raw_season.loc[row, 'Points'] = raw_season.loc[row, 'Points'] + pts
            raw_season.loc[row, 'Points Allowed'] = raw_season.loc[row, 'Points Allowed'] + opts
            
            raw_season.loc[row, 'FGM'] = raw_season.loc[row, 'FGM'] + fgm
            raw_season.loc[row,'FGA'] = raw_season.loc[row,'FGA'] + fga
            
            raw_season.loc[row,'3PM'] = raw_season.loc[row,'3PM'] + p3m
            try:
                raw_season.loc[row,'3PA'] = raw_season.loc[row,'3PA'] + int(p3a)
            except:
                print('e')
            
            raw_season.loc[row,'FTA'] = raw_season.loc[row,'FTA'] + fta
            
            raw_season.loc[row,'ORB'] = raw_season.loc[row,'ORB'] + orb
            raw_season.loc[row,'DRB'] = raw_season.loc[row,'DRB'] + drb
            raw_season.loc[row,'TRB'] = raw_season.loc[row,'TRB'] + trb
            
            raw_season.loc[row,'TOV'] = raw_season.loc[row,'TOV'] + tov
            
            raw_season.loc[row,'oFGM'] = raw_season.loc[row,'oFGM'] + ofgm
            raw_season.loc[row,'oFGA'] = raw_season.loc[row,'oFGA'] + ofga
            raw_season.loc[row,'o3PM'] = raw_season.loc[row,'o3PM'] + op3m
            raw_season.loc[row,'o3PA'] = raw_season.loc[row,'o3PA'] + op3a
            raw_season.loc[row,'oFTA'] = raw_season.loc[row,'oFTA'] + ofta
            raw_season.loc[row,'oORB'] = raw_season.loc[row,'oORB'] + oorb
            raw_season.loc[row,'oDRB'] = raw_season.loc[row,'oDRB'] + odrb
            raw_season.loc[row,'oTRB'] = raw_season.loc[row,'oTRB'] + otrb
            raw_season.loc[row,'oTOV'] = raw_season.loc[row,'oTOV'] + otov
        
    print(raw_season)
    
def aggregateAwayAverages(df, raw_season):
    row = 0
    
    for i in df.index:
        team = df['Team'][i]
        if i == 0:
                raw_season = raw_season.append({'Team': team, 'Games': 0, 'Wins': 0, 'Losses': 0,
                                        'Points': 0, 'Points Allowed': 0, 'FGM': 0, 'FGA': 0,
                                        '3PM': 0, '3PA': 0, 'FTA': 0, 'ORB': 0, 'DRB': 0,
                                        'TRB': 0, 'TOV': 0, 'oFGM': 0, 'oFGA': 0, 'o3PM': 0,
                                        'o3PA': 0, 'oFTA': 0, 'oORB': 0, 'oDRB': 0, 'oTRB': 0, 'oTOV': 0}, ignore_index=True)
        location = df['Loc'][i]
        
        if raw_season.empty:
            pass
        elif team != raw_season.loc[row, 'Team']:
            row += 1
            raw_season = raw_season.append({'Team': team, 'Games': 0, 'Wins': 0, 'Losses': 0,
                                    'Points': 0, 'Points Allowed': 0, 'FGM': 0, 'FGA': 0,
                                    '3PM': 0, '3PA': 0, 'FTA': 0, 'ORB': 0, 'DRB': 0,
                                    'TRB': 0, 'TOV': 0, 'oFGM': 0, 'oFGA': 0, 'o3PM': 0,
                                    'o3PA': 0, 'oFTA': 0, 'oORB': 0, 'oDRB': 0, 'oTRB': 0, 'oTOV': 0}, ignore_index=True)
        
        if location == 'A':
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
            
            
            raw_season.loc[row, 'Games'] += 1
            
            if win == 'W':
                raw_season.loc[row, 'Wins'] = raw_season.loc[row, 'Wins'] + 1
            else:
                raw_season.loc[row, 'Losses'] = raw_season.loc[row, 'Losses'] + 1 
                
            raw_season.loc[row, 'Points'] = raw_season.loc[row, 'Points'] + pts
            raw_season.loc[row, 'Points Allowed'] = raw_season.loc[row, 'Points Allowed'] + opts
            
            raw_season.loc[row, 'FGM'] = raw_season.loc[row, 'FGM'] + fgm
            raw_season.loc[row,'FGA'] = raw_season.loc[row,'FGA'] + fga
            
            raw_season.loc[row,'3PM'] = raw_season.loc[row,'3PM'] + p3m
            try:
                raw_season.loc[row,'3PA'] = raw_season.loc[row,'3PA'] + int(p3a)
            except:
                print('e')
            
            raw_season.loc[row,'FTA'] = raw_season.loc[row,'FTA'] + fta
            
            raw_season.loc[row,'ORB'] = raw_season.loc[row,'ORB'] + orb
            raw_season.loc[row,'DRB'] = raw_season.loc[row,'DRB'] + drb
            raw_season.loc[row,'TRB'] = raw_season.loc[row,'TRB'] + trb
            
            raw_season.loc[row,'TOV'] = raw_season.loc[row,'TOV'] + tov
            
            raw_season.loc[row,'oFGM'] = raw_season.loc[row,'oFGM'] + ofgm
            raw_season.loc[row,'oFGA'] = raw_season.loc[row,'oFGA'] + ofga
            raw_season.loc[row,'o3PM'] = raw_season.loc[row,'o3PM'] + op3m
            raw_season.loc[row,'o3PA'] = raw_season.loc[row,'o3PA'] + op3a
            raw_season.loc[row,'oFTA'] = raw_season.loc[row,'oFTA'] + ofta
            raw_season.loc[row,'oORB'] = raw_season.loc[row,'oORB'] + oorb
            raw_season.loc[row,'oDRB'] = raw_season.loc[row,'oDRB'] + odrb
            raw_season.loc[row,'oTRB'] = raw_season.loc[row,'oTRB'] + otrb
            raw_season.loc[row,'oTOV'] = raw_season.loc[row,'oTOV'] + otov
        
    print(raw_season)
            
        


def main():
    df = pd.read_csv("E:\\Sports-Betting-Models\\Data\\NBA\\NBA Game Log by Team - Raw Log.csv")
    colum_names = ['Team', 'Games', 'Wins', 'Losses', 'Points', 'Points Allowed', 'FGM', 'FGA', '3PM', '3PA', 'FTA', 'ORB', 'DRB', 'TRB', 'TOV', 'oFGM', 'oFGA', 'o3PM', 'o3PA', 'oFTA', 'oORB', 'oDRB', 'oTRB', 'oTOV']
    
    raw_season = pd.DataFrame(columns = colum_names)
    home_season = pd.DataFrame(columns = colum_names)
    away_season = pd.DataFrame(columns = colum_names)
    
    aggregateAverages(df, raw_season)
    aggregateHomeAverages(df, home_season)
    aggregateAwayAverages(df, away_season)
    
    
if __name__ == "__main__":
    main()
        
    
