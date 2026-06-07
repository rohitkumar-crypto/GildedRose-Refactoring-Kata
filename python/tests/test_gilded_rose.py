# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

# Helper function to run the update_quality method for a given number of days
def run_days(items, days=1):
    shop = GildedRose(items)
    for _ in range(days):
        shop.update_quality()
    return items


#Normal items
class TestNormalItem(unittest.TestCase):

    def test_quality_decreases_by_1_before_sell_date(self):
        items = run_days([Item("Elixir of the Mongoose", sell_in=10, quality=20)])
        self.assertEqual(19, items[0].quality)
        self.assertEqual(9, items[0].sell_in)

    def test_quality_decreases_by_2_after_sell_date(self):
        # sell_in starts at 0 → after one day it is -1 (past sell date)
        items = run_days([Item("Elixir of the Mongoose", sell_in=0, quality=20)])
        self.assertEqual(18, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_quality_never_goes_below_zero(self):
        items = run_days([Item("Elixir of the Mongoose", sell_in=5, quality=0)])
        self.assertEqual(0, items[0].quality)


# Aged Brie
class TestAgedBrie(unittest.TestCase):

    def test_quality_increases_by_1_before_sell_date(self):
        items = run_days([Item("Aged Brie", sell_in=10, quality=20)])
        self.assertEqual(21, items[0].quality)
        self.assertEqual(9, items[0].sell_in)

    def test_quality_increases_by_2_after_sell_date(self):
        items = run_days([Item("Aged Brie", sell_in=0, quality=20)])
        self.assertEqual(22, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_quality_never_exceeds_50(self):
        items = run_days([Item("Aged Brie", sell_in=10, quality=50)])
        self.assertEqual(50, items[0].quality)



# Sulfuras
class TestSulfuras(unittest.TestCase):

    def test_quality_never_changes(self):
        items = run_days([Item("Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)])
        self.assertEqual(80, items[0].quality)

    def test_sell_in_never_changes(self):
        items = run_days([Item("Sulfuras, Hand of Ragnaros", sell_in=10, quality=80)])
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(80, items[0].quality)


# Backstage passes
class TestBackstagePass(unittest.TestCase):
    NAME = "Backstage passes to a TAFKAL80ETC concert"
    def test_quality_increases_by_1_more_than_10_days_before_sell_date(self):
        items = run_days([Item(self.NAME, sell_in=15, quality=20)])
        self.assertEqual(21, items[0].quality)
        self.assertEqual(14, items[0].sell_in)

    def test_quality_increases_by_2_between_10_and_5_days_before_sell_date(self):
        items = run_days([Item(self.NAME, sell_in=10, quality=20)])
        self.assertEqual(22, items[0].quality)
        self.assertEqual(9, items[0].sell_in)
    
    def test_quality_increases_by_3_between_5_and_0_days_before_sell_date(self):
        items = run_days([Item(self.NAME, sell_in=5, quality=20)])
        self.assertEqual(23, items[0].quality)
        self.assertEqual(4, items[0].sell_in)
    
    def test_quality_drops_neve_exceeds_50(self):
        items = run_days([Item(self.NAME, sell_in=5, quality=49)])
        self.assertEqual(50, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

# Conjured items
class TestConjuredItem(unittest.TestCase):
    def test_quality_decreases_by_2_before_sell_date(self):
        items = run_days([Item("Conjured Mana Cake", sell_in=10, quality=20)])
        self.assertEqual(18, items[0].quality)
        self.assertEqual(9, items[0].sell_in)

    def test_quality_decreases_by_4_after_sell_date(self):
        items = run_days([Item("Conjured Mana Cake", sell_in=0, quality=20)])
        self.assertEqual(16, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_quality_never_goes_below_zero(self):
        items = run_days([Item("Conjured Mana Cake", sell_in=5, quality=1)])
        self.assertEqual(0, items[0].quality)

   
if __name__ == '__main__':
    unittest.main()