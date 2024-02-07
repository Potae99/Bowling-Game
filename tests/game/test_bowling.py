"""Test module for the Bowling Kata. """

#Standard Library

#3rd Party Library

#Project Library
from game.bowling import BowlingGame


#-----------------------------------------------------------------------------


def test_constuctor():
    """Construct a BowlingGame object.

    Given: -
    When: Construct a BowlingGame object.
    Then: The initial score must be 0.
    
    """
    #Arrang

    excepted_initial_score = 0

    #Act

    game = BowlingGame()

    #Assert

    result = game.score()

    assert result == excepted_initial_score