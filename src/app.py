from src.menu.main_menu import MainMenu
from src.menu.aws_menu import AWSMenu
from src.models.resource import Resource

class App:
    def main(self):
        """Main application loop handling authentication and AWS menu."""
        # Main menu loop
        while True:
            user_credentials = MainMenu().handle()
            
            # AWS menu loop
            while True:
                AWSMenu(user_credentials).handle()
                break

if __name__ == "__main__":
    app = App()
    app.main()
