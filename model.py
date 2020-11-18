#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:46:29 2020

@author: ashish
"""
import pandas as pd
#from sklearn.model_selection import train_test_split
#from sklearn.neighbors import KNeighborsClassifier


teams = ['England', ' South Africa', '', 'West Indies', 
            'Pakistan', 'New Zealand', 'Sri Lanka', 'Afghanistan', 
            'Australia', 'Bangladesh', 'India']

results = pd.read_csv('results.csv')


df_teams_1 = results[results['Team_1'].isin(teams)]
df_teams_2 = results[results['Team_2'].isin(teams)]
df_teams = pd.concat((df_teams_1, df_teams_2))
df_teams.drop_duplicates()
df_teams = df_teams.drop(['date','Margin', 'Ground'], axis=1)
df_teams.loc[df_teams.Winner == df_teams.Team_1,'winning_team']=1
df_teams.loc[df_teams.Winner == df_teams.Team_2, 'winning_team']=2
df_teams = df_teams.drop(['Winner'], axis=1)

X = df_teams.drop(['winning_team'], axis=1)
Y = df_teams["winning_team"]





