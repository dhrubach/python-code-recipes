from bit_manipulation.m_powx_n import Powxn


class TestPowxn:
    def test_alg(self):
        powxn = Powxn()

        result = powxn.calculate(2, 10)
        assert result == 1024
