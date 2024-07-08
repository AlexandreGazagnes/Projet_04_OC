from chess.views.main import MainView
from chess.views.player import PlayerView
from chess.views.tournament import TournamentView


routes = {
    #
    "MainView.menu": MainView.menu,
    #
    "PlayerView.menu": PlayerView.menu,
    "PlayerView.create_player": PlayerView.create_player,
    "PlayerView.read_all_players": PlayerView.read_all_players,
    #
    "TournamentView.menu": TournamentView.menu,
    "TournamentView.create_tournament": TournamentView.create_tournament,
    "TournamentView.add_player_to_tournament": TournamentView.add_player_to_tournament,
    "TournamentView.launch_tournament_menu": TournamentView.launch_tournament_menu,
    "TournamentView.create_new_round": TournamentView.create_new_round,
    "TournamentView.display_rankings": TournamentView.display_rankings,
    "TournamentView.list_all_tournaments": TournamentView.list_all_tournaments,
    "TournamentView.view_rounds_and_input_scores": TournamentView.view_rounds_and_input_scores,
    #
    "exit": "exit",
}
