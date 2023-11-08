import team
import stadium
import player

from faker import Faker
fake = Faker()


def main():
   teams = team.gen_teams()
   # for t in teams: print(t)
   # stadiums = stadium.gen_stadiums()
   # for s in stadiums: print(s)
   players = player.gen_players(teams)
   for p in players: print(p)




if __name__ == "__main__":
   main()