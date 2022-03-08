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

def hyperparameters():
  print("Bij een machine-learning agent kan het gedrag aangepast worden door middel van parameters te gebruiken. In het aangeleverde stukje code van Fundament zijn hiervoor al twee hyperparameters gebruikt; Alpha en Epsilon \nEpsilon bepaalt de frequentie waarmee de agent een nieuwe zet zal proberen te maken. De waarde ligt, net zoals bij Alpha, tussen de 0 en de 1. Hoe hoger het Epsilon getal is, bepaald de randomness van een zet. Dichterbij de 0 geeft bekendere zetten, dichterbij de 1 geeft meer random zetten. \nAlpha als parameter bepaalt de snelheid waarmee de agent nieuwe kennis vergaart. Oude kennis wordt sneller vervangen door de nieuwere kennis indien deze Alpha waarde dichterbij de 1 ligt.")
  while True:
    try:
      Epsilonwaarde = float(input("Epsilon: \n"))
      Alphawaarde = float(input("Alpha: \n"))
      
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

def Spelen():

  while True:
    play_agent = input("Vul de naam in van de agent waar tegen jij wilt spelen \n")
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
  naam = input("Typ hier de naam van je agent \n")

  my_agent = hyperparameters()
  
  train(my_agent, 5000)

  save(my_agent, naam)

  print("Opgeslagen onder" + naam)


def Grafiek():
  print("Als de grafiek getekend is, klik het weg om verder te gaan")

  while True:
    try:
      naam = input("Hoe heet de agent \n")
      my_agent = load(naam)
    except:
      print("deze agent bestaat niet")
      continue
    else:
      my_agent = load(naam)
      break
      
  while True:
    symbol = input("Wil je dat jouw agent x of o is? (x begint altijd) \n")
    if symbol == "O" or symbol == "X":
      break
  
  my_agent.learning = False
 
  validation_agent = RandomAgent()

  if symbol == "X":
    validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)

  if symbol == "O":
    validation_result = validate(agent_o=my_agent, agent_x=validation_agent, iterations=100)

  plot_validation(validation_result)

def Vergelijking():
  random.seed(1)

  while True:
    try:
      itterate = int(input("Hoeveel iteraties tussen de 1 en 50 wil je gebruiken? \n"))
    except:
      print("Een getal tussen 1 en 50!")
      continue
    else:
      if itterate <= 50:
        break

  random_agent = RandomAgent()
  my_agent = hyperparameters()
 
  train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=itterate,
    trainings=100,
    validations=1000)
  
  print("Om naar het menu te gaan klik je op het kruisje rechtsbovenin")

#Test
  
while True:
  keuzemenu = input("Kies hier wat je wilt spelen \n")
  
  if keuzemenu == '1':
    start()
  if keuzemenu == '2':
    Agenttrainen()
  if keuzemenu == '3':
    Spelen()
  if keuzemenu == '4':
    Grafiek()
  if keuzemenu == '5':
    Vergelijking()

  play = input("Spel afsluiten? (ja/nee) \n")
  if play == 'nee':
    continue
  else:
    break
    
