from faker import Faker
from stadium import Stadium
from prelude import Prelude
from datetime import datetime, timedelta

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

def gen_matches(preludes: [Prelude], stadiums: [Stadium]) -> [Match]:
   ids = 0
   
   current_year = datetime.now().year
   start_time = datetime(current_year, 1, 1, 14, 0, 0)  
   end_time = datetime(current_year, 12, 31, 18, 0, 0)  
   
   for prelude in preludes:
      home_team_id = prelude.home[0]
      away_team_id = prelude.away[0]
      stadium_id = fake.random_element(stadiums).stadium_id
      
      date_time = fake.date_time_between(start_time, end_time).strftime("%Y-%m-%d %H:%M:%S")
      yield Match(ids := ids + 1, stadium_id, home_team_id, away_team_id, date_time)
   
# Write to the csv file
def write_matches(matches: [Match]):
   with open(path, "w+") as f:
      for match in matches:
         f.write(str(match) + "\n")
