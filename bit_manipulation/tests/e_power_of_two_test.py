from bit_manipulation.e_power_of_two import PowerOfTwo


class TestPowerOfTwo:
    def test_alg(self):
        powerOfTwo = PowerOfTwo()

        result = powerOfTwo.calculate(64)
        assert result is True

        result = powerOfTwo.calculate(14)
        assert result is False

        result = powerOfTwo.calculate(45)
        assert result is False

        result = powerOfTwo.calculate(-32)
        assert result is False
