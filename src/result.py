from faker import Faker
from match import Match
from prelude import Prelude, GameRes
from team import Team
fake = Faker()

path = "tables/result.csv"

class Result:
   def __init__(self, home_score: int, away_score: int, outcome: str, match_id: int):
      self.home_score = home_score
      self.away_score = away_score
      self.outcome = outcome
      self.match_id = match_id
            
   # Make sure this matches the order of the attributes in the schema.sql file
   def __str__(self):
      return f"{self.home_score},{self.away_score},{self.outcome},{self.match_id}"

def gen_results(teams: [Team], preludes: [Prelude], matches: [Match]) -> [Result]:
   for prelude, match in zip(preludes, matches):
      home_goals = prelude.home[1]
      away_goals = prelude.away[1]
      winner_id = prelude.result.winner
      loser_id = prelude.result.loser
      
      winner_team_name = next((team.team_name for team in teams if team.team_id == winner_id), None)
      loser_team_name = next((team.team_name for team in teams if team.team_id == loser_id), None)
      
      if prelude.result.status == GameRes.WINNER:
         yield Result(home_goals, away_goals, f"{winner_team_name} beat {loser_team_name}", match.match_id)
      elif prelude.result.status == GameRes.TIE:
         yield Result(home_goals, away_goals, f"Tied Game", match.match_id)
   
# Write to the csv file
def write_results(results: [Result]):
   with open(path, "w+") as f:
      for res in results:
         f.write(str(res) + "\n")
