from kivy.uix.boxlayout import BoxLayout


class ViewStackLayout(BoxLayout):
    """
    A ViewStack Layout, derived from a BoxLayout that allows for a UI
    concept of a stack of views, where only the top view is visible
    """

    def __init__(self, **kwargs):
        super(ViewStackLayout, self).__init__(**kwargs)
        self.view_stack = []
        self.active_index = 0

    def add_widget(self, view_layout):
        self.add_view(view_layout)

    def add_view(self, view_layout, view_name = None):
        if not self.view_stack:
            # if this is the first one, then add it to the view
            super(ViewStackLayout, self).add_widget(view_layout)

        if view_name is None:
            view_name = "view_{0}".format(len(self.view_stack))

        self.view_stack.append({'view_name': view_name, 'view_layout': view_layout})

    def next_view(self):
        next_view_index = self.active_index+1
        if next_view_index == len(self.view_stack):
            # then we should wrap around to the beginning
            next_view_index = 0

        self.activate_view(next_view_index)

    def previous_view(self):
        next_view_index = self.active_index - 1
        if next_view_index < 0:
            # then we should wrap around to the beginning
            next_view_index = len(self.view_stack)-1

        self.activate_view(next_view_index)

    def activate_view(self, index):
        super(ViewStackLayout, self).remove_widget(self.view_stack[self.active_index]['view_layout'])
        super(ViewStackLayout, self).add_widget(self.view_stack[index])
        self.active_index = index

    def activate_view_by_name(self, view_name):
        super(ViewStackLayout, self).remove_widget(self.view_stack[self.active_index]['view_layout'])
        for idx,item in enumerate(self.view_stack):
            if item['view_name'] == view_name:
                super(ViewStackLayout, self).add_widget(item['view_layout'])
                self.active_index = idx
