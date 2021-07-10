from bit_manipulation.e_reverse_bits import ReverseBits


class TestReverseBits:
    def test_alg_one(self):
        rv = ReverseBits()

        rev = rv.alg_one(43261596)
        assert rev == 964176192

        rev = rv.alg_one(4294967293)
        assert rev == 3221225471

    def test_alg_two(self):
        rv = ReverseBits()

        rev = rv.alg_two(43261596)
        assert rev == 964176192

        rev = rv.alg_two(4294967293)
        assert rev == 3221225471
