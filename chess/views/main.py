"""
Main View module : Contains the MainView class and the main function.
"""

from chess.templates.main import MainTemplate


class MainView:

    @staticmethod
    def menu(data={}):
        """Display the main menu and handle user input."""

        choice = MainTemplate.menu()

        if choice == "1":
            return "PlayerView.menu", data
        elif choice == "2":
            return "TournamentView.menu", data
        elif choice == "3":
            return "exit", data
        else:
            return "MainView.menu", data
