import random
#import numpy as np


head = 1
tail =2
names ={head:'heads',tail:'tails'}
def coin_toss():
    home_team = move()
    away_team = random.randint(1, 2)
    result(home_team, away_team)

def move():
    home_team = input(" home team chose either heads or tails ")
   # home_team = int(home_team)
    try:
        if home_team in ('head','heads','tails'):
            return home_team
    except ValueError:
        pass
    print("please enter head or tails")

def result(home_team,away_team ):
    print('aotomatic choice for away team was {0}'.format(names[away_team]))
    #print(home_team,away_team)

def kick():
    if home_team == away_team:
        print('home team wins the toss')

kick()
scoin_toss()