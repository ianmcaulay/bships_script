import urllib.request
import time

def pull_number():
	url = "http://makemehost.com/games.php"
	content = str(urllib.request.urlopen(url).read())
	search_string = "Battleships Pro 4v4"
	bships_index = content.find(search_string)
	bships_string = content[bships_index: bships_index + 50]
	ingame_index = bships_string.find("/8")
	return int(bships_string[ingame_index - 1])


def start_checking_num_players():
	alert_threshold = 7
	while 1:
		num_players = pull_number()
		if num_players >= alert_threshold:
			# alert here
		time.sleep(10)





