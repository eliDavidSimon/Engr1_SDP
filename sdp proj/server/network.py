#these imports are only the ones im using, we need to handle socketserver stuff

#from socketserver import ThreadingTCPServer, StreamRequestHandler
#from jsonChecker import isValidCard, isCorrectPlayer
from random import shuffle
import sys


class UnoServer:
    #class variables

    default_card_num = sys.maxsize
    deck=[]
    playerList =[]
    playerHands = []
    top_card = []
   
    card_type = list(range(10))
    card_type += ["draw 2", "reverse"]
    isReversed =False

    

    rounds=0;    
    num_iter_cards=3

    #initialization protocol
    def start_game(self, num_players):
        
        #intialize game state
        self.list_players(num_players)
        self.create_deck()
        self.pass_cards()
        print(self.playerList)
        self.top_card = self.deck.pop(0)
        
        for i in self.playerHands:
            print(i)


        #starts the game
        self.play_game()


    
    
    #this handles round to round interactions
    def play_game(self):
        
        #this is initiated to -1 because no one starts off with an empty hand
        hand_with_no_cards= -1
        
        #this while loop checks if theres a winner
        while hand_with_no_cards < 0:
            self.resetRound()
            #goes thru the 4 players
            while self.rounds < 4 and self.rounds >-1:
                
                
                #checks who's turn it be
                    if(self.playerList[self.rounds].find("bot")>-1):
                        #goes thru bot turn protocol
                            self.bot_turn(self.rounds)
                    else:
                        #goes thru player turn protocol
                       self.player_turn(self.rounds)

                    self.check_condition(self.rounds)
                    self.iter_rounds()
            

            #checks if someone won
            hand_with_no_cards = self.isThereAWinner()
        #tells the mf they won
        print(self.playerList[hand_with_no_cards]+" is the motherfucking winner")        
        
        

    #create the list of players
    def list_players(self, num_players):

        #goes through the 4 slots and makes a player    
        for i in range(4):

            #checks if the number of players has been met and makes bots if not all slots are filled
            if(i < num_players):
                self.playerList.append("player "+str(i+1))
                print(self.playerList[i])
            else:
                self.playerList.append("bot "+str(i+1))
    
    def skip(self):
        if self.isReversed:
            self.rounds -=1
        else:
            self.rounds +=1

    #passes cards out to players
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
            self.playerHands.append(player)


    def resetRound(self):
        if(self.isReversed):
            self.rounds = 3
        else:
            self.rounds = 0 
        
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
    
    #checks if card can be put on top
    def cardIsValid(self,  card):
        
        return self.top_card[0] == card[0] or self.top_card[1] == card[1]

    #checks win condition
    def isThereAWinner(self):
        for i in range(4):
            if len(self.playerHands[i]) ==0:
                return i
        return -1

    def iter_rounds(self):
        if self.isReversed:
            self.rounds -=1
        else:
           self.rounds +=1 

    def check_condition(self,hand_num):

    
        if self.top_card[1] == 'draw 2':
            self.iter_rounds()
            self.draw_card(self.rounds)
            self.draw_card(self.rounds)
            self.iter_rounds()
        
        """
        elif self.top_card[1] == 'reverse':
            self.playerHands = reversed(self.playerHands)
            self.playerList = reversed(self.playerList)
            self.isReversed= not self.isReversed
            self.iter_rounds()
        """

    

    



    #bot mechnics, we might make this in matlab for more points
    def bot_turn(self, hand_num):
 


        has_played = False
        hand = self.playerHands[hand_num]
        for i in range(len(hand)):
            if(self.cardIsValid(hand[i])):
                self.deck.append(self.top_card)
                self.top_card = hand.pop(i)
                has_played=True
                break
        if(not has_played):
            self.draw_card(hand_num)
        else:
            self.playerHands[hand_num] = hand

    #makes them draw a card 
    def draw_card(self, hand_num):
        
        drawn_card = self.deck.pop(0)
        self.playerHands[hand_num].append(drawn_card)
                
        


    #modify for server bs
    def player_turn(self, hand_num):
        
        
        
        playable= False
        cardToPlay = self.default_card_num
        hands = self.playerHands
        hand= hands[hand_num]
  
        
        
        for i in range(len(hand)):
            if(self.cardIsValid(hand[i])):
                playable=True
                break        
        if(not playable):
            self.draw_card(hand_num)
            print("you had to draw, womp womp")
            return 0
        

    
        while not(cardToPlay < len(hand)) or cardToPlay < 0:
            #print('\n' * 50)
            print(self.top_card)
            self.display_hand(hand)
           
            cardToPlay = int(input("input a valid card(index), "+self.playerList[hand_num]))
        
        self.top_card = hand.pop(cardToPlay)
        self.playerHands[hand_num]= hand
        


    #shows player hand
    def display_hand(self,hand):
        for i in range(len(hand)):
            print(str(i)+": " + str(hand[i]))

        
        

serve = UnoServer()
serve.start_game(1)



'''class echoHandler(StreamRequestHandler):
    def handle(self):
        message = self.rfile.readline().decode()
        print(f"Received: {message}")
        
        response = 'fuck'
        self.wfile.write(response.encode())
'''