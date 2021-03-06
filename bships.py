import urllib.request
import time
import winsound
import os

# Number of seconds to sleep between checking website.
REFRESH_TIME = 1

class Game:

	def __init__(self, name, search_string, max_players, alert_threshold=-1):
		self.name = name
		self.search_string = search_string
		self.max_players = max_players
		self.alert_threshold = alert_threshold
		if alert_threshold == -1:
			self.alert_threshold = max_players
		self.curr_players = -1
		self.prev_players = -1

		
def pull_number(games):
	url = "http://makemehost.com/games.php"
	content = str(urllib.request.urlopen(url).read())
	for game in games:
		game.prev_players = game.curr_players
		search_string = game.search_string
		index = content.find(search_string)
		game_string = content[index: index + 50]
		ingame_index = game_string.find("/" + str(game.max_players))
		game.curr_players = int(game_string[ingame_index-1])


def start_checking_num_players():
	games = generate_games()
	os.system('cls')
	while True:
		pull_number(games)
		if is_update_needed(games):
			output_string = ""
			for game in games:
				if game != games[0]:
					output_string += "    "
				output_string += "Current " + game.name + " Players: " + str(game.curr_players)
				
				if game.curr_players >= game.alert_threshold:
					winsound.PlaySound('bships_alert.wav', winsound.SND_FILENAME)
					print(output_string)
					return
			print(output_string)
		time.sleep(REFRESH_TIME)


def generate_games():
	battleships = Game("Battleships", "Battleships Pro", 8)
	jurassic_park = Game("Jurassic Park", "Jurassic Park Survival!", 7, alert_threshold=5)
	troll_and_elves = Game("Troll and Elves", "Troll and Elves", 11)
	civ_wars = Game("Civilization Wars", "Civilization Wars", 6)
	return [battleships, jurassic_park, troll_and_elves,civ_wars]


def is_update_needed(games):
	for game in games:
		if game.prev_players != game.curr_players:
			return True
	return False

start_checking_num_players()

