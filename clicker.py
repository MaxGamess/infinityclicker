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

DATA_FILE = 'data.json'
TEXTURES_DIR = './textures/'

OFFSET_Y = 50
TITLE_OFFSET_Y = 20

ITEMS = {
    'wooden_drag': {
        'name': 'Деревянный драг',
        'chance': 0.01,
        'bonus': 1,
        'color': (139, 69, 19),
        'next': 'stone_drag',
        'type': 'drag',
        'rarity': 1,
        'price': 1000
    },
    'apple': {
        'name': 'Яблоко',
        'chance': 0.005,
        'bonus': 1,
        'color': (255, 50, 50),
        'next': 'wooden_apple',
        'type': 'apple',
        'rarity': 1,
        'price': 1500
    },
    'stone_drag': {
        'name': 'Каменный драг',
        'chance': 0.003,
        'bonus': 2,
        'color': (128, 128, 128),
        'next': 'copper_drag',
        'type': 'drag',
        'rarity': 2,
        'price': 5000
    },
    'wooden_apple': {
        'name': 'Деревянное яблоко',
        'chance': 0.00075,
        'bonus': 2,
        'color': (139, 69, 19),
        'next': 'stone_apple',
        'type': 'apple',
        'rarity': 2,
        'price': 4500
    },
    'copper_drag': {
        'name': 'Медный драг',
        'chance': 0.0005,
        'bonus': 3,
        'color': (184, 115, 51),
        'next': 'iron_drag',
        'type': 'drag',
        'rarity': 3,
        'price': 25000
    },
    'stone_apple': {
        'name': 'Каменное яблоко',
        'chance': 0.00015,
        'bonus': 3,
        'color': (128, 128, 128),
        'next': 'copper_apple',
        'type': 'apple',
        'rarity': 3,
        'price': 13500
    },
    'iron_drag': {
        'name': 'Железный драг',
        'chance': 0.00005,
        'bonus': 4,
        'color': (192, 192, 192),
        'next': 'golden_drag',
        'type': 'drag',
        'rarity': 4,
        'price': 120000
    },
    'copper_apple': {
        'name': 'Медное яблоко',
        'chance': 0.000025,
        'bonus': 4,
        'color': (184, 115, 51),
        'next': 'iron_apple',
        'type': 'apple',
        'rarity': 4,
        'price': 40000
    },
    'golden_drag': {
        'name': 'Золотой драг',
        'chance': 0.000005,
        'bonus': 5,
        'color': (255, 215, 0),
        'next': 'emerald_drag',
        'type': 'drag',
        'rarity': 5,
        'price': 550000
    },
    'iron_apple': {
        'name': 'Железное яблоко',
        'chance': 0.000025,
        'bonus': 5,
        'color': (192, 192, 192),
        'next': 'golden_apple',
        'type': 'apple',
        'rarity': 5,
        'price': 120000
    },
    'emerald_drag': {
        'name': 'Изумрудный драг',
        'chance': 0.0000005,
        'bonus': 7,
        'color': (80, 200, 80),
        'next': 'diamond_drag',
        'type': 'drag',
        'rarity': 6,
        'price': 2500000
    },
    'golden_apple': {
        'name': 'Золотое яблоко',
        'chance': 0.0000025,
        'bonus': 7,
        'color': (255, 215, 0),
        'next': 'emerald_apple',
        'type': 'apple',
        'rarity': 6,
        'price': 360000
    },
    'diamond_drag': {
        'name': 'Алмазный драг',
        'chance': 0.00000005,
        'bonus': 9,
        'color': (0, 255, 255),
        'next': 'ruby_drag',
        'type': 'drag',
        'rarity': 7,
        'price': 10000000
    },
    'emerald_apple': {
        'name': 'Изумрудное яблоко',
        'chance': 0.00000025,
        'bonus': 9,
        'color': (80, 200, 80),
        'next': 'diamond_apple',
        'type': 'apple',
        'rarity': 7,
        'price': 1000000
    },
    'ruby_drag': {
        'name': 'Рубиновый драг',
        'chance': 0.000000005,
        'bonus': 12,
        'color': (200, 0, 0),
        'next': 'netherite_drag',
        'type': 'drag',
        'rarity': 8,
        'price': 50000000
    },
    'diamond_apple': {
        'name': 'Алмазное яблоко',
        'chance': 0.000000025,
        'bonus': 12,
        'color': (0, 255, 255),
        'next': 'ruby_apple',
        'type': 'apple',
        'rarity': 8,
        'price': 3000000
    },
    'netherite_drag': {
        'name': 'Незеритовый драг',
        'chance': 0.0000000005,
        'bonus': 15,
        'color': (80, 0, 80),
        'next': None,
        'type': 'drag',
        'rarity': 9,
        'price': 250000000
    },
    'ruby_apple': {
        'name': 'Рубиновое яблоко',
        'chance': 0.0000000025,
        'bonus': 15,
        'color': (200, 0, 0),
        'next': 'netherite_apple',
        'type': 'apple',
        'rarity': 9,
        'price': 9000000
    },
    'netherite_apple': {
        'name': 'Незеритовое яблоко',
        'chance': 0.00000000025,
        'bonus': 20,
        'color': (80, 0, 80),
        'next': None,
        'type': 'apple',
        'rarity': 10,
        'price': 25000000
    }
}

