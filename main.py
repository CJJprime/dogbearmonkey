import ui
import subprocess
import time
import keyboard


class Main:
    def __init__(self):
        self.ui = ui.UI()
        self.movement_process = None

    def run(self):
        self.start_movement_process()
        keyboard.on_press_key("f12", self.on_f12_press)
        self.ui.root.mainloop()

    def start_movement_process(self):
        self.movement_process = subprocess.Popen(["python", "movement.py"])

    def on_f12_press(self, event):
        if self.movement_process:
            self.movement_process.terminate()
            time.sleep(1)
            self.start_movement_process()


if __name__ == "__main__":
    main = Main()
    main.run()