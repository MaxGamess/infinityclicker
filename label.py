import pygame
import json
import os
import math
import sys
import random

pygame.init()

GOLD = (255, 215, 0)
DARK_GOLD = (184, 134, 11)
LIGHT_GOLD = (255, 240, 150)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_BROWN = (26, 11, 0)
BROWN = (61, 26, 0)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 150, 255)
DARK_BLUE = (30, 30, 150)
PURPLE = (150, 50, 255)
GRAY = (100, 100, 100)
DARK_GRAY = (50, 50, 50)
LIGHT_GRAY = (180, 180, 180)
SAPPHIRE = (15, 82, 186)
LIGHT_SAPPHIRE = (100, 180, 255)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)
PINK = (255, 105, 180)
TITANIUM = (150, 150, 200)
LIGHT_TITANIUM = (200, 200, 255)
COBALT = (0, 200, 180)
LIGHT_COBALT = (100, 230, 210)
IRIDIUM = (255, 130, 0)
LIGHT_IRIDIUM = (255, 200, 100)
PALLADIUM = (200, 150, 255)
LIGHT_PALLADIUM = (230, 200, 255)
STRONTIUM = (255, 150, 200)
LIGHT_STRONTIUM = (255, 200, 230)
CHROMIUM = (150, 220, 255)
LIGHT_CHROMIUM = (200, 240, 255)
VANADIUM = (255, 140, 0)
LIGHT_VANADIUM = (255, 200, 100)
ZINK = (220, 220, 220)
LIGHT_ZINK = (240, 240, 240)

CASES = {
    'wooden_case': 0.001,
    'stone_case': 0.0005,
    'copper_case': 0.0003,
    'iron_case': 0.0001,
    'golden_case': 0.00005,
    'emerald_case': 0.000025,
    'diamond_case': 0.00001,
    'ruby_case': 0.000005,
    'netherite_case': 0.0000025,
    'obsidian_case': 0.0000005,
    'magic_case': 0.0000001,
    'sapphire_case': 0.00000005,
    'titan_case': 0.000000025,
    'cobalt_case': 0.0000000125,
    'iridium_case': 0.00000000625,
    'palladium_case': 0.000000003125,
    'strontium_case': 0.0000000015625,
    'chromium_case': 0.00000000078125,
    'vanadium_case': 0.000000000390625,
    'zink_case': 0.000000000078125
}

CASE_NAMES = {
    'wooden_case': 'Деревянный кейс',
    'stone_case': 'Каменный кейс',
    'copper_case': 'Медный кейс',
    'iron_case': 'Железный кейс',
    'golden_case': 'Золотой кейс',
    'emerald_case': 'Изумрудный кейс',
    'diamond_case': 'Алмазный кейс',
    'ruby_case': 'Рубиновый кейс',
    'netherite_case': 'Незеритовый кейс',
    'obsidian_case': 'Обсидиановый кейс',
    'magic_case': 'Магический кейс',
    'sapphire_case': 'Сапфировый кейс',
    'titan_case': 'Титановый кейс',
    'cobalt_case': 'Кобальтовый кейс',
    'iridium_case': 'Иридиевый кейс',
    'palladium_case': 'Палладиевый кейс',
    'strontium_case': 'Стронциевый кейс',
    'chromium_case': 'Хромовый кейс',
    'vanadium_case': 'Ванадиевый кейс',
    'zink_case': 'Цинковый кейс'
}

