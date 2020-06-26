class Game():

    _points = 0
    __level = 1

    def __init__(self,name):
        self._name = name

    def add_points(self):
        self._points += 1

    def upgrade_level(self):
        if self._points == 3:
            self._level += 1
            print("Gongratulations! LEVEL 2")
    
    def stop_game(self,x):
        self._points = self._points - x
        
        if self._points <= 0:
            print("GAME OVER")
        

class Game2(Game):
    pass



man = Game2("Manas")
man.__level = 19
print(man.__level)




    