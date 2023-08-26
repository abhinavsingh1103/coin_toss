# Importing all the library
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from random import choice

class Coin_Toss(App):
    def build(self):
        self.icon = "icon.png"
        self.title = "Coin Toss"
        self.root = CoinTossUI()
        return self.root

class CoinTossUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.img = Image(source='icon.png', size_hint_y = 0.5)
        self.add_widget(self.img)
        self.toss_button = TossButton(text = "Toss Coin!", size_hint_y = None, height = 150)
        self.toss_button.bind(on_press=self.start_toss)
        self.add_widget(self.toss_button)
        self.coin_toss_sound = SoundLoader.load('toss_sound.mp3')
        self.sound_fade_event = None
    
    def start_toss(self, instance):
        self.toss_button.disabled = True
        self.img.source = 'toss.png'
        if self.coin_toss_sound:
            self.coin_toss_sound.play()
            self.sound_fade_event = Clock.schedule_interval(self.fade_sound, 0.1)
        Clock.schedule_once(self.finish_toss, 4)
    
    def fade_sound(self, dt):
        if self.coin_toss_sound.volume > 0.1:
            self.coin_toss_sound.volume -= 0.02
        else:
            self.sound_fade_event.cancel()  # Stop the fading when volume is low enough
            self.coin_toss_sound.stop()

    def finish_toss(self, instance):
        coin_side = choice([0,1])
        if coin_side == 0:
            self.img.source = 'heads.png'
        else:
            self.img.source = 'tails.png'
        self.toss_button.disabled = False

class TossButton(Button):
    pass
    
if __name__ == "__main__":
    app = Coin_Toss()
    app.run()