def get_rarity_order():
    rarity_groups = {}
    for item_id, item_data in ITEMS.items():
        rarity = item_data.get('rarity', 0)
        if rarity not in rarity_groups:
            rarity_groups[rarity] = []
        rarity_groups[rarity].append(item_id)
    
    sorted_items = []
    for rarity in sorted(rarity_groups.keys(), reverse=True):
        drags = [id for id in rarity_groups[rarity] if ITEMS[id]['type'] == 'drag']
        apples = [id for id in rarity_groups[rarity] if ITEMS[id]['type'] == 'apple']
        sorted_items.extend(drags + apples)
    
    return sorted_items

ITEM_ORDER = ['wooden_drag', 'stone_drag', 'copper_drag', 'iron_drag', 
              'golden_drag', 'emerald_drag', 'diamond_drag', 'ruby_drag', 'netherite_drag',
              'apple', 'wooden_apple', 'stone_apple', 'copper_apple', 'iron_apple',
              'golden_apple', 'emerald_apple', 'diamond_apple', 'ruby_apple', 'netherite_apple']

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {'money': 0, 'multiplier': 0, 'click_count': 0, 'passive_income': 0, 'passive_level': 0, 'inventory': []}
    else:
        return {'money': 0, 'multiplier': 0, 'click_count': 0, 'passive_income': 0, 'passive_level': 0, 'inventory': []}

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
        
        # Цена снизу
        price = ITEMS[self.item_id]['price']
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

