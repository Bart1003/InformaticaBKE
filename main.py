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
    
 
my_agent = load('MyAgent_3000')
my_agent.learning = True
 
validation_agent = RandomAgent()
 
validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)
 
plot_validation(validation_result)

def parameters():
  print("Bij een machine-learning agent kan het gedrag aangepast worden door middel van parameters te gebruiken. In het aangeleverde stukje code van Fundament zijn hiervoor al twee hyperparameters gebruikt; Alpha en Epsilon \nEpsilon bepaalt de frequentie waarmee de agent een nieuwe zet zal proberen te maken. De waarde ligt, net zoals bij Alpha, tussen de 0 en de 1. Hoe hoger het Epsilon getal is, bepaald de randomness van een zet. Dichterbij de 0 geeft bekendere zetten, dichterbij de 1 geeft meer random zetten. \nAlpha als parameter bepaalt de snelheid waarmee de agent nieuwe kennis vergaart. Oude kennis wordt sneller vervangen door de nieuwere kennis indien deze Alpha waarde dichterbij de 1 ligt.")

  

  
  my_agent = MyAgent(alpha=chosen_alpha, epsilon=chosen_epsilon)
  return my_agent