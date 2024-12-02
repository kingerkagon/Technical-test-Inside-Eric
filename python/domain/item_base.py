# -*- coding: utf-8 -*-
class ItemBase:
    def __init__(self, item):
        self.item = item

    def update(self):
        raise NotImplementedError("Subclass was not implemented")

    def increase_quality(self, amount=1):
        self.item.quality = min(50, self.item.quality + amount)

    def decrease_quality(self, amount=1):
        self.item.quality = max(0, self.item.quality - amount)

    def decrease_sell_in(self):
        self.item.sell_in -= 1