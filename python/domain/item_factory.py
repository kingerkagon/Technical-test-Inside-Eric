# -*- coding: utf-8 -*-
from domain.items.regular_item import RegularItem
from domain.items.maturing_item import MaturingItem
from domain.items.backstage_pass import BackstagePass
from domain.items.constant_quality_item import ConstantQualityItem
from domain.items.conjured_item import ConjuredItem


class ItemFactory:
    ITEM_MAP = {
        "Aged Brie": MaturingItem,
        "Sulfuras, Hand of Ragnaros": ConstantQualityItem,
    }

    @staticmethod
    def create_item(item):
        if item.name in ItemFactory.ITEM_MAP:
            return ItemFactory.ITEM_MAP[item.name](item)
        if item.name.startswith("Conjured"):
            return ConjuredItem(item)
        if item.name.startswith("Backstage passes"):
            return BackstagePass(item)
        return RegularItem(item)