import json

from kivy.properties import ListProperty
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase

from libs.applibs.utils import load_kv


class ChatsTab(FloatLayout, MDTabsBase):

    users_data = ListProperty()


load_kv("chats.kv")