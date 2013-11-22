SPELL_EFFECTS = {
	'weapon_process': {

		'Core Shatter': {
			'name': 'Core Shatter',
			'type': 'cold',
			'DD': 500,
			'DoT': (),
			'debuff': ('fire', 20),
			'proc_chance': 0.10},

		'Jagged Puncture': {
			'name': 'Jagged Puncture',
			'type': 'physical',
			'DD': 500,
			'DoT': (100, 3, 30),
			'debuff': (),
			'proc_chance': 0.10},

		'Plasma Flare': {
			'name': 'Plasma Flare',
			'type': 'fire',
			'DD': 500,
			'DoT': (),
			'debuff': ('cold', 20),
			'proc_chance': 0.10},

		'Windwalker\'s Fury': {
			'name': 'Windwalker\'s Fury',
			'type': 'physical',
			'DD': 0,
			'DoT': (200, 3, 27),
			'debuff': (),
			'proc_chance': 0.3}
		}
	}