# -*- coding: utf-8 -*-
from domain.item_factory import ItemFactory

class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            ItemFactory.create_item(item).update()