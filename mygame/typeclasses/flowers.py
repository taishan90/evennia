# -*- coding:utf-8 -*-  

"""
Characters

Characters are (by default) Objects setup to be puppeted by Players.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from typeclasses.objects import Object

class Rose(Object):
        """
        This creates a simple rose object        
        """    
        def at_object_creation(self):
            "this is called only once, when object is first created"
            # add a persistent attribute 'desc' 
            # to object (silly example).
            self.db.desc = "This is a pretty rose with thorns." 
            #          self.db.    
