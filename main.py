import pprint
import threading
import time
from pathlib import Path

from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.uix.label import Label


class SimpleClockApp(App):
    def update_time(self):
        self.lbl.text = time.strftime('%H:%M:%S')
        if self.root_size != self.lbl.size:
            self.root_size = self.lbl.size.copy()
            self.lbl.font_size = self.root_size[1] // 2

    def build(self):
        self.lbl = Label()
        self.root_size = self.lbl.size.copy()
        self.lbl.font_name = 'LCD'
        self.lbl.font_size = self.root_size[1] // 2
        return self.lbl

    def on_stop(self):
        super().on_stop()


if __name__ == '__main__':
    app = SimpleClockApp()
    LabelBase.register(name="LCD", fn_regular=str(Path(__name__).parent / "LCD.ttf"))
    Clock.schedule_interval(lambda x: app.update_time(), timeout=1)
    app.run()
