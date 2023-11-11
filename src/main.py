import team
import stadium
import player
import stats
import sponsor
import staff
import contract
import prelude
import match
import result

# Everything with a list() cast is because its a generator
def main():
   
   # Generate a prelude (this is like the glue that makes tables actually correlate and be consistent with data)
   
   preludes = list(prelude.prelude())
   
   # Generate the stuff
   
   teams = team.gen_teams_from_preludes(preludes)
   stadiums = list(stadium.gen_stadiums())
   players = player.gen_players(teams)
   statss = list(stats.gen_statistics(players))
   sponsors = sponsor.gen_sponsors(teams)
   staffs = staff.gen_staff(stadiums)
   contracts = list(contract.gen_contracts(players))
   matches = list(match.gen_matches(preludes, stadiums))
   results = list(result.gen_results(teams, preludes, matches)) 
   
   # Write to CSV for exporting
   
   team.write_teams(teams)
   stadium.write_stadiums(stadiums)
   player.write_players(players)
   stats.write_statistics(statss)
   sponsor.write_sponsors(sponsors)
   staff.write_staff(staffs)
   contract.write_contracts(contracts)
   match.write_matches(matches)
   result.write_results(results)
   
if __name__ == "__main__":
   main()