CASE_CONTENTS = {
    'wooden_case': {
        'items': ['wooden_drag', 'wooden_apple', 'wooden_roll', 'wooden_act', 'wooden_rob'],
        'chance_per_item': 0.19,
        'apple_chance': 0.05,
        'color': (139, 69, 19)
    },
    'stone_case': {
        'items': ['stone_drag', 'stone_apple', 'stone_roll', 'stone_act', 'stone_rob'],
        'chance_per_item': 0.19,
        'apple_chance': 0.05,
        'color': (128, 128, 128)
    },
    'copper_case': {
        'items': ['copper_drag', 'copper_apple', 'copper_roll', 'copper_act', 'copper_rob'],
        'chance_per_item': 0.19,
        'apple_chance': 0.05,
        'color': (184, 115, 51)
    },
    'iron_case': {
        'items': ['iron_drag', 'iron_apple', 'iron_roll', 'iron_act', 'iron_rob'],
        'chance_per_item': 0.19,
        'apple_chance': 0.05,
        'color': (192, 192, 192)
    },
    'golden_case': {
        'items': ['golden_drag', 'golden_apple', 'golden_roll', 'golden_act', 'golden_rob'],
        'chance_per_item': 0.19,
        'apple_chance': 0.05,
        'color': (255, 215, 0)
    },
    'emerald_case': {
        'items': ['emerald_drag', 'emerald_apple', 'emerald_roll', 'emerald_act', 'emerald_rob'],
        'chance_per_item': 0.19,
        'apple_chance': 0.05,
        'color': (80, 200, 80)
    },
    'diamond_case': {
        'items': ['diamond_drag', 'diamond_apple', 'diamond_roll', 'diamond_act', 'diamond_rob'],
        'chance_per_item': 0.19,
        'apple_chance': 0.05,
        'color': (0, 255, 255)
    },
    'ruby_case': {
        'items': ['ruby_drag', 'ruby_apple', 'ruby_roll', 'ruby_act', 'ruby_rob'],
        'chance_per_item': 0.19,
        'apple_chance': 0.05,
        'color': (200, 0, 0)
    },
    'netherite_case': {
        'items': ['netherite_drag', 'netherite_apple', 'netherite_roll', 'netherite_act', 'netherite_rob'],
        'chance_per_item': 0.19,
        'apple_chance': 0.05,
        'color': (80, 0, 80)
    },
    'obsidian_case': {
        'items': ['obsidian_drag', 'obsidian_apple', 'obsidian_roll', 'obsidian_act', 'obsidian_rob'],
        'chance_per_item': 0.19,
        'apple_chance': 0.05,
        'color': (60, 20, 80)
    },
    'magic_case': {
        'items': ['magic_drag', 'magic_apple', 'magic_roll', 'magic_act', 'magic_rob'],
        'chance_per_item': 0.19,
        'apple_chance': 0.05,
        'color': (200, 50, 255)
    },
    'sapphire_case': {
        'items': ['sapphire_drag', 'sapphire_apple', 'sapphire_roll', 'sapphire_act', 'sapphire_rob'],
        'chance_per_item': 0.19,
        'apple_chance': 0.05,
        'color': LIGHT_SAPPHIRE
    },
    'titan_case': {
        'items': ['titan_drag', 'titan_apple', 'titan_roll', 'titan_act', 'titan_rob'],
        'chance_per_item': 0.19,
        'apple_chance': 0.05,
        'color': TITANIUM
    },
    'cobalt_case': {
        'items': ['cobalt_drag', 'cobalt_apple', 'cobalt_roll', 'cobalt_act', 'cobalt_rob'],
        'chance_per_item': 0.19,
        'apple_chance': 0.05,
        'color': COBALT
    },
    'iridium_case': {
        'items': ['iridium_drag', 'iridium_apple', 'iridium_roll', 'iridium_act', 'iridium_rob'],
        'chance_per_item': 0.19,
        'apple_chance': 0.05,
        'color': IRIDIUM
    },
    'palladium_case': {
        'items': ['palladium_drag', 'palladium_apple', 'palladium_roll', 'palladium_act', 'palladium_rob'],
        'chance_per_item': 0.19,
        'apple_chance': 0.05,
        'color': PALLADIUM
    },
    'strontium_case': {
        'items': ['strontium_drag', 'strontium_apple', 'strontium_roll', 'strontium_act', 'strontium_rob'],
        'chance_per_item': 0.19,
        'apple_chance': 0.05,
        'color': STRONTIUM
    },
    'chromium_case': {
        'items': ['chromium_drag', 'chromium_apple', 'chromium_roll', 'chromium_act', 'chromium_rob'],
        'chance_per_item': 0.19,
        'apple_chance': 0.05,
        'color': CHROMIUM
    },
    'vanadium_case': {
        'items': ['vanadium_drag', 'vanadium_apple', 'vanadium_roll', 'vanadium_act', 'vanadium_rob'],
        'chance_per_item': 0.19,
        'apple_chance': 0.05,
        'color': VANADIUM
    },
    'zink_case': {
        'items': ['zink_drag', 'zink_apple', 'zink_roll', 'zink_act', 'zink_rob'],
        'chance_per_item': 0.19,
        'apple_chance': 0.05,
        'color': ZINK
    }
}

CASE_ORDER = ['wooden_case', 'stone_case', 'copper_case', 'iron_case', 'golden_case', 
              'emerald_case', 'diamond_case', 'ruby_case', 'netherite_case', 
              'obsidian_case', 'magic_case', 'sapphire_case', 'titan_case', 'cobalt_case', 'iridium_case', 'palladium_case', 'strontium_case', 'chromium_case', 'vanadium_case', 'zink_case']

TIER_ORDER = ['zink', 'vanadium', 'chromium', 'strontium', 'palladium', 'iridium', 'cobalt', 'titan', 'sapphire', 'magic', 'obsidian', 'netherite', 'ruby', 'diamond', 
              'emerald', 'golden', 'iron', 'copper', 'stone', 'wooden']

CROSS_ITEMS = {
    'wooden_cross': {
        'name': 'Деревянный крест',
        'price': 10000,
        'color': (139, 69, 19),
        'tier': 'wooden'
    },
    'stone_cross': {
        'name': 'Каменный крест',
        'price': 30000,
        'color': (128, 128, 128),
        'tier': 'stone'
    },
    'copper_cross': {
        'name': 'Медный крест',
        'price': 90000,
        'color': (184, 115, 51),
        'tier': 'copper'
    },
    'iron_cross': {
        'name': 'Железный крест',
        'price': 270000,
        'color': (192, 192, 192),
        'tier': 'iron'
    },
    'golden_cross': {
        'name': 'Золотой крест',
        'price': 800000,
        'color': (255, 215, 0),
        'tier': 'golden'
    },
    'emerald_cross': {
        'name': 'Изумрудный крест',
        'price': 2400000,
        'color': (80, 200, 80),
        'tier': 'emerald'
    },
    'diamond_cross': {
        'name': 'Алмазный крест',
        'price': 7200000,
        'color': (0, 255, 255),
        'tier': 'diamond'
    },
    'ruby_cross': {
        'name': 'Рубиновый крест',
        'price': 21000000,
        'color': (200, 0, 0),
        'tier': 'ruby'
    },
    'netherite_cross': {
        'name': 'Незеритовый крест',
        'price': 63000000,
        'color': (80, 0, 80),
        'tier': 'netherite'
    },
    'obsidian_cross': {
        'name': 'Обсидиановый крест',
        'price': 180000000,
        'color': (60, 20, 80),
        'tier': 'obsidian'
    },
    'magic_cross': {
        'name': 'Магический крест',
        'price': 540000000,
        'color': (200, 50, 255),
        'tier': 'magic'
    },
    'sapphire_cross': {
        'name': 'Сапфировый крест',
        'price': 1600000000,
        'color': LIGHT_SAPPHIRE,
        'tier': 'sapphire'
    },
    'titan_cross': {
        'name': 'Титановый крест',
        'price': 4800000000,
        'color': TITANIUM,
        'tier': 'titan'
    },
    'cobalt_cross': {
        'name': 'Кобальтовый крест',
        'price': 14400000000,
        'color': COBALT,
        'tier': 'cobalt'
    },
    'iridium_cross': {
        'name': 'Иридиевый крест',
        'price': 43000000000,
        'color': IRIDIUM,
        'tier': 'iridium'
    },
    'palladium_cross': {
        'name': 'Палладиевый крест',
        'price': 120000000000,
        'color': PALLADIUM,
        'tier': 'palladium'
    },
    'strontium_cross': {
        'name': 'Стронциевый крест',
        'price': 360000000000,
        'color': STRONTIUM,
        'tier': 'strontium'
    },
    'chromium_cross': {
        'name': 'Хромовый крест',
        'price': 1000000000000,
        'color': CHROMIUM,
        'tier': 'chromium'
    },
    'vanadium_cross': {
        'name': 'Ванадиевый крест',
        'price': 3000000000000,
        'color': VANADIUM,
        'tier': 'vanadium'
    },
    'zink_cross': {
        'name': 'Цинковый крест',
        'price': 27000000000000,
        'color': ZINK,
        'tier': 'zink'
    }
}

