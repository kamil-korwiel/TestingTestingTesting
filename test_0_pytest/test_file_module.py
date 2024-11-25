import pytest

@pytest.mark.usefixtures("setupmethod")
class TestModule:
    def test_m_1(self):
        print("calling inside test test_module")
        # assert False

    def test_m_2(self):
        print("usadofa")
        # assert False

