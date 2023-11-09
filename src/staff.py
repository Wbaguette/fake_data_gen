from faker import Faker
import random
from stadium import Stadium

fake = Faker()

path = "../tables/staff.csv"

class Staff:
   def __init__(self, staff_id: int, name: str, salary: float, role: str, stadium_id: int):
      # The PK is (staff_id, stadium_id)
      self.staff_id = staff_id
      self.name = name
      self.salary = salary
      self.role = role
      self.stadium_id = stadium_id
      
   # Make sure this matches the order of the attributes in the schema.sql file
   def __str__(self):
      return f"{self.staff_id},{self.name},{self.salary},{self.role},{self.stadium_id}"
   
def gen_staff(stadiums: [Stadium]) -> [Staff]:
   # Every stadium will have this number staff of each role
   num_refs = 3
   num_announcers = 2
   num_doctors = 5
   num_security = 40
   num_concessions = 100
   num_tech = 10
   num_grounds = 15
   num_admins = 5
   
   # This is a list of lists of staff, gets flattened on return
   staff = []
   id = 0
   for stadium in stadiums:
      # Walrus operator used !!!!!
      staff.append([Staff(id := id + 1, fake.name(), round(random.uniform(70000, 100000), 2), "Referee", stadium.stadium_id) for _ in range(num_refs)])
      staff.append([Staff(id := id + 1, fake.name(), round(random.uniform(50000, 70000), 2), "Announcer", stadium.stadium_id) for _ in range(num_announcers)])
      staff.append([Staff(id := id + 1, f"Dr. {fake.name()}", round(random.uniform(100000, 300000), 2), "Doctor", stadium.stadium_id) for _ in range(num_doctors)])
      staff.append([Staff(id := id + 1, fake.name(), round(random.uniform(40000, 70000), 2), "Security", stadium.stadium_id) for _ in range(num_security)])
      staff.append([Staff(id := id + 1, fake.name(), round(random.uniform(30000, 50000), 2), "Concessions", stadium.stadium_id) for _ in range(num_concessions)])
      staff.append([Staff(id := id + 1, fake.name(), round(random.uniform(80000, 95000), 2), "Technical", stadium.stadium_id) for _ in range(num_tech)])
      staff.append([Staff(id := id + 1, fake.name(), round(random.uniform(40000, 60000), 2), "Groundskeeping", stadium.stadium_id) for _ in range(num_grounds)])
      staff.append([Staff(id := id + 1, fake.name(), round(random.uniform(68000, 84000), 2), "Administration", stadium.stadium_id) for _ in range(num_admins)])
   return [s for staff_list in staff for s in staff_list]
   
# Write to the csv file
def write_staff(staff: [Staff]):
   with open(path, "w+") as f:
      for s in staff:
         f.write(str(s) + "\n")
