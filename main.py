from beyblade import Beyblade
from match import Match

from kivy.core.window import Window

# Set window size to match common mobile dimensions (e.g., iPhone 12)
Window.size = (390, 844)

# Enable touch emulation
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class BeybladeCreationScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Input fields for Beyblade 1
        self.bey1_blade = MDTextField(hint_text="Beyblade 1 Blade")
        self.bey1_ratchet = MDTextField(hint_text="Beyblade 1 Ratchet")
        self.bey1_bit = MDTextField(hint_text="Beyblade 1 Bit")
        
        # Input fields for Beyblade 2
        self.bey2_blade = MDTextField(hint_text="Beyblade 2 Blade")
        self.bey2_ratchet = MDTextField(hint_text="Beyblade 2 Ratchet")
        self.bey2_bit = MDTextField(hint_text="Beyblade 2 Bit")
        
        # Start battle button
        start_button = MDRaisedButton(
            text="Start Battle",
            on_release=self.start_battle
        )
        
        # Add all widgets to layout
        for widget in [self.bey1_blade, self.bey1_ratchet, self.bey1_bit,
                      self.bey2_blade, self.bey2_ratchet, self.bey2_bit,
                      start_button]:
            layout.add_widget(widget)
        
        self.add_widget(layout)
    
    def start_battle(self, instance):
        bey1 = Beyblade(self.bey1_blade.text, self.bey1_ratchet.text, self.bey1_bit.text)
        bey2 = Beyblade(self.bey2_blade.text, self.bey2_ratchet.text, self.bey2_bit.text)
        self.parent.get_screen('battle').start_match(bey1, bey2)
        self.parent.current = 'battle'

class BattleScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.match = None
        
        layout = MDBoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Status labels
        self.battle_number = MDLabel(text="Battle: 1")
        self.score_label = MDLabel(text="Score: 0 - 0")
        
        # Beyblade selection buttons
        bey_layout = MDBoxLayout(orientation='horizontal', spacing=10)
        self.bey1_button = MDRaisedButton(text="Beyblade 1")
        self.bey2_button = MDRaisedButton(text="Beyblade 2")
        bey_layout.add_widget(self.bey1_button)
        bey_layout.add_widget(self.bey2_button)
        
        # Victory type buttons
        victory_layout = MDBoxLayout(orientation='horizontal', spacing=10)
        victory_types = ['spin', 'over', 'burst', 'x']
        self.victory_buttons = []
        for vt in victory_types:
            btn = MDRaisedButton(
                text=vt.capitalize(),
                on_release=lambda x, vt=vt: self.record_victory(vt)
            )
            victory_layout.add_widget(btn)
            self.victory_buttons.append(btn)
        
        # Add all widgets to main layout
        for widget in [self.battle_number, self.score_label, bey_layout, victory_layout]:
            layout.add_widget(widget)
        
        self.add_widget(layout)
    
    def start_match(self, bey1, bey2):
        self.match = Match(bey1, bey2)
        self.bey1_button.text = str(bey1)
        self.bey2_button.text = str(bey2)
        self.update_display()
    
    def record_victory(self, victory_type):
        if not self.selected_beyblade:
            return
            
        winner = self.match.battle_gui(self.selected_beyblade, victory_type)
        self.update_display()
        
        if winner:
            self.show_results()
    
    def update_display(self):
        self.battle_number.text = f"Battle: {self.match.get_battles()}"
        self.score_label.text = f"Score: {self.match.get_bey1_points()} - {self.match.get_bey2_points()}"

class BeybladeApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        
        sm = MDScreenManager()
        sm.add_widget(BeybladeCreationScreen(name='create'))
        sm.add_widget(BattleScreen(name='battle'))
        return sm

if __name__ == '__main__':
    BeybladeApp().run() 