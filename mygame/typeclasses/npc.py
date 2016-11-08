# -*- coding:utf-8 -*-  

"""
Characters

Characters are (by default) Objects setup to be puppeted by Players.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
#from evennia import DefaultCharacter as Character
from  typeclasses.characters import Character 
#from characters import zhuCharacter

class Npc(Character):
    """
    A NPC typeclass which extends the character class.
    """
    def at_char_entered(self, character):
        """
         A simple is_aggressive check. 
         Can be expanded upon later.
        """       
        if self.db.is_aggressive:
            self.execute_cmd("say Graaah, die %s!" % character)
        else:
            self.execute_cmd("say %s大人您好，我是机器人,我要念李白的将进酒 !"% character)
