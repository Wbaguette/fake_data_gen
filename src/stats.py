from faker import Faker
import random
from player import Player

fake = Faker()

path = "../tables/statistics.csv"

class Statistics:
   def __init__(self, player_id: int, goals: int, blocks: int, yellow_cards: int, red_cards: int):
      self.player_id = player_id
      self.goals = goals
      self.blocks = blocks
      self.yellow_cards = yellow_cards
      self.red_cards = red_cards
      
   # Make sure this matches the order of the attributes in the schema.sql file
   def __str__(self):
      return f"{self.player_id},{self.goals},{self.blocks},{self.yellow_cards},{self.red_cards}"

def gen_statistics(players: [Player]) -> [Statistics]:
   stats = []
   for player in players:
      player_id = player.player_id
      if player.player_pos == "ST": 
         goals = random.randint(5, 12)
         blocks = 0
      elif player.player_pos in ["CAM" "LM", "RM", "LW", "RW"]: 
         goals = random.randint(0, 5)
         blocks = 0
      elif player.player_pos in ["CB", "LB", "RB", "CDM", "CM"]: 
         goals = random.randint(0, 3)
         blocks = random.randint(2, 5)
      else: 
         goals = 0
         blocks = random.randint(5, 20)
      yellow_cards = random.randint(0, 10)
      red_cards = random.randint(0, 2)
      stats.append(Statistics(player_id, goals, blocks, yellow_cards, red_cards))
      
   return stats

# Write to the csv file
def write_statistics(statistics: [Statistics]):
   with open(path, "w+") as f:
      for stat in statistics:
         f.write(str(stat) + "\n")
