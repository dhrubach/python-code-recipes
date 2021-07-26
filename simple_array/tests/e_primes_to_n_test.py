from simple_array.e_primes_to_n import PrimeNumber


class TestPrimeNumber:
    def test_generate_primes(self):
        pn = PrimeNumber()

        input = 10
        result = pn.generate_primes(input)
        assert result[0] == 4
        assert result[1] == [2, 3, 5, 7]
