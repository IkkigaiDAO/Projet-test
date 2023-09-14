import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import random

kivy.require('2.2.1')

class GameView(BoxLayout):
    def __init__(self):
        super(GameView,self).__init__()
        self.randomvalue = random.randint(0,1000)
    def check_number(self):
        if int(self.answer_input.text) == self.randomvalue :
            self.result_label.text = "Congrats!"
            self.result_label.color ="#00EF0B"
        elif int(self.answer_input.text) < self.randomvalue :
            self.result_label.text = "More"
            self.result_label.color ="#00EF0B"
        elif int(self.answer_input.text) > self.randomvalue :
            self.result_label.text = "Less"
            self.result_label.color ="#00EF0B"
            

class MonAppTuto(App):
    def build(self):
        return GameView()
    
LancementAPP=MonAppTuto()
LancementAPP.run()