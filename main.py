from strategies import *
from tournament import tournament

if __name__=="__main__":
    strategies={
        "Always Cooperate": always_cooperate,
        "Always Defect" : always_defect,
        "Tit for Tat": tit_for_tat,
        "Double Tit for Tat": double_tit_for_tat,
        "Generous Tit for Tat": generous_tit_for_tat,
        "Moses": moses,
        "Random": random_choice,
        "Sneaky Tit for Tat": sneaky_tit_for_tat,
        "Lucifer": lucifer,
        "Friedman": friedman,  
    }

    results= tournament(strategies,rounds=10)

    print("\nFinal Leaderboard:")
    for name,score in sorted(results.items(), key=lambda x:x[1],reverse=True):
        print(f"{name}: {score} points")