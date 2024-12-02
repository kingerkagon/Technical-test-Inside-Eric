# -*- coding: utf-8 -*-
from domain.item_base import ItemBase

class RegularItem(ItemBase):
    def update(self):
        self.decrease_quality()
        self.decrease_sell_in()
        if self.item.sell_in < 0:
            self.decrease_quality()