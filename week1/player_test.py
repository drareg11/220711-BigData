#File created to include unit code to test each unit of code
#something behaioral that we can see in our code to modify the state 

from player import Player
import unittest

class TestPlayer(unittest.Testcase):
    def test_attack(self):
        p1 = Player("Fred", 10, 10, 5)
        self.assertEquzl(p1.attack(), 20)


if __name__ == '__main__':
    unittest.main()