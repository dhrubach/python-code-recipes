from simple_array.e_buy_sell_stock_once import BuySellStock


class TestBuySellStock:
    def test_max_profit(self):
        bs = BuySellStock()

        input = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
        result = bs.calculate(input)
        assert result == 30

    def test_decrease_price(self):
        bs = BuySellStock()

        input = [310, 300, 290, 280, 270]
        result = bs.calculate(input)
        assert result == 0
