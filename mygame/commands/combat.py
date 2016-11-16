# -*- coding:utf-8 -*-  
"""
1
        self.db.level = 1    等级
        self.db.HP = 100 生命
        self.db.XP = 0 经验值

        self.db.STR = randint(1, 10) 力量
        self.db.dex=randint(1, 10) 灵敏度

        self.db.combat = randint(5, 10) 战斗力

        精 hp 健康
        气 内力
        神 疲劳度
另外还有：http://www.spls.org/forums/t15768/
气 ： 113/ 113 (100%) 内力： 54 / 54 (+3)
神 ： 100/ 100 (100%) 法力： 23 / 33 (+1)
气和神的定义和用处可以参考 help basic，这里先简单的介绍
一下。气代表的是人的肉体，人必须有气才能生存。它会随年龄
变化，也受到内力影响。神就是人的精神，学习任何新的技能、
知识、武功都需要耗费神。内力是人的能量，当你学了基本内功
及特殊内功后应尽快将气转为内力储备起来。法力则是比较抽象
的精神上的能量，有了法力才能施展法术。祥见 help stats。

相关命令：exercise, meditate, enforce, enchant

learn
skills
    SKILLS = {"combat": skill_combat}
            "瑜伽",

dazuo

yunqi 瑜伽
    精 hp 健康
        气 内力
       ➕ 加神100 疲劳度 降低

skill
指定技能
    打坐
        增加气 降低神 减少一部分hp


    读书：
        诗歌
        增加智力
        疲劳


        外功
        治疗help＋
        疲劳－

    精气神


    拳法
    棍法
    剑法

practise
练习
你练习瑜伽头部运动





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