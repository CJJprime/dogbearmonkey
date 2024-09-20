import ui
import catch
import battle
import logging
import ui

logging.basicConfig(level=logging.INFO)

class EncounterModule:
    def __init__(self):
        self.ui = ui.UI()
        self.settings = self.ui.get_settings()

    def start(self):
        # Determine encounter type
        if self.is_rare_encounter():
            # Handle rare encounter
            pass
        elif self.is_catch_list_encounter():
            # Enter catch mode
            catch.CatchModule().start()
        else:
            # Enter battle mode
            battle.BattleModule().start()

        # Update UI statistics
        self.ui.update_statistics()


class EncounterModule:
    def __init__(self):
        self.ui_settings = ui.get_settings()

    def start(self):
        try:
            # Determine encounter type
            if self.is_rare_encounter():
                # Handle rare encounter
                pass
            elif self.is_catch_list_encounter():
                # Enter catch mode
                catch.CatchModule().start()
            else:
                # Enter battle mode
                battle.BattleModule().start()
        except Exception as e:
            logging.error(f"Error in EncounterModule: {str(e)}")
            print(f"Error: {str(e)}")

        # Update UI statistics
        ui.update_statistics()