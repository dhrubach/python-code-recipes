from stack.m_online_stock_span import StockSpanner


class TestStockSpanner:
    def test_stock_span(self):
        sp = StockSpanner()
        sp.next(100)
        sp.next(80)
        sp.next(60)

        assert sp.next(70) == 2

        sp.next(60)

        assert sp.next(75) == 4
        assert sp.next(85) == 6
