from simple_array.advance_by_offsets import AdvanceByOffsets


class TestAdvanceByOffsets:
    def test_can_reach_end(self):
        adv = AdvanceByOffsets()

        arr = [3, 3, 1, 0, 2, 0, 1]
        isEndReachable = adv.can_reach_end(arr)
        assert isEndReachable is True

        arr = [3, 2, 0, 0, 2, 0, 1]
        isEndReachable = adv.can_reach_end(arr)
        assert isEndReachable is False
