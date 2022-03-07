from _ml import MLAgent, train, save, load, train_and_plot, RandomAgent, validate, plot_validation
from _core import is_winner, opponent, start
import random
 


 
 
class MyAgent(MLAgent):
  def evaluate(self, board):
    if is_winner(board, self.symbol):
        reward = 1
    elif is_winner(board, opponent[self.symbol]):
      reward = -1
    else:
      reward = 0
    return reward

def Spelen():

  while True:
    play_agent = input("vul de naam in van de agent waar tegen jij wilt spelen")
    try:
      my_agent = load(play_agent)
    except:
      print("Deze bestaat niet, selecteer alsjeblieft een uit de lijst van bestaande agenten")
      continue
    else: 
      my_agent = load(play_agent)
      break

  my_agent.learning = False

  while True:
      teamkeuze = input("Wil je x of o zijn? (x begint altijd) \n")
      if teamkeuze == "O":
        start(player_x=my_agent) 
        break 
      elif teamkeuze == "X":
        start(player_o=my_agent)
        break




def Agenttrainen():
  naam = input("Typ hier de naam van je agent")

  my_agent = hyperparameters()
  
  train(my_agent, 5000)

  save(my_agent, naam)

  print("Opgeslagen onder" + naam)


def hyperparameters():
  print("Bij een machine-learning agent kan het gedrag aangepast worden door middel van parameters te gebruiken. In het aangeleverde stukje code van Fundament zijn hiervoor al twee hyperparameters gebruikt; Alpha en Epsilon \nEpsilon bepaalt de frequentie waarmee de agent een nieuwe zet zal proberen te maken. De waarde ligt, net zoals bij Alpha, tussen de 0 en de 1. Hoe hoger het Epsilon getal is, bepaald de randomness van een zet. Dichterbij de 0 geeft bekendere zetten, dichterbij de 1 geeft meer random zetten. \nAlpha als parameter bepaalt de snelheid waarmee de agent nieuwe kennis vergaart. Oude kennis wordt sneller vervangen door de nieuwere kennis indien deze Alpha waarde dichterbij de 1 ligt.")
  while True:
    try:
      Epsilonwaarde = float(input("epsilon: \n"))
      Alphawaarde = float(input("alpha: \n"))
      
    except:
      print("Neem een waarde tussen de 1 en de 0")
      continue
    else:
      if Alphawaarde <= 1 and Epsilonwaarde <= 1:
        break
      else:
        print("Neem een waarde tussen de 1 en de 0")
  
  my_agent = MyAgent(alpha=Alphawaarde, epsilon=Epsilonwaarde)
  return my_agent

def Grafiek():




  
while True:
  keuzemenu = input("Kies hier wat je wilt spelen")
  
  if keuzemenu == '1':
    start()
  if keuzemenu == '2':
    Agenttrainen()
  if keuzemenu == '3':
    Spelen()

  play = input("Spel afsluiten? (ja/nee) \n")
  if play == 'nee':
    continue
  else:
    break
    
