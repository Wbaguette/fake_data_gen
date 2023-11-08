from faker import Faker
import random

fake = Faker()
teams = []
players = []

def main():
   gen_teams()
   gen_players()
   
def gen_teams():
   global teams
   path = "tables/team.csv"
   num_teams = 25
   games_played = (num_teams - 1) * 2 
   for i in range(num_teams):
      team_id = i + 1
      team_name = fake.city() + " " + fake.random_element(["FC", "United", "City", "Athletic"])
      team_val = random.randint(50000, 4000000)
      team_wins = random.randint(0, games_played)
      team_losses = random.randint(0, games_played - team_wins)
      team_ties = games_played - team_wins - team_losses
      
      win_percentage = round((team_wins + (0.5 * team_ties)) / games_played, 4)
      team = [team_id, team_name, team_wins, team_losses, team_ties, win_percentage, team_val]
      teams.append(team)
   teams.sort(key=lambda x: x[5], reverse=True)
   teams = [team[:5] + [i + 1] + team[6:] for i, team in enumerate(teams)]
   teams.sort(key=lambda x: x[0])
   # with open(path, "w") as f:
   #    for team in teams:
   #          f.write(",".join([str(x) for x in team]) + "\n")   

def gen_players():
   path = "tables/player.csv"
   # 25 teams, 15 players each team
   num_players = 25 * 15
   for i in range(num_players):
      player_id = i + 1
      player_name = fake.name()
      player_team = random.randint(1, 25)
      player_val = random.randint(50000, 4000000)
      player = [player_id, player_name, player_team, player_val]
      players.append(player)
   
   

if __name__ == "__main__":
   main()