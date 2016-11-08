# -*- coding:utf-8 -*-  

"""
Room

Rooms are simple containers that has no location of their own.

"""

import random
from evennia import DefaultRoom, TICKER_HANDLER

#------------------------------------------------------------
#
# Weather room - room with a ticker
#
#------------------------------------------------------------


# These are rainy weather strings
ECHOES = (        
        "万里无云",
        "千骑卷云岗",
        "建立导图",
        "Bright fingers of lightning flash over the sky, moments later followed by a deafening rumble.",
        "It rains so hard you can hardly see your hand in front of you. You'll soon be drenched to the bone.",
        "Lightning strikes in several thundering bolts, striking the trees in the forest to your west.",
        "You hear the distant howl of what sounds like some sort of dog or wolf.",
        "Large clouds rush across the sky, throwing their load of rain over the world.")

class WeatherRoom(DefaultRoom):
    """
    This should probably better be called a rainy room...

    This sets up an outdoor room typeclass. At irregular intervals,
    the effects of weather will show in the room. Outdoor rooms should
    inherit from this.

    """
    def at_object_creation(self):
         TICKER_HANDLER.add(60 * 60, self.at_weather_update)

    def at_weather_update(self, *args, **kwargs):
        "ticked at regular intervals"
        echo = random.choice(ECHOES)
        self.msg_contents(echo)