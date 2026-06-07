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
        try:
            #Check if the item is past its sell by date
            if item.sell_in < 0:
                #If it is, degrade quality twice as fast
                item.quality = max(0, item.quality - 2)
            else:
                #Otherwise, degrade quality normally
                item.quality = max(0, item.quality - 1)
            item.sell_in -= 1
        except Exception as e:
            print(f"Error updating normal item: {e}")

    def _update_aged_brie(self, item):
        try:    
            #Check if the item is past its sell by date
            if item.sell_in < 0:
                #If it is, increase quality twice as fast
                item.quality = min(50, item.quality + 2)
            else:
                #Otherwise, increase quality normally
                item.quality = min(50, item.quality + 1)
            item.sell_in -= 1
        except Exception as e:
            print(f"Error updating Aged Brie: {e}")

    def _update_backstage_pass(self, item):
        #Need to implement the logic for Backstage passes here
        pass

    def _update_sulfuras(self, item):
        #Sulfuras does not change in quality or sell_in
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
