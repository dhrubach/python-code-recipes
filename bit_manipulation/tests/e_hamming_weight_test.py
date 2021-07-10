from bit_manipulation.e_hamming_weight import HammingWeight


class TestHammingWeight:
    def test_calculate(self):
        hm = HammingWeight()

        hweight = hm.calculate(11)
        assert hweight == 3
