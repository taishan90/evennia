import random
from evennia import DefaultScript


class Weather(DefaultScript):
    """Displays weather info. Meant to be attached to a room."""

    def at_script_creation(self):
        self.key = "weather_script"
        self.desc = "Gives random weather messages."
        self.interval = 60 * 5  # every 5 minutes
        self.persistent = True

    def at_repeat(self):
        "called every self.interval seconds."
        rand = random.random()
        if rand < 0.5:
            weather = "A faint breeze is felt."
        elif rand < 0.7:
            weather = "Clouds sweep across the sky."
        else:
            weather = "There is a light drizzle of rain."
        # send this message to everyone inside the object this
        # script is attached to (likely a room)
        self.obj.msg_contents(weather)