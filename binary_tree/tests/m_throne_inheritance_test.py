from binary_tree.m_throne_inheritance import ThroneInheritance


class TestThroneInheritance:
    def test_lc_data_1(self):
        ti = ThroneInheritance("king")
        ti.birth("king", "andy")
        ti.birth("king", "bob")
        ti.birth("king", "catherine")
        ti.birth("andy", "matthew")
        ti.birth("bob", "alex")
        ti.birth("bob", "asha")

        curOrder = ti.getInheritanceOrder()
        assert curOrder == [
            "king",
            "andy",
            "matthew",
            "bob",
            "alex",
            "asha",
            "catherine",
        ]

        ti.death("bob")

        curOrder = ti.getInheritanceOrder()
        assert curOrder == ["king", "andy", "matthew", "alex", "asha", "catherine"]

    def test_lc_data_2(self):
        ti = ThroneInheritance("king")

        curOrder = ti.getInheritanceOrder()
        assert curOrder == ["king"]

        ti.death("king")
        curOrder = ti.getInheritanceOrder()
        assert curOrder == []

    def test_lc_data_3(self):
        ti = ThroneInheritance("king")
        ti.birth("king", "andy")
        ti.birth("king", "bob")
        ti.birth("king", "catherine")
        ti.death("bob")
        ti.birth("andy", "matthew")
        ti.birth("catherine", "alex")

        curOrder = ti.getInheritanceOrder()
        assert curOrder == [
            "king",
            "andy",
            "matthew",
            "catherine",
            "alex",
        ]
