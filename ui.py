import tkinter as tk
from tkinter import ttk


class UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pokémon Bot")
        self.root.geometry("800x600")

        self.phi = 1.618
        self.width = 800
        self.height = 600

        self.tab_control = ttk.Notebook(self.root)
        self.tab_control.place(x=self.width * 0.05, y=self.height * 0.05, width=self.width * 0.9, height=self.height * 0.9)

        self.settings_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.settings_tab, text="Settings")

        self.settings_frame = ttk.Frame(self.settings_tab)
        self.settings_frame.place(x=self.width * 0.1 / self.phi, y=self.height * 0.1 / self.phi,
                                  width=self.width * 0.8 / self.phi, height=self.height * 0.8 / self.phi)

        self.run_time_label = ttk.Label(self.settings_frame, text="Run Time (minutes):")
        self.run_time_label.place(x=self.width * 0.1 / (self.phi ** 2), y=self.height * 0.1 / (self.phi ** 2))
        self.run_time_entry = tk.Entry(self.settings_frame, width=5)
        self.run_time_entry.place(x=self.width * 0.47 / (self.phi ** 2), y=self.height * 0.1 / (self.phi ** 2))

        self.movement_label = ttk.Label(self.settings_frame, text="Movement:")
        self.movement_label.place(x=self.width * 0.1 / (self.phi ** 2), y=self.height * 0.2 / (self.phi ** 2))
        self.movement_var = tk.StringVar()
        ttk.OptionMenu(self.settings_frame, self.movement_var, "Horizontal", "Vertical").place(
            x=self.width * 0.3 / (self.phi ** 2), y=self.height * 0.2 / (self.phi ** 2))

        self.rares_label = ttk.Label(self.settings_frame, text="Rares:")
        self.rares_label.place(x=self.width * 0.1 / (self.phi ** 2), y=self.height * 0.3 / (self.phi ** 2))
        self.rares_var = tk.StringVar()
        ttk.OptionMenu(self.settings_frame, self.rares_var, "Stop", "Catch").place(
            x=self.width * 0.3 / (self.phi ** 2), y=self.height * 0.3 / (self.phi ** 2))

        self.battle_mode_label = ttk.Label(self.settings_frame, text="Battle Mode:")
        self.battle_mode_label.place(x=self.width * 0.1 / (self.phi ** 2), y=self.height * 0.4 / (self.phi ** 2))
        self.battle_mode_var = tk.StringVar()
        ttk.OptionMenu(self.settings_frame, self.battle_mode_var, "Catch/Run", "Catch/Fight", "Fight").place(
            x=self.width * 0.3 / (self.phi ** 2), y=self.height * 0.4 / (self.phi ** 2))

        self.catch_label = ttk.Label(self.settings_frame, text="Catch:")
        self.catch_label.place(x=self.width * 0.1 / (self.phi ** 2), y=self.height * 0.5 / (self.phi ** 2))
        self.catch_var = tk.StringVar()
        ttk.OptionMenu(self.settings_frame, self.catch_var, "Pause", "KeyPress 1", "KeyPress 2", "KeyPress 3", "KeyPress 4",
                       "KeyPress 5", "KeyPress 6").place(
            x=self.width * 0.3 / (self.phi ** 2), y=self.height * 0.5 / (self.phi ** 2))

        self.catch_list_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.catch_list_tab, text="Catch List")

        self.catch_list_frame = ttk.Frame(self.catch_list_tab)
        self.catch_list_frame.place(x=self.width * 0.1 / self.phi, y=self.height * 0.1 / self.phi,
                                    width=self.width * 0.8 / self.phi, height=self.height * 0.8 / self.phi)

        self.catch_list_label = ttk.Label(self.catch_list_frame, text="Catch List:")
        self.catch_list_label.place(x=self.width * 0.1 / (self.phi ** 2), y=self.height * 0.1 / (self.phi ** 2))

        self.catch_list_entry = tk.Entry(self.catch_list_frame)
        self.catch_list_entry.place(x=self.width * 0.3 / (self.phi ** 2), y=self.height * 0.1 / (self.phi ** 2),
                                    width=self.width * 0.5 / (self.phi ** 2))

        self.add_button = tk.Button(self.catch_list_frame, text="Add", command=self.add_to_catch_list)
        self.add_button.place(x=self.width * 0.8 / (self.phi ** 2), y=self.height * 0.1 / (self.phi ** 2))

        self.remove_button = tk.Button(self.catch_list_frame, text="Remove", command=self.remove_from_catch_list)
        self.remove_button.place(x=self.width * 0.8 / (self.phi ** 2), y=self.height * 0.2 / (self.phi ** 2))

        self.catch_list_listbox = tk.Listbox(self.catch_list_frame)
        self.catch_list_listbox.place(x=self.width * 0.1 / (self.phi ** 2), y=self.height * 0.3 / (self.phi ** 2),
                                      width=self.width * 0.8 / (self.phi ** 2),
                                      height=self.height * 0.6 / (self.phi ** 2))

        self.statistics_frame = ttk.Frame(self.root)
        self.statistics_frame.place(x=self.width * 0.05, y=self.height * 0.95 / self.phi,
                                    width=self.width * 0.9, height=self.height * 0.05)

        self.encounters_label = ttk.Label(self.statistics_frame, text="Encounters: 0")
        self.encounters_label.place(x=self.width * 0.1 / (self.phi ** 2), y=self.height * 0.01 / (self.phi ** 2))

        self.catches_label = ttk.Label(self.statistics_frame, text="Catches: 0")
        self.catches_label.place(x=self.width * 0.4 / (self.phi ** 2), y=self.height * 0.01 / (self.phi ** 2))

        self.battles_won_label = ttk.Label(self.statistics_frame, text="Battles Won: 0")
        self.battles_won_label.place(x=self.width * 0.7 / (self.phi ** 2), y=self.height * 0.01 / (self.phi ** 2))

        self.log_frame = ttk.Frame(self.root)
        self.log_frame.place(x=self.width * 0.05, y=self.height * 1.0 / self.phi,
                             width=self.width * 0.9, height=self.height * 0.4 / self.phi)

        self.log_text = tk.Text(self.log_frame)
        self.log_text.place(x=self.width * 0.01, y=self.height * 0.01,
                            width=self.width * 0.98, height=self.height * 0.98)

        self.catch_list = []

    def add_to_catch_list(self):
        pokemon_name = self.catch_list_entry.get()
        self.catch_list.append(pokemon_name)
        self.catch_list_listbox.insert(tk.END, pokemon_name)
        self.catch_list_entry.delete(0, tk.END)

    def remove_from_catch_list(self):
        selected_index = self.catch_list_listbox.curselection()
        self.catch_list_listbox.delete(selected_index)
        self.catch_list.pop(selected_index[0])

    def run(self):
        self.root.mainloop()

def main():
        ui = UI()
        ui.run()

if __name__ == "__main__":
        main()