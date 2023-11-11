from faker import Faker
from math import ceil
import random
from team import Team

fake = Faker()

path = "tables/sponsor.csv"

class Sponsor:
   def __init__(self, sponsor_id: int, team_id: int, sponsor_name: str, value: float):
      # The PK is (sponsor_id, team_id), as a sponsor can sponsor multiple teams
      self.sponsor_id = sponsor_id
      self.team_id = team_id
      self.sponsor_name = sponsor_name
      self.value = value
      
   # Make sure this matches the order of the attributes in the schema.sql file
   def __str__(self):
      return f"{self.sponsor_id},{self.team_id},{self.sponsor_name},{self.value}"
   
def gen_sponsors(teams: [Team]) -> [Sponsor]:
   # Lets say each team has 4 sponsors
   num_sponsors = 4
   sponsors = [fake.unique.company() for _ in range(ceil(len(teams) / 2))] + ["Nike", "Adidas", "Puma", "Under Armour", "New Balance"]
   # Replace , with ""
   sponsors = [sponsor.replace(",", "") for sponsor in sponsors]
   ret_sponsors = []
   for team in teams:
      team_sponsors = random.sample(sponsors, num_sponsors)
      for i in range(num_sponsors):
         sponsor_id = sponsors.index(team_sponsors[i]) + 1
         team_id = team.team_id
         sponsor_name = team_sponsors[i]
         value = round(random.uniform(50000, 1000000), 2)
         new_sponsor = Sponsor(sponsor_id, team_id, sponsor_name, value)
         ret_sponsors.append(new_sponsor)
   
   return ret_sponsors
   
# Write to the csv file
def write_sponsors(sponsors: [Sponsor]):
   with open(path, "w+") as f:
      for sponsor in sponsors:
         f.write(str(sponsor) + "\n")
