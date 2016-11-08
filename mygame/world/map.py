#mygame/world/map.py

SYMBOLS = {
        'you' : '[@]',
    'SECT_INSIDE': '[.]'
}

class Map(object):

    def __init__(self, ch, max_width=9, max_length=9):
        self.ch = ch
        self.max_width = max_width
        self.max_length = max_length
        self.worm_has_mapped = {}
        self.curX = None
        self.curY = None

        if self.check_grid():
            # we actually have to store the grid into variable
            self.grid = self.create_grid()
            self.draw_room_on_map(ch.location, 
                                 ((min(max_width, max_length) -1 ) / 2))

    def update_pos(self, room, exit_name):
        # this ensures the pointer variables always 
        # stays up to date to where the worm is currently at.
        self.curX, self.curY = \
           self.worm_has_mapped[room][0], self.worm_has_mapped[room][1]

        # now we have to actually move the pointer 
        # variables depending on which 'exit' it found
        if exit_name == 'east':
            self.curY += 1
        elif exit_name == 'west':
            self.curY -= 1
        elif exit_name == 'north':
            self.curX -= 1
        elif exit_name == 'south':
            self.curX += 1

    def draw_room_on_map(self, room, max_distance):
        self.draw(room)

        if max_distance == 0:
            return
        for exit in self.get_all_room_exits(room):
            if self.has_drawn(exit.destination): continue

            # this setup doesn't support exits that are 'up' or 'down' it 
            # makes the map all funky. So if it encounters an exit named up/down 
            # it simply skips it. It would be a great project if someone want 
            # to implement it! 
            if exit.name.lower == 'up' or exit.name.lower() == 'down': continue
            self.update_pos(room, exit.name.lower())
            self.draw_room_on_map(exit.destination, max_distance - 1)

    def draw(self, room):
        # draw initial ch location on map first!
        if room == self.ch.location:
            self.start_loc_on_grid()
            self.worm_has_mapped[room] = [self.curX, self.curY]

        # map all other rooms
        self.worm_has_mapped[room] = [self.curX, self.curY]
        print(self.curX)
        print(self.curY)
        print(self.grid)
        #print(room.db.sector_type)
        #self.grid[self.curX][self.curY] = SYMBOLS[room.db.sector_type]
        self.grid[self.curX][self.curY] = SYMBOLS['SECT_INSIDE']
        # here if you defined an attribute on a room that exists in
        # your SYMBOLS dictionary is will update accordingly.


    def median(self, num):
        lst = sorted(range(0, num))
        n = len(lst)
        m = n -1
        return (lst[n/2] + lst[m/2]) / 2.0

    def start_loc_on_grid(self):
        x = self.median(self.max_width)
        y = self.median(self.max_length)
        # x and y are floats by default, can't index lists with float types
        x, y = int(x), int(y) 

        self.grid[x][y] = SYMBOLS['you']
        self.curX, self.curY = x, y # updating worms current location


    def has_drawn(self, room):
        return True if room in self.worm_has_mapped.keys() else False


    def create_grid(self):
        # This method simply creates an empty grid 
        # with the specified variables from __init__(self):
        board = []
        for row in range(self.max_width):
            board.append([])
            for column in range(self.max_length):
                board[row].append('   ')
        return board

    def check_grid(self):
        # this method simply checks the grid to make sure 
        # both max_l and max_w are odd numbers
        return True if self.max_length % 2 != 0 or \
                    self.max_width % 2 != 0 else False


    def get_all_room_exits(self, room):
        # this method you have to be careful with, depending on your 
        # mud set up and what objects have 'destination' defined.
        # Say for example you have a magical mirror object lying in a 
        # room, with a destination set - this method will pick it up 
        # and add it to the list of places the worm will try to map.
        # It can cause all sorts of strange behaviors.

        room_exits = []
        for stuff in room.contents:
            if stuff.destination:
                room_exits.append(stuff)
        return room_exits


    def show_map(self):
        map_string = ""
        for row in self.grid:
            map_string += " ".join(row)
            map_string += "\n"

        return map_string