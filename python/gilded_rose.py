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
        #Need to implement the logic for normal items here
        pass

    def _update_aged_brie(self, item):
        #Need to implement the logic for Aged Brie here
        pass
    

    def _update_backstage_pass(self, item):
        #Need to implement the logic for Backstage passes here
        pass

    def _update_sulfuras(self, item):
        #Need to implement the logic for Sulfuras here
        pass

    def _update_conjured(self, item):
        #Need to implement the logic for Conjured items here
        pass


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