class InventorySlot:
    def __init__(self, x, y, size=50):
        self.rect = pygame.Rect(x, y, size, size)
        self.size = size
        self.item = None
        self.is_hovered = False
        self.texture = None
        
    def draw(self, surface, font):
        # Фон слота
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
        # Стиль как у слотов
        shadow_rect = self.rect.copy()
        shadow_rect.x += 2
        shadow_rect.y += 2
        pygame.draw.rect(surface, (0, 0, 0, 50), shadow_rect, border_radius=8)
        
        if self.is_hovered:
            pygame.draw.rect(surface, (80, 40, 120), self.rect, border_radius=8)
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
        
        self.textures = {}
        self.load_textures()
        
        self.floating_texts = []
        self.passive_timer = 0
        self.current_tab = 'main'
        self.inventory_slots = []
        self.craft_slots = []
        self.dragging_item = None
        self.drag_source = None
        self.drag_offset = (0, 0)
        self.shop_items = []
        
        self.create_buttons()
        self.create_inventory_slots()
        self.create_shop()
        
        self.data_changed = False
        self.apply_item_bonuses()
        
    def sort_inventory_by_rarity(self):
        """Сортирует инвентарь по редкости (от самого редкого к самому частому)"""
        item_counts = {}
        for item_id in self.inventory:
            if item_id not in item_counts:
                item_counts[item_id] = 0
            item_counts[item_id] += 1
        
        sorted_items = get_rarity_order()
        
        new_inventory = []
        for item_id in sorted_items:
            if item_id in item_counts:
                new_inventory.extend([item_id] * item_counts[item_id])
        
        self.inventory = new_inventory
        self.data_changed = True
        
    def load_textures(self):
        for item_id in ITEMS.keys():
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
        shop_item_ids = []
        for item_id, item_data in ITEMS.items():
            if 'price' in item_data and item_data['price'] > 0:
                shop_item_ids.append(item_id)
        
        shop_item_ids.sort(key=lambda x: ITEMS[x]['rarity'], reverse=True)
        
        item_size = 60
        spacing = 8
        cols = 5
        total_width = cols * item_size + (cols - 1) * spacing
        start_x = (WINDOW_WIDTH - total_width) // 2
        start_y = 130 + OFFSET_Y
        
        self.shop_items = []
        for i, item_id in enumerate(shop_item_ids):
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
        total_width = 7 * slot_size + 6 * spacing
        start_x = (WINDOW_WIDTH - total_width) // 2
        
        for row in range(3):
            for col in range(7):
                x = start_x + col * (slot_size + spacing)
                y = 300 + row * (slot_size + spacing)
                slot = InventorySlot(x, y, slot_size)
                self.inv_grid_slots.append(slot)
        
        self.update_inventory_slots()
        
    def update_inventory_slots(self):
        self.sort_inventory_by_rarity()
        
        for slot in self.inv_grid_slots:
            slot.item = None
            slot.texture = None
        
        for i, item_id in enumerate(self.inventory[:21]):
            if i < len(self.inv_grid_slots):
                self.inv_grid_slots[i].item = item_id
                self.inv_grid_slots[i].texture = self.textures.get(item_id)
        
        for slot in self.inventory_slots:
            if slot.item:
                slot.texture = self.textures.get(slot.item)
    
    def get_all_slots(self):
        """Возвращает все слоты (инвентарь + крафт)"""
        return self.inv_grid_slots + self.inventory_slots
    
    def sync_inventory_from_slots(self):
        """Синхронизирует список инвентаря с содержимым слотов"""
        new_inventory = []
        for slot in self.inv_grid_slots:
            if slot.item is not None:
                new_inventory.append(slot.item)
        self.inventory = new_inventory
        self.data_changed = True
        
    def buy_item(self, item_id):
        """Покупает предмет в магазине"""
        if item_id not in ITEMS:
            return False
        
        price = ITEMS[item_id]['price']
        if self.money >= price:
            self.money -= price
            self.inventory.append(item_id)
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
        
    def craft_items(self):
        """Совмещает предметы в слотах крафта"""
        items_in_slots = {}
        craft_slots_with_items = []
        
        for slot in self.inventory_slots:
            if slot.item is not None:
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
            if item_id not in ITEMS:
                continue
                
            item_type = ITEMS[item_id]['type']
            required_count = 5 if item_type == 'drag' else 3
            
            if count >= required_count and ITEMS[item_id]['next'] is not None:
                removed = 0
                for slot in self.inventory_slots:
                    if slot.item == item_id:
                        slot.item = None
                        slot.texture = None
                        removed += 1
                        if removed >= required_count:
                            break
                
                next_item = ITEMS[item_id]['next']
                self.inventory.append(next_item)
                
                self.data_changed = True
                self.update_inventory_slots()
                self.apply_item_bonuses()
                
                self.add_floating_text(
                    WINDOW_WIDTH//2,
                    570 + OFFSET_Y,
                    f"Совмещено! +{ITEMS[next_item]['name']}",
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
                    f"Нужно 3 (яблоки) или 5 (драги) одинаковых!",
                    RED
                )
            else:
                for item_id, count in items_in_slots.items():
                    if count >= 3 and ITEMS[item_id]['next'] is None:
                        self.add_floating_text(
                            WINDOW_WIDTH//2,
                            570 + OFFSET_Y,
                            f"{ITEMS[item_id]['name']} нельзя улучшить!",
                            RED
                        )
                        break
        
        return crafted
        
    def apply_item_bonuses(self):
        total_bonus = 0
        total_passive = 0
        for item_id in self.inventory:
            if item_id in ITEMS:
                if ITEMS[item_id]['type'] == 'drag':
                    total_bonus += ITEMS[item_id]['bonus']
                elif ITEMS[item_id]['type'] == 'apple':
                    total_passive += ITEMS[item_id]['bonus']
        self.item_bonus = total_bonus
        self.item_passive_bonus = total_passive
        self.data_changed = True
        
    def find_nearest_empty_slot(self, mouse_pos):
        """Находит ближайший пустой слот"""
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
        """Возвращает индекс слота в общем списке"""
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
        earnings = 1 + self.multiplier + getattr(self, 'item_bonus', 0)
        self.money += earnings
        self.click_count += 1
        self.data_changed = True
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.add_floating_text(mouse_x, mouse_y - 30, f"+{earnings}")
        
        self.try_drop_item()
        
    def try_drop_item(self):
        roll = random.random() * 100
        
        for item_id in reversed(ITEM_ORDER):
            chance = ITEMS[item_id]['chance'] * 100
            if roll < chance:
                self.inventory.append(item_id)
                
                self.data_changed = True
                self.apply_item_bonuses()
                self.update_inventory_slots()
                
                self.add_floating_text(
                    WINDOW_WIDTH//2,
                    300 + OFFSET_Y,
                    f"Выпал {ITEMS[item_id]['name']}!",
                    ITEMS[item_id]['color']
                )
                break
        
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
                f"Улучшено! +{1 + self.multiplier + getattr(self, 'item_bonus', 0)}",
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
            if self.passive_timer >= FPS:
                self.money += total_income
                self.passive_timer = 0
                self.data_changed = True
                self.add_floating_text(
                    WINDOW_WIDTH//2,
                    200 + OFFSET_Y,
                    f"+{total_income}",
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
                'inventory': self.inventory
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
        
        click_info = self.font_small.render(f"Кликов: {self.click_count}", True, (200, 200, 200))
        click_rect = click_info.get_rect(center=(WINDOW_WIDTH//2, 115 + OFFSET_Y))
        self.screen.blit(click_info, click_rect)
        
        total_bonus = self.multiplier + getattr(self, 'item_bonus', 0)
        total_passive = self.passive_income + getattr(self, 'item_passive_bonus', 0)
        earnings = 1 + total_bonus
        earnings_text = self.font_small.render(f"+{earnings} за клик / +{total_passive} в сек", True, GOLD)
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
        
    def draw_shop_tab(self):
        title = self.font_medium.render("МАГАЗИН", True, GOLD)
        title_rect = title.get_rect(center=(WINDOW_WIDTH//2, 70 + OFFSET_Y))
        self.screen.blit(title, title_rect)
        
        subtitle = self.font_tiny.render("Купите предметы за монеты", True, LIGHT_GRAY)
        subtitle_rect = subtitle.get_rect(center=(WINDOW_WIDTH//2, 95 + OFFSET_Y))
        self.screen.blit(subtitle, subtitle_rect)
        
        for shop_item in self.shop_items:
            texture = self.textures.get(shop_item.item_id)
            shop_item.draw(self.screen, self.font_mini, texture)
        
        hint = self.font_mini.render("ЛКМ по товару - покупка", True, (150, 150, 150))
        hint_rect = hint.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT - 60))
        self.screen.blit(hint, hint_rect)
        
    def draw_item_bonuses(self):
        """Рисует бонусы предметов в правом верхнем углу"""
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
                
            if item_id in ITEMS:
                item = ITEMS[item_id]
                bonus_text = f"{item['name'][:8]}: {count}шт"
                color = item['color']
                text = self.font_mini.render(bonus_text, True, color)
                text_rect = text.get_rect(topright=(x, y))
                self.screen.blit(text, text_rect)
                y += 16
                items_shown += 1
        
    def draw_inventory_tab(self):
        title = self.font_medium.render("ИНВЕНТАРЬ", True, GOLD)
        title_rect = title.get_rect(center=(WINDOW_WIDTH//2, 70 + OFFSET_Y))
        self.screen.blit(title, title_rect)
        
        count_text = self.font_small.render(f"Всего: {len(self.inventory)} / 21", True, LIGHT_GRAY)
        count_rect = count_text.get_rect(center=(WINDOW_WIDTH//2, 100 + OFFSET_Y))
        self.screen.blit(count_text, count_rect)
        
        for slot in self.inv_grid_slots:
            slot.draw(self.screen, self.font_mini)
        
        craft_label = self.font_tiny.render("КРАФТ (3 яблока или 5 драгов)", True, LIGHT_GRAY)
        craft_label_rect = craft_label.get_rect(center=(WINDOW_WIDTH//2, 505 + OFFSET_Y))
        self.screen.blit(craft_label, craft_label_rect)
        
        for slot in self.inventory_slots:
            slot.draw(self.screen, self.font_mini)
        
        self.craft_button.draw(self.screen, self.font_large)
        
        self.draw_item_bonuses()
        
    def draw_background(self):
        for i in range(WINDOW_HEIGHT):
            ratio = i / WINDOW_HEIGHT
            r = int(26 + 35 * ratio)
            g = int(11 + 21 * ratio)
            b = int(0)
            pygame.draw.line(self.screen, (r, g, b), (0, i), (WINDOW_WIDTH, i))
            
    def run(self):
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            
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
                
                elif self.current_tab == 'inventory':
                    action = self.craft_button.handle_event(event)
                    if action == 'click':
                        self.craft_items()
                    
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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
                    
                    elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        if self.dragging_item is not None:
                            self.handle_drop(mouse_pos)
                    
                    elif event.type == pygame.MOUSEMOTION:
                        for slot in self.inv_grid_slots + self.inventory_slots:
                            slot.handle_event(event)
                
                elif self.current_tab == 'shop':
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
