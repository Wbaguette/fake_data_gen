from faker import Faker
import random
from team import Team
from stadium import Stadium

fake = Faker()

path = "tables/match.csv"

class Match:
   def __init__(self, match_id: int, stadium_id: int, home: int, away: int, datetime: str):
      self.match_id = match_id
      self.stadium_id = stadium_id
      self.home = home
      self.away = away
      self.datetime = datetime
            
   # Make sure this matches the order of the attributes in the schema.sql file
   def __str__(self):
      return f"{self.match_id},{self.stadium_id},{self.home},{self.away},{self.datetime}"

def gen_matches(teams: [Team], stadiums: [Stadium]) -> [Match]:
   # Every team plays every other team twice, at a random stadium
   matches = []
   # Going to have to keep track of a few things:
   #  Map 
   

# Write to the csv file
def write_matches(matches: [Match]):
   with open(path, "w+") as f:
      for match in matches:
         f.write(str(match) + "\n")
