00 [-] AmpServerFactory starting on 5000
2016-10-30T10:45:20+0000 [evennia.server.amp.AmpServerFactory#info] Starting factory <evennia.server.amp.AmpServerFactory instance at 0x102778a70>
2016-10-30T10:45:20+0000 [-] Website starting on 5001
2016-10-30T10:45:20+0000 [evennia.server.webserver.Website#info] Starting factory <evennia.server.webserver.Website instance at 0x1027dd758>
2016-10-30T10:45:21+0000 [evennia.server.amp.AmpServerFactory] AMPProtocol connection established (HOST:IPv4Address(TCP, '127.0.0.1', 5000) PEER:IPv4Address(TCP, '127.0.0.1', 61863))
2016-10-30T10:45:21+0000 [stdout#info] ('typeclasses', <class 'mygame.typeclasses.trainscript.TrainStoppedScript'>)
2016-10-30T10:45:21+0000 [stdout#info] ('typeclasses', <class 'mygame.typeclasses.trainscript.TrainDrivingScript'>)
2016-10-30T10:45:21+0000 [stdout#info] ('typeclasses', <class 'mygame.typeclasses.combat_handler.CombatHandler'>)
2016-10-30T10:45:21+0000 [stdout#info] ('typeclasses', <class 'mygame.typeclasses.train.TrainObject'>)
2016-10-30T10:45:21+0000 [AMPProtocol,0,127.0.0.1] [::] Traceback (most recent call last):
2016-10-30T10:45:21+0000 [AMPProtocol,0,127.0.0.1] [::]   File "/Volumes/data/mountain-sea/evennia/evennia/evennia/scripts/scripts.py", line 408, in unpause
2016-10-30T10:45:21+0000 [AMPProtocol,0,127.0.0.1] [::]     self.at_start()
2016-10-30T10:45:21+0000 [AMPProtocol,0,127.0.0.1] [::]   File "/Volumes/data/mountain-sea/evennia/evennia/mygame/typeclasses/combat_handler.py", line 58, in at_start
2016-10-30T10:45:21+0000 [AMPProtocol,0,127.0.0.1] [::]     for character in self.db.characters.values():
2016-10-30T10:45:21+0000 [AMPProtocol,0,127.0.0.1] [::] AttributeError: 'NoneType' object has no attribute 'values'
2016-10-30T10:45:37+0000 [stdout#info] ('typeclasses', <class 'typeclasses.characters.Character'>)
2016-10-30T10:45:37+0000 [stdout#info] ('typeclasses', <class 'typeclasses.characters.zhuCharacter'>)
2016-10-30T10:45:37+0000 [stdout#info] ('typeclasses', <class 'typeclasses.npc.Npc'>)
2016-10-30T10:45:37+0000 [stdout#info] ('typeclasses', <class 'typeclasses.rooms.Room'>)
2016-10-30T10:45:37+0000 [stdout#info] ('typeclasses', <class 'typeclasses.exits.Exit'>)