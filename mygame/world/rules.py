# -*- coding:utf-8 -*-  
import random

# messages 
# messages
from typeclasses import zklog

from random import randint

def roll_hit():
    "Roll 1d100"
    return randint(1, 100)

def roll_dmg():
    "Roll 1d6"
    return randint(1, 6)

def check_defeat(character):
    "Checks if a character is 'defeated'."
    if character.db.HP <= 0:
       character.msg("You fall down, defeated!")
       character.db.HP = 100   # reset

def add_XP(character, amount):
    "Add XP to character, tracking level increases."
    character.db.XP += amount
    if character.db.XP >= (character.db.level + 1) ** 2:
        character.db.level += 1
        character.db.STR += 1
        character.db.combat += 2
        character.msg("You are now level %i!" % character.db.level)

def skill_combat(*args):
    """
    This determines outcome of combat. The one who
    rolls under their combat skill AND higher than
    their opponent's roll hits. 
    """     
    char1, char2 = args
    roll1, roll2 = roll_hit(), roll_hit()        
    failtext = "You are hit by %s for %i damage!"
    wintext = "You hit %s for %i damage!"
    xp_gain = randint(1, 3)
    if char1.db.combat >= roll1 > roll2:
        # char 1 hits
        dmg = roll_dmg() + char1.db.STR
        char1.msg(wintext % (char2, dmg))        
        add_XP(char1, xp_gain)
        char2.msg(failtext % (char1, dmg))
        char2.db.HP -= dmg
        check_defeat(char2) 
    elif char2.db.combat >= roll2 > roll1:
        # char 2 hits
        dmg = roll_dmg() + char2.db.STR
        char1.msg(failtext % (char2, dmg))
        char1.db.HP -= dmg
        check_defeat(char1)
        char2.msg(wintext % (char1, dmg))       
        add_XP(char2, xp_gain) 
    else:
        # a draw
        drawtext = "Neither of you can find an opening."
        char1.msg(drawtext)
        char2.msg(drawtext)    

def skill_yunqi(*args):
    """
    运气（瑜伽、易筋经）

        治疗help＋
        疲劳－
    """
def skill_dazuo(*args):
    """
    运气（瑜伽、易筋经）

        治疗help＋
        疲劳－
    """
SKILLS = {"combat": skill_combat,"dazuo":skill_dazuo ,"yuqi":skill_yunqi}



def roll_challenge(character1, character2, skillname):
    """
    Determine the outcome of a skill challenge between
    two characters based on the skillname given. 
    """
    if skillname in SKILLS:
        SKILLS[skillname](character1, character2)
    else: 
        raise RunTimeError("Skillname %s not found." % skillname)


def resolve_combat(combat_handler, actiondict):
    """
    This is called by the combat handler
    actiondict is a dictionary with a list of two actions
    for each character:
    {char.id:[(action1, char, target), (action2, char, target)], ...}
    """
    #_functionId(actiondict)
    zklog.zkprint("resolve_combat")
    flee = {} # track number of flee commands per character
    for isub in range(2):
         # loop over sub-turns
         messages = []

         zklog.zkprint(["actiondict",locals()["actiondict"]])



         for subturn in (sub[isub] for sub in actiondict.values()):
             # for each character, resolve the sub-turn
             action, char, target = subturn
             taction=""
             tchar=""
             ttarget=""
             zklog.zkprint(["target",target])

             if target: 
                 taction, tchar, ttarget = actiondict[target.id][isub]


             if action == "hit":
                 if taction == "parry" and ttarget == char:
                    msg = "%s tries to hit %s, but %s parries the attack!" 
                    messages.append(msg % (char, tchar, tchar))
                 elif taction == "defend" and roll_dmg() < 4:
                     msg = "%s defends against the attack by %s."
                     messages.append(msg % (tchar, char))
                 elif taction == "flee":
                     msg = "%s stops %s from disengaging, with a hit!"
                     flee[tchar] = -2
                     messages.append(msg % (char, tchar))
                 else:
                     msg = "%s hits %s, bypassing their %s!"
                     messages.append(msg % (char, tchar, taction))
             elif action == "parry":
                  if taction == "hit":
                      msg = "%s parries the attack by %s."
                      messages.append(msg % (char, tchar))                
                  elif taction == "feint":
                      msg = "%s tries to parry, but %s feints and hits!"
                      messages.append(msg % (char, tchar))
                  else:
                      msg = "%s parries to no avail."
                      messages.append(msg % char)
             elif action == "feint":
                  if taction == "parry":
                      msg = "%s feints past %s's parry, landing a hit!"
                      messages.append(msg % (char, tchar))
                  elif taction == "hit":
                      msg = "%s feints but is defeated by %s hit!"
                      messages.append(msg % (char, tchar))
                  else:
                      msg = "%s feints to no avail."
                      messages.append(msg % char)
             elif action == "defend":
                  msg = "%s defends."
                  messages.append(msg % char)
             elif action == "flee":
                  if char in flee:
                      flee[char] += 1
                  else:
                      flee[char] = 1
                  msg = "%s tries to disengage (two subsequent turns needed)"
                  messages.append(msg % char)
             else :
                print("108")
                print ([target,action,taction, tchar, ttarget])
                msg = " 出现其他情况，请管理员处理"
        # echo results of each subturn
    combat_handler.msg_all("\n".join(messages))

    # at the end of both sub-turns, test if anyone fled
    msg = "%s withdraws from combat."
    for (char, fleevalue) in flee.items():
        if fleevalue == 2:
            combat_handler.msg_all(msg % char)
            combat_handler.remove_character(char)