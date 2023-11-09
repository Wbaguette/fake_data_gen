from faker import Faker
import random
from team import Team

fake = Faker()

path = "tables/player.csv"
# The possible positions a player can play in soccer
player_positions = ["GK", "CB", "LB", "RB", "CDM", "CM", "CAM", "LM", "RM", "LW", "RW", "ST"]

class Player:
   def __init__(self, player_id: int, player_name: str, player_age: int, player_pos: str, player_jersey: int, player_team: int):
      self.player_id: int = player_id
      self.player_name: str = player_name
      self.player_age: int = player_age
      self.player_pos: str = player_pos
      self.player_jersey: int = player_jersey
      # FK to team table 
      self.player_team: int = player_team
      
   # Make sure this matches the order of the attributes in the schema.sql file
   def __str__(self):
      return f"{self.player_id},{self.player_name},{self.player_age},{self.player_pos},{self.player_jersey},{self.player_team}"

# Will somehow need the player objects for other tables' generation (consistency)
def gen_players(teams: [Team]) -> [Player]:
   # Will need to flatten this list later as it will be a list of lists 
   all_players = []
   # 15 players on each team
   num_players = 15
   for i, team in enumerate(teams):
      team_players = []
      for j in range(num_players):
         player_id = int(f"{i+1}{j+1}")
         player_name = fake.name_male()
         player_age = random.randint(18, 35)
         # If we don't already have one player in every position...
         if len(team_players) < len(player_positions):
            player_pos = player_positions[len(team_players)]
         else:
            # If we already have a player in every position, then the remaining players will be substitutes
            player_pos = fake.random_element(player_positions)
         
         player_jersey = random.randint(1, 99)
         # FK to team table
         player_team = team.team_id
         team_players.append(Player(player_id, player_name, player_age, player_pos, player_jersey, player_team))
      all_players.append(team_players)
   return [player for team in all_players for player in team]

# Write to the csv file
def write_players(players: [Player]):
   with open(path, "w+") as f:
      for player in players:
         f.write(str(player) + "\n")
