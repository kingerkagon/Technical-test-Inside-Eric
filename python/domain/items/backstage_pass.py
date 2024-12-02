# -*- coding: utf-8 -*-
from domain.item_base import ItemBase

class BackstagePass(ItemBase):
    def update(self):
        if self.item.sell_in > 10:
            self.increase_quality()
        elif self.item.sell_in > 5:
            self.increase_quality(2)
        elif self.item.sell_in > 0:
            self.increase_quality(3)
        else:
            self.item.quality = 0
        self.decrease_sell_in()