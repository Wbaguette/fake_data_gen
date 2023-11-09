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

def gen_stadiums() -> [Stadium]:
   # Somehow we have 100 stadiums to use
   num_stadiums = 100
   for i in range(num_stadiums):
      stadium_id = i + 1
      stadium_name = (fake.unique.company() + " " + fake.random_element(["Arena", "Stadium", "Field", "Park"])).replace(",", "")
      # Somehow this rounds to the nearest 10th
      stadium_cap = round(random.randint(5000, 950000), -1)
      stadium_loc = fake.unique.city()
      yield Stadium(stadium_id, stadium_name, stadium_cap, stadium_loc)
   
# Write to the csv file
def write_stadiums(stadiums: [Stadium]):
   with open(path, "w+") as f:
      for stadium in stadiums:
         f.write(str(stadium) + "\n")