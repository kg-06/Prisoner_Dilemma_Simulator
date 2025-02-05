import random

def always_cooperate(opponents_move):
    return "C"


def always_defect(opponents_move):
    return "D"


def tit_for_tat(opponents_move):
    if not opponents_move:
      return "C"
    return opponents_move[-1]

def double_tit_for_tat(opponents_move):
    if len(opponents_move)>=2 and opponents_move[-2]=="D" and opponents_move[-1]=="D":
        return "D"
    return "C"

def generous_tit_for_tat(opponents_move):
    if not opponents_move:
        return "C"
    if opponents_move[-1]=="D" and random.random()<0.3:
        return "C"
    return opponents_move[-1]

def sneaky_tit_for_tat(opponents_move):
    if not opponents_move:
        return "C"
    if len(opponents_move)>=3 and random.random()<0.2:
        return "D"
    return opponents_move[-1]

def lucifer(opponents_move):
    if(len(opponents_move)<=3):
        return "C"
    return "D"

def random_choice(opponents_move):
    return random.choice(["C","D"])

def friedman(opponents_move):
    if "D" in opponents_move:
        return "D"
    return "C"

def moses(opponents_move,state={}):    
    if state.get("defect",False):
        return "D"
        
    if len(opponents_move)>=2 and opponents_move[-2]=="D" and opponents_move[-1]=="D":
        state["defect"]=True
        return "D"
    return "C"

