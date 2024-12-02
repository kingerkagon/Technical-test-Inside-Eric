# -*- coding: utf-8 -*-
from domain.item_base import ItemBase

class MaturingItem(ItemBase):
    def update(self):
        self.increase_quality()
        self.decrease_sell_in()
        if self.item.sell_in < 0:
            self.increase_quality()