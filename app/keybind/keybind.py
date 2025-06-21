from __future__ import annotations
import keyboard
from typing import Iterable

class Keybind:
    def __init__(self, key: str, bind):
        self.key = key
        self.bind = lambda e: bind()

    @staticmethod
    def SetupKeybinds(keybinds: Iterable[Keybind]):
        for keybind in keybinds:
            keyboard.on_press_key(keybind.key, keybind.bind)

class ScouterBinds:
    def __init__(self, restartHD2: str = None):
        self.restartHD2 = restartHD2