ITEMS = {
    'wooden_drag': {
        'name': 'Деревянный драг',
        'bonus': 1,
        'color': (139, 69, 19),
        'next': 'stone_drag',
        'type': 'drag',
        'rarity': 1,
        'price': 1000,
        'tier': 'wooden'
    },
    'apple': {
        'name': 'Яблоко',
        'bonus': 1,
        'color': (255, 50, 50),
        'next': 'wooden_apple',
        'type': 'apple',
        'rarity': 1,
        'price': 1500,
        'tier': 'wooden'
    },
    'wooden_roll': {
        'name': 'Деревянный ролл',
        'bonus': 1.1,
        'color': (139, 69, 19),
        'next': 'stone_roll',
        'type': 'roll',
        'rarity': 1,
        'price': 2000,
        'tier': 'wooden'
    },
    'stone_drag': {
        'name': 'Каменный драг',
        'bonus': 2,
        'color': (128, 128, 128),
        'next': 'copper_drag',
        'type': 'drag',
        'rarity': 2,
        'price': 5000,
        'tier': 'stone'
    },
    'wooden_apple': {
        'name': 'Деревянное яблоко',
        'bonus': 2,
        'color': (139, 69, 19),
        'next': 'stone_apple',
        'type': 'apple',
        'rarity': 2,
        'price': 4500,
        'tier': 'wooden'
    },
    'stone_roll': {
        'name': 'Каменный ролл',
        'bonus': 1.3,
        'color': (128, 128, 128),
        'next': 'copper_roll',
        'type': 'roll',
        'rarity': 2,
        'price': 6000,
        'tier': 'stone'
    },
    'copper_drag': {
        'name': 'Медный драг',
        'bonus': 3,
        'color': (184, 115, 51),
        'next': 'iron_drag',
        'type': 'drag',
        'rarity': 3,
        'price': 25000,
        'tier': 'copper'
    },
    'stone_apple': {
        'name': 'Каменное яблоко',
        'bonus': 3,
        'color': (128, 128, 128),
        'next': 'copper_apple',
        'type': 'apple',
        'rarity': 3,
        'price': 13500,
        'tier': 'stone'
    },
    'copper_roll': {
        'name': 'Медный ролл',
        'bonus': 1.5,
        'color': (184, 115, 51),
        'next': 'iron_roll',
        'type': 'roll',
        'rarity': 3,
        'price': 18000,
        'tier': 'copper'
    },
    'iron_drag': {
        'name': 'Железный драг',
        'bonus': 4,
        'color': (192, 192, 192),
        'next': 'golden_drag',
        'type': 'drag',
        'rarity': 4,
        'price': 120000,
        'tier': 'iron'
    },
    'copper_apple': {
        'name': 'Медное яблоко',
        'bonus': 4,
        'color': (184, 115, 51),
        'next': 'iron_apple',
        'type': 'apple',
        'rarity': 4,
        'price': 40000,
        'tier': 'copper'
    },
    'iron_roll': {
        'name': 'Железный ролл',
        'bonus': 1.7,
        'color': (192, 192, 192),
        'next': 'golden_roll',
        'type': 'roll',
        'rarity': 4,
        'price': 55000,
        'tier': 'iron'
    },
    'golden_drag': {
        'name': 'Золотой драг',
        'bonus': 5,
        'color': (255, 215, 0),
        'next': 'emerald_drag',
        'type': 'drag',
        'rarity': 5,
        'price': 550000,
        'tier': 'golden'
    },
    'iron_apple': {
        'name': 'Железное яблоко',
        'bonus': 5,
        'color': (192, 192, 192),
        'next': 'golden_apple',
        'type': 'apple',
        'rarity': 5,
        'price': 120000,
        'tier': 'iron'
    },
    'golden_roll': {
        'name': 'Золотой ролл',
        'bonus': 2.0,
        'color': (255, 215, 0),
        'next': 'emerald_roll',
        'type': 'roll',
        'rarity': 5,
        'price': 160000,
        'tier': 'golden'
    },
    'emerald_drag': {
        'name': 'Изумрудный драг',
        'bonus': 7,
        'color': (80, 200, 80),
        'next': 'diamond_drag',
        'type': 'drag',
        'rarity': 6,
        'price': 2500000,
        'tier': 'emerald'
    },
    'golden_apple': {
        'name': 'Золотое яблоко',
        'bonus': 7,
        'color': (255, 215, 0),
        'next': 'emerald_apple',
        'type': 'apple',
        'rarity': 6,
        'price': 360000,
        'tier': 'golden'
    },
    'emerald_roll': {
        'name': 'Изумрудный ролл',
        'bonus': 2.2,
        'color': (80, 200, 80),
        'next': 'diamond_roll',
        'type': 'roll',
        'rarity': 6,
        'price': 450000,
        'tier': 'emerald'
    },
    'diamond_drag': {
        'name': 'Алмазный драг',
        'bonus': 9,
        'color': (0, 255, 255),
        'next': 'ruby_drag',
        'type': 'drag',
        'rarity': 7,
        'price': 10000000,
        'tier': 'diamond'
    },
    'emerald_apple': {
        'name': 'Изумрудное яблоко',
        'bonus': 9,
        'color': (80, 200, 80),
        'next': 'diamond_apple',
        'type': 'apple',
        'rarity': 7,
        'price': 1000000,
        'tier': 'emerald'
    },
    'diamond_roll': {
        'name': 'Алмазный ролл',
        'bonus': 2.5,
        'color': (0, 255, 255),
        'next': 'ruby_roll',
        'type': 'roll',
        'rarity': 7,
        'price': 1200000,
        'tier': 'diamond'
    },
    'ruby_drag': {
        'name': 'Рубиновый драг',
        'bonus': 12,
        'color': (200, 0, 0),
        'next': 'netherite_drag',
        'type': 'drag',
        'rarity': 8,
        'price': 50000000,
        'tier': 'ruby'
    },
    'diamond_apple': {
        'name': 'Алмазное яблоко',
        'bonus': 12,
        'color': (0, 255, 255),
        'next': 'ruby_apple',
        'type': 'apple',
        'rarity': 8,
        'price': 3000000,
        'tier': 'diamond'
    },
    'ruby_roll': {
        'name': 'Рубиновый ролл',
        'bonus': 2.7,
        'color': (200, 0, 0),
        'next': 'netherite_roll',
        'type': 'roll',
        'rarity': 8,
        'price': 3500000,
        'tier': 'ruby'
    },
    'netherite_drag': {
        'name': 'Незеритовый драг',
        'bonus': 15,
        'color': (80, 0, 80),
        'next': 'obsidian_drag',
        'type': 'drag',
        'rarity': 9,
        'price': 250000000,
        'tier': 'netherite'
    },
    'ruby_apple': {
        'name': 'Рубиновое яблоко',
        'bonus': 15,
        'color': (200, 0, 0),
        'next': 'netherite_apple',
        'type': 'apple',
        'rarity': 9,
        'price': 9000000,
        'tier': 'ruby'
    },
    'netherite_roll': {
        'name': 'Незеритовый ролл',
        'bonus': 3.0,
        'color': (80, 0, 80),
        'next': 'obsidian_roll',
        'type': 'roll',
        'rarity': 9,
        'price': 12000000,
        'tier': 'netherite'
    },
    'netherite_apple': {
        'name': 'Незеритовое яблоко',
        'bonus': 20,
        'color': (80, 0, 80),
        'next': 'obsidian_apple',
        'type': 'apple',
        'rarity': 10,
        'price': 25000000,
        'tier': 'netherite'
    },
    'obsidian_drag': {
        'name': 'Обсидиановый драг',
        'bonus': 20,
        'color': (60, 20, 80),
        'next': 'magic_drag',
        'type': 'drag',
        'rarity': 10,
        'price': 1000000000,
        'tier': 'obsidian'
    },
    'obsidian_apple': {
        'name': 'Обсидиановое яблоко',
        'bonus': 30,
        'color': (60, 20, 80),
        'next': 'magic_apple',
        'type': 'apple',
        'rarity': 11,
        'price': 75000000,
        'tier': 'obsidian'
    },
    'obsidian_roll': {
        'name': 'Обсидиановый ролл',
        'bonus': 5.0,
        'color': (60, 20, 80),
        'next': 'magic_roll',
        'type': 'roll',
        'rarity': 10,
        'price': 35000000,
        'tier': 'obsidian'
    },
    'magic_drag': {
        'name': 'Магический драг',
        'bonus': 30,
        'color': (200, 50, 255),
        'next': 'sapphire_drag',
        'type': 'drag',
        'rarity': 11,
        'price': 5000000000,
        'tier': 'magic'
    },
    'magic_apple': {
        'name': 'Магическое яблоко',
        'bonus': 40,
        'color': (200, 50, 255),
        'next': 'sapphire_apple',
        'type': 'apple',
        'rarity': 12,
        'price': 220000000,
        'tier': 'magic'
    },
    'magic_roll': {
        'name': 'Магический ролл',
        'bonus': 10.0,
        'color': (200, 50, 255),
        'next': 'sapphire_roll',
        'type': 'roll',
        'rarity': 11,
        'price': 100000000,
        'tier': 'magic'
    },
    'sapphire_drag': {
        'name': 'Сапфировый драг',
        'bonus': 50,
        'color': SAPPHIRE,
        'next': 'titan_drag',
        'type': 'drag',
        'rarity': 12,
        'price': 20000000000,
        'tier': 'sapphire'
    },
    'sapphire_apple': {
        'name': 'Сапфировое яблоко',
        'bonus': 50,
        'color': LIGHT_SAPPHIRE,
        'next': 'titan_apple',
        'type': 'apple',
        'rarity': 13,
        'price': 600000000,
        'tier': 'sapphire'
    },
    'sapphire_roll': {
        'name': 'Сапфировый ролл',
        'bonus': 20.0,
        'color': LIGHT_SAPPHIRE,
        'next': 'titan_roll',
        'type': 'roll',
        'rarity': 12,
        'price': 300000000,
        'tier': 'sapphire'
    },
    'wooden_act': {
        'name': 'Деревянный акт',
        'bonus': 1.1,
        'color': (139, 69, 19),
        'next': 'stone_act',
        'type': 'act',
        'rarity': 1,
        'price': 15000,
        'tier': 'wooden'
    },
    'stone_act': {
        'name': 'Каменный акт',
        'bonus': 1.2,
        'color': (128, 128, 128),
        'next': 'copper_act',
        'type': 'act',
        'rarity': 2,
        'price': 45000,
        'tier': 'stone'
    },
    'copper_act': {
        'name': 'Медный акт',
        'bonus': 1.3,
        'color': (184, 115, 51),
        'next': 'iron_act',
        'type': 'act',
        'rarity': 3,
        'price': 130000,
        'tier': 'copper'
    },
    'iron_act': {
        'name': 'Железный акт',
        'bonus': 1.4,
        'color': (192, 192, 192),
        'next': 'golden_act',
        'type': 'act',
        'rarity': 4,
        'price': 390000,
        'tier': 'iron'
    },
    'golden_act': {
        'name': 'Золотой акт',
        'bonus': 1.5,
        'color': (255, 215, 0),
        'next': 'emerald_act',
        'type': 'act',
        'rarity': 5,
        'price': 1200000,
        'tier': 'golden'
    },
    'emerald_act': {
        'name': 'Изумрудный акт',
        'bonus': 2.0,
        'color': (80, 200, 80),
        'next': 'diamond_act',
        'type': 'act',
        'rarity': 6,
        'price': 3600000,
        'tier': 'emerald'
    },
    'diamond_act': {
        'name': 'Алмазный акт',
        'bonus': 2.5,
        'color': (0, 255, 255),
        'next': 'ruby_act',
        'type': 'act',
        'rarity': 7,
        'price': 12000000,
        'tier': 'diamond'
    },
    'ruby_act': {
        'name': 'Рубиновый акт',
        'bonus': 3.0,
        'color': (200, 0, 0),
        'next': 'netherite_act',
        'type': 'act',
        'rarity': 8,
        'price': 36000000,
        'tier': 'ruby'
    },
    'netherite_act': {
        'name': 'Незеритовый акт',
        'bonus': 4.0,
        'color': (80, 0, 80),
        'next': 'obsidian_act',
        'type': 'act',
        'rarity': 9,
        'price': 180000000,
        'tier': 'netherite'
    },
    'obsidian_act': {
        'name': 'Обсидиановый акт',
        'bonus': 5.0,
        'color': (60, 20, 80),
        'next': 'magic_act',
        'type': 'act',
        'rarity': 10,
        'price': 500000000,
        'tier': 'obsidian'
    },
    'magic_act': {
        'name': 'Магический акт',
        'bonus': 7.5,
        'color': (200, 50, 255),
        'next': 'sapphire_act',
        'type': 'act',
        'rarity': 11,
        'price': 1500000000,
        'tier': 'magic'
    },
    'sapphire_act': {
        'name': 'Сапфировый акт',
        'bonus': 10.0,
        'color': LIGHT_SAPPHIRE,
        'next': 'titan_act',
        'type': 'act',
        'rarity': 12,
        'price': 4500000000,
        'tier': 'sapphire'
    },
    'wooden_rob': {
        'name': 'Деревянная роба',
        'bonus': 1.5,
        'color': (139, 69, 19),
        'next': 'stone_rob',
        'type': 'rob',
        'rarity': 1,
        'price': 30000,
        'tier': 'wooden'
    },
    'stone_rob': {
        'name': 'Каменная роба',
        'bonus': 2.0,
        'color': (128, 128, 128),
        'next': 'copper_rob',
        'type': 'rob',
        'rarity': 2,
        'price': 90000,
        'tier': 'stone'
    },
    'copper_rob': {
        'name': 'Медная роба',
        'bonus': 2.5,
        'color': (184, 115, 51),
        'next': 'iron_rob',
        'type': 'rob',
        'rarity': 3,
        'price': 260000,
        'tier': 'copper'
    },
    'iron_rob': {
        'name': 'Железная роба',
        'bonus': 3.0,
        'color': (192, 192, 192),
        'next': 'golden_rob',
        'type': 'rob',
        'rarity': 4,
        'price': 780000,
        'tier': 'iron'
    },
    'golden_rob': {
        'name': 'Золотая роба',
        'bonus': 4.0,
        'color': (255, 215, 0),
        'next': 'emerald_rob',
        'type': 'rob',
        'rarity': 5,
        'price': 2350000,
        'tier': 'golden'
    },
    'emerald_rob': {
        'name': 'Изумрудная роба',
        'bonus': 5.0,
        'color': (80, 200, 80),
        'next': 'diamond_rob',
        'type': 'rob',
        'rarity': 6,
        'price': 7000000,
        'tier': 'emerald'
    },
    'diamond_rob': {
        'name': 'Алмазная роба',
        'bonus': 7.0,
        'color': (0, 255, 255),
        'next': 'ruby_rob',
        'type': 'rob',
        'rarity': 7,
        'price': 21000000,
        'tier': 'diamond'
    },
    'ruby_rob': {
        'name': 'Рубиновая роба',
        'bonus': 10.0,
        'color': (200, 0, 0),
        'next': 'netherite_rob',
        'type': 'rob',
        'rarity': 8,
        'price': 63000000,
        'tier': 'ruby'
    },
    'netherite_rob': {
        'name': 'Незеритовая роба',
        'bonus': 15.0,
        'color': (80, 0, 80),
        'next': 'obsidian_rob',
        'type': 'rob',
        'rarity': 9,
        'price': 180000000,
        'tier': 'netherite'
    },
    'obsidian_rob': {
        'name': 'Обсидиановая роба',
        'bonus': 20.0,
        'color': (60, 20, 80),
        'next': 'magic_rob',
        'type': 'rob',
        'rarity': 10,
        'price': 540000000,
        'tier': 'obsidian'
    },
    'magic_rob': {
        'name': 'Магическая роба',
        'bonus': 30.0,
        'color': (200, 50, 255),
        'next': 'sapphire_rob',
        'type': 'rob',
        'rarity': 11,
        'price': 1600000000,
        'tier': 'magic'
    },
    'sapphire_rob': {
        'name': 'Сапфировая роба',
        'bonus': 40.0,
        'color': LIGHT_SAPPHIRE,
        'next': 'titan_rob',
        'type': 'rob',
        'rarity': 12,
        'price': 4800000000,
        'tier': 'sapphire'
    },
    'titan_drag': {
        'name': 'Титановый драг',
        'bonus': 75,
        'color': TITANIUM,
        'next': 'cobalt_drag',
        'type': 'drag',
        'rarity': 13,
        'price': 100000000000,
        'tier': 'titan'
    },
    'titan_apple': {
        'name': 'Титановое яблоко',
        'bonus': 75,
        'color': LIGHT_TITANIUM,
        'next': 'cobalt_apple',
        'type': 'apple',
        'rarity': 14,
        'price': 1800000000,
        'tier': 'titan'
    },
    'titan_roll': {
        'name': 'Титановый ролл',
        'bonus': 30.0,
        'color': LIGHT_TITANIUM,
        'next': 'cobalt_roll',
        'type': 'roll',
        'rarity': 13,
        'price': 900000000,
        'tier': 'titan'
    },
    'titan_act': {
        'name': 'Титановый акт',
        'bonus': 15.0,
        'color': LIGHT_TITANIUM,
        'next': 'cobalt_act',
        'type': 'act',
        'rarity': 13,
        'price': 13000000000,
        'tier': 'titan'
    },
    'titan_rob': {
        'name': 'Титановая роба',
        'bonus': 50.0,
        'color': LIGHT_TITANIUM,
        'next': 'cobalt_rob',
        'type': 'rob',
        'rarity': 13,
        'price': 14000000000,
        'tier': 'titan'
    },
    'cobalt_drag': {
        'name': 'Кобальтовый драг',
        'bonus': 100,
        'color': COBALT,
        'next': 'iridium_drag',
        'type': 'drag',
        'rarity': 14,
        'price': 500000000000,
        'tier': 'cobalt'
    },
    'cobalt_apple': {
        'name': 'Кобальтовое яблоко',
        'bonus': 100,
        'color': LIGHT_COBALT,
        'next': 'iridium_apple',
        'type': 'apple',
        'rarity': 15,
        'price': 5400000000,
        'tier': 'cobalt'
    },
    'cobalt_roll': {
        'name': 'Кобальтовый ролл',
        'bonus': 40.0,
        'color': LIGHT_COBALT,
        'next': 'iridium_roll',
        'type': 'roll',
        'rarity': 14,
        'price': 2700000000,
        'tier': 'cobalt'
    },
    'cobalt_act': {
        'name': 'Кобальтовый акт',
        'bonus': 20.0,
        'color': LIGHT_COBALT,
        'next': 'iridium_act',
        'type': 'act',
        'rarity': 14,
        'price': 39000000000,
        'tier': 'cobalt'
    },
    'cobalt_rob': {
        'name': 'Кобальтовая роба',
        'bonus': 75.0,
        'color': LIGHT_COBALT,
        'next': 'iridium_rob',
        'type': 'rob',
        'rarity': 14,
        'price': 42000000000,
        'tier': 'cobalt'
    },
    'iridium_drag': {
        'name': 'Иридиевый драг',
        'bonus': 150,
        'color': IRIDIUM,
        'next': 'palladium_drag',
        'type': 'drag',
        'rarity': 15,
        'price': 2500000000000,
        'tier': 'iridium'
    },
    'iridium_apple': {
        'name': 'Иридиевое яблоко',
        'bonus': 150,
        'color': LIGHT_IRIDIUM,
        'next': 'palladium_apple',
        'type': 'apple',
        'rarity': 16,
        'price': 16000000000,
        'tier': 'iridium'
    },
    'iridium_roll': {
        'name': 'Иридиевый ролл',
        'bonus': 50.0,
        'color': LIGHT_IRIDIUM,
        'next': 'palladium_roll',
        'type': 'roll',
        'rarity': 15,
        'price': 8000000000,
        'tier': 'iridium'
    },
    'iridium_act': {
        'name': 'Иридиевый акт',
        'bonus': 30.0,
        'color': LIGHT_IRIDIUM,
        'next': 'palladium_act',
        'type': 'act',
        'rarity': 15,
        'price': 115000000000,
        'tier': 'iridium'
    },
    'iridium_rob': {
        'name': 'Иридиевая роба',
        'bonus': 100.0,
        'color': LIGHT_IRIDIUM,
        'next': 'palladium_rob',
        'type': 'rob',
        'rarity': 15,
        'price': 120000000000,
        'tier': 'iridium'
    },
    'palladium_drag': {
        'name': 'Палладиевый драг',
        'bonus': 200,
        'color': PALLADIUM,
        'next': 'strontium_drag',
        'type': 'drag',
        'rarity': 16,
        'price': 12000000000000,
        'tier': 'palladium'
    },
    'palladium_apple': {
        'name': 'Палладиевое яблоко',
        'bonus': 200,
        'color': LIGHT_PALLADIUM,
        'next': 'strontium_apple',
        'type': 'apple',
        'rarity': 17,
        'price': 48000000000,
        'tier': 'palladium'
    },
    'palladium_roll': {
        'name': 'Палладиевый ролл',
        'bonus': 75.0,
        'color': LIGHT_PALLADIUM,
        'next': 'strontium_roll',
        'type': 'roll',
        'rarity': 16,
        'price': 24000000000,
        'tier': 'palladium'
    },
    'palladium_act': {
        'name': 'Палладиевый акт',
        'bonus': 40.0,
        'color': LIGHT_PALLADIUM,
        'next': 'strontium_act',
        'type': 'act',
        'rarity': 16,
        'price': 340000000000,
        'tier': 'palladium'
    },
    'palladium_rob': {
        'name': 'Палладиевая роба',
        'bonus': 150.0,
        'color': LIGHT_PALLADIUM,
        'next': 'strontium_rob',
        'type': 'rob',
        'rarity': 16,
        'price': 360000000000,
        'tier': 'palladium'
    },
    'strontium_drag': {
        'name': 'Стронциевый драг',
        'bonus': 300,
        'color': STRONTIUM,
        'next': 'chromium_drag',
        'type': 'drag',
        'rarity': 17,
        'price': 60000000000000,
        'tier': 'strontium'
    },
    'strontium_apple': {
        'name': 'Стронциевое яблоко',
        'bonus': 300,
        'color': LIGHT_STRONTIUM,
        'next': 'chromium_apple',
        'type': 'apple',
        'rarity': 18,
        'price': 140000000000,
        'tier': 'strontium'
    },
    'strontium_roll': {
        'name': 'Стронциевый ролл',
        'bonus': 100.0,
        'color': LIGHT_STRONTIUM,
        'next': 'chromium_roll',
        'type': 'roll',
        'rarity': 17,
        'price': 72000000000,
        'tier': 'strontium'
    },
    'strontium_act': {
        'name': 'Стронциевый акт',
        'bonus': 50.0,
        'color': LIGHT_STRONTIUM,
        'next': 'chromium_act',
        'type': 'act',
        'rarity': 17,
        'price': 1000000000000,
        'tier': 'strontium'
    },
    'strontium_rob': {
        'name': 'Стронциевая роба',
        'bonus': 200.0,
        'color': LIGHT_STRONTIUM,
        'next': 'chromium_rob',
        'type': 'rob',
        'rarity': 17,
        'price': 1000000000000,
        'tier': 'strontium'
    },
    'chromium_drag': {
        'name': 'Хромовый драг',
        'bonus': 400,
        'color': CHROMIUM,
        'next': 'vanadium_drag',
        'type': 'drag',
        'rarity': 18,
        'price': 300000000000000,
        'tier': 'chromium'
    },
    'chromium_apple': {
        'name': 'Хромовое яблоко',
        'bonus': 400,
        'color': LIGHT_CHROMIUM,
        'next': 'vanadium_apple',
        'type': 'apple',
        'rarity': 19,
        'price': 420000000000,
        'tier': 'chromium'
    },
    'chromium_roll': {
        'name': 'Хромовый ролл',
        'bonus': 150.0,
        'color': LIGHT_CHROMIUM,
        'next': 'vanadium_roll',
        'type': 'roll',
        'rarity': 18,
        'price': 210000000000,
        'tier': 'chromium'
    },
    'chromium_act': {
        'name': 'Хромовый акт',
        'bonus': 75.0,
        'color': LIGHT_CHROMIUM,
        'next': 'vanadium_act',
        'type': 'act',
        'rarity': 18,
        'price': 3000000000000,
        'tier': 'chromium'
    },
    'chromium_rob': {
        'name': 'Хромовая роба',
        'bonus': 300.0,
        'color': LIGHT_CHROMIUM,
        'next': 'vanadium_rob',
        'type': 'rob',
        'rarity': 18,
        'price': 3000000000000,
        'tier': 'chromium'
    },
    'vanadium_drag': {
        'name': 'Ванадиевый драг',
        'bonus': 500,
        'color': VANADIUM,
        'next': 'zink_drag',
        'type': 'drag',
        'rarity': 19,
        'price': 1500000000000000,
        'tier': 'vanadium'
    },
    'vanadium_apple': {
        'name': 'Ванадиевое яблоко',
        'bonus': 500,
        'color': LIGHT_VANADIUM,
        'next': 'zink_apple',
        'type': 'apple',
        'rarity': 20,
        'price': 1200000000000,
        'tier': 'vanadium'
    },
    'vanadium_roll': {
        'name': 'Ванадиевый ролл',
        'bonus': 200.0,
        'color': LIGHT_VANADIUM,
        'next': 'zink_roll',
        'type': 'roll',
        'rarity': 19,
        'price': 600000000000,
        'tier': 'vanadium'
    },
    'vanadium_act': {
        'name': 'Ванадиевый акт',
        'bonus': 100.0,
        'color': LIGHT_VANADIUM,
        'next': 'zink_act',
        'type': 'act',
        'rarity': 19,
        'price': 9000000000000,
        'tier': 'vanadium'
    },
    'vanadium_rob': {
        'name': 'Ванадиевая роба',
        'bonus': 400.0,
        'color': LIGHT_VANADIUM,
        'next': 'zink_rob',
        'type': 'rob',
        'rarity': 19,
        'price': 9000000000000,
        'tier': 'vanadium'
    },
    'zink_drag': {
        'name': 'Цинковый драг',
        'bonus': 600,
        'color': ZINK,
        'next': None,
        'type': 'drag',
        'rarity': 20,
        'price': 7500000000000000,
        'tier': 'zink'
    },
    'zink_apple': {
        'name': 'Цинковое яблоко',
        'bonus': 600,
        'color': LIGHT_ZINK,
        'next': None,
        'type': 'apple',
        'rarity': 21,
        'price': 3600000000000,
        'tier': 'zink'
    },
    'zink_roll': {
        'name': 'Цинковый ролл',
        'bonus': 300.0,
        'color': LIGHT_ZINK,
        'next': None,
        'type': 'roll',
        'rarity': 20,
        'price': 1800000000000,
        'tier': 'zink'
    },
    'zink_act': {
        'name': 'Цинковый акт',
        'bonus': 150.0,
        'color': LIGHT_ZINK,
        'next': None,
        'type': 'act',
        'rarity': 20,
        'price': 27000000000000,
        'tier': 'zink'
    },
    'zink_rob': {
        'name': 'Цинковая роба',
        'bonus': 500.0,
        'color': LIGHT_ZINK,
        'next': None,
        'type': 'rob',
        'rarity': 20,
        'price': 27000000000000,
        'tier': 'zink'
    }
}

