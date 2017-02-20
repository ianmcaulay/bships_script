import urllib.request
import time
import winsound
import os

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
	#url = "https://entgaming.net/forum/games.php"
	#req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
	#content = str(urllib.request.urlopen(url, headers={'User-Agent' : "Magic Browser"}).read())
	content = str(urllib.request.urlopen(url).read())
	for game in games:
		game.prev_players = game.curr_players
		#search_string = "Battleships Pro"
		search_string = game.search_string
		index = content.find(search_string)
		#bships_index = content.find(search_string)
		game_string = content[index: index + 50]
		#bships_string = content[bships_index: bships_index + 50]
		#ingame_index = bships_string.find("/8")
		ingame_index = game_string.find("/" + str(game.max_players))
		game.curr_players = int(game_string[ingame_index-1])
	#return int(bships_string[ingame_index - 1])


def start_checking_num_players():
	refresh_time = 1
	#old_val = -1
	games = generate_games()
	os.system('cls')
	while True:
		pull_number(games)
		#num_players = pull_number()
		if is_update_needed(games):
			output_string = ""
			for game in games:
				#os.system('cls')
				if game != games[0]:
					output_string += "    "
				output_string += "Current " + game.name + " Players: " + str(game.curr_players)
				
				if game.curr_players >= game.alert_threshold:
					winsound.PlaySound('bships_alert.wav', winsound.SND_FILENAME)
					break
			print(output_string)
		time.sleep(refresh_time)


		# if num_players != old_val:
		# 	os.system('cls')
		# 	print("Current Number of Players: " + str(num_players))
		# 	old_val = num_players
		# if num_players >= alert_threshold:
			
		# 	winsound.PlaySound('bships_alert.wav', winsound.SND_FILENAME)
		# 	print("Game starting soon")
		# 	break
		# time.sleep(refresh_time)

def generate_games():
	battleships = Game("Battleships", "Battleships Pro", 8)
	jurassic_park = Game("Jurassic Park", "Jurassic Park Survival!", 7, alert_threshold=5)
	return [battleships, jurassic_park]

def is_update_needed(games):
	for game in games:
		if game.prev_players != game.curr_players:
			return True
	return False

start_checking_num_players()






