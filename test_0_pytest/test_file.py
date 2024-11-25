import pytest

@pytest.mark.usefixtures("setupmethod")
class TestSample:
    def test1(self,setupmethod):
        print("calling inside test test1")
        print("waps")
        print(setupmethod, "loss")
        # assert False

    def test2(self):
        print("calling inside test tes`enter code here`t2")
        # assert False
        
class TestSemplago:
    def test_uno(self):
        print("uuuuuuuuuuuuuu")
        # assert False

    def test_dos(self):
        print("espaniole ???")
        # assert False

