# bships_script

This script allows monitoring Warcraft 3 custom games hosted on Battle.net to play an alert when the lobby is full, so users can have other windows open while waiting for lobbies to fill without missing the start of their game. The script pulls data from http://makemehost.com/games.php.  
This was originally created specifically for Battleships Pro but can be used for any game by creating and returning a new Game instance in the generate_games function.
