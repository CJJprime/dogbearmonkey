import ui
import ui
import time

class CatchModule:
    def __init__(self):
        self.ui = ui.UI()

    def start(self):
        catch_list = self.ui.get_catch_list()
        # Simulate catch attempt
        time.sleep(2)
        catch_result = random.choice(["Success", "Failure"])
        if catch_result == "Success":
            self.ui.update_statistics(encounters=1, catches=1)
            print("Pokémon caught successfully!")
        else:
            self.ui.update_statistics(encounters=1)
            print("Pokémon catch failed.")

