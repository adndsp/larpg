from lib.playerlib import Player, time_delay_attack

def main():
	player1 = Player('Wiggles', 'Rogue')
	player1.testLevels(100)
#	player1.EQUIPMENT_SLOTS['primary'] = WEAPONS['Stick of Tuning']
#	player1.EQUIPMENT_SLOTS['secondary'] = WEAPONS['Solar Flame Tachi']
#	player1.EQUIPMENT_SLOTS['ranged'] = WEAPONS['Forest Stalker Recurve Bow']
#	player1.EQUIPMENT_SLOTS['ammo'] = WEAPONS['Feathered Steel Nock Broadhead']
	player1.one_hand_attackStats()
#	player1.ranged_attackStats()
	
	player2 = Player('Squirms', 'testMin')
	player2.testLevels(100)
#	player2.EQUIPMENT_SLOTS['primary'] = WEAPONS['Scimitar of Glacial Fury']
#	player2.EQUIPMENT_SLOTS['secondary'] = WEAPONS['Solar Flame Tachi']
#	player2.EQUIPMENT_SLOTS['ranged'] = WEAPONS['Forest Stalker Recurve Bow']
#	player2.EQUIPMENT_SLOTS['ammo'] = WEAPONS['Feathered Steel Nock Broadhead']
	player2.one_hand_attackStats()
#	player1.ranged_attackStats()

	player2.health = 10000

	time_delay_attack(player1, player2, player1.primStats)

#	player1.showPlayer()

if __name__ == '__main__':
	main()