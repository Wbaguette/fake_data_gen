import team
import stadium
import player
import stats
import sponsor
import staff

from faker import Faker
fake = Faker()


def main():
   teams = team.gen_teams()
   # for te in teams: print(te)
   stadiums = stadium.gen_stadiums()
   # for st in stadiums: print(st)
   players = player.gen_players(teams)
   # for pl in players: print(pl)
   statss = stats.gen_statistics(players)
   # for st in statss: print(st)
   sponsors = sponsor.gen_sponsors(teams)
   # for sp in sponsors: print(sp)
   staffs = staff.gen_staff(stadiums)
   for sta in staffs: print(sta)
   
   
   
   
   
if __name__ == "__main__":
   main()