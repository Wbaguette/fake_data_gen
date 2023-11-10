from faker import Faker
import random
from prelude import *

fake = Faker()

path = "tables/team.csv"

class Team:
   def __init__(self, team_id: int, team_name: str, wins: int, losses: int, ties: int, rank: int, value: float):
      self.team_id: int = team_id
      self.team_name: str = team_name
      self.wins: int = wins
      self.losses: int = losses
      self.ties: int = ties
      self.rank: int = rank
      self.value: float = value

   # Make sure this matches the order of the attributes in the schema.sql file
   def __str__(self):
      return f"{self.team_id},{self.team_name},{self.wins},{self.losses},{self.ties},{self.rank},{self.value}"

def gen_teams_from_preludes(preludes: [Prelude]) -> [Team]:
   teams_dict = {}
   for prelude in preludes:
      home_team_id = prelude.home[0]
      away_team_id = prelude.away[0]

      if home_team_id not in teams_dict:
         teams_dict[home_team_id] = [0, 0, 0]

      if away_team_id not in teams_dict:
         teams_dict[away_team_id] = [0, 0, 0]

      if prelude.result.status == GameRes.WINNER:
         teams_dict[prelude.result.winner][0] += 1  # Incrementing wins
         teams_dict[prelude.result.loser][1] += 1  # Incrementing losses
      elif prelude.result.status == GameRes.TIE:
         teams_dict[home_team_id][2] += 1 # Incrementing ties for both teams
         teams_dict[away_team_id][2] += 1

   teams = []
   for team_id, stats in teams_dict.items():
      team_name = fake.unique.city() + " " + fake.random_element(["FC", "United", "City", "Athletic"])
      team_val = round(random.uniform(50000, 5000000), 2)
      team_wins = stats[0]
      team_losses = stats[1]
      team_ties = stats[2]

      games_played = team_wins + team_losses + team_ties
      win_percentage = round((team_wins + (0.5 * team_ties)) / games_played, 6)
      teams.append([team_id, team_name, team_wins, team_losses, team_ties, win_percentage, team_val])

   teams.sort(key=lambda x: x[5], reverse=True)
   teams = [team[:5] + [i + 1] + team[6:] for i, team in enumerate(teams)]
   teams.sort(key=lambda x: x[0])

   # Make sure the items in team are in the proper order of the constructor to ensure the * unpacking works
   return [Team(*team) for team in teams]
      
# Write to the csv file
def write_teams(teams: [Team]):
   with open(path, "w+") as f:
      for team in teams:
         f.write(str(team) + "\n")