import pytest
import number_guessing_game

def test_guess_number():
    assert number_guessing_game.guess_number(50, 40) == "Too low!"
    assert number_guessing_game.guess_number(50, 60) == "Too high!"
    assert number_guessing_game.guess_number(50, 50) == "Congratulations! You guessed it!"

def test_generate_number():
    number = number_guessing_game.generate_number()
    assert 1 <= number <= 100
    assert 1 <= number <= 10 # there is a posebelity of ereur