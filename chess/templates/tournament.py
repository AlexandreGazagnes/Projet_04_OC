#### NO MODELS IN TEMPLATES !!!!      ####
from typing import List, Dict

import logging


class TournamentTemplate:
    """Template for tournament management."""

    @staticmethod
    def menu(cls) -> str:
        """Display tournament menu options."""

        print("\nTournament Menu")
        print("1. Create a tournament")
        print("2. Add a player")
        print("3. Launch tournament")
        print("4. Create a new round")
        print("5. Display rankings")
        print("6. Return to the main menu")  # "" to return to the main menu ?

        return input("Enter the number you want: ")

    @staticmethod
    def create(cls) -> Dict:
        """Template for creating a tournament."""

        print("\nCreating a new tournament...")

        name = input("Enter the name of the tournament: ")
        start_date = input("Enter the start date of the tournament (YYYY-MM-DD): ")
        end_date = input("Enter the end date of the tournament (YYYY-MM-DD): ")
        description = input("Enter the description of the tournament: ")
        location = input("Enter the location of the tournament: ")

        return {
            "name": name,
            "start_date": start_date,
            "end_date": end_date,
            "description": description,
            "location": location,
        }

    @staticmethod
    def update(cls, tournament: Dict) -> Dict:
        """Template for updating a tournament."""

        print("\nUpdating the tournament... NOT IMPLETED YET !")

    @staticmethod
    def delete(cls, tournament: Dict) -> Dict:
        """Template for deleting a tournament."""

        print("\nDeleting the tournament... NOT IMPLETED YET !")

    @staticmethod
    def add_player(cls) -> Dict:
        """Template for adding a player to the tournament."""

        print("\nAdding a new player...")

        firstname = input("Enter the first name of the player: ")
        lastname = input("Enter the last name of the player: ")
        birthdate = input("Enter the birthdate of the player (YYYY-MM-DD): ")

        return {
            "firstname": firstname,
            "lastname": lastname,
            "birthdate": birthdate,
        }

    @staticmethod
    def launch(cls) -> bool:
        """Template for launching the tournament."""

        print("\nLaunching the tournament...")
        choice = input(
            "Press Enter to confirm launching the tournament / Any key to cancel."
        )

        # if choice:
        #    return False

        # return True

        return False if choice else True  # ternary operator

    @staticmethod
    def new_round(cls) -> None:
        """Template for creating a new round."""

        print("\Going to netx round")
        choice = input("Press Enter to confirm / Any key to cancel.")

        return False if choice else True  # ternary operator

    @staticmethod
    def update_current_round(cls, match_list: List[List]) -> List[List]:
        """Template for updating the current round."""

        # logging.info(f"BEFORE: {match_list}")

        print("\nUpdating the current round...")

        for n_match, match in enumerate(match_list):
            print(f"Match {n_match}:")

            # logging.info(f"match: {match}")

            for n_player, player in enumerate(match):

                # logging.info(f"player: {player}")
                print(f"Enter the score of the player id {player[0]}: ")
                score = int(input())

                # logging.info(f"???: {match_list[n_match][n_player][1]} ==> {score}")
                # AWFUL PATCH !!! => to fix in the models drirecty
                match_list[n_match][n_player] = list(match_list[n_match][n_player])
                match_list[n_match][n_player][1] = score

        # logging.info(f"AFTER: {match_list}")

        return match_list

    @staticmethod
    def display_rankings(cls, rankings: List[Dict]) -> None:
        """Template for displaying rankings."""

        print("\nRankings:")

        for rank, player in enumerate(rankings, start=1):
            print(
                f"{rank}. {player['firstname']} {player['lastname']} - {player['score']} points"
            )

    @staticmethod
    def display_tournament(tournament):
        """Display the details of the selected tournament."""

        print("\nTournament Details:")
        print(f"ID: {tournament.id}")
        print(f"Name: {tournament.name}")
        print(f"Start Date: {tournament.start_date}")
        print(f"End Date: {tournament.end_date}")
        print(f"Description: {tournament.description}")
        print(f"Location: {tournament.location}")
        print(f"Status: {tournament.status}")
        print(f"Number of Players: {len(tournament.players)}")
