from stack.m_decoded_string import DecodeString


class TestDecodeString:
    def test_lc_data_1(self):
        ds = DecodeString()

        ans = ds.valueAtIndex_bf("leet2code3", 15)
        assert ans == "e"

        ans = ds.valueAtIndex_opm("leet2code3", 15)
        assert ans == "e"

        ans = ds.valueAtIndex_opm_2("leet2code3", 15)
        assert ans == "e"

    def test_lc_data_2(self):
        ds = DecodeString()

        ans = ds.valueAtIndex_bf("ha22", 5)
        assert ans == "h"

    def test_lc_data_3(self):
        ds = DecodeString()

        ans = ds.valueAtIndex_bf("a2345678999999999999999", 1)
        assert ans == "a"

        ans = ds.valueAtIndex_opm("a2345678999999999999999", 18)
        assert ans == "a"

        ans = ds.valueAtIndex_opm_2("a2345678999999999999999", 18)
        assert ans == "a"

    def test_lc_data_4(self):
        ds = DecodeString()

        ans = ds.valueAtIndex_bf("test3code4", 15)
        assert ans == "d"
