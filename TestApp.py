import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.actionbar import ActionToggleButton, ActionButton, ActionBar, ActionView, ActionOverflow, ActionPrevious, ActionItem
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from ViewStackLayout import ViewStackLayout
from kivy.uix.button import Button

class TestApp(App):
    """
    Simple app to demonstrate the usage for a Kivy ViewStackLayout that is
    part of this project.

    """
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)

    def _on_view1_action_button_press(self, btn):
        self.view_stack_layout.activate_view_by_name('view1')

    def _on_view2_action_button_press(self, btn):
        self.view_stack_layout.activate_view_by_name('view2')

    def _on_view3_action_button_press(self, btn):
        self.view_stack_layout.activate_view_by_name('view3')

    def _create_action_bar(self):
        # ----------  ActionBar  ------------
        # https://github.com/abhijangda/KivyExamples/blob/master/action_bar/actionbar.py
        overflow_group = ActionOverflow()
        action_previous = ActionPrevious(title='ViewStack Example')
        action_view = ActionView()
        action_view.add_widget(action_previous)
        action_view.add_widget(overflow_group)

        action_bar = ActionBar(size_hint=(1,0.1),pos_hint={'top':1})
        action_bar.add_widget(action_view)

        self.view1_action_button = ActionToggleButton(text="View 1", group="left_view", state='down')
        self.view1_action_button.bind(on_press=self._on_view1_action_button_press)
        action_view.add_widget(self.view1_action_button)

        self.view2_action_button = ActionToggleButton(text="View 2", group="left_view")
        self.view2_action_button.bind(on_press=self._on_view2_action_button_press)
        action_view.add_widget(self.view2_action_button)

        self.view3_action_button = ActionToggleButton(text="View 3", group="left_view")
        self.view3_action_button.bind(on_press=self._on_view3_action_button_press)
        action_view.add_widget(self.view3_action_button)

        self.action_bar = action_bar
        return action_bar

    def build(self):
        #top level box with the status bar and main content
        root = BoxLayout(orientation='vertical', padding=10)

        with root.canvas.before:
            Color(.2, .2, .2, 1)

        self._create_action_bar()
        self.view_stack_layout = ViewStackLayout()

        self.view1_layout = BoxLayout(orientation='vertical')
        self.view1_layout.add_widget(Button(text="View 1"))
        self.view_stack_layout.add_view(self.view1_layout, 'view1')

        self.view2_layout = BoxLayout(orientation='vertical')
        self.view2_layout.add_widget(Button(text="View 2"))
        self.view_stack_layout.add_view(self.view2_layout, 'view2')

        self.view3_layout = BoxLayout(orientation='vertical')
        self.view3_layout.add_widget(Button(text="View 3"))
        self.view_stack_layout.add_view(self.view3_layout, 'view3')

        root.add_widget(self.action_bar)
        root.add_widget(self.view_stack_layout)

        return root

if __name__ == '__main__':
    TestApp().run()
