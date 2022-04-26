from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.storage.jsonstore import JsonStore
from kivy.base import runTouchApp
from kivy.properties import ObjectProperty

Builder.load_string("""
<Calc>:
    # This are attributes of the class Calc now
    a: _a
    b: _b
    result: _result
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        ScreenManager:
            size_hint: 1, .9
            id: _screen_manager
            Screen:
                name: 'screen1'
                GridLayout:
                    cols:1
                    TextInput:
                        id: _a
                        hint_text: 'weight'
                    TextInput:
                        id: _b
                        hint_text: 'height'
                    TextInput:
                        id: _c
                        hint_text: 'age'
                    Label:
                        id: _result

                    Button:
                        text: 'MAN BMR'
                        # You can do the opertion directly
                        on_press: _result.text = str(float(66.47)+(float(13.75)*float(_a.text)) + (float(5)*float(_b.text))-float(6.76)*float(_c.text))
                    Button:
                        text: 'WOMAN BMR'
                        # Or you can call a method from the root class (instance of calc)
                        on_press: _result.text = str(float(665.1)+(float(9.56)*float(_a.text)) + (float(1.85)*float(_b.text))-float(4.68)*float(_c.text))
                    Button:
                        text: 'NEXT'
                        on_press: _screen_manager.current = 'screen2'


            Screen: 
                name: 'screen2'
                BoxLayout:
                    Button:
                        text: 'Breakfast'

                    Label:
                        id:_calorie1

                    Button:
                        text: 'Lunch'

                    Label:
                        id:_calorie2

                    Button:
                        text: 'Dinner'

                    Label:
                        id:_calorie3

                    Button:
                        text:'sum calorie'

                    Label:
                        id:_tcalorie

                    Button:
                        text: 'Back'

                    Button:
                        text: 'Go To Exercise'





""")


class Calc(FloatLayout):
    pass


class TestApp(App):
    def build(self):
        return Calc()


if __name__ == '__main__':
    TestApp().run()