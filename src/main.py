import team
import stadium
import player
import stats
import sponsor

from faker import Faker
fake = Faker()


def main():
   teams = team.gen_teams()
   for t in teams: print(t)
   stadiums = stadium.gen_stadiums()
   # for s in stadiums: print(s)
   players = player.gen_players(teams)
   # for p in players: print(p)
   statss = stats.gen_statistics(players)
   # for s in statss: print(s)
   sponsors = sponsor.gen_sponsors(teams)
   # for sp in sponsors: print(sp)
   




if __name__ == "__main__":
   main()