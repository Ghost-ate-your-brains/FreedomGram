from kivymd.uix.card import MDCard
from kivymd.uix.navigationdrawer import MDNavigationDrawer

import utils

utils.load_kv("content_nav_drawer.kv")


class Card(MDCard):
    pass


class ContentNavigationDrawer(MDNavigationDrawer):
    """
    Content for NavigationDrawer.
    """
