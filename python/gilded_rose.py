# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                self._update_sulfuras(item)
            elif item.name == "Aged Brie":
                self._update_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._update_backstage_pass(item)
            elif "Conjured" in item.name:
                self._update_conjured(item)
            else:
                self._update_normal(item)

    def _update_normal(self, item):
        if item.sell_in <= 0:
            item.quality = max(0, item.quality - 2)
        else:
            item.quality = max(0, item.quality - 1)
        item.sell_in -= 1

    def _update_aged_brie(self, item):
        if item.sell_in <= 0:
            item.quality = min(50, item.quality + 2)
        else:
            item.quality = min(50, item.quality + 1)
        item.sell_in -= 1

    def _update_backstage_pass(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality = min(50, item.quality + 3)
        elif item.sell_in <= 10:
            item.quality = min(50, item.quality + 2)
        else:
            item.quality = min(50, item.quality + 1)
        item.sell_in -= 1

    def _update_sulfuras(self, item):
        pass

    def _update_conjured(self, item):
        if item.sell_in <= 0:
            item.quality = max(0, item.quality - 4)
        else:
            item.quality = max(0, item.quality - 2)
        item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
