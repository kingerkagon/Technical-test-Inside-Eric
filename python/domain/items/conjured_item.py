# -*- coding: utf-8 -*-
from domain.items.regular_item import RegularItem

class ConjuredItem(RegularItem):
    def update(self):
        self.decrease_quality(2)
        self.decrease_sell_in()
        if self.item.sell_in < 0:
            self.decrease_quality(2)