import game from game
def test_game_01():
    assert game('rock', 'scissor') == 'win Player1' , 'Player 1 should win'
    assert game('scissor', 'rock') =='win Player2' , 'Unexpected result'
    assert game('scissor', 'paper') == 'win Player1' , 'Unexpected result'
    assert game('rock', 'rock') == 'empate' , 'se debio imprimir empate'
