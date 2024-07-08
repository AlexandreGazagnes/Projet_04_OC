from .routes import MV, routes


class App:
    """The main application class."""

    @staticmethod
    def run(self):
        """Run the application."""

        view_str = "MainView.menu"
        data = {}

        while view_str != "exit":

            # Get the view function from the routes dictionary
            view_function = routes.get(view_str)

            # If the view function is not found, print an error message and exit the program
            if not view_function:
                print(f"Error: No route found for {view_str}")
                raise SystemExit("Exiting the program...")

            # Call the view function and get the next view and data
            view_str, data = view_function(data)

        raise SystemExit("Exiting the program...")
