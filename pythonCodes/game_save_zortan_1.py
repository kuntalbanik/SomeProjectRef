"""
Zortan is under attack by Thanos and the Avengers are trying to save.
Avengers can attack only in pairs.
There are only three chances to attack on thanos.

Avengers need to kill to win the game or 
else Thanos will kill avengers and captured zortan.
"""

# import the requirements
from typing import Final

# declare our constraints
IRONMAN_ATTACK_POWER: Final[int] = 250
BLACKWIDOW_ATTACK_POWER: Final[int] = 180
SPIDERMAN_ATTACK_POWER: Final[int] = 190
HULK_ATTACK_POWER: Final[int] = 300

thanos_life: int = 1500
choice: int = 0
attack_number: int = 0

# declare helper message
MSG = """
--------------------------
Enter attack combination

1) Ironman & Black Widow
2) Black Widow & Spiderman
3) Spiderman & Hulk
4) Hulk & Ironman
--------------------------
"""