INVENTORY_LEVELS = {
    'wooden_inver': {
        'name': 'Деревянный инвентарь',
        'cols': 5,
        'rows': 3,
        'cost': 5000,
        'color': (139, 69, 19),
        'next': 'stone_inver',
        'rarity': 1
    },
    'stone_inver': {
        'name': 'Каменный инвентарь',
        'cols': 7,
        'rows': 3,
        'cost': 50000,
        'color': (128, 128, 128),
        'next': 'copper_inver',
        'rarity': 2
    },
    'copper_inver': {
        'name': 'Медный инвентарь',
        'cols': 9,
        'rows': 3,
        'cost': 1000000,
        'color': (184, 115, 51),
        'next': 'iron_inver',
        'rarity': 3
    },
    'iron_inver': {
        'name': 'Железный инвентарь',
        'cols': 9,
        'rows': 4,
        'cost': 25000000,
        'color': (192, 192, 192),
        'next': 'golden_inver',
        'rarity': 4
    },
    'golden_inver': {
        'name': 'Золотой инвентарь',
        'cols': 9,
        'rows': 5,
        'cost': 100000000,
        'color': (255, 215, 0),
        'next': 'emerald_inver',
        'rarity': 5
    },
    'emerald_inver': {
        'name': 'Изумрудный инвентарь',
        'cols': 9,
        'rows': 6,
        'cost': 500000000,
        'color': (80, 200, 80),
        'next': 'diamond_inver',
        'rarity': 6
    },
    'diamond_inver': {
        'name': 'Алмазный инвентарь',
        'cols': 9,
        'rows': 7,
        'cost': 5000000000,
        'color': (0, 255, 255),
        'next': None,
        'rarity': 7
    }
}

