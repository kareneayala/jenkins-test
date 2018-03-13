def game(P1ayer1, Player2):
    """
    Enter values that represent the player choice
    Return p1 if player 1 wins otherway p2
    """
    if P1ayer1 == 'rock' and Player2 == 'rock':
        return 'empate'
    elif P1ayer1 == 'rock' and Player2 == 'scissor':
        return 'win Player1'
    elif P1ayer1 == 'rock' and Player2 == 'paper':
        return 'win Player1'
    elif P1ayer1 == 'scissor' and Player2 == 'scissor':
        return 'win empate'
    elif P1ayer1 == 'scissor' and Player2 == 'rock':
        return 'win Player2'
    elif P1ayer1 == 'scissor' and Player2 == 'paper':
        return 'win Player1'
    elif P1ayer1 == 'paper' and Player2 == 'paper':
        return 'empate'
    elif P1ayer1 == 'paper' and Player2 == 'rock':
        return 'win paper'
    elif P1ayer1 == 'paper' and Player2 == 'scissor':
        return 'win scissor'
    else: 
        return 'start new game'
