from time import time
from random import random, randrange

from model.items_weapons import WEAPONS
from model.spells import SPELL_EFFECTS
from model.player import *

class Player:
	def __init__(self, name, pclass, **stats):
		self.name = name

		self.pclass = pclass
		
		self.EQUIPMENT_SLOTS = EQUIPMENT_SLOTS.copy()

		self.INVENTORY_SLOTS = INVENTORY_SLOTS.copy()
		
		player_stats = DEFAULT_PLAYER_STATS.copy()
		
		for (k, v) in CLASS_STATS_MODIFIER_DICT[self.pclass].items():
			player_stats[k] += v

		for (k, v) in stats.items():
			player_stats[k] = v

		for (k, v) in player_stats.items():
			setattr(self, k, v)

	def one_hand_attackStats(self):
		primDmg = self.EQUIPMENT_SLOTS['primary']['damage'] * (self.attack / 100)
		primaryBase = self.EQUIPMENT_SLOTS['primary']['delay'] * 0.02
		primDly =  '{:.3f}'.format(primaryBase - (primaryBase * self.haste))
		if self.EQUIPMENT_SLOTS['primary']['effect']:
			self.proc1 = SPELL_EFFECTS['weapon_process'][self.EQUIPMENT_SLOTS['primary']['effect']]

		secDmg = self.EQUIPMENT_SLOTS['secondary']['damage'] * (self.attack / 120)
		secondaryBase = self.EQUIPMENT_SLOTS['secondary']['delay'] * 0.03
		secDly = '{:.3f}'.format(secondaryBase - (secondaryBase * self.haste))
		if self.EQUIPMENT_SLOTS['secondary']['effect']:
			self.proc2 = SPELL_EFFECTS['weapon_process'][self.EQUIPMENT_SLOTS['secondary']['effect']]

		primaryDmgType = self.EQUIPMENT_SLOTS['primary']['hit_msg']
		secondaryDmgType = self.EQUIPMENT_SLOTS['secondary']['hit_msg']

		self.primStats = (primDmg, float(primDly), primaryDmgType)
		self.secStats = (secDmg, float(secDly), secondaryDmgType)
	
		return self.primStats, self.secStats, self.proc1, self.proc2

	def two_hand_attackStats(self):
		primDmg = (self.EQUIPMENT_SLOTS['primary']['damage'] * 1.3) * (self.attack / 100)
		primaryBase = self.EQUIPMENT_SLOTS['primary']['delay'] * 0.02
		primDly =  '{:.3f}'.format(primaryBase - (primaryBase * self.haste))
		if self.EQUIPMENT_SLOTS['primary']['effect']:
			self.proc1 = SPELL_EFFECTS['weapon_process'][self.EQUIPMENT_SLOTS['primary']['effect']]

		primaryDmgType = self.EQUIPMENT_SLOTS['primary']['hit_msg']

		self.primStats = (primDmg, float(primDly), primaryDmgType)

		return self.primStats, self.proc1

	def ranged_attackStats(self):
		rngDmg = (self.EQUIPMENT_SLOTS['ranged']['damage'] + self.EQUIPMENT_SLOTS['ammo']['damage']) * (self.attack / 200)
		rangedBase = self.EQUIPMENT_SLOTS['ranged']['delay'] * 0.02
		rngDly = '{:.3f}'.format(rangedBase - (rangedBase * self.haste))
		rngRng = self.EQUIPMENT_SLOTS['ranged']['range'] + self.EQUIPMENT_SLOTS['ammo']['range']
		if self.EQUIPMENT_SLOTS['ranged']['effect']:
			self.proc3 = SPELL_EFFECTS['weapon_process'][self.EQUIPMENT_SLOTS['ranged']['effect']]

		rangedDmgType = self.EQUIPMENT_SLOTS['ranged']['hit_msg']

		self.rngStats = (rngDmg, float(rngDly), rngRng, rangedDmgType)

		return self.rngStats, self.proc3

	def levelUp(self):
		self.level += 1
		if self.pclass != 'Admin':
			self.health     += int((0.04284 * self.health)     - (0.000 * (self.health     / 200)))
			self.stamina    += int((0.04430 * self.stamina)    - (0.057 * (self.stamina    / 200)))
			self.mana       += int((0.04284 * self.mana)       - (0.000 * (self.mana       / 200)))
			self.avoidance  += int((0.01725 * self.avoidance)  - (0.004 * (self.avoidance  / 300)))
			self.mitigation += int((0.02256 * self.mitigation) - (0.055 * (self.mitigation / 300)))
			self.accuracy   += int((0.00900 * self.accuracy)   - (0.000 * (self.accuracy   / 100)))
			self.attack     += int((0.02418 * self.attack)     - (0.000 * (self.attack     / 100)))
			self.critical   += int((0.02299 * self.critical)   - (0.012 * (self.critical   / 100)))

	def showPlayer(self):
		for v in (
			('Chr', 'name'),
			('Lvl', 'level'),
			('Cls', 'pclass'),
			(' HP', 'health'),
			('Sta', 'stamina'),
			(' MP', 'mana'),
			('Avd', 'avoidance'),
			('Mit', 'mitigation'),
			('Acc', 'accuracy'),
			('Atk', 'attack'),
			('Crt', 'critical'),
			('Hst', 'haste'),
			'primStats',
			'secStats',
			'rngStats',
			'proc1',
			'proc2',
			'proc3',
			'debuff',
			'zone',
			'locX',
			'locY',
			'agro',
			):
			print('%s: %s' % (
				(v[0], getattr(self, v[1])) if isinstance(v, tuple) else
				(v, getattr(self, v))))
		print sorted(self.EQUIPMENT_SLOTS['primary'].items(), reverse=True), '\n', \
			  sorted(self.EQUIPMENT_SLOTS['secondary'].items(), reverse=True), '\n',\
			  sorted(self.EQUIPMENT_SLOTS['ranged'].items(), reverse=True), '\n', \
			  sorted(self.EQUIPMENT_SLOTS['ammo'].items(), reverse=True)

	def testLevels(self, level):
		for i in xrange(level - 1):
			self.levelUp()

def time_delay_attack(attacker, target, attackStats):

	def execute_attack(attacker, target, attackStats):
		hitChance = (((attacker.accuracy / 10) - (10 * random())) * \
					((1000 - target.avoidance) / 1000) + (10 * random())) - \
					(attacker.accuracy / 10) * \
					((1000 - target.avoidance) / 1000)
		if hitChance > 1:
			if attacker.attack < target.mitigation:
				totalDMG = attacker.level
			else:
				baseDMG = int(((attackStats[0] * ((1000 - target.mitigation) /  \
						  (100 + (15 * random()))))) * 0.1)
				if (attacker.critical / 10) > randrange(99):
					totalDMG = int(baseDMG * 1.75) + attacker.level
					print 'Critical Hit!'
				else:
					totalDMG = baseDMG + attacker.level
			target.health = target.health - totalDMG
			print '%s %s %s for %s points of damage!\n%s HP: %s' % \
				  (attacker.name, attackStats[-1], target.name, totalDMG, \
				  target.name, target.health)
		else:
			print 'Missed'

	startTime = time()
	delay = attackStats[1]
	attackTime = startTime + delay
	while target.health > 0:
		endTime = time()
		if endTime >= attackTime:
			execute_attack(attacker, target, attacker.primStats)
			time_delay_attack(attacker, target, attacker.primStats)