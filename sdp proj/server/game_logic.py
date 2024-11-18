from random import shuffle
from time import sleep


class UnoServer:
    card_type = ["1",
                 "2",
                 "3",
                 "4",
                 "5",
                 "6",
                 "7",
                 "8",
                 "9",
                 "0",
                 "draw2",
                 "reverse",
                 ]
    
    special_type = ["wild", "draw4"]

    player_hand = []

    deck=[]

    shift =-1

    rounds=0
    
    top_card = []

    def start_game(self):
        self.create_deck()
        self.pass_cards()
        self.get_top_card()
        self.play_game()
 
    def play_game(self):
        is_there_a_winner = self.isThereAWinner()
        while is_there_a_winner <0:
           
            self.turn()
            
            
            self.iter_turn()

    
    def turn(self):
        
        self.display()
        index_of_action = int(input("enter action, player " +str(self.rounds+1)+": "))

        while index_of_action != -1 and ((index_of_action >=len(self.player_hand[self.rounds]) or index_of_action <0) and not self.cardIsValid(self.player_hand[self.rounds])):
            self.display()
            print("enter valid num")
            index_of_action = int(input("enter action, player " +str(self.rounds+1)+": ")) 

        if index_of_action == -1:
            self.draw()
        else:
            self.deck.append(self.top_card)

        
    def draw():
        pass

    def cardIsValid(self, card):
        
        return self.top_card[0] == card[0] or self.top_card[1] == card[1]


    def iter_turn(self):
        if self.shift > 0 and self.rounds == 3:
                self.rounds = 0
        elif self.shift < 0 and self.rounds == 0:
            self.rounds = 3
        else:
            self.rounds += self.shift



    def isThereAWinner(self):
        hands = self.player_hand
        for i in range(4):
            
            if len(hands[i]) == 0:
                return i
        return -1    


    

    def get_top_card(self):
        for i in range(len(self.deck)):
            print(self.deck[i])
            if len(self.deck[i][1]) ==1:
                self.top_card= self.deck.pop(i)
                break


    #uses for loop to create deck
    def create_deck(self):
        
        # all colors we usin
        colors = ["red", "blue", "green","yellow"]
        
        #PLS_FIX: change the range for K to a class var, i made it hardcoded to get smt to work
        for k in range(5):

            #iterates colors
            for i in colors:

                #iterates 0-9, we need to make a 
                for j in self.card_type:
                    self.deck.append([i, str(j)])
        shuffle(self.deck)


    def pass_cards(self):

        #intiates vars
        player = []
        
        #goes through for each player
        for i in range(4):
            #starts player at no cards
            player = []

            #interates to append
            for j in range(7):

                #adds card to hand
                player.append(self.deck.pop(j))
            
            #adds new hand to the list of hands
            self.player_hand.append(player)
    

    def display(self):

        hand = self.player_hand[self.rounds]
        print()
        print(self.top_card)
        print("-1: draw")
        for i in range(len(hand)):
            print(str(i)+": " + str(hand[i]))
        
       


    def skip():
        pass



server = UnoServer()
server.start_game()