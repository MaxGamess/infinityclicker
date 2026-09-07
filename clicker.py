import pygame
import json
import os
import math
import sys
import random

pygame.init()

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 700
FPS = 60

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

DATA_FILE = 'data.json'
TEXTURES_DIR = './textures/'

OFFSET_Y = 50
TITLE_OFFSET_Y = 20

CASES = {
    'wooden_case': 0.001,
    'stone_case': 0.0005,
    'copper_case': 0.0003,
    'iron_case': 0.00005,
    'golden_case': 0.00001,
    'emerald_case': 0.0000025,
    'diamond_case': 0.0000005,
    'ruby_case': 0.0000001,
    'netherite_case': 0.000000025,
    'obsidian_case': 0.000000005,
    'magic_case': 0.000000001,
    'sapphire_case': 0.00000000025
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
    'sapphire_case': 'Сапфировый кейс'
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
    }
}

CASE_ORDER = ['wooden_case', 'stone_case', 'copper_case', 'iron_case', 'golden_case', 
              'emerald_case', 'diamond_case', 'ruby_case', 'netherite_case', 
              'obsidian_case', 'magic_case', 'sapphire_case']

TIER_ORDER = ['sapphire', 'magic', 'obsidian', 'netherite', 'ruby', 'diamond', 
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
        'next': None,
        'type': 'drag',
        'rarity': 12,
        'price': 20000000000,
        'tier': 'sapphire'
    },
    'sapphire_apple': {
        'name': 'Сапфировое яблоко',
        'bonus': 50,
        'color': LIGHT_SAPPHIRE,
        'next': None,
        'type': 'apple',
        'rarity': 13,
        'price': 600000000,
        'tier': 'sapphire'
    },
    'sapphire_roll': {
        'name': 'Сапфировый ролл',
        'bonus': 20.0,
        'color': LIGHT_SAPPHIRE,
        'next': None,
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
        'next': None,
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
        'price': 1750000000,
        'tier': 'magic'
    },
    'sapphire_rob': {
        'name': 'Сапфировая роба',
        'bonus': 40.0,
        'color': LIGHT_SAPPHIRE,
        'next': None,
        'type': 'rob',
        'rarity': 12,
        'price': 5000000000,
        'tier': 'sapphire'
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

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {'money': 0, 'multiplier': 0, 'click_count': 0, 'passive_income': 0, 
                    'passive_level': 0, 'inventory': [], 'inventory_level': None, 'active_multiplier': 1.0}
    else:
        return {'money': 0, 'multiplier': 0, 'click_count': 0, 'passive_income': 0, 
                'passive_level': 0, 'inventory': [], 'inventory_level': None, 'active_multiplier': 1.0}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_upgrade_cost(multiplier):
    return math.ceil(multiplier * 100 * (multiplier / 2))

def get_passive_cost(level):
    if level == 0:
        return 100
    return math.ceil(level * 100 * (level / 2))

def format_number(num):
    if num < 1000:
        return str(num)
    elif num < 1000000:
        return f"{num/1000:.2f}K".rstrip('0').rstrip('.')
    elif num < 1000000000:
        return f"{num/1000000:.2f}M".rstrip('0').rstrip('.')
    elif num < 1000000000000:
        return f"{num/1000000000:.2f}B".rstrip('0').rstrip('.')
    elif num < 1000000000000000:
        return f"{num/1000000000000:.2f}T".rstrip('0').rstrip('.')
    elif num < 1000000000000000000:
        return f"{num/1000000000000000:.2f}Q".rstrip('0').rstrip('.')
    elif num < 10**21:
        return f"{num/10**18:.2f}S".rstrip('0').rstrip('.')
    elif num < 10**24:
        return f"{num/10**21:.2f}O".rstrip('0').rstrip('.')
    elif num < 10**27:
        return f"{num/10**24:.2f}N".rstrip('0').rstrip('.')
    elif num < 10**30:
        return f"{num/10**27:.2f}D".rstrip('0').rstrip('.')
    elif num < 10**33:
        return f"{num/10**30:.2f}U".rstrip('0').rstrip('.')
    elif num < 10**36:
        return f"{num/10**33:.2f}T".rstrip('0').rstrip('.')
    elif num < 10**39:
        return f"{num/10**36:.2f}Qt".rstrip('0').rstrip('.')
    elif num < 10**42:
        return f"{num/10**39:.2f}Qn".rstrip('0').rstrip('.')
    elif num < 10**45:
        return f"{num/10**42:.2f}Sx".rstrip('0').rstrip('.')
    elif num < 10**48:
        return f"{num/10**45:.2f}Sp".rstrip('0').rstrip('.')
    elif num < 10**51:
        return f"{num/10**48:.2f}Oc".rstrip('0').rstrip('.')
    elif num < 10**54:
        return f"{num/10**51:.2f}No".rstrip('0').rstrip('.')
    elif num < 10**57:
        return f"{num/10**54:.2f}Dc".rstrip('0').rstrip('.')
    elif num < 10**60:
        return f"{num/10**57:.2f}Ud".rstrip('0').rstrip('.')
    elif num < 10**63:
        return f"{num/10**60:.2f}Td".rstrip('0').rstrip('.')
    elif num < 10**66:
        return f"{num/10**63:.2f}Qad".rstrip('0').rstrip('.')
    elif num < 10**69:
        return f"{num/10**66:.2f}Qid".rstrip('0').rstrip('.')
    elif num < 10**72:
        return f"{num/10**69:.2f}Sxd".rstrip('0').rstrip('.')
    elif num < 10**75:
        return f"{num/10**72:.2f}Spd".rstrip('0').rstrip('.')
    elif num < 10**78:
        return f"{num/10**75:.2f}Ocd".rstrip('0').rstrip('.')
    elif num < 10**81:
        return f"{num/10**78:.2f}Nod".rstrip('0').rstrip('.')
    elif num < 10**84:
        return f"{num/10**81:.2f}Dcd".rstrip('0').rstrip('.')
    elif num < 10**87:
        return f"{num/10**84:.2f}Udd".rstrip('0').rstrip('.')
    elif num < 10**90:
        return f"{num/10**87:.2f}Tdd".rstrip('0').rstrip('.')
    elif num < 10**93:
        return f"{num/10**90:.2f}Qadd".rstrip('0').rstrip('.')
    elif num < 10**96:
        return f"{num/10**93:.2f}Qidd".rstrip('0').rstrip('.')
    elif num < 10**99:
        return f"{num/10**96:.2f}Sxdd".rstrip('0').rstrip('.')
    elif num < 10**100:
        return f"{num/10**99:.2f}Spdd".rstrip('0').rstrip('.')
    else:
        return f"{num/10**99:.2f}Googol".rstrip('0').rstrip('.')

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color=WHITE, border_color=GOLD):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.border_color = border_color
        self.current_color = color
        self.is_hovered = False
        
    def draw(self, surface, font):
        shadow_rect = self.rect.copy()
        shadow_rect.x += 3
        shadow_rect.y += 3
        pygame.draw.rect(surface, (0, 0, 0, 50), shadow_rect, border_radius=12)
        
        pygame.draw.rect(surface, self.current_color, self.rect, border_radius=12)
        pygame.draw.rect(surface, self.border_color, self.rect, 2, border_radius=12)
        
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
            self.current_color = self.hover_color if self.is_hovered else self.color
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered:
                if event.button == 1:
                    return 'click'
        return None

