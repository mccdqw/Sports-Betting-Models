# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 12:19:26 2021

@author: mattc
"""

import pandas as pd

def aggregateTotals(df, raw_season):
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
        
        ofta = df['oFTA'][i]
        
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
        
    return raw_season
    
def aggregateHomeTotals(df, raw_season):
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
            
            ofta = df['oFTA'][i]
            
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
        
    return raw_season
    
def aggregateAwayTotals(df, raw_season):
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
            
            ofta = df['oFTA'][i]
            
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
        
    return raw_season

def aggregateTotalAverages(total_season, raw_avg_season):
    raw_avg_season['Team'] = total_season['Team'].copy()
    raw_avg_season['Games'] = total_season['Games'].copy()
    raw_avg_season['Wins'] = total_season['Wins'].copy()
    raw_avg_season['Losses'] = total_season['Losses'].copy()
    
    # get the averages for stats for all games
    for (columnName, columnData) in raw_avg_season.iteritems():
        if columnName == 'Team' or columnName == 'Games' or columnName == 'Wins' or columnName == 'Losses':
            pass
        else:
            raw_avg_season[columnName] = total_season[columnName] / total_season['Games']
            
    return raw_avg_season

def aggregateHomeAverages(total_home_season, raw_avg_home_season):
    raw_avg_home_season['Team'] = total_home_season['Team'].copy()
    raw_avg_home_season['Games'] = total_home_season['Games'].copy()
    raw_avg_home_season['Wins'] = total_home_season['Wins'].copy()
    raw_avg_home_season['Losses'] = total_home_season['Losses'].copy()
    
    # get the averages for stats for all home games
    for (columnName, columnData) in raw_avg_home_season.iteritems():
        if columnName == 'Team' or columnName == 'Games' or columnName == 'Wins' or columnName == 'Losses':
            pass
        else:
            raw_avg_home_season[columnName] = total_home_season[columnName] / total_home_season['Games']
            
    return raw_avg_home_season

def aggregateAwayAverages(total_away_season, raw_avg_away_season):
    raw_avg_away_season['Team'] = total_away_season['Team'].copy()
    raw_avg_away_season['Games'] = total_away_season['Games'].copy()
    raw_avg_away_season['Wins'] = total_away_season['Wins'].copy()
    raw_avg_away_season['Losses'] = total_away_season['Losses'].copy()
    
    # get the averages for stats for all away games
    for (columnName, columnData) in raw_avg_away_season.iteritems():
        if columnName == 'Team' or columnName == 'Games' or columnName == 'Wins' or columnName == 'Losses':
            pass
        else:
            raw_avg_away_season[columnName] = total_away_season[columnName] / total_away_season['Games']
            
    return raw_avg_away_season
        

def main():
    df = pd.read_csv("E:\\Sports-Betting-Models\\Data\\NBA\\NBA Game Log by Team - Raw Log.csv")
    colum_names = ['Team', 'Games', 'Wins', 'Losses', 'Points', 'Points Allowed', 'FGM', 'FGA', '3PM', '3PA', 'FTA', 'ORB', 'DRB', 'TRB', 'TOV', 'oFGM', 'oFGA', 'o3PM', 'o3PA', 'oFTA', 'oORB', 'oDRB', 'oTRB', 'oTOV']
    
    raw_season = pd.DataFrame(columns = colum_names)
    home_season = pd.DataFrame(columns = colum_names)
    away_season = pd.DataFrame(columns = colum_names)
    
    total_season = aggregateTotals(df, raw_season)
    ras = total_season
    
    total_home_season = aggregateHomeTotals(df, home_season)
    rahs = total_home_season
    
    total_away_season = aggregateAwayTotals(df, away_season)
    raas = total_away_season
    
    # get the averages for stats for all games
    for (columnName, columnData) in ras.iteritems():
        if columnName == 'Team' or columnName == 'Games' or columnName == 'Wins' or columnName == 'Losses':
            pass
        else:
            ras[columnName] = total_season[columnName] / total_season['Games']        
            
    
    # get the averages for stats for all games
    for (columnName, columnData) in rahs.iteritems():
        if columnName == 'Team' or columnName == 'Games' or columnName == 'Wins' or columnName == 'Losses':
            pass
        else:
            rahs[columnName] = total_home_season[columnName] / total_home_season['Games']
            
    # get the averages for stats for all games
    for (columnName, columnData) in raas.iteritems():
        if columnName == 'Team' or columnName == 'Games' or columnName == 'Wins' or columnName == 'Losses':
            pass
        else:
            raas[columnName] = total_away_season[columnName] / total_away_season['Games']
    
    #tempo calculations, possible start of new function
    ras['Tempo'] = ras['FGA'] - ras['ORB'] + ras['TOV'] + (ras['FTA'] * 0.4)
    ras['oTempo'] = ras['oFGA'] - ras['oORB'] + ras['oTOV'] + (ras['oFTA'] * 0.4)
    ras['Avg Tempo'] = (ras['Tempo'] + ras['oTempo']) / 2
    
    rahs['Tempo'] = rahs['FGA'] - rahs['ORB'] + rahs['TOV'] + (rahs['FTA'] * 0.4)
    rahs['oTempo'] = rahs['oFGA'] - rahs['oORB'] + rahs['oTOV'] + (rahs['oFTA'] * 0.4)
    rahs['Avg Tempo'] = (rahs['Tempo'] + rahs['oTempo']) / 2
    
    raas['Tempo'] = raas['FGA'] - raas['ORB'] + raas['TOV'] + (raas['FTA'] * 0.4)
    raas['oTempo'] = raas['oFGA'] - raas['oORB'] + raas['oTOV'] + (raas['oFTA'] * 0.4)
    raas['Avg Tempo'] = (raas['Tempo'] + raas['oTempo']) / 2
    
    #offensive efficiency calculations
    ras['OE'] = (ras['Points'] / ras['Tempo']) * 100
    rahs['OE'] = (rahs['Points'] / rahs['Tempo']) * 100
    raas['OE'] = (raas['Points'] / raas['Tempo']) * 100
    
    #defensive efficiency calculations
    ras['DE'] = (ras['Points Allowed'] / ras['oTempo']) * 100
    rahs['DE'] = (rahs['Points Allowed'] / rahs['oTempo']) * 100
    raas['DE'] = (ras['Points Allowed'] / raas['oTempo']) * 100
    
    # effective field goal percentage calculations
    # adds additional weight to 3-pointers made
    # multiply by 100 to get percentage value
    ras['EFG%'] = ((ras['FGM'] + 0.5 * ras['3PM']) / ras['FGA']) * 100
    rahs['EFG%'] = ((rahs['FGM'] + 0.5 * rahs['3PM']) / rahs['FGA']) * 100
    raas['EFG%'] = ((raas['FGM'] + 0.5 * raas['3PM']) / raas['FGA']) * 100
    
    # defensive effective field goal percentage
    ras['dEFG%'] = (ras['oFGM'] + 0.5 * ras['o3PM']) / ras['oFGA'] * 100
    rahs['dEFG%'] = (rahs['oFGM'] + 0.5 * rahs['o3PM']) / rahs['oFGA'] * 100
    raas['dEFG%'] = (raas['oFGM'] + 0.5 * raas['o3PM']) / raas['oFGA'] * 100
    
    # offensive rebound percentage
    # what percent of misses does a team rebound
    ras['ORB%'] = ras['ORB'] / (ras['ORB'] + ras['oDRB']) * 100
    rahs['ORB%'] = rahs['ORB'] / (rahs['ORB'] + rahs['oDRB']) * 100
    raas['ORB%'] = raas['ORB'] / (raas['ORB'] + raas['oDRB']) * 100
    
    # defensive rebound percentage
    # what percent of opponents misses were rebounded by team
    ras['DRB%'] = ras['DRB'] / (ras['DRB'] + ras['oORB']) * 100
    rahs['DRB%'] = rahs['DRB'] / (rahs['DRB'] + rahs['oORB']) * 100
    raas['DRB%'] = raas['DRB'] / (raas['DRB'] + raas['oORB']) * 100
    
    # total rebound percentage
    ras['TRB%'] = ras['TRB'] / (ras['TRB'] + ras['oTRB']) * 100
    rahs['TRB%'] = rahs['TRB'] / (rahs['TRB'] + rahs['oTRB']) * 100
    raas['TRB%'] = raas['TRB'] / (raas['TRB'] + raas['oTRB']) * 100
    
    # stat to show how well a team gets to the free throw line
    # FTA FGA ratio
    ras['FTA FGA R'] = ras['FTA'] / ras['FGA']
    rahs['FTA FGA R'] = rahs['FTA'] / rahs['FGA']
    raas['FTA FGA R'] = raas['FTA'] / raas['FGA']
    
    # opponent FTA FGA ratio
    ras['oFTA FGA R'] = ras['oFTA'] / ras['oFGA']
    rahs['oFTA FGA R'] = rahs['oFTA'] / rahs['oFGA']
    raas['oFTA FGA R'] = raas['oFTA'] / raas['oFGA']
    
    # turnover percentage
    ras['TOV%'] = ras['TOV'] / ras['Tempo'] * 100
    rahs['TOV%'] = rahs['TOV'] / rahs['Tempo'] * 100
    raas['TOV%'] = raas['TOV'] / raas['Tempo'] * 100
    
    # defensive turnover percentage
    ras['DTOV%'] = ras['oTOV'] / ras['oTempo'] * 100
    rahs['DTOV%'] = rahs['oTOV'] / rahs['oTempo'] * 100
    raas['DTOV%'] = raas['oTOV'] / raas['oTempo'] * 100
    
    #avg_list = ['Points', 'Points Allowed', 'FGM', 'FGA', '3PM', '3PA', 'FTA', 'ORB', 'DRB', 'TRB', 'TOV', 'oFGM', 'oFGA', 'o3PM', 'o3PA', 'oFTA', 'oORB', 'oDRB', 'oTRB', 'oTOV', 'Tempo', 'oTempo', 'Avg Tempo', 'OE', 'DE', 'EFG', 'dEFG', 'ORB%', 'DRB%', 'TRB%', 'FTA FGA R', 'oFTA FGA R', 'TOV%', 'DTOV%']
    
    ras = ras.append({'Team': 'League'}, ignore_index=True)
    rahs = rahs.append({'Team': 'League'}, ignore_index=True)
    raas = raas.append({'Team': 'League'}, ignore_index=True)
    
    for (columnName, columnData) in ras.iteritems():
        if columnName == 'Team':
            pass
        elif columnName == 'Games' or columnName == 'Wins' or columnName == 'Losses':
            ras.loc[30][columnName] = ras[columnName].sum()
        else:
            ras.loc[30][columnName] = ras[columnName].mean()
            
    for (columnName, columnData) in rahs.iteritems():
        if columnName == 'Team':
            pass
        elif columnName == 'Games' or columnName == 'Wins' or columnName == 'Losses':
            rahs.loc[30][columnName] = rahs[columnName].sum()
        else:
            rahs.loc[30][columnName] = rahs[columnName].mean()
            
    for (columnName, columnData) in raas.iteritems():
        if columnName == 'Team':
            pass
        elif columnName == 'Games' or columnName == 'Wins' or columnName == 'Losses':
            raas.loc[30][columnName] = raas[columnName].sum()
        else:
            raas.loc[30][columnName] = raas[columnName].mean()
    
    '''
    ras.append({'Team': 'League', 
                'Games': 0, 'Wins': 0, 'Losses': 0,
                                    'Points': 0, 'Points Allowed': 0, 'FGM': 0, 'FGA': 0,
                                    '3PM': 0, '3PA': 0, 'FTA': 0, 'ORB': 0, 'DRB': 0,
                                    'TRB': 0, 'TOV': 0, 'oFGM': 0, 'oFGA': 0, 'o3PM': 0,
                                    'o3PA': 0, 'oFTA': 0, 'oORB': 0, 'oDRB': 0, 'oTRB': 0, 'oTOV': 0,
                                    'Tempo': 0, 'oTempo': 0, 'Avg Tempo': 0, 'OE': 0, 'DE': 0,
                                    'EFG': 0, 'dEFG': 0, 'ORB%': 0, 'DRB%': 0, 'TRB%': 0,
                                    'FTA FGA R': 0, 'oFTA FGA R': 0, 'TOV%': 0, 'DTOV%': 0}, ignore_index=True)
    '''
if __name__ == "__main__":
    main()
        
    
