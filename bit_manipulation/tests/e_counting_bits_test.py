from bit_manipulation.e_counting_bits import CountBits


class TestCountingBits:
    def test_invalid_input(self):
        cb = CountBits()
        ans = cb.calculate(-1)

        assert ans == []

    def test_default_inputs(self):
        cb = CountBits()

        ans = cb.calculate(0)
        assert ans == [0]

        ans = cb.calculate(1)
        assert ans == [0, 1]

    def test_lc_inputs(self):
        cb = CountBits()

        ans = cb.calculate(2)
        assert ans == [0, 1, 1]

        ans = cb.calculate(5)
        assert ans == [0, 1, 1, 2, 1, 2]

    def test_lc_inputs_caching(self):
        cb = CountBits()

        ans = cb.calculate_caching(2)
        assert ans == [0, 1, 1]

        ans = cb.calculate_caching(5)
        assert ans == [0, 1, 1, 2, 1, 2]