class ShopItem:
    def __init__(self, x, y, size, item_id):
        self.rect = pygame.Rect(x, y, size, size)
        self.size = size
        self.item_id = item_id
        self.is_hovered = False
        
    def draw(self, surface, font_tiny, font_mini, texture):
        shadow_rect = self.rect.copy()
        shadow_rect.x += 2
        shadow_rect.y += 2
        pygame.draw.rect(surface, (0, 0, 0, 80), shadow_rect, border_radius=10)
        
        if self.is_hovered:
            pygame.draw.rect(surface, (80, 80, 80), self.rect, border_radius=10)
            pygame.draw.rect(surface, GOLD, self.rect, 3, border_radius=10)
        else:
            pygame.draw.rect(surface, (40, 40, 40), self.rect, border_radius=10)
            pygame.draw.rect(surface, GRAY, self.rect, 2, border_radius=10)
        
        if texture:
            tex_rect = texture.get_rect(center=(self.rect.centerx, self.rect.centery - 8))
            surface.blit(texture, tex_rect)
        
        if self.item_id in CROSS_ITEMS:
            price = CROSS_ITEMS[self.item_id]['price']
        else:
            price = ITEMS[self.item_id]['price']
        price_text = font_mini.render(format_number(price), True, GOLD)
        price_rect = price_text.get_rect(center=(self.rect.centerx, self.rect.bottom - 8))
        surface.blit(price_text, price_rect)
        
    def draw_tooltip(self, surface, font_tiny, font_mini, mouse_pos):
        if not self.is_hovered:
            return
        
        if self.item_id in CROSS_ITEMS:
            cross_data = CROSS_ITEMS[self.item_id]
            tooltip_width = 160
            tooltip_height = 35
            tooltip_x = mouse_pos[0] - tooltip_width // 2
            tooltip_y = mouse_pos[1] + 15
            
            if tooltip_y + tooltip_height > WINDOW_HEIGHT - 50:
                tooltip_y = mouse_pos[1] - tooltip_height - 15
            
            if tooltip_x < 5:
                tooltip_x = 5
            elif tooltip_x + tooltip_width > WINDOW_WIDTH - 5:
                tooltip_x = WINDOW_WIDTH - tooltip_width - 5
            
            tooltip_rect = pygame.Rect(tooltip_x, tooltip_y, tooltip_width, tooltip_height)
            pygame.draw.rect(surface, (20, 20, 20, 230), tooltip_rect, border_radius=8)
            pygame.draw.rect(surface, GOLD, tooltip_rect, 1, border_radius=8)
            
            name_text = font_tiny.render(cross_data['name'], True, cross_data['color'])
            name_rect = name_text.get_rect(center=(tooltip_rect.centerx, tooltip_rect.centery))
            surface.blit(name_text, name_rect)
            return
        
        item_data = ITEMS[self.item_id]
        item_type = item_data['type']
        bonus = item_data['bonus']
        
        tooltip_width = 180
        tooltip_height = 50
        tooltip_x = mouse_pos[0] - tooltip_width // 2
        tooltip_y = mouse_pos[1] + 15
        
        if tooltip_y + tooltip_height > WINDOW_HEIGHT - 50:
            tooltip_y = mouse_pos[1] - tooltip_height - 15
        
        if tooltip_x < 5:
            tooltip_x = 5
        elif tooltip_x + tooltip_width > WINDOW_WIDTH - 5:
            tooltip_x = WINDOW_WIDTH - tooltip_width - 5
        
        tooltip_rect = pygame.Rect(tooltip_x, tooltip_y, tooltip_width, tooltip_height)
        pygame.draw.rect(surface, (20, 20, 20, 230), tooltip_rect, border_radius=8)
        pygame.draw.rect(surface, GOLD, tooltip_rect, 1, border_radius=8)
        
        name_text = font_tiny.render(item_data['name'], True, item_data['color'])
        name_rect = name_text.get_rect(center=(tooltip_rect.centerx, tooltip_rect.y + 12))
        surface.blit(name_text, name_rect)
        
        if item_type == 'drag':
            bonus_text = f"+{bonus} за клик"
        elif item_type == 'apple':
            bonus_text = f"+{bonus} в сек"
        elif item_type == 'roll':
            bonus_text = f"x{bonus} скорость пассива"
        elif item_type == 'act':
            bonus_text = f"x{bonus} активный доход"
        elif item_type == 'rob':
            bonus_text = f"x{bonus} шанс кейсов"
        else:
            bonus_text = f"+{bonus}"
        
        bonus_color = GOLD if item_type == 'drag' else (GREEN if item_type == 'apple' else (BLUE if item_type == 'roll' else (PURPLE if item_type == 'act' else ORANGE)))
        bonus_text_surf = font_mini.render(bonus_text, True, bonus_color)
        bonus_rect = bonus_text_surf.get_rect(center=(tooltip_rect.centerx, tooltip_rect.y + 32))
        surface.blit(bonus_text_surf, bonus_rect)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered and event.button == 1:
                return 'click'
        return None

class InventorySlot:
    def __init__(self, x, y, size=50):
        self.rect = pygame.Rect(x, y, size, size)
        self.size = size
        self.item = None
        self.is_hovered = False
        self.texture = None
        
    def draw(self, surface, font):
        pygame.draw.rect(surface, DARK_GRAY, self.rect, border_radius=5)
        pygame.draw.rect(surface, GRAY, self.rect, 2, border_radius=5)
        
        if self.item:
            if self.texture:
                tex_rect = self.texture.get_rect(center=self.rect.center)
                surface.blit(self.texture, tex_rect)
            
            if self.is_hovered:
                pygame.draw.rect(surface, (255, 255, 255, 50), self.rect, 3, border_radius=5)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered and event.button == 1:
                return 'click'
        return None

class CraftButton:
    def __init__(self, x, y, size):
        self.rect = pygame.Rect(x, y, size, size)
        self.is_hovered = False
        
    def draw(self, surface, font):
        shadow_rect = self.rect.copy()
        shadow_rect.x += 2
        shadow_rect.y += 2
        pygame.draw.rect(surface, (0, 0, 0, 50), shadow_rect, border_radius=8)
        
        if self.is_hovered:
            pygame.draw.rect(surface, DARK_GRAY, self.rect, border_radius=8)
        else:
            pygame.draw.rect(surface, DARK_GRAY, self.rect, border_radius=8)
        
        if self.is_hovered:
            pygame.draw.rect(surface, GOLD, self.rect, 2, border_radius=8)
        else:
            pygame.draw.rect(surface, GRAY, self.rect, 2, border_radius=8)
        
        text_surface = font.render("=", True, GRAY)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered and event.button == 1:
                return 'click'
        return None

