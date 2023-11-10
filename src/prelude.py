from enum import Enum
import random

# Theres probably a better way to structure this but I am too lazy to think of it

class GameRes(Enum):
   WINNER = 1
   TIE = 2
   
class GameResult:
   def __init__(self, status: GameRes, winner: int, loser: int):
      self.status: GameRes = status
      # team_id of winner
      self.winner: int = winner
      # team_id of loser
      self.loser: int = loser

class Prelude:
   def __init__(self, home: [int, int], away: [int, int], result: GameResult):
      # [team_id, goals]
      self.home: [int, int] = home
      self.away: [int, int] = away
      # [GameRes, team_id]
      self.result: GameResult = result
      
   def __str__(self):
      return f"""  
         Home Team ID: {self.home[0]}  Home Team Goals: {self.home[1]}
         Away Team ID: {self.away[0]}  Away Team Goals: {self.away[1]}
         Game Result: {self.result.status}  Winner: {self.result.winner}
      """
      
def prelude() -> [Prelude]:
   num_teams = 3
   for i in range(1, num_teams + 1):
      for j in range(i + 1, num_teams + 1):
         home_team = i
         away_team = j
         
         game_1_home_goals = random.randint(0, 6)
         game_1_away_goals = random.randint(0, 6)
         
         game_2_home_goals = random.randint(0, 6)
         game_2_away_goals = random.randint(0, 6)
                  
         game_1_res = GameRes.TIE if game_1_home_goals == game_1_away_goals else GameRes.WINNER
         game_2_res = GameRes.TIE if game_2_home_goals == game_2_away_goals else GameRes.WINNER

         game_1_winner_id = home_team if game_1_home_goals > game_1_away_goals else away_team if game_1_away_goals > game_1_home_goals else -1
         game_1_loser_id = home_team if game_1_home_goals < game_1_away_goals else away_team if game_1_away_goals < game_1_home_goals else -1
         game_2_winner_id = home_team if game_2_home_goals > game_2_away_goals else away_team if game_2_away_goals > game_2_home_goals else -1
         game_2_loser_id = home_team if game_2_home_goals < game_2_away_goals else away_team if game_2_away_goals < game_2_home_goals else -1

         yield Prelude([home_team, game_1_home_goals], [away_team, game_1_away_goals], GameResult(game_1_res, game_1_winner_id, game_1_loser_id))
         yield Prelude([away_team, game_2_away_goals], [home_team, game_2_home_goals], GameResult(game_2_res, game_2_winner_id, game_2_loser_id))