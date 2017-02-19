import urllib.request

def pull_number():
	url = "http://makemehost.com/games.php"
	content = urllib.request.urlopen(url)
	search_string = "Battleships Pro 4v4"
	bships_index = content.find(bships_string)
	bships_string = content[bships_index: bships_index + 50]
	ingame_index = bships_string.find("/8")
	return bships_string[ingame_index - 1]




