from chess.templates.player import PlayerTemplate
from chess.models.players import Player
from chess.templates.error import GenericErrorTemplate


class PlayerView:
    """View class for player management."""

    @staticmethod
    def menu(data={}):
        """Display the player menu and handle user input."""

        choice = PlayerTemplate.menu()

        if choice == "1":
            return "PlayerView.create_player", data
        elif choice == "2":
            return "PlayerView.read_all_players", data
        elif choice == "3":
            return "MainView.menu", data

        return "PlayerView.menu", data

    @staticmethod
    def create_player(data={}):
        """Create a new player."""

        player_data = PlayerTemplate.create()

        new_player = Player(
            firstname=player_data["firstname"],
            lastname=player_data["lastname"],
            birthdate=player_data["birthdate"],
        )
        new_player.create()

        return "PlayerView.menu", data

    @staticmethod
    def read_all_players(data={}):  # Update method name
        """List all players."""

        players = Player.read_all()

        players_dict = [
            player.to_dict() for player in players if isinstance(player, Player)
        ]

        PlayerTemplate.read_all(players_dict)

        return "PlayerView.menu", data

    @staticmethod
    def select_a_player(data={}):
        """Display a list of players."""

        GenericErrorTemplate.not_implemented("Not implemented yet")

        return "PlayerView.menu", data

    @staticmethod
    def update_player(data={}) -> dict:
        """Update player attributes."""

        GenericErrorTemplate.not_implemented("Not implemented yet")

        return "PlayerView.menu", data

    @staticmethod
    def confirm_delete(data={}) -> bool:
        """Confirm player deletion."""

        GenericErrorTemplate.not_implemented("Not implemented yet")

        return "PlayerView.menu", data

    @staticmethod
    def list_players(data={}):
        """List all players."""

        players = Player.read_all()

        players_dict = [
            player.to_dict() for player in players if isinstance(player, Player)
        ]

        PlayerTemplate.read_all(players_dict)

        return "PlayerView.menu", data

    @staticmethod
    def select_player(data={}):
        """Select a player from the list."""

        players = Player.read_all()

        players_dict = [
            player.to_dict() for player in players if isinstance(player, Player)
        ]

        PlayerView.select_player(players_dict)

        p_dict = input(
            "Enter the number of the player to add to a tournament('' or 0 to return):"
        )

        if not p_dict:
            print("No player selected.")
            return "PlayerView.menu", data

        return "PlayerView.menu", {"p_dict": p_dict}