class TabButton:
    def __init__(self, x, y, width, height, text, tab_id):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.tab_id = tab_id
        self.is_hovered = False
        self.is_active = False
        
    def draw(self, surface, font):
        shadow_rect = self.rect.copy()
        shadow_rect.x += 2
        shadow_rect.y += 2
        pygame.draw.rect(surface, (0, 0, 0, 50), shadow_rect, border_radius=8)
        
        if self.is_active:
            pygame.draw.rect(surface, GOLD, self.rect, border_radius=8)
            pygame.draw.rect(surface, DARK_GOLD, self.rect, 2, border_radius=8)
            text_color = BLACK
        else:
            if self.is_hovered:
                pygame.draw.rect(surface, (80, 80, 80), self.rect, border_radius=8)
            else:
                pygame.draw.rect(surface, BLACK, self.rect, border_radius=8)
            pygame.draw.rect(surface, GOLD, self.rect, 2, border_radius=8)
            text_color = WHITE
        
        text_surface = font.render(self.text, True, text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered and event.button == 1:
                return 'click'
        return None

class ShopTabButton:
    def __init__(self, x, y, width, height, text, tab_id):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.tab_id = tab_id
        self.is_hovered = False
        self.is_active = False
        
    def draw(self, surface, font):
        if self.is_active:
            pygame.draw.rect(surface, GOLD, self.rect, border_radius=6)
            pygame.draw.rect(surface, DARK_GOLD, self.rect, 2, border_radius=6)
            text_color = BLACK
        else:
            if self.is_hovered:
                pygame.draw.rect(surface, (80, 80, 80), self.rect, border_radius=6)
            else:
                pygame.draw.rect(surface, (30, 30, 30), self.rect, border_radius=6)
            pygame.draw.rect(surface, GRAY, self.rect, 1, border_radius=6)
            text_color = WHITE
        
        text_surface = font.render(self.text, True, text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered and event.button == 1:
                return 'click'
        return None

class InventoryUpgradeButton:
    def __init__(self, x, y, size):
        self.rect = pygame.Rect(x, y, size, size)
        self.is_hovered = False
        self.level_id = None
        
    def draw(self, surface, font_tiny, texture):
        shadow_rect = self.rect.copy()
        shadow_rect.x += 2
        shadow_rect.y += 2
        pygame.draw.rect(surface, (0, 0, 0, 80), shadow_rect, border_radius=10)
        
        if self.is_hovered:
            pygame.draw.rect(surface, (80, 80, 80), self.rect, border_radius=10)
            pygame.draw.rect(surface, GOLD, self.rect, 3, border_radius=10)
        else:
            pygame.draw.rect(surface, (40, 40, 40), self.rect, border_radius=10)
            pygame.draw.rect(surface, GRAY, self.rect, 2, border_radius=10)
        
        if texture:
            tex_rect = texture.get_rect(center=(self.rect.centerx, self.rect.centery - 5))
            surface.blit(texture, tex_rect)
        
        if self.level_id and self.level_id in INVENTORY_LEVELS:
            price = INVENTORY_LEVELS[self.level_id]['cost']
            price_text = font_tiny.render(format_number(price), True, GOLD)
            price_rect = price_text.get_rect(center=(self.rect.centerx, self.rect.bottom - 10))
            surface.blit(price_text, price_rect)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered and event.button == 1:
                return 'click'
        return None

class ClickerGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Вечный Кликер")
        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.Font(None, 52)
        self.font_medium = pygame.font.Font(None, 38)
        self.font_small = pygame.font.Font(None, 28)
        self.font_tiny = pygame.font.Font(None, 22)
        self.font_mini = pygame.font.Font(None, 16)
        
        self.data = load_data()
        self.money = self.data['money']
        self.multiplier = self.data['multiplier']
        self.click_count = self.data['click_count']
        self.passive_income = self.data['passive_income']
        self.passive_level = self.data['passive_level']
        self.inventory = self.data.get('inventory', [])
        self.inventory_level = self.data.get('inventory_level', None)
        self.active_multiplier = self.data.get('active_multiplier', 1.0)
        
        self.textures = {}
        self.load_textures()
        
        self.floating_texts = []
        self.passive_timer = 0
        self.current_tab = 'main'
        self.shop_subtab = 'drag'
        self.inventory_slots = []
        self.craft_slots = []
        self.dragging_item = None
        self.drag_source = None
        self.drag_offset = (0, 0)
        self.shop_items = []
        self.hovered_inventory_slot = None
        self.passive_speed_multiplier = 1.0
        self.hovered_item_info = None
        self.active_click_multiplier = 1.0
        self.case_chance_multiplier = 1.0
        
        if self.inventory_level is None or self.inventory_level not in INVENTORY_LEVELS:
            self.inventory_level = None
        
        self.create_buttons()
        self.create_inventory_slots()
        self.create_shop()
        
        self.data_changed = False
        self.apply_item_bonuses()
        
    def get_inventory_size(self):
        if self.inventory_level and self.inventory_level in INVENTORY_LEVELS:
            level_data = INVENTORY_LEVELS[self.inventory_level]
            return level_data['cols'], level_data['rows']
        return 3, 3
    
    def get_inventory_slot_count(self):
        cols, rows = self.get_inventory_size()
        return cols * rows
    
    def get_next_level(self):
        if self.inventory_level is None:
            return 'wooden_inver'
        if self.inventory_level in INVENTORY_LEVELS:
            return INVENTORY_LEVELS[self.inventory_level].get('next')
        return None
        
    def sort_inventory_by_rarity(self):
        item_counts = {}
        for item_id in self.inventory:
            if item_id not in item_counts:
                item_counts[item_id] = 0
            item_counts[item_id] += 1
        
        def get_tier(item_id):
            if item_id in ITEMS:
                return ITEMS[item_id].get('tier', 'wooden')
            elif item_id in CASES:
                tier = item_id.replace('_case', '')
                return tier
            elif item_id in CROSS_ITEMS:
                return CROSS_ITEMS[item_id]['tier']
            return 'wooden'
        
        def get_tier_order(tier):
            return TIER_ORDER.index(tier) if tier in TIER_ORDER else len(TIER_ORDER)
        
        sorted_ids = sorted(item_counts.keys(), key=lambda x: (get_tier_order(get_tier(x)), -(CROSS_ITEMS[x]['price'] if x in CROSS_ITEMS else (ITEMS[x]['price'] if x in ITEMS else 0))))
        
        new_inventory = []
        for item_id in sorted_ids:
            if item_id in item_counts:
                new_inventory.extend([item_id] * item_counts[item_id])
        
        self.inventory = new_inventory
        self.data_changed = True
        
    def load_textures(self):
        all_items = list(ITEMS.keys()) + list(CASES.keys()) + list(CROSS_ITEMS.keys())
        for item_id in all_items:
            path = os.path.join(TEXTURES_DIR, f"{item_id}.png")
            if os.path.exists(path):
                try:
                    tex = pygame.image.load(path).convert_alpha()
                    tex = pygame.transform.scale(tex, (40, 40))
                    self.textures[item_id] = tex
                except:
                    self.textures[item_id] = None
            else:
                self.textures[item_id] = None
                
        for level_id in INVENTORY_LEVELS.keys():
            path = os.path.join(TEXTURES_DIR, f"{level_id}.png")
            if os.path.exists(path):
                try:
                    tex = pygame.image.load(path).convert_alpha()
                    tex = pygame.transform.scale(tex, (40, 40))
                    self.textures[level_id] = tex
                except:
                    self.textures[level_id] = None
            else:
                self.textures[level_id] = None
                
    def create_buttons(self):
        self.click_button = Button(
            WINDOW_WIDTH//2 - 100,
            200 + OFFSET_Y,
            200,
            200,
            "КЛИК",
            DARK_BROWN,
            BROWN,
            WHITE,
            GOLD
        )
        
        self.passive_button = Button(
            WINDOW_WIDTH//2 - 100,
            520 + OFFSET_Y,
            200,
            50,
            "",
            GOLD,
            LIGHT_GOLD,
            BLACK,
            DARK_GOLD
        )
        
        self.inv_upgrade_button = InventoryUpgradeButton(
            10,
            70 + OFFSET_Y,
            60
        )
        next_level = self.get_next_level()
        if next_level:
            self.inv_upgrade_button.level_id = next_level
        
        self.main_tab_button = TabButton(
            10,
            WINDOW_HEIGHT - 45,
            80,
            35,
            "Главная",
            'main'
        )
        
        self.inventory_tab_button = TabButton(
            95,
            WINDOW_HEIGHT - 45,
            80,
            35,
            "Инвентарь",
            'inventory'
        )
        
        self.shop_tab_button = TabButton(
            180,
            WINDOW_HEIGHT - 45,
            80,
            35,
            "Магазин",
            'shop'
        )
        
    def create_shop(self):
        self.shop_items = []
        self.shop_sub_buttons = []
        
        tab_width = 65
        tab_height = 25
        total_width = len(SHOP_TABS) * tab_width + (len(SHOP_TABS) - 1) * 5
        start_x = (WINDOW_WIDTH - total_width) // 2
        start_y = 110 + OFFSET_Y
        
        for i, tab_id in enumerate(SHOP_TABS):
            x = start_x + i * (tab_width + 5)
            btn = ShopTabButton(x, start_y, tab_width, tab_height, SHOP_TAB_NAMES[tab_id], tab_id)
            if tab_id == self.shop_subtab:
                btn.is_active = True
            self.shop_sub_buttons.append(btn)
        
        item_size = 60
        spacing = 8
        cols = 7
        total_width = cols * item_size + (cols - 1) * spacing
        start_x = (WINDOW_WIDTH - total_width) // 2
        start_y = start_y + tab_height + 15
        
        item_ids = []
        
        if self.shop_subtab == 'cross':
            for cross_id, cross_data in CROSS_ITEMS.items():
                item_ids.append(cross_id)
            item_ids.sort(key=lambda x: CROSS_ITEMS[x]['price'])
        else:
            for item_id, item_data in ITEMS.items():
                if 'price' in item_data and item_data['price'] > 0:
                    if item_data['type'] == self.shop_subtab:
                        item_ids.append(item_id)
            item_ids.sort(key=lambda x: ITEMS[x]['price'])
        
        for i, item_id in enumerate(item_ids):
            row = i // cols
            col = i % cols
            x = start_x + col * (item_size + spacing)
            y = start_y + row * (item_size + spacing)
            shop_item = ShopItem(x, y, item_size, item_id)
            self.shop_items.append(shop_item)
        
    def create_inventory_slots(self):
        slot_size = 48
        spacing = 6
        
        self.inventory_slots = []
        total_craft_width = 5 * slot_size + 4 * spacing
        start_x = (WINDOW_WIDTH - total_craft_width - slot_size - spacing) // 2
        
        for i in range(5):
            x = start_x + i * (slot_size + spacing)
            y = 520 + OFFSET_Y
            slot = InventorySlot(x, y, slot_size)
            self.inventory_slots.append(slot)
        
        craft_button_x = start_x + 5 * (slot_size + spacing)
        self.craft_button = CraftButton(craft_button_x, 520 + OFFSET_Y, slot_size)
        
        self.inv_grid_slots = []
        cols, rows = self.get_inventory_size()
        total_width = cols * slot_size + (cols - 1) * spacing
        start_x = (WINDOW_WIDTH - total_width) // 2
        start_y = 120 + OFFSET_Y
        
        for row in range(rows):
            for col in range(cols):
                x = start_x + col * (slot_size + spacing)
                y = start_y + row * (slot_size + spacing)
                slot = InventorySlot(x, y, slot_size)
                self.inv_grid_slots.append(slot)
        
        self.update_inventory_slots()
        
    def update_inventory_slots(self):
        self.sort_inventory_by_rarity()
        
        for slot in self.inv_grid_slots:
            slot.item = None
            slot.texture = None
        
        max_slots = len(self.inv_grid_slots)
        if len(self.inventory) > max_slots:
            self.add_floating_text(
                WINDOW_WIDTH//2,
                200 + OFFSET_Y,
                "Инвентарь переполнен!",
                RED
            )
        
        for i, item_id in enumerate(self.inventory[:max_slots]):
            if i < len(self.inv_grid_slots):
                self.inv_grid_slots[i].item = item_id
                self.inv_grid_slots[i].texture = self.textures.get(item_id)
        
        for slot in self.inventory_slots:
            if slot.item:
                slot.texture = self.textures.get(slot.item)
    
    def get_all_slots(self):
        return self.inv_grid_slots + self.inventory_slots
    
    def sync_inventory_from_slots(self):
        new_inventory = []
        for slot in self.inv_grid_slots:
            if slot.item is not None:
                new_inventory.append(slot.item)
        self.inventory = new_inventory
        self.data_changed = True
        
    def update_hovered_item(self):
        mouse_pos = pygame.mouse.get_pos()
        self.hovered_item_info = None
        self.hovered_inventory_slot = None
        
        if self.current_tab == 'inventory':
            for slot in self.inv_grid_slots:
                if slot.rect.collidepoint(mouse_pos) and slot.item is not None:
                    self.hovered_inventory_slot = slot
                    self.hovered_item_info = (slot.item, slot.rect)
                    return
            
            for slot in self.inventory_slots:
                if slot.rect.collidepoint(mouse_pos) and slot.item is not None:
                    self.hovered_inventory_slot = slot
                    self.hovered_item_info = (slot.item, slot.rect)
                    return
    
    def upgrade_inventory(self):
        next_level = self.get_next_level()
        
        if next_level is None:
            self.add_floating_text(
                WINDOW_WIDTH//2,
                120 + OFFSET_Y,
                "Максимальный уровень!",
                RED
            )
            return False
        
        cost = INVENTORY_LEVELS[next_level]['cost']
        if self.money >= cost:
            self.money -= cost
            self.inventory_level = next_level
            self.data_changed = True
            
            self.create_inventory_slots()
            
            next_level_after = self.get_next_level()
            if next_level_after:
                self.inv_upgrade_button.level_id = next_level_after
            else:
                self.inv_upgrade_button.level_id = None
            
            self.add_floating_text(
                WINDOW_WIDTH//2,
                120 + OFFSET_Y,
                f"Инвентарь улучшен!",
                GREEN
            )
            return True
        else:
            self.add_floating_text(
                WINDOW_WIDTH//2,
                120 + OFFSET_Y,
                f"Нужно: {format_number(cost)}",
                RED
            )
            return False
    
    def buy_item(self, item_id):
        if item_id in CROSS_ITEMS:
            price = CROSS_ITEMS[item_id]['price']
            if self.money >= price:
                self.money -= price
                if not self.add_item_to_inventory(item_id):
                    self.money += price
                    self.add_floating_text(
                        WINDOW_WIDTH//2,
                        300 + OFFSET_Y,
                        "Инвентарь полон!",
                        RED
                    )
                    return False
                self.data_changed = True
                self.update_inventory_slots()
                self.add_floating_text(
                    WINDOW_WIDTH//2,
                    300 + OFFSET_Y,
                    f"Куплен {CROSS_ITEMS[item_id]['name']}!",
                    GREEN
                )
                return True
            else:
                self.add_floating_text(
                    WINDOW_WIDTH//2,
                    300 + OFFSET_Y,
                    f"Недостаточно монет! Нужно: {format_number(price)}",
                    RED
                )
                return False
        elif item_id in ITEMS:
            price = ITEMS[item_id]['price']
            if self.money >= price:
                self.money -= price
                if not self.add_item_to_inventory(item_id):
                    self.money += price
                    self.add_floating_text(
                        WINDOW_WIDTH//2,
                        300 + OFFSET_Y,
                        "Инвентарь полон!",
                        RED
                    )
                    return False
                self.data_changed = True
                self.apply_item_bonuses()
                self.update_inventory_slots()
                self.add_floating_text(
                    WINDOW_WIDTH//2,
                    300 + OFFSET_Y,
                    f"Куплен {ITEMS[item_id]['name']}!",
                    GREEN
                )
                return True
            else:
                self.add_floating_text(
                    WINDOW_WIDTH//2,
                    300 + OFFSET_Y,
                    f"Недостаточно монет! Нужно: {format_number(price)}",
                    RED
                )
                return False
        return False
    
    def add_item_to_inventory(self, item_id):
        if len(self.inventory) < len(self.inv_grid_slots):
            self.inventory.append(item_id)
            return True
        return False
        
    def craft_items(self):
        items_in_slots = {}
        craft_slots_with_items = []
        
        for slot in self.inventory_slots:
            if slot.item is not None:
                if slot.item in CROSS_ITEMS:
                    self.add_floating_text(
                        WINDOW_WIDTH//2,
                        570 + OFFSET_Y,
                        "Кресты нельзя совмещать!",
                        RED
                    )
                    return False
                if slot.item not in items_in_slots:
                    items_in_slots[slot.item] = 0
                items_in_slots[slot.item] += 1
                craft_slots_with_items.append(slot)
        
        if not items_in_slots:
            self.add_floating_text(
                WINDOW_WIDTH//2,
                570 + OFFSET_Y,
                "Нет предметов для совмещения!",
                RED
            )
            return False
        
        crafted = False
        for item_id, count in items_in_slots.items():
            if item_id in CROSS_ITEMS:
                continue
                
            if item_id in CASES:
                required_count = 5
            elif item_id in ITEMS:
                item_type = ITEMS[item_id]['type']
                if item_type == 'roll' or item_type == 'act' or item_type == 'rob':
                    required_count = 3
                else:
                    required_count = 5 if item_type == 'drag' else 3
            else:
                continue
            
            next_item = None
            if item_id in CASES:
                case_index = CASE_ORDER.index(item_id)
                if case_index < len(CASE_ORDER) - 1:
                    next_item = CASE_ORDER[case_index + 1]
            elif item_id in ITEMS and ITEMS[item_id]['next'] is not None:
                next_item = ITEMS[item_id]['next']
            
            if count >= required_count and next_item is not None:
                removed = 0
                for slot in self.inventory_slots:
                    if slot.item == item_id:
                        slot.item = None
                        slot.texture = None
                        removed += 1
                        if removed >= required_count:
                            break
                
                if len(self.inventory) >= len(self.inv_grid_slots):
                    self.add_floating_text(
                        WINDOW_WIDTH//2,
                        570 + OFFSET_Y,
                        "Инвентарь полон!",
                        RED
                    )
                    return False
                
                self.inventory.append(next_item)
                
                self.data_changed = True
                self.update_inventory_slots()
                self.apply_item_bonuses()
                
                if next_item in ITEMS:
                    name = ITEMS[next_item]['name']
                else:
                    name = CASE_NAMES.get(next_item, next_item.replace('_', ' ').title())
                
                self.add_floating_text(
                    WINDOW_WIDTH//2,
                    570 + OFFSET_Y,
                    f"Совмещено! +{name}",
                    GREEN
                )
                crafted = True
                break
        
        if not crafted:
            max_count = max(items_in_slots.values()) if items_in_slots else 0
            if max_count < 3:
                self.add_floating_text(
                    WINDOW_WIDTH//2,
                    570 + OFFSET_Y,
                    f"Нужно 3 одинаковых!",
                    RED
                )
            else:
                for item_id, count in items_in_slots.items():
                    if item_id in CROSS_ITEMS:
                        continue
                    next_item = None
                    if item_id in CASES:
                        case_index = CASE_ORDER.index(item_id)
                        if case_index < len(CASE_ORDER) - 1:
                            next_item = CASE_ORDER[case_index + 1]
                    elif item_id in ITEMS:
                        next_item = ITEMS[item_id].get('next')
                    
                    if count >= 3 and next_item is None:
                        if item_id in ITEMS:
                            name = ITEMS[item_id]['name']
                        else:
                            name = CASE_NAMES.get(item_id, item_id.replace('_', ' ').title())
                        self.add_floating_text(
                            WINDOW_WIDTH//2,
                            570 + OFFSET_Y,
                            f"{name} нельзя улучшить!",
                            RED
                        )
                        break
        
        return crafted
        
    def apply_item_bonuses(self):
        total_bonus = 0
        total_passive = 0
        roll_multiplier = 1.0
        active_multiplier = 1.0
        case_multiplier = 1.0
        
        act_bonuses = []
        rob_bonuses = []
        
        for item_id in self.inventory:
            if item_id in ITEMS:
                if ITEMS[item_id]['type'] == 'drag':
                    total_bonus += ITEMS[item_id]['bonus']
                elif ITEMS[item_id]['type'] == 'apple':
                    total_passive += ITEMS[item_id]['bonus']
                elif ITEMS[item_id]['type'] == 'roll':
                    roll_multiplier *= ITEMS[item_id]['bonus']
                elif ITEMS[item_id]['type'] == 'act':
                    act_bonuses.append(ITEMS[item_id]['bonus'])
                elif ITEMS[item_id]['type'] == 'rob':
                    rob_bonuses.append(ITEMS[item_id]['bonus'])
        
        act_bonuses.sort(reverse=True)
        top_acts = act_bonuses[:5]
        for bonus in top_acts:
            active_multiplier += bonus
        
        rob_bonuses.sort(reverse=True)
        top_robs = rob_bonuses[:5]
        for bonus in top_robs:
            case_multiplier += bonus
        
        self.item_bonus = total_bonus
        self.item_passive_bonus = total_passive
        self.passive_speed_multiplier = roll_multiplier
        self.active_click_multiplier = active_multiplier
        self.case_chance_multiplier = case_multiplier
        self.data_changed = True
        
    def find_nearest_empty_slot(self, mouse_pos):
        all_slots = self.get_all_slots()
        nearest_slot = None
        min_dist = float('inf')
        
        for slot in all_slots:
            if slot.item is None:
                if slot != self.drag_source:
                    dist = math.sqrt((slot.rect.centerx - mouse_pos[0])**2 + (slot.rect.centery - mouse_pos[1])**2)
                    if dist < min_dist:
                        min_dist = dist
                        nearest_slot = slot
        
        return nearest_slot
    
    def get_slot_index(self, slot):
        all_slots = self.get_all_slots()
        for i, s in enumerate(all_slots):
            if s is slot:
                return i
        return -1
        
    def handle_drop(self, mouse_pos):
        if self.dragging_item is None:
            return
        
        all_slots = self.get_all_slots()
        target_slot = None
        
        for slot in all_slots:
            if slot.rect.collidepoint(mouse_pos) and slot != self.drag_source:
                target_slot = slot
                break
        
        if target_slot:
            if target_slot.item is not None:
                old_item = target_slot.item
                old_texture = target_slot.texture
                
                target_slot.item = self.dragging_item
                target_slot.texture = self.textures.get(self.dragging_item)
                
                if self.drag_source:
                    self.drag_source.item = old_item
                    self.drag_source.texture = old_texture
                else:
                    self.inventory.append(old_item)
            else:
                target_slot.item = self.dragging_item
                target_slot.texture = self.textures.get(self.dragging_item)
                
                if self.drag_source:
                    self.drag_source.item = None
                    self.drag_source.texture = None
        else:
            if self.drag_source:
                self.drag_source.item = self.dragging_item
                self.drag_source.texture = self.textures.get(self.dragging_item)
            else:
                self.inventory.append(self.dragging_item)
        
        self.sync_inventory_from_slots()
        self.update_inventory_slots()
        self.apply_item_bonuses()
        
        self.dragging_item = None
        self.drag_source = None
        
    def add_floating_text(self, x, y, text, color=GOLD):
        self.floating_texts.append({
            'x': x,
            'y': y,
            'text': text,
            'color': color,
            'alpha': 255,
            'life': 60
        })
        
        if len(self.floating_texts) > 20:
            self.floating_texts.pop(0)
        
    def update_floating_texts(self):
        for text in self.floating_texts[:]:
            text['y'] -= 2
            text['alpha'] -= 4
            text['life'] -= 1
            if text['life'] <= 0 or text['alpha'] <= 0:
                self.floating_texts.remove(text)
                
    def draw_floating_texts(self):
        for text in self.floating_texts:
            font = pygame.font.Font(None, 36)
            surf = font.render(text['text'], True, text['color'])
            surf.set_alpha(max(0, text['alpha']))
            self.screen.blit(surf, (text['x'] - surf.get_width()//2, text['y']))
            
    def handle_click(self):
        base_earnings = 1 + self.multiplier + getattr(self, 'item_bonus', 0)
        earnings = int(base_earnings * getattr(self, 'active_click_multiplier', 1.0))
        self.money += earnings
        self.click_count += 1
        self.data_changed = True
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.add_floating_text(mouse_x, mouse_y - 30, f"+{format_number(earnings)}")
        
        self.try_drop_item()
        
    def try_drop_item(self):
        case_multiplier = getattr(self, 'case_chance_multiplier', 1.0)
        roll = random.random() * 100
        
        has_crosses = {}
        for item_id in self.inventory:
            if item_id in CROSS_ITEMS:
                tier = CROSS_ITEMS[item_id]['tier']
                has_crosses[tier] = True
        
        for case_id in reversed(CASE_ORDER):
            case_tier = case_id.replace('_case', '')
            
            if has_crosses.get(case_tier, False):
                continue
                
            chance = CASES[case_id] * 100 * case_multiplier
            if roll < chance:
                if len(self.inventory) >= len(self.inv_grid_slots):
                    price = 100
                    self.money += price
                    self.data_changed = True
                    self.add_floating_text(
                        WINDOW_WIDTH//2,
                        300 + OFFSET_Y,
                        f"+{format_number(price)}",
                        GOLD
                    )
                    return
                
                self.inventory.append(case_id)
                self.data_changed = True
                self.apply_item_bonuses()
                self.update_inventory_slots()
                self.add_floating_text(
                    WINDOW_WIDTH//2,
                    300 + OFFSET_Y,
                    f"Выпал {CASE_NAMES[case_id]}!",
                    CASE_CONTENTS[case_id]['color']
                )
                return
        
    def open_case(self, case_id):
        if case_id not in CASE_CONTENTS:
            return
        
        if len(self.inventory) >= len(self.inv_grid_slots):
            self.add_floating_text(
                WINDOW_WIDTH//2,
                300 + OFFSET_Y,
                "Инвентарь полон!",
                RED
            )
            return
        
        case_index = -1
        for i, item in enumerate(self.inventory):
            if item == case_id:
                case_index = i
                break
        
        if case_index == -1:
            return
        
        contents = CASE_CONTENTS[case_id]
        roll = random.random()
        
        if roll < contents['apple_chance']:
            item_id = 'apple'
        else:
            item_id = random.choice(contents['items'])
        
        del self.inventory[case_index]
        
        if len(self.inventory) < len(self.inv_grid_slots):
            self.inventory.append(item_id)
            self.data_changed = True
            self.apply_item_bonuses()
            self.update_inventory_slots()
            
            if item_id in ITEMS:
                self.add_floating_text(
                    WINDOW_WIDTH//2,
                    300 + OFFSET_Y,
                    f"Из кейса выпал {ITEMS[item_id]['name']}!",
                    ITEMS[item_id]['color']
                )
            else:
                self.add_floating_text(
                    WINDOW_WIDTH//2,
                    300 + OFFSET_Y,
                    f"Из кейса выпал {item_id.replace('_', ' ').title()}!",
                    ORANGE
                )
        else:
            if item_id in ITEMS:
                price = ITEMS[item_id]['price'] // 2
                self.money += price
                self.data_changed = True
                self.add_floating_text(
                    WINDOW_WIDTH//2,
                    300 + OFFSET_Y,
                    f"Инвентарь полон! Продано за {format_number(price)}",
                    GOLD
                )
            else:
                self.add_floating_text(
                    WINDOW_WIDTH//2,
                    300 + OFFSET_Y,
                    "Инвентарь полон!",
                    RED
                )
            self.update_inventory_slots()
        
    def handle_upgrade(self):
        next_level = self.multiplier + 1
        cost = get_upgrade_cost(next_level)
        
        if self.money >= cost:
            self.money -= cost
            self.multiplier += 1
            self.data_changed = True
            self.add_floating_text(
                WINDOW_WIDTH//2,
                150 + OFFSET_Y,
                f"Улучшено! +{format_number(1 + self.multiplier + getattr(self, 'item_bonus', 0))}",
                GREEN
            )
            return True
        else:
            self.add_floating_text(
                WINDOW_WIDTH//2,
                150 + OFFSET_Y,
                f"Нужно: {format_number(cost)}",
                RED
            )
            return False
    
    def handle_passive_purchase(self):
        cost = get_passive_cost(self.passive_level)
        
        if self.money >= cost:
            self.money -= cost
            self.passive_level += 1
            self.passive_income += 1
            self.data_changed = True
            self.add_floating_text(
                WINDOW_WIDTH//2,
                500 + OFFSET_Y,
                f"Доход +1/сек!",
                GREEN
            )
            return True
        else:
            self.add_floating_text(
                WINDOW_WIDTH//2,
                500 + OFFSET_Y,
                f"Нужно: {format_number(cost)}",
                RED
            )
            return False
            
    def update_passive_income(self):
        total_income = self.passive_income + getattr(self, 'item_passive_bonus', 0)
        if total_income > 0:
            self.passive_timer += 1
            speed_multiplier = getattr(self, 'passive_speed_multiplier', 1.0)
            required_ticks = max(1, int(FPS / speed_multiplier))
            
            if self.passive_timer >= required_ticks:
                self.money += total_income
                self.passive_timer = 0
                self.data_changed = True
                if self.current_tab == 'main':
                    self.add_floating_text(
                        WINDOW_WIDTH//2,
                        200 + OFFSET_Y,
                        f"+{format_number(total_income)}",
                        GOLD
                    )
            
    def save_game(self):
        if self.data_changed:
            self.data = {
                'money': self.money,
                'multiplier': self.multiplier,
                'click_count': self.click_count,
                'passive_income': self.passive_income,
                'passive_level': self.passive_level,
                'inventory': self.inventory,
                'inventory_level': self.inventory_level,
                'active_multiplier': self.active_click_multiplier
            }
            save_data(self.data)
            self.data_changed = False
            
    def draw_stats(self):
        money_str = format_number(self.money)
        money_text = self.font_large.render(money_str, True, GOLD)
        money_rect = money_text.get_rect(center=(WINDOW_WIDTH//2, 75 + OFFSET_Y))
        self.screen.blit(money_text, money_rect)
        
        label = self.font_tiny.render("БАЛАНС", True, (180, 180, 180))
        label_rect = label.get_rect(center=(WINDOW_WIDTH//2, 45 + OFFSET_Y))
        self.screen.blit(label, label_rect)
        
        click_info = self.font_small.render(f"Кликов: {format_number(self.click_count)}", True, (200, 200, 200))
        click_rect = click_info.get_rect(center=(WINDOW_WIDTH//2, 115 + OFFSET_Y))
        self.screen.blit(click_info, click_rect)
        
        total_bonus = self.multiplier + getattr(self, 'item_bonus', 0)
        total_passive = self.passive_income + getattr(self, 'item_passive_bonus', 0)
        speed_mult = getattr(self, 'passive_speed_multiplier', 1.0)
        active_mult = getattr(self, 'active_click_multiplier', 1.0)
        earnings = int((1 + total_bonus) * active_mult)
        earnings_text = self.font_small.render(f"+{earnings} за клик (x{active_mult:.1f}) / +{format_number(total_passive)} в сек (x{speed_mult:.1f})", True, GOLD)
        earnings_rect = earnings_text.get_rect(center=(WINDOW_WIDTH//2, 145 + OFFSET_Y))
        self.screen.blit(earnings_text, earnings_rect)
        
        level_text = self.font_small.render(f"Уровень: {self.multiplier} (+{getattr(self, 'item_bonus', 0)} от драгов)", True, (180, 180, 180))
        level_rect = level_text.get_rect(center=(WINDOW_WIDTH//2, 175 + OFFSET_Y))
        self.screen.blit(level_text, level_rect)
        
    def draw_main_tab(self):
        self.click_button.draw(self.screen, self.font_medium)
        
        next_level = self.multiplier + 1
        cost = get_upgrade_cost(next_level)
        
        cost_text = self.font_tiny.render(f"ПКМ для улучшения: {format_number(cost)}", True, GOLD)
        cost_rect = cost_text.get_rect(center=(WINDOW_WIDTH//2, 440 + OFFSET_Y))
        self.screen.blit(cost_text, cost_rect)
        
        hint = self.font_tiny.render("ЛКМ - заработок", True, (150, 150, 150))
        hint_rect = hint.get_rect(center=(WINDOW_WIDTH//2, 465 + OFFSET_Y))
        self.screen.blit(hint, hint_rect)
        
        passive_cost = get_passive_cost(self.passive_level)
        passive_button_text = f"Купить доход: {format_number(passive_cost)}"
        self.passive_button.text = passive_button_text
        self.passive_button.draw(self.screen, self.font_tiny)
        
        texture = None
        if self.inv_upgrade_button.level_id:
            texture = self.textures.get(self.inv_upgrade_button.level_id)
        self.inv_upgrade_button.draw(self.screen, self.font_mini, texture)
        
    def draw_shop_tab(self):
        title = self.font_medium.render("МАГАЗИН", True, GOLD)
        title_rect = title.get_rect(center=(WINDOW_WIDTH//2, 70 + OFFSET_Y))
        self.screen.blit(title, title_rect)
        
        for btn in self.shop_sub_buttons:
            btn.draw(self.screen, self.font_mini)
        
        mouse_pos = pygame.mouse.get_pos()
        for shop_item in self.shop_items:
            texture = self.textures.get(shop_item.item_id)
            shop_item.draw(self.screen, self.font_tiny, self.font_mini, texture)
        
        for shop_item in self.shop_items:
            shop_item.draw_tooltip(self.screen, self.font_tiny, self.font_mini, mouse_pos)
        
        balance_text = self.font_tiny.render(f"Баланс: {format_number(self.money)}", True, GOLD)
        balance_rect = balance_text.get_rect(bottomright=(WINDOW_WIDTH - 10, WINDOW_HEIGHT - 10))
        self.screen.blit(balance_text, balance_rect)
        
    def draw_item_bonuses(self):
        if not self.inventory:
            return
        
        x = WINDOW_WIDTH - 10
        y = 45
        
        title = self.font_mini.render("Бонусы:", True, LIGHT_GRAY)
        title_rect = title.get_rect(topright=(x, y))
        self.screen.blit(title, title_rect)
        y += 18
        
        item_counts = {}
        for item_id in self.inventory:
            if item_id not in item_counts:
                item_counts[item_id] = 0
            item_counts[item_id] += 1
        
        items_shown = 0
        for item_id, count in item_counts.items():
            if items_shown >= 5:
                more_text = self.font_mini.render(f"+ еще {len(item_counts) - 5} видов", True, GRAY)
                more_rect = more_text.get_rect(topright=(x, y))
                self.screen.blit(more_text, more_rect)
                break
                
            if item_id in CROSS_ITEMS:
                cross = CROSS_ITEMS[item_id]
                bonus_text = f"{cross['name'][:8]}: {count}шт"
                color = cross['color']
                text = self.font_mini.render(bonus_text, True, color)
                text_rect = text.get_rect(topright=(x, y))
                self.screen.blit(text, text_rect)
                y += 16
                items_shown += 1
            elif item_id in ITEMS:
                item = ITEMS[item_id]
                bonus_text = f"{item['name'][:8]}: {count}шт"
                color = item['color']
                text = self.font_mini.render(bonus_text, True, color)
                text_rect = text.get_rect(topright=(x, y))
                self.screen.blit(text, text_rect)
                y += 16
                items_shown += 1
            elif item_id in CASES:
                bonus_text = f"{CASE_NAMES[item_id][:8]}: {count}шт"
                text = self.font_mini.render(bonus_text, True, CASE_CONTENTS[item_id]['color'])
                text_rect = text.get_rect(topright=(x, y))
                self.screen.blit(text, text_rect)
                y += 16
                items_shown += 1
        
    def draw_item_tooltip(self):
        if self.hovered_item_info is None:
            return
        
        item_id, slot_rect = self.hovered_item_info
        
        if item_id in CROSS_ITEMS:
            cross_data = CROSS_ITEMS[item_id]
            tooltip_width = 160
            tooltip_height = 35
            tooltip_x = slot_rect.centerx - tooltip_width // 2
            tooltip_y = slot_rect.bottom + 5
            
            if tooltip_y + tooltip_height > WINDOW_HEIGHT - 50:
                tooltip_y = slot_rect.top - tooltip_height - 5
            
            if tooltip_x < 5:
                tooltip_x = 5
            elif tooltip_x + tooltip_width > WINDOW_WIDTH - 5:
                tooltip_x = WINDOW_WIDTH - tooltip_width - 5
            
            tooltip_rect = pygame.Rect(tooltip_x, tooltip_y, tooltip_width, tooltip_height)
            pygame.draw.rect(self.screen, (20, 20, 20, 230), tooltip_rect, border_radius=8)
            pygame.draw.rect(self.screen, GOLD, tooltip_rect, 1, border_radius=8)
            
            name_text = self.font_mini.render(cross_data['name'], True, cross_data['color'])
            name_rect = name_text.get_rect(center=(tooltip_rect.centerx, tooltip_rect.centery))
            self.screen.blit(name_text, name_rect)
            return
        
        if item_id not in ITEMS and item_id not in CASES:
            return
        
        if item_id in CASES:
            tooltip_width = 160
            tooltip_height = 35
            tooltip_x = slot_rect.centerx - tooltip_width // 2
            tooltip_y = slot_rect.bottom + 5
            
            if tooltip_y + tooltip_height > WINDOW_HEIGHT - 50:
                tooltip_y = slot_rect.top - tooltip_height - 5
            
            if tooltip_x < 5:
                tooltip_x = 5
            elif tooltip_x + tooltip_width > WINDOW_WIDTH - 5:
                tooltip_x = WINDOW_WIDTH - tooltip_width - 5
            
            tooltip_rect = pygame.Rect(tooltip_x, tooltip_y, tooltip_width, tooltip_height)
            pygame.draw.rect(self.screen, (20, 20, 20, 230), tooltip_rect, border_radius=8)
            pygame.draw.rect(self.screen, GOLD, tooltip_rect, 1, border_radius=8)
            
            use_text = self.font_mini.render("ПКМ для открытия", True, GOLD)
            use_rect = use_text.get_rect(center=(tooltip_rect.centerx, tooltip_rect.centery))
            self.screen.blit(use_text, use_rect)
            return
        
        item_data = ITEMS[item_id]
        item_type = item_data['type']
        bonus = item_data['bonus']
        
        tooltip_width = 180
        tooltip_height = 50
        tooltip_x = slot_rect.centerx - tooltip_width // 2
        tooltip_y = slot_rect.bottom + 5
        
        if tooltip_y + tooltip_height > WINDOW_HEIGHT - 50:
            tooltip_y = slot_rect.top - tooltip_height - 5
        
        if tooltip_x < 5:
            tooltip_x = 5
        elif tooltip_x + tooltip_width > WINDOW_WIDTH - 5:
            tooltip_x = WINDOW_WIDTH - tooltip_width - 5
        
        tooltip_rect = pygame.Rect(tooltip_x, tooltip_y, tooltip_width, tooltip_height)
        pygame.draw.rect(self.screen, (20, 20, 20, 230), tooltip_rect, border_radius=8)
        pygame.draw.rect(self.screen, GOLD, tooltip_rect, 1, border_radius=8)
        
        name_text = self.font_tiny.render(item_data['name'], True, item_data['color'])
        name_rect = name_text.get_rect(center=(tooltip_rect.centerx, tooltip_rect.y + 12))
        self.screen.blit(name_text, name_rect)
        
        if item_type == 'drag':
            bonus_text = f"+{bonus} за клик"
        elif item_type == 'apple':
            bonus_text = f"+{bonus} в сек"
        elif item_type == 'roll':
            bonus_text = f"x{bonus} скорость пассива"
        elif item_type == 'act':
            bonus_text = f"x{bonus} активный доход"
        elif item_type == 'rob':
            bonus_text = f"x{bonus} шанс кейсов"
        else:
            bonus_text = f"+{bonus}"
        
        bonus_color = GOLD if item_type == 'drag' else (GREEN if item_type == 'apple' else (BLUE if item_type == 'roll' else (PURPLE if item_type == 'act' else ORANGE)))
        bonus_text_surf = self.font_mini.render(bonus_text, True, bonus_color)
        bonus_rect = bonus_text_surf.get_rect(center=(tooltip_rect.centerx, tooltip_rect.y + 32))
        self.screen.blit(bonus_text_surf, bonus_rect)
        
    def draw_inventory_tab(self):
        title = self.font_medium.render("ИНВЕНТАРЬ", True, GOLD)
        title_rect = title.get_rect(center=(WINDOW_WIDTH//2, 70 + OFFSET_Y))
        self.screen.blit(title, title_rect)
        
        cols, rows = self.get_inventory_size()
        total_slots = cols * rows
        count_text = self.font_small.render(f"Всего: {len(self.inventory)} / {total_slots} ({cols}x{rows})", True, LIGHT_GRAY)
        count_rect = count_text.get_rect(center=(WINDOW_WIDTH//2, 100 + OFFSET_Y))
        self.screen.blit(count_text, count_rect)
        
        for slot in self.inv_grid_slots:
            slot.draw(self.screen, self.font_mini)
        
        craft_label = self.font_tiny.render("КРАФТ (3 одинаковых, для кейсов 5)", True, LIGHT_GRAY)
        craft_label_rect = craft_label.get_rect(center=(WINDOW_WIDTH//2, 505 + OFFSET_Y))
        self.screen.blit(craft_label, craft_label_rect)
        
        for slot in self.inventory_slots:
            slot.draw(self.screen, self.font_mini)
        
        self.craft_button.draw(self.screen, self.font_large)
        
        self.draw_item_bonuses()
        self.draw_item_tooltip()
        
    def draw_background(self):
        for i in range(WINDOW_HEIGHT):
            ratio = i / WINDOW_HEIGHT
            r = int(26 + 35 * ratio)
            g = int(11 + 21 * ratio)
            b = int(0)
            pygame.draw.line(self.screen, (r, g, b), (0, i), (WINDOW_WIDTH, i))
            
    def move_item_to_craft_slot(self, slot_index):
        if self.hovered_inventory_slot is None:
            return False
        
        if slot_index < 0 or slot_index >= len(self.inventory_slots):
            return False
        
        craft_slot = self.inventory_slots[slot_index]
        if craft_slot.item is not None:
            self.add_floating_text(
                WINDOW_WIDTH//2,
                570 + OFFSET_Y,
                f"Слот {slot_index + 1} занят!",
                RED
            )
            return False
        
        source_slot = self.hovered_inventory_slot
        if source_slot.item is None:
            return False
        
        if source_slot in self.inventory_slots:
            return False
        
        craft_slot.item = source_slot.item
        craft_slot.texture = source_slot.texture
        source_slot.item = None
        source_slot.texture = None
        
        self.sync_inventory_from_slots()
        self.update_inventory_slots()
        self.apply_item_bonuses()
        
        self.add_floating_text(
            WINDOW_WIDTH//2,
            570 + OFFSET_Y,
            f"Предмет в слот {slot_index + 1}!",
            GREEN
        )
        return True
    
    def sell_item(self, slot):
        if slot is None or slot.item is None:
            return False
        
        if slot in self.inventory_slots:
            return False
        
        item_id = slot.item
        price = 0
        if item_id in CROSS_ITEMS:
            price = CROSS_ITEMS[item_id]['price'] // 2
        elif item_id in ITEMS:
            price = ITEMS[item_id]['price'] // 2
        elif item_id in CASES:
            price = 100
        
        if price == 0:
            return False
        
        self.money += price
        slot.item = None
        slot.texture = None
        
        self.sync_inventory_from_slots()
        self.update_inventory_slots()
        self.apply_item_bonuses()
        self.data_changed = True
        
        self.add_floating_text(
            WINDOW_WIDTH//2,
            570 + OFFSET_Y,
            f"Продано за {format_number(price)}!",
            GOLD
        )
        return True

    def run(self):
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            
            self.update_hovered_item()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                action = self.main_tab_button.handle_event(event)
                if action == 'click':
                    self.current_tab = 'main'
                    
                action = self.inventory_tab_button.handle_event(event)
                if action == 'click':
                    self.current_tab = 'inventory'
                    
                action = self.shop_tab_button.handle_event(event)
                if action == 'click':
                    self.current_tab = 'shop'
                
                if self.current_tab == 'main':
                    action = self.click_button.handle_event(event)
                    if action == 'click':
                        self.handle_click()
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.click_button.is_hovered:
                            if event.button == 3:
                                self.handle_upgrade()
                    
                    action = self.passive_button.handle_event(event)
                    if action == 'click':
                        self.handle_passive_purchase()
                    
                    action = self.inv_upgrade_button.handle_event(event)
                    if action == 'click':
                        self.upgrade_inventory()
                
                elif self.current_tab == 'inventory':
                    if event.type == pygame.MOUSEMOTION:
                        self.hovered_inventory_slot = None
                        for slot in self.inv_grid_slots:
                            if slot.rect.collidepoint(event.pos) and slot.item is not None:
                                self.hovered_inventory_slot = slot
                                self.hovered_item_info = (slot.item, slot.rect)
                                break
                        if self.hovered_inventory_slot is None:
                            for slot in self.inventory_slots:
                                if slot.rect.collidepoint(event.pos) and slot.item is not None:
                                    self.hovered_inventory_slot = slot
                                    self.hovered_item_info = (slot.item, slot.rect)
                                    break
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.craft_items()
                        elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5]:
                            slot_index = event.key - pygame.K_1
                            self.move_item_to_craft_slot(slot_index)
                    
                    action = self.craft_button.handle_event(event)
                    if action == 'click':
                        self.craft_items()
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            for slot in self.inv_grid_slots:
                                if slot.is_hovered and slot.item is not None:
                                    self.dragging_item = slot.item
                                    self.drag_source = slot
                                    self.drag_offset = (slot.rect.x - mouse_pos[0], slot.rect.y - mouse_pos[1])
                                    slot.item = None
                                    slot.texture = None
                                    self.sync_inventory_from_slots()
                                    break
                            
                            if self.dragging_item is None:
                                for slot in self.inventory_slots:
                                    if slot.is_hovered and slot.item is not None:
                                        self.dragging_item = slot.item
                                        self.drag_source = slot
                                        self.drag_offset = (slot.rect.x - mouse_pos[0], slot.rect.y - mouse_pos[1])
                                        slot.item = None
                                        slot.texture = None
                                        break
                        elif event.button == 3:
                            clicked_slot = None
                            for slot in self.inv_grid_slots:
                                if slot.is_hovered and slot.item is not None:
                                    clicked_slot = slot
                                    break
                            
                            if clicked_slot is not None:
                                if clicked_slot.item in CASES:
                                    case_id = clicked_slot.item
                                    self.open_case(case_id)
                                else:
                                    self.sell_item(clicked_slot)
                    
                    elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        if self.dragging_item is not None:
                            self.handle_drop(mouse_pos)
                    
                    elif event.type == pygame.MOUSEMOTION:
                        for slot in self.inv_grid_slots + self.inventory_slots:
                            slot.handle_event(event)
                
                elif self.current_tab == 'shop':
                    for btn in self.shop_sub_buttons:
                        action = btn.handle_event(event)
                        if action == 'click':
                            self.shop_subtab = btn.tab_id
                            for b in self.shop_sub_buttons:
                                b.is_active = (b.tab_id == self.shop_subtab)
                            self.create_shop()
                    
                    for shop_item in self.shop_items:
                        action = shop_item.handle_event(event)
                        if action == 'click':
                            self.buy_item(shop_item.item_id)
            
            self.update_floating_texts()
            self.update_passive_income()
            
            self.draw_background()
            
            title = self.font_large.render("ВЕЧНЫЙ КЛИКЕР", True, GOLD)
            title_rect = title.get_rect(center=(WINDOW_WIDTH//2, 20 + TITLE_OFFSET_Y))
            self.screen.blit(title, title_rect)
            
            self.main_tab_button.is_active = (self.current_tab == 'main')
            self.inventory_tab_button.is_active = (self.current_tab == 'inventory')
            self.shop_tab_button.is_active = (self.current_tab == 'shop')
            
            self.main_tab_button.draw(self.screen, self.font_mini)
            self.inventory_tab_button.draw(self.screen, self.font_mini)
            self.shop_tab_button.draw(self.screen, self.font_mini)
            
            if self.current_tab == 'main':
                self.draw_stats()
                self.draw_main_tab()
            elif self.current_tab == 'inventory':
                self.draw_inventory_tab()
            elif self.current_tab == 'shop':
                self.draw_shop_tab()
                
            self.draw_floating_texts()
            
            if self.dragging_item is not None and self.textures.get(self.dragging_item):
                tex = self.textures[self.dragging_item]
                tex_rect = tex.get_rect(center=mouse_pos)
                self.screen.blit(tex, tex_rect)
            
            pygame.display.flip()
            self.clock.tick(FPS)
            
        self.save_game()
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = ClickerGame()
    game.run()
