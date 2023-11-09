import team
import stadium
import player
import stats
import sponsor
import staff
import contract

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
   # for sta in staffs: print(sta)
   contracts = contract.gen_contracts(players)
   # for co in contracts: print(co)
   
   # TODO: some pre calculated thing for winning and losing teams
   # { home { team_id, goals }, away { team_id, goals }  win/loss/tie }
   # (winner_id: goals, loser_id: goals)
   # this will be used to generate matches and used to generate the teams' stats (win loss tie)
   
   
   
if __name__ == "__main__":
   main()