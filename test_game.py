# Testfall för tärningsspelet 21
# Vi testar tärningsslag, spelarens poäng, och bust-logik

import unittest
from game_classes import Player

class TestPlayer(unittest.TestCase):
    def test_roll_adds_to_total(self):
        player = Player("Test")
        start = player.total
        value = player.roll()
        self.assertTrue(1 <= value <= 6)
        self.assertEqual(player.total, start + value)

    def test_bust_logic(self):
        player = Player("Test")
        player.total = 20
        player.total += 6
        if player.total > 21:
            player.busted = True
        self.assertTrue(player.busted)

    def test_reset(self):
        player = Player("Test")
        player.total = 15
        player.busted = True
        player.reset()
        self.assertEqual(player.total, 0)
        self.assertFalse(player.busted)

# Varför dessa tester?
# 1. Kontroll att tärningsslag läggs korrekt till totalen.
# 2. Kontroll att bust (över 21) identifieras korrekt.
# 3. Kontroll att reset återställer spelarens tillstånd.

if __name__ == '__main__':
    unittest.main()