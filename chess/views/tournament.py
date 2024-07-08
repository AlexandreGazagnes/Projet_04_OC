import secrets

from chess.models.players import Player
from chess.models.rounds import Round
from chess.models.tournaments import Tournament
from chess.templates.tournament import TournamentTemplate
from chess.views.player import PlayerView


class TournamentView:
    """Handles tournament management operations."""

    @staticmethod
    def menu(data={}):
        while True:
            choice = TournamentTemplate.menu()

            if choice == "1":
                # name = input("Enter tournament name: ")
                # start_date = input("Enter start date (YYYY-MM-DD): ")
                # end_date = input("Enter end date (YYYY-MM-DD): ")
                # description = input("Enter tournament description: ")
                # location = input("Enter tournament location: ")

                # self.create_tournament(
                #     name, start_date, end_date, description, location
                # )
                raise ArithmeticError("NO PRINT IN VIEW ;) ")
            elif choice == "2":
                self.add_player_to_tournament()

            elif choice == "3":
                self.launch_tournament_menu()

            elif choice == "4":
                self.display_rankings()

            elif choice == "5":
                self.list_all_tournaments()

            elif choice == "6":
                self.view_rounds_and_input_scores()

            elif choice == "7":
                return "MainView.menu", data
            else:
                "TournamentView.menu", data

    @staticmethod
    def list_all_tournaments(data={}):
        """List all available tournaments."""
        tournaments_data = Tournament.db.all()
        tournaments = [Tournament.from_dict(data) for data in tournaments_data]

        TournamentView.display_available_tournaments(tournaments)

    @staticmethod
    def create_tournament(name, start_date, end_date, description, location):
        """Creates a new tournament."""
        tournament_id = secrets.token_hex(2)
        tournament = Tournament(
            name,
            start_date,
            end_date,
            description,
            location,
            tournament_id=tournament_id,
        )
        tournament.create()
        TournamentView.auto_create_rounds(tournament)

    @staticmethod
    def auto_create_rounds(tournament):
        """Automatically creates rounds for the tournament."""
        if tournament:
            print("Automatically creating rounds...")
            for round_number in range(tournament.N_ROUNDS):
                matches = []
                tournament._add_round(round_number, matches)
            print("Rounds created successfully.")

    @staticmethod
    def launch_tournament_menu(data={}):
        """Menu to select and launch a tournament."""

        TournamentView.list_all_tournaments()
        choice = input(
            "Enter the number of the tournament to launch ('' or 0 to return): "
        )

        if choice.isdigit():
            index = int(choice) - 1
            list_tournaments = Tournament.read_all()
            if 0 <= index < len(list_tournaments):
                selected_tournament = list_tournaments[index]
                TournamentView.launch_tournament(selected_tournament)
            else:
                print("Invalid tournament selection.")
        elif choice == "" or choice == "0":
            print("Returning to main menu.")
        else:
            print("Invalid input. Returning to main menu.")

    @staticmethod
    def launch_tournament(tournament):
        """Launches the selected tournament."""

        if tournament:
            if tournament.status == "Created":
                try:
                    if TournamentTemplate.launch():
                        tournament.update_status("In Progress")
                        print(f"Tournament '{tournament.name}' launched successfully.")
                    else:
                        print("Launch cancelled.")
                except ValueError as e:
                    print(e)
            else:
                print(f"Tournament '{tournament.name}' cannot be launched.")
        else:
            print("No tournament selected.")

    @staticmethod
    def create_new_round(tournament):
        """Create a new round in the tournament."""

        if tournament:
            if TournamentTemplate.new_round():
                TournamentView.auto_create_rounds(tournament)
            else:
                print("Round creation cancelled.")
        else:
            print("No tournament available to create a new round.")

    @staticmethod
    def display_available_tournaments(list_tournaments: list) -> str:
        """Display a list of available tournaments with numbering."""

        if list_tournaments:
            print("\nAvailable Tournaments:")
            for i, tournament in enumerate(list_tournaments):
                print(f"{i + 1}.")
                print(f"Name: {tournament.name}")
                print(f"Description: {tournament.description}")
                print(f"Location: {tournament.location}")
                print(f"Status: {tournament.status}")
                print(f"Start Date: {tournament.start_date}")
                print(f"End Date: {tournament.end_date}")
        else:
            print("No tournaments available.")
        return ""

    @staticmethod
    def add_player_to_tournament(data={}):
        """Add a player to a selected tournament."""

        player = PlayerView.select_player()
        if not player:
            return

        tournaments = Tournament.read_all()
        TournamentView.display_available_tournaments(tournaments)

        choice = input(
            "Enter the number of the tournament to add the player ('' or 0 to return): "
        )

        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(tournaments):
                selected_tournament = tournaments[index]
                selected_tournament.add_player(player.player_id)
                print(
                    f"{player.firstname} {player.lastname} added to {selected_tournament.name}."
                )
            else:
                print("Invalid tournament selection.")
        elif choice == "" or choice == "0":
            print("Returning to menu.")
        else:
            print("Invalid input.")

    @staticmethod
    def view_rounds_and_input_scores():
        """View rounds of a selected tournament and input scores."""

        tournaments = Tournament.read_all()
        TournamentView.display_available_tournaments(tournaments)

        choice = input(
            "Enter the number of the tournament to view rounds and input scores('' or 0 to return):"
        )

        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(tournaments):
                selected_tournament = tournaments[index]
                print(f"Debug: Selected tournament: {selected_tournament.to_dict()}")
                TournamentView.display_rounds(selected_tournament)
            else:
                print("Invalid tournament selection.")
        elif choice == "" or choice == "0":
            print("Returning to menu.")
        else:
            print("Invalid input.")

    @staticmethod
    def display_rounds(tournament):
        """Display rounds of the selected tournament and allow score input."""

        print(f"\nRounds for Tournament: {tournament.name}")
        for i, round_id in enumerate(tournament.round_id_list):
            print(f"{i + 1}. Round {i + 1}")

        round_choice = input(
            "Enter the number of the round to input scores ('' or 0 to return): "
        )
        if round_choice.isdigit():
            round_index = int(round_choice) - 1
            if 0 <= round_index < len(tournament.round_id_list):
                round_id = tournament.round_id_list[round_index]
                print(f"Debug: Selected round_id: {round_id}")
                TournamentView.input_scores(round_id)
            else:
                print("Invalid round selection.")
        elif round_choice == "" or round_choice == "0":
            print("Returning to menu.")
        else:
            print("Invalid input.")

    @staticmethod
    def input_scores(round_id):
        """Input scores for matches in a selected round."""

        round_data = Round.read_one(round_id)
        if not round_data:
            print(f"Round with ID {round_id} not found.")
            return

        print(f"\nRound Number: {round_data.round_number}")
        print("\nMatches in the round:")
        print(f"Debug: round_data.matches = {round_data.matches}")

        if not round_data.matches:
            print("No matches found in this round.")
            return

        for match in round_data.matches:
            if isinstance(match, list) and len(match) == 2:
                player_id = match[0]
                score = match[1]

                # Ensure player ID is valid
                if not player_id or player_id == -1:
                    print("Invalid player ID in match data.")
                    continue

                # Retrieve player data
                player = Player.read_one(player_id)

                # Validate player data
                if not player:
                    print(f"Invalid data for Player ID: {player_id}")
                    continue

                # Safely retrieve player attributes using attribute access
                player_firstname = (
                    player.firstname if hasattr(player, "firstname") else ""
                )
                player_lastname = player.lastname if hasattr(player, "lastname") else ""

                print(f"Match: {player_firstname} {player_lastname} " f"Score: {score}")

                try:
                    new_score = float(
                        input(
                            f"Enter new score for {player_firstname} {player_lastname}: "
                        )
                    )
                except ValueError:
                    print("Invalid score input. Please enter a valid number.")
                    continue

                # Update match score in the round_data
                match[1] = new_score

            else:
                print("Match data not found or has invalid structure.")

        # After updating all matches, update the round_data
        round_data.matches = (
            round_data.matches
        )  # Ensure round_data.matches is correctly structured
        round_data.update()

    @staticmethod
    def display_rankings():
        """Static method to display rankings of the selected tournament."""
        TournamentView.list_all_tournaments()
        choice = input(
            "Enter the number of the tournament to display rankings (or 0 to return): "
        )

        if choice.isdigit():
            index = int(choice) - 1
            tournaments = Tournament.read_all()
            if 0 <= index < len(tournaments):
                selected_tournament = tournaments[index]
                print(f"Debug: Selected tournament: {selected_tournament.to_dict()}")
                TournamentView.display_rankings_for_tournament(selected_tournament)
            else:
                print("Invalid tournament selection.")
        elif choice == "" or choice == "0":
            print("Returning to menu.")
        else:
            print("Invalid input.")

    @staticmethod
    def display_rankings_for_tournament(tournament):
        """Static method to display rankings of the selected tournament."""
        if tournament:
            rankings = tournament.get_rankings()
            if rankings:
                TournamentTemplate.display_rankings(rankings=rankings)
            else:
                print("No rankings available.")
        else:
            print("No tournament available to display rankings.")
