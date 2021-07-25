from simple_array.h_buy_sell_stock_twice import BuySellStockTwice


class TestBuySellStockTwice:
    def test_max_profit(self):
        bs = BuySellStockTwice()

        input = [12, 11, 13, 9, 12, 8, 14, 13, 15]
        result = bs.calculate(input)
        assert result == 10

        input = [1, 2, 3, 4, 5]
        result = bs.calculate(input)
        assert result == 4

    def test_decrease_price(self):
        bs = BuySellStockTwice()

        input = [7.6, 4, 3, 1]
        result = bs.calculate(input)
        assert result == 0
