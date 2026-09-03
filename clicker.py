import pygame
import json
import os
import math
import sys

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

DATA_FILE = 'data.json'

OFFSET_Y = 50
TITLE_OFFSET_Y = 20

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {'money': 0, 'multiplier': 0, 'click_count': 0}
    else:
        return {'money': 0, 'multiplier': 0, 'click_count': 0}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_upgrade_cost(multiplier):
    return math.ceil(multiplier * 100 * (multiplier / 2))

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
    else:
        return f"{num/1000000000000000000:.2f}S".rstrip('0').rstrip('.')

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
                elif event.button == 3:
                    return 'upgrade'
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
        
        self.data = load_data()
        self.money = self.data['money']
        self.multiplier = self.data['multiplier']
        self.click_count = self.data['click_count']
        
        self.floating_texts = []
        
        self.create_buttons()
        
        self.data_changed = False
        
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
        earnings = 1 + self.multiplier
        self.money += earnings
        self.click_count += 1
        self.data_changed = True
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.add_floating_text(mouse_x, mouse_y - 30, f"+{earnings}")
        
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
                f"Улучшено! +{1 + self.multiplier}",
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
            
    def save_game(self):
        if self.data_changed:
            self.data = {
                'money': self.money,
                'multiplier': self.multiplier,
                'click_count': self.click_count
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
        
        earnings = 1 + self.multiplier
        earnings_text = self.font_small.render(f"+{earnings} за клик", True, GOLD)
        earnings_rect = earnings_text.get_rect(center=(WINDOW_WIDTH//2, 150 + OFFSET_Y))
        self.screen.blit(earnings_text, earnings_rect)
        
        level_text = self.font_small.render(f"Уровень: {self.multiplier}", True, (180, 180, 180))
        level_rect = level_text.get_rect(center=(WINDOW_WIDTH//2, 185 + OFFSET_Y))
        self.screen.blit(level_text, level_rect)
        
    def draw_clicker_tab(self):
        self.click_button.draw(self.screen, self.font_medium)
        
        next_level = self.multiplier + 1
        cost = get_upgrade_cost(next_level)
        
        cost_text = self.font_tiny.render(f"ПКМ для улучшения: {format_number(cost)}", True, GOLD)
        cost_rect = cost_text.get_rect(center=(WINDOW_WIDTH//2, 440 + OFFSET_Y))
        self.screen.blit(cost_text, cost_rect)
        
        hint = self.font_tiny.render("ЛКМ - заработок", True, (150, 150, 150))
        hint_rect = hint.get_rect(center=(WINDOW_WIDTH//2, 470 + OFFSET_Y))
        self.screen.blit(hint, hint_rect)
        
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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                action = self.click_button.handle_event(event)
                if action == 'click':
                    self.handle_click()
                elif action == 'upgrade':
                    self.handle_upgrade()
                        
            self.update_floating_texts()
            
            self.draw_background()
            
            title = self.font_large.render("ВЕЧНЫЙ КЛИКЕР", True, GOLD)
            title_rect = title.get_rect(center=(WINDOW_WIDTH//2, 20 + TITLE_OFFSET_Y))
            self.screen.blit(title, title_rect)
            
            self.draw_stats()
            
            self.draw_clicker_tab()
                
            self.draw_floating_texts()
            
            pygame.display.flip()
            self.clock.tick(FPS)
            
        self.save_game()
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = ClickerGame()
    game.run()
