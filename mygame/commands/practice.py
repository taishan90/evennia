# -*- coding:utf-8 -*-

"""

指令格式：practice <技能种类>

这个指令让你练习某个种类的技能，这个技能必须是经过 enable 的专业技能。

如果你该项的基本技能足够高，可以经由练习直接升级，而且升级的上限只跟
你基本技能的等级有关，换句话说，勤加练习是使你的所学「青出于蓝胜于蓝」
的唯一途径，当然，在这之前你必须从实际运用中获得足够的经验以提升你的基
本技能。
TEXT

"""
import random
from django.conf import settings

from evennia import Command

ECHOES = (
        "祈祷式,挺身直立，双脚并拢。双手胸前合掌。放松全身。调匀呼吸。建立集中和宁静的状态，为要做的练习做准备。",
        "祈祷式,挺身直立，双脚并拢。双手胸前合掌。放松全身。调匀呼吸。建立集中和宁静的状态，为要做的练习做准备。",
        "祈祷式,挺身直立，双脚并拢。双手胸前合掌。放松全身。调匀呼吸。建立集中和宁静的状态，为要做的练习做准备。",
        "祈祷式,挺身直立，双脚并拢。双手胸前合掌。放松全身。调匀呼吸。建立集中和宁静的状态，为要做的练习做准备。")

_TXTDIR = None

class Cmdpractice(Command):
    """
    initiates combat

    Usage:
      attack <target>

    This will initiate combat with <target>. If <target is
    already in combat, you will join the combat.
    """
    key = "practice"
    help_category = "General"

    def func(self):
        "Handle command"
        if not self.args:
            self.caller.msg("Usage: practice <target>")
            return

        # 搜索技能，学过的
        skill=self.args.lstrip(' ')
        """

        target = self.caller.search(self.args.lstrip(' '))

        if not target:
            return
        """
        # 如果已经练功
        if self.caller.ndb.pratice_handler:
            # target is already in combat - join it
            target.ndb.combat_handler.add_character(self.caller)
            target.ndb.combat_handler.msg_all("%s 正在练习中!" % self.caller)
        else:
            #等待
            #self.caller.ndb.pratice_handler
            #wait(3)

            # create a new combat handler
            #chandler = create_script("combat_handler.CombatHandler")

            #chandler.add_character(self.caller)
            #chandler.add_character(target)
            #读取技能名称和动作要领
            echo = random.choice(ECHOES)
            msg = "%s开始练习%s。%s"
            messages=(msg % (self.caller ,'' ,''))

            self.caller.msg(messages)

            import re,os

            global _TXTDIR
            if not _TXTDIR:
                from django.conf import settings
                _TXTDIR = settings.TXTDIR

            filename = os.path.join(_TXTDIR, "yujia.txt")
            f = open(filename)
            s = f.read()
            s1 = re.split(' ', s)  # 利用正则函数进行分割
            for i in s1:
                self.caller.msg(i)





