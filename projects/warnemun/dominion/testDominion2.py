# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 2020

@author: nicole warnemuende
"""

import Dominion
import testUtility

# Get player names
player_names = ["Nicole","Andrew","Prajwal"]

#number of curses and victory cards
nV = 0
nC = testUtility.setcursecards(player_names)

# Define box
box = testUtility.getboxes(nV)

supply_order = testUtility.getsupplyorder()

# Pick 10 cards from box to be in the supply.
supply = testUtility.getsupply(box, player_names, nV, nC)

supply["Estate"] = [Dominion.Estate()] * nV
supply["Duchy"] = [Dominion.Duchy()] * nV
supply["Province"] = [Dominion.Province()] * nV
supply["Curse"] = [Dominion.Curse()] * nC

# initialize the trash
trash = []

# Costruct the Player objects
players = testUtility.constructplayers(player_names)

# Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:
                print(stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name, player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)

# Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc['VICTORY POINTS']
vpmax = vp.max()
winners = []
for i in vp.index:
    if vp.loc[i] == vpmax:
        winners.append(i)
if len(winners) > 1:
    winstring = ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0], 'wins!'])

print("\nGAME OVER!!!\n" + winstring + "\n")
print(dcs)