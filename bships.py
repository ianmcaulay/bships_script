import urllib.request
import time
import winsound

def pull_number():
	url = "http://makemehost.com/games.php"
	#url = "https://entgaming.net/forum/games.php"
	req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
	#content = str(urllib.request.urlopen(url, headers={'User-Agent' : "Magic Browser"}).read())
	content = str(urllib.request.urlopen(req).read())
	search_string = "Battleships Pro"
	bships_index = content.find(search_string)
	bships_string = content[bships_index: bships_index + 50]
	ingame_index = bships_string.find("/8")
	return int(bships_string[ingame_index - 1])


def start_checking_num_players():
	alert_threshold = 8
	refresh_time = 1
	old_val = -1
	while True:
		num_players = pull_number()
		if num_players != old_val:
			print("Current Number of Players: " + str(num_players))
			old_val = num_players
		if num_players >= alert_threshold:
			
			winsound.PlaySound('bships_alert.wav', winsound.SND_FILENAME)
			print("Game starting soon")
			break
		time.sleep(refresh_time)

start_checking_num_players()






