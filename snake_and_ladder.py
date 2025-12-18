import random
from abc import abstractmethod,ABC
from collections import defaultdict,deque
class Game:
    def __init__(self,board=None,player_queue=None,dice=None):
        self.board=board
        self.player_queue=player_queue
        self.dice=dice
        self.game_end=False
        self.winner=[]
        self.total_players=len(player_queue)
    def play(self):
        print("🎮 Game Started!\n")
        while not self.game_end:
            player=self.player_queue.popleft()
            roll_val=self.dice.roll()
            print(f"{player.name} rolled a {roll_val}")
            new_position=player.position+roll_val
            if new_position==self.board.size:
                self.winner.append(player)
                player.position=new_position
                pos=len(self.winner)
                print(f"{player.name} won the {len(self.winner)} position")
                if len(self.winner)==(self.total_players -1):
                    self.game_end=True
                continue
            if new_position<self.board.size:
                player.position=new_position 
            if self.board.snakes[new_position]:
                player.position=self.board.snakes[new_position]   
                print(f"{player.name} fell to snake {self.board.snakes[new_position]}")
            elif self.board.ladders[new_position]:
                print(f"{player.name} claimber a ladder {self.board.ladders[new_position]}")
                player.position=self.board.ladders[new_position]         
            self.player_queue.append(player)

    
class Board:
    def __init__(self,size,snakes,ladders):
        self.size=size
        self.snakes=snakes
        self.ladders=ladders

class Dice:
    def __init__(self,count):
        self.dice_count=count
    def roll(self):
        rolled_value=0
        for _ in range(self.dice_count):
            rolled_value+=random.randrange(1,7)
        return rolled_value
class Player:
    def __init__(self,Name):
        self.name=Name
        self.position=0
    def get_position(self):
        return self.position
    def set_position(self,val):
        self.position=val
    def __str__(self):
        return f"{self.name} at {self.get_position()}"
    
if __name__=="__main__":
    snakes_count=5
    ladders_count=5
    snakes=defaultdict(lambda :None )
    ladders=defaultdict(lambda :None)
    for snake in range(snakes_count):
        while True:
            random_start=random.randrange(2,101)
            random_end=random.randrange(1,random_start+1)
            if random_start not in snakes.keys():
                snakes[random_start]=random_end
                break
    for ladder in range(ladders_count):
        while True:
            random_start=random.randrange(1,99)
            random_end=random.randrange(random_start+1,101)
            if random_start not in ladders.keys() and random_start not in snakes.keys():
                ladders[random_start]=random_end
                break 
    dice=Dice(1)
    board=Board(100,snakes,ladders)
    players=deque([Player("kartish"),Player("kj"),Player("jan")])
    game=Game(board,players,dice)
    game.play()