SHOP_TABS = ['drag', 'apple', 'roll', 'act', 'rob', 'cross']
SHOP_TAB_NAMES = {
    'drag': 'Драги',
    'apple': 'Яблоки',
    'roll': 'Роллы',
    'act': 'Акты',
    'rob': 'Робы',
    'cross': 'Кресты'
}

def get_rarity_order():
    item_counts = {}
    for item_id, item_data in ITEMS.items():
        tier = item_data.get('tier', 'wooden')
        if tier not in item_counts:
            item_counts[tier] = []
        item_counts[tier].append(item_id)
    
    sorted_items = []
    for tier in TIER_ORDER:
        if tier in item_counts:
            items = item_counts[tier]
            drags = [id for id in items if ITEMS[id]['type'] == 'drag']
            apples = [id for id in items if ITEMS[id]['type'] == 'apple']
            rolls = [id for id in items if ITEMS[id]['type'] == 'roll']
            acts = [id for id in items if ITEMS[id]['type'] == 'act']
            robs = [id for id in items if ITEMS[id]['type'] == 'rob']
            sorted_items.extend(drags + apples + rolls + acts + robs)
    
    case_items = [id for id in CASE_ORDER if id in ITEMS]
    sorted_items.extend(case_items)
    
    return sorted_items

ITEM_ORDER = sorted(ITEMS.keys(), key=lambda x: ITEMS[x].get('price', 0), reverse=True)

