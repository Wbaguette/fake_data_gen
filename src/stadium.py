from faker import Faker
import random

fake = Faker()

path = "../tables/stadium.csv"

class Stadium:
   def __init__(self, stadium_id: int, stadium_name: str, stadium_capacity: int, stadium_location: str):
      self.stadium_id: int = stadium_id
      self.stadium_name: str = stadium_name
      self.stadium_capacity: int = stadium_capacity
      self.stadium_location: str = stadium_location

   # Make sure this matches the order of the attributes in the schema.sql file
   def __str__(self):
      return f"{self.stadium_id},{self.stadium_name},{self.stadium_capacity},{self.stadium_location}"

# Will somehow need the stadium objects for other tables' generation (consistency)
def gen_stadiums() -> [Stadium]:
   pass

# Write to the csv file
def write_stadiums(stadiums: [Stadium]):
   with open(path, "w+") as f:
      for stadium in stadiums:
         f.write(str(stadium) + "\n")