from faker import Faker
import random
import datetime
from player import Player

fake = Faker()

path = "../tables/contract.csv"

class Contract:
   def __init__(self, player_id: int, salary: float, start: str, end: str):
      self.player_id = player_id
      self.salary = salary
      self.start = start
      self.end = end
      
   # Make sure this matches the order of the attributes in the schema.sql file
   def __str__(self):
      return f"{self.player_id},{self.salary},{self.start},{self.end}"

def gen_contracts(players: [Player]) -> [Contract]:
   for player in players:
      player_id = player.player_id
      salary = round(random.uniform(500000, 20000000), 2)
      start = fake.date_between(start_date="-10y", end_date="today")
      end = fake.date_between(start_date=start, end_date="+10y")
      yield Contract(player_id, salary, start, end)

# Write to the csv file
def write_contracts(contracts: [Contract]):
   with open(path, "w+") as f:
      for contract in contracts:
         f.write(str(contract) + "\n")
