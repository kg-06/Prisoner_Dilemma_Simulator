from game import play_game

def tournament(strategies,rounds=10):
    scores={name:0 for name in strategies}

    for name_A,strategy_A in strategies.items():
        for name_B, strategy_B in strategies.items():
            score_A, score_B= play_game(strategy_A,strategy_B,rounds)
            scores[name_A]+=score_A
            scores[name_B]+=score_B
    
    return scores