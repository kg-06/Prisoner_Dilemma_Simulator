from payoff import payoff_matrix

def play_game(strategy_A, strategy_B,rounds=10):
    history_A,history_B=[],[]
    score_A,score_B=0,0

    for _ in range(rounds):
        move_A= strategy_A(history_B)
        move_B= strategy_B(history_A)

        payoff_A,payoff_B=payoff_matrix[(move_A,move_B)]
        score_A+=payoff_A
        score_B+=payoff_B

        history_A.append(move_A)
        history_B.append(move_B)

    return score_A,score_B