INVENTORY_LEVEL_ORDER = ['wooden_inver', 'stone_inver', 'copper_inver', 'iron_inver', 
                         'golden_inver', 'emerald_inver', 'diamond_inver']

ACHIEVEMENTS = {
    'novice': {
        'name': 'Новичок',
        'texture': 'act1',
        'condition': 100,
        'description': 'Заработать 100 монет',
        'color': GOLD
    },
    'expert': {
        'name': 'Знаток',
        'texture': 'act2',
        'condition': 1000,
        'description': 'Заработать 1К монет',
        'color': GOLD
    },
    'businessman': {
        'name': 'Бизнесмен',
        'texture': 'act3',
        'condition': 100000,
        'description': 'Заработать 100К монет',
        'color': GOLD
    },
    'rich': {
        'name': 'Богач',
        'texture': 'act4',
        'condition': 1000000,
        'description': 'Заработать 1М монет',
        'color': GOLD
    },
    'millionaire': {
        'name': 'Миллионер',
        'texture': 'act5',
        'condition': 10000000,
        'description': 'Заработать 10М монет',
        'color': GOLD
    },
    'organization': {
        'name': 'Организация',
        'texture': 'act6',
        'condition': 100000000,
        'description': 'Заработать 100М монет',
        'color': GOLD
    },
    'company': {
        'name': 'Компания',
        'texture': 'act7',
        'condition': 1000000000,
        'description': 'Заработать 1B монет',
        'color': GOLD
    },
    'billionaire': {
        'name': 'Миллиардер',
        'texture': 'act8',
        'condition': 10000000000,
        'description': 'Заработать 10B монет',
        'color': GOLD
    },
    'corporation': {
        'name': 'Корпорация',
        'texture': 'act9',
        'condition': 100000000000,
        'description': 'Заработать 100B монет',
        'color': GOLD
    },
    'elon': {
        'name': 'Илон',
        'texture': 'act10',
        'condition': 1000000000000,
        'description': 'Заработать 1Т монет',
        'color': GOLD
    },
    'trillionaire': {
        'name': 'Триллионер',
        'texture': 'act11',
        'condition': 10000000000000,
        'description': 'Заработать 10Т монет',
        'color': GOLD
    },
    'magnat': {
        'name': 'Магнат',
        'texture': 'act12',
        'condition': 100000000000000,
        'description': 'Заработать 100Т монет',
        'color': GOLD
    },
    'king': {
        'name': 'Король',
        'texture': 'act13',
        'condition': 1000000000000000,
        'description': 'Заработать 1Q монет',
        'color': GOLD
    },
    'imperator': {
        'name': 'Император',
        'texture': 'act14',
        'condition': 10000000000000000,
        'description': 'Заработать 10Q монет',
        'color': GOLD
    }
}

ACHIEVEMENT_ORDER = ['novice', 'expert', 'businessman', 'rich', 'millionaire', 
                     'organization', 'company', 'billionaire', 'corporation', 
                     'elon', 'trillionaire', 'magnat', 'king', 'imperator']
