from model.items_weapons import WEAPONS
from time import time

__ALL__ = ('EQUIPMENT_SLOTS', 'INVENTORY_SLOTS', 'DEFAULT_PLAYER_STATS',
           'CLASS_STATS_MODIFIER_DICT')

EQUIPMENT_SLOTS = {
	'head': '',
	'chest': '',
	'arms': '',
	'l_wrist': '',
	'r_wrist': '',
	'hands': '',
	'legs': '',
	'feet': '',
	'face': '',
	'neck': '',
	'l_ring': '',
	'r_ring': '',
	'primary': WEAPONS['Barehand'],
	'secondary': WEAPONS['Barehand'],
	'ranged': '',
	'ammo': ''
	}

INVENTORY_SLOTS = {
	'inv_slot_1': '',
	'inv_slot_2': '',
	'inv_slot_3': '',
	'inv_slot_4': '',
	'inv_slot_5': '',
	'inv_slot_6': '',
	'inv_slot_7': '',
	'inv_slot_8': ''
	}

DEFAULT_PLAYER_STATS = {
	'level': 1,
	'health': 50,
	'stamina': 50,
	'mana': 50,
	'avoidance': 100,
	'mitigation': 100,
	'accuracy': 350,
	'attack': 200,
	'critical': 0,
	'haste': 0,
	'primStats': (),
	'primDelay': time(),
	'secStats': (),
	'secDelay': time(),
	'rngStats': (),
	'rngDelay': time(),
	'proc1': '',
	'proc2': '',
	'proc3': '',
	'debuff': 0,
	'zone': 'tutorial',
	'locX': 0,
	'locY': 0,
	'agro': 0
	}

CLASS_STATS_MODIFIER_DICT = {
	'Admin': {
		'health': 10000 - DEFAULT_PLAYER_STATS['health'],
		'stamina': 10000 - DEFAULT_PLAYER_STATS['stamina'],
		'mana': 10000 - DEFAULT_PLAYER_STATS['mana'],
		'avoidance': 1000 - DEFAULT_PLAYER_STATS['avoidance'],
		'mitigation': 1000 - DEFAULT_PLAYER_STATS['mitigation'],
		'accuracy': 1000 - DEFAULT_PLAYER_STATS['accuracy'],
		'attack': 5000 - DEFAULT_PLAYER_STATS['attack'],
		'critical': 1000 - DEFAULT_PLAYER_STATS['critical']
		},

	'testBase': {},

	'testMin': {
		'health': -15,
		'stamina': -15,
		'mana': -50,
		'avoidance': -25,
		'mitigation': -35,
		'accuracy': -200,
		'attack': -100,
		},

	'testMax': {
		'health': +25,
		'stamina': +10,
		'mana': +25,
		'avoidance': +100,
		'mitigation': +25,
		'accuracy': +75,
		'attack': +100,
		'critical': +75
		},

	'Warrior': {
		'health': +25,
		'stamina': +10,
		'mana': -50,
		'avoidance': -25,
		'mitigation': +25
		},

	'Rogue': {
		'health': -10,
		'stamina': +5,
		'mana': -50,
		'avoidance': +25,
		'mitigation': -20,
		'accuracy': +75,
		'attack': +50,
		'critical': +75
		},

	'Monk': {
		'health': +10,
		'stamina': +10,
		'mana': -50,
		'avoidance': +100,
		'mitigation': -30,
		'accuracy': +50,
		'attack': +100,
		'critical': +50
		},

	'Ranger': {
		'health': +5,
		'stamina': +5,
		'mana': -10,
		'accuracy': +50,
		'attack': +25,
		'critical': +45
		},

	'Paladin': {
		'health': +15,
		'stamina': +5,
		'mana': -10,
		'avoidance': -5,
		'mitigation': +25,
		'accuracy': -35,
		'attack': +35
		},

	'Shadow Knight': {
		'health': +15,
		'stamina': +5,
		'mana': -10,
		'avoidance': -10,
		'mitigation': +20,
		'accuracy': -40,
		'attack': +50
		},

	'Cleric': {
		'health': +15,
		'stamina': -10,
		'mana': +15,
		'avoidance': -15,
		'mitigation': +10,
		'accuracy': -100,
		'attack': -50
		},

	'Wizard': {
		'health': -15,
		'stamina': -15,
		'mana': +25,
		'avoidance': +50,
		'mitigation': -35,
		'accuracy': -200,
		'attack': -100
		},

	'Necromancer': {
		'health': -15,
		'stamina': -15,
		'mana': +25,
		'avoidance': +40,
		'mitigation': -25,
		'accuracy': -100,
		'attack': -25
		}
	}
