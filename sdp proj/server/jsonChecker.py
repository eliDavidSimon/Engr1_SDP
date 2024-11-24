import json

def isCorrectPlayer(currentPlayer, json_request):
    return currentPlayer == json_request["player"]


#add more to this function for game states
def isValidCard(currentCard, json_request):
    card = json_request["card"]
    if(currentCard["color"] == card["color"] or currentCard["type"] == card["type"]):
        return card
    return "err"

