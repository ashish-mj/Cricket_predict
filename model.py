#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:46:29 2020

@author: ashish
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


teams = ['England', 'South Africa', 'West Indies', 
            'Pakistan', 'New Zealand', 'Sri Lanka', 'Afghanistan', 
            'Australia', 'Bangladesh', 'India','Kenya','Netherlands','Canada',
            'Zimbabwe','Ireland','Kenya','Scotland','U.A.E.','Hong Kong','P.N.G.']
teams_dict = {'England': 1, 'South Africa': 2, 'West Indies':3, 
            'Pakistan':4, 'New Zealand':5, 'Sri Lanka':6, 'Afghanistan':7, 
            'Australia':8, 'Bangladesh':9, 'India':10,'Netherlands':11,'Canada':12,
            'Zimbabwe':13,'Ireland':14, 'Kenya':15,'Scotland':16,'U.A.E.':17,
            'Hong Kong':18,'P.N.G.':19}

df_teams = pd.read_csv('results.csv')



df_teams = df_teams.drop(['date','Margin', 'Ground'], axis=1)
df_teams.loc[df_teams.Winner == df_teams.Team_1,'winning_team']=1
df_teams.loc[df_teams.Winner == df_teams.Team_2, 'winning_team']=2
df_teams.loc[df_teams.Winner == 'no result', 'winning_team']=3
df_teams.loc[df_teams.Winner == 'tied', 'winning_team']=4


df_teams.loc[df_teams.Team_1 =='England','Team_1']=1
df_teams.loc[df_teams.Team_2 =='England','Team_2']=1
    
df_teams.loc[df_teams.Team_1 =='South Africa','Team_1']=2
df_teams.loc[df_teams.Team_2 =='South Africa','Team_2']=2

df_teams.loc[df_teams.Team_1 =='West Indies','Team_1']=3
df_teams.loc[df_teams.Team_2 =='West Indies','Team_2']=3

df_teams.loc[df_teams.Team_1 =='Pakistan','Team_1']=4
df_teams.loc[df_teams.Team_2 =='Pakistan','Team_2']=4

df_teams.loc[df_teams.Team_1 =='New Zealand','Team_1']=5
df_teams.loc[df_teams.Team_2 =='New Zealand','Team_2']=5

df_teams.loc[df_teams.Team_1 =='Sri Lanka','Team_1']=6
df_teams.loc[df_teams.Team_2 =='Sri Lanka','Team_2']=6
    
df_teams.loc[df_teams.Team_1 =='Afghanistan','Team_1']=7
df_teams.loc[df_teams.Team_2 =='Afghanistan','Team_2']=7

df_teams.loc[df_teams.Team_1 =='Australia','Team_1']=8
df_teams.loc[df_teams.Team_2 =='Australia','Team_2']=8

df_teams.loc[df_teams.Team_1 =='Bangladesh','Team_1']=9
df_teams.loc[df_teams.Team_2 =='Bangladesh','Team_2']=9

df_teams.loc[df_teams.Team_1 =='India','Team_1']=10
df_teams.loc[df_teams.Team_2 =='India','Team_2']=10

df_teams.loc[df_teams.Team_1 =='Netherlands','Team_1']=11
df_teams.loc[df_teams.Team_2 =='Netherlands','Team_2']=11

df_teams.loc[df_teams.Team_1 =='Canada','Team_1']=12
df_teams.loc[df_teams.Team_2 =='Canada','Team_2']=12

df_teams.loc[df_teams.Team_1 =='Zimbabwe','Team_1']=13
df_teams.loc[df_teams.Team_2 =='Zimbabwe','Team_2']=13

df_teams.loc[df_teams.Team_1 =='Ireland','Team_1']=14
df_teams.loc[df_teams.Team_2 =='Ireland','Team_2']=14

df_teams.loc[df_teams.Team_1 =='Kenya','Team_1']=15
df_teams.loc[df_teams.Team_2 =='Kenya','Team_2']=15

df_teams.loc[df_teams.Team_1 =='Scotland','Team_1']=16
df_teams.loc[df_teams.Team_2 =='Scotland','Team_2']=16

df_teams.loc[df_teams.Team_1 =='U.A.E.','Team_1']=17
df_teams.loc[df_teams.Team_2 =='U.A.E.','Team_2']=17

df_teams.loc[df_teams.Team_1 =='Hong Kong','Team_1']=18
df_teams.loc[df_teams.Team_2 =='Hong Kong','Team_2']=18

df_teams.loc[df_teams.Team_1 =='P.N.G.','Team_1']=19
df_teams.loc[df_teams.Team_2 =='P.N.G.','Team_2']=19

df = df_teams.reset_index()


df_teams = df_teams.drop(['Winner'], axis=1)
X = df_teams.drop(['winning_team'], axis=1)
Y = df_teams["winning_team"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y,random_state=0)

rf = RandomForestClassifier(n_estimators=100, max_depth=20, random_state=0) 

rf.fit(X_train, Y_train)

print("Enter Teams from list")
print(teams)
team1,team2=map(str,input().split())
winner_predict = rf.predict([[teams_dict[team1],teams_dict[team2]]])
if winner_predict[0]==1:
    print(team1)
elif winner_predict[0]==2:
    print(team2)
elif winner_predict[0]==3:
    print("no result")
elif winner_predict[0]==4:
    print("tied")

print(rf.score(X_test,Y_test))



