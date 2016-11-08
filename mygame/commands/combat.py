# -*- coding:utf-8 -*-  
"""





"""
from django.conf import settings
from evennia import Command
from world import rules

from evennia import create_script
from typeclasses import zklog

        
 
class CmdAttack(Command):
    """
    initiates combat

    Usage:
      attack <target>

    This will initiate combat with <target>. If <target is
    already in combat, you will join the combat. 
    """
    key = "attack"
    help_category = "General"

    def func(self):
        "Handle command"
        if not self.args:
            self.caller.msg("Usage: attack <target>")            
            return



        target=self.caller.search(self.args.lstrip(' '))


        
        if not target:
            return
        # set up combat
        if target.ndb.combat_handler:
            # target is already in combat - join it            
            target.ndb.combat_handler.add_character(self.caller)
            target.ndb.combat_handler.msg_all("%s joins combat!" % self.caller)
        else:
            # create a new combat handler
            chandler = create_script("combat_handler.CombatHandler")


            chandler.add_character(self.caller)
            chandler.add_character(target)
            self.caller.msg("You attack %s! You are in combat." %target)
            target.msg("%s attacks you! You are in combat." % self.caller)


def zkcmd(a, target):
    ok = a.ndb.combat_handler.add_action("hit",
                                         a,
                                         target)
    if ok:
        a.msg("You add 'hit' to the combat queue")
    else:
        a.msg("You can only queue two actions per turn!")

    # tell the handler to check if turn is over
    a.ndb.combat_handler.check_end_turn()

class CmdHit(Command):
    """
    hit an enemy

    Usage:
      hit <target>

    Strikes the given enemy with your current weapon.
    """
    key = "hit"
    aliases = ["strike", "slash"]
    help_category = "combat"
    def func(self):
        "Implements the command"
        if not self.args:
            self.caller.msg("Usage: hit <target>")
            return 
        
       
        
        
        #返回目标的所在位置
        target = self.caller.search(self.args.lstrip(' '))


        if not target:
            return
        zkcmd(self.caller,target)
        """
        ok = self.caller.ndb.combat_handler.add_action("hit", 
                                                       self.caller,
                                                       target)
        if ok:
            self.caller.msg("You add 'hit' to the combat queue")
        else:
            self.caller.msg("You can only queue two actions per turn!")

        # tell the handler to check if turn is over
        self.caller.ndb.combat_handler.check_end_turn()
        """


class CmdParry(Command):
    """
    hit an enemy

    Usage:
      hit <target>

    Strikes the given enemy with your current weapon.
    """
    key = "parry"
    aliases = ["par", "dang"]
    help_category = "combat"

    def func(self):
        "Implements the command"
        if not self.args:
            self.caller.msg("Usage: %s <target>"%  self.key)
            return

        target = self.caller.search(self.args.lstrip(' '))

        if not target:
            return
        zkcmd(self.caller, target)
        
        
class CmdDefend(Command):
    """
    hit an enemy

    Usage:
      hit <target>

    Strikes the given enemy with your current weapon.
    """
    key = "defend"
    aliases = ["def", "fang"]
    help_category = "combat"

    def func(self):
        "Implements the command"




        zkcmd(self.caller, None)
class CmdFeint(Command):
    """
    hit an enemy

    Usage:
      hit <target>

    Strikes the given enemy with your current weapon.
    """
    key = "feint"
    aliases = ["f"]
    help_category = "combat"

    def func(self):
        "Implements the command"

        zkcmd(self.caller, None)


class CmdDisengage(Command):
    """
    hit an enemy

    Usage:
      hit <target>

    Strikes the given enemy with your current weapon.
    """
    key = "flee"
    aliases = ["dis"]
    help_category = "combat"

    def func(self):
        "Implements the command"

        zkcmd(self.caller, None)




        
from evennia import CmdSet
from evennia import default_cmds

class CombatCmdSet(CmdSet):
    key = "combat_cmdset"
    mergetype = "Replace"
    priority = 10 
    no_exits = True

    def at_cmdset_creation(self):
        self.add(CmdHit())
        self.add(CmdParry())
        self.add(CmdFeint())
        self.add(CmdDefend())
        self.add(CmdDisengage())    
        #self.add(CmdHelp())
        
        self.add(default_cmds.CmdPose())
        self.add(default_cmds.CmdSay())