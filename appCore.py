from tkinter import messagebox
import json
import customtkinter as ctk
from PIL.ImageTk import PhotoImage
import os

maplist = ""
ui_maplist = ""

modes = [{"name": "Air Superiority", "modeID": "AirSuperiority0"}, #0
         {"name": "Capture the Flag", "modeID": "CaptureTheFlag0"}, #1
         {"name": "Conquest", "modeID": "ConquestSmall0"}, #2
         {"name": "Conquest 64", "modeID": "ConquestLarge0"}, #3
         {"name": "Conquest Assault", "modeID": "ConquestAssaultSmall0"}, #4
         {"name": "Conquest Assault 64", "modeID": "ConquestAssaultLarge0"}, #5
         {"name": "Conquest Assault: Day 2", "modeID": "ConquestAssaultSmall1"}, #6
         {"name": "Conquest Domination", "modeID": "Domination0"}, #7
         {"name": "Gun Master", "modeID": "GunMaster0"}, #8
         {"name": "Rush", "modeID": "RushLarge0"}, #9
         {"name": "Scavenger", "modeID": "Scavenger0"}, #10
         {"name": "Squad Deathmatch", "modeID": "SquadDeathMatch0"}, #11
         {"name": "Squad Rush", "modeID": "SquadRush0"}, #12
         {"name": "Tank Superiority", "modeID": "TankSuperiority0"}, #13
         {"name": "Team Deathmatch", "modeID": "TeamDeathMatch0"}, #14
         {"name": "Team DM Close Quarters", "modeID": "TeamDeathMatchC0"}, #15
         ]

maps = [{"name": "Alborz Mountains", "mapID": "XP3_Alborz", "modes": [modes[2], modes[3], modes[9], modes[11], modes[14], modes[15]]},
        {"name": "Armored Shield", "mapID": "XP3_Shield", "modes": [modes[2], modes[3], modes[9], modes[11], modes[12], modes[13], modes[14], modes[15]]},
        {"name": "Azadi Palace", "mapID": "XP4_Parl", "modes": [modes[2], modes[3], modes[8], modes[9], modes[10], modes[11], modes[14], modes[15]]},
        {"name": "Bandar Desert", "mapID": "XP3_Desert", "modes": [modes[2], modes[3], modes[9], modes[11], modes[12], modes[13], modes[14], modes[15]]},
        {"name": "Caspian Border", "mapID": "MP_007", "modes": [modes[2], modes[3], modes[8], modes[9], modes[11], modes[12], modes[14], modes[15]]},
        {"name": "Damavand Peak", "mapID": "MP_013", "modes": [modes[2], modes[3], modes[8], modes[9], modes[10], modes[14], modes[15]]},
        {"name": "Death Valley", "mapID": "XP3_Valley", "modes": [modes[2], modes[3], modes[9], modes[11], modes[12], modes[13], modes[14], modes[15]]},
        {"name": "Donya Fortress", "mapID": "XP2_Palace", "modes": [modes[7], modes[8], modes[11], modes[15]]},
        {"name": "Epicenter", "mapID": "XP4_Quake", "modes": [modes[2], modes[3], modes[8], modes[9], modes[10], modes[11], modes[12], modes[14], modes[15]]},
        {"name": "Grand Bazaar", "mapID": "MP_001", "modes": [modes[2], modes[3], modes[8], modes[9], modes[10], modes[11], modes[12], modes[14], modes[15]]},
        {"name": "Gulf of Oman", "mapID": "XP1_002", "modes": [modes[4], modes[2], modes[3], modes[9], modes[11], modes[14], modes[15]]},
        {"name": "Kharg Island", "mapID": "MP_018", "modes": [modes[2], modes[3], modes[8], modes[9], modes[11], modes[12], modes[14], modes[15]]},
        {"name": "Kiasar Railroad", "mapID": "XP5_003", "modes": [modes[1], modes[2], modes[3], modes[8], modes[9], modes[11], modes[14], modes[15]]},
        {"name": "Markaz Monolith", "mapID": "MP_007", "modes": [modes[2], modes[3], modes[8], modes[9], modes[10], modes[11], modes[14], modes[15]]},
        {"name": "Nebandan Flats", "mapID": "XP5_002", "modes": [modes[2], modes[3], modes[8], modes[9], modes[11], modes[12], modes[14], modes[15]]},
        {"name": "Noshahr Canals", "mapID": "MP_017", "modes": [modes[2], modes[3], modes[8], modes[9], modes[11], modes[12], modes[14], modes[15]]},
        {"name": "Operation 925", "mapID": "XP2_Office", "modes": [modes[7], modes[8], modes[11], modes[12], modes[15]]},
        {"name": "Operation Firestorm", "mapID": "MP_007", "modes": [modes[2], modes[3], modes[8], modes[9], modes[11], modes[12], modes[14], modes[15]]},
        {"name": "Operation Metro", "mapID": "MP_Subway", "modes": [modes[3], modes[8], modes[9], modes[11], modes[12], modes[14], modes[15]]},
        {"name": "Operation Riverside", "mapID": "XP5_001", "modes": [modes[2], modes[3], modes[9], modes[11], modes[14], modes[15]]},
        {"name": "Sabalan Pipeline", "mapID": "XP5_004", "modes": [modes[2], modes[3], modes[9], modes[11], modes[12], modes[14], modes[15]]},
        {"name": "Scrapmetal", "mapID": "XP2_Factory", "modes": [modes[7], modes[8], modes[11], modes[12], modes[15]]},
        {"name": "Seine Crossing", "mapID": "MP_011", "modes": [modes[2], modes[3], modes[8], modes[9], modes[11], modes[12], modes[14], modes[15]]},
        {"name": "Sharqi Peninsula", "mapID": "XP1_003", "modes": [modes[4], modes[5], modes[6], modes[8], modes[9], modes[14], modes[15]]},
        {"name": "Talah Market", "mapID": "XP4_Rubble", "modes": [modes[4], modes[8], modes[9], modes[10], modes[11], modes[12], modes[14], modes[15]]},
        {"name": "Tehran Highway", "mapID": "MP_003", "modes": [modes[2], modes[3], modes[8], modes[9], modes[11], modes[12], modes[14], modes[15]]},
        ]


class AppCore(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mod Config Tool")
        self.geometry("900x850")
        self.configure(bg="#2C2C2C")
        self.resizable(False, False)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.top_menu_frame = TopMenuFrame(self,
                                           fg_color="#1E1E1E",
                                           bg_color="#1E1E1E",
                                           width=900,
                                           height=115,
                                           )

        self.top_menu_frame.grid(row=0,
                                 column=0,

                                 sticky="new",
                                 )

        self.main_content_tabview = MainContentTabView(self, fg_color="#2C2C2C", bg_color="#1E1E1E")
        self.main_content_tabview.grid(row=0,
                                       column=0,
                                       sticky="ewn",
                                       pady=95,
                                       )

        self._set_appearance_mode("dark")


####################TOP MENU FRAME
class TopMenuFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.menu_icon_button = ctk.CTkButton(master=master,
                                              text="",
                                              image=PhotoImage(file="assets/icons/menu.png"),
                                              height=50,
                                              width=50,
                                              bg_color="#1E1E1E",
                                              fg_color="transparent",
                                              anchor="left"
                                              )

        self.menu_icon_button.grid(row=0,
                                   column=0,
                                   pady=25,
                                   padx=15,
                                   sticky="nw",
                                   )

        self.top_menu_title_label = ctk.CTkLabel(master=master,
                                                 text="Mod Configuration Tool",
                                                 font=("Segoe UI", 32),
                                                 fg_color="#1E1E1E",
                                                 text_color="#FFFFFF",
                                                 anchor="center"
                                                 )

        self.top_menu_title_label.grid(row=0,
                                       column=0,
                                       padx=15,
                                       pady=35,
                                       sticky="n",
                                       )


###################MAIN CONTENT
class MainContentTabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.add("Map Config")
        self.add("Server Config")

        ####################MAP CONFIG
        self.mapConfigMainLabel = ctk.CTkLabel(master=self.tab("Map Config"),
                                               text="BF3 Server Map Configuration Tool",
                                               font=("Segoe UI", 24),
                                               text_color="#FFFFFF",
                                               )

        self.mapConfigMainLabel.grid(row=0,
                                     column=0,
                                     padx=250,
                                     pady=15,
                                     sticky="n",
                                     )

        self.mapConfigOptionsTabFrame = MapConfigOptionsTabFrame(self.tab("Map Config"),
                                                                 fg_color="#1E1E1E",
                                                                 bg_color="#1E1E1E",
                                                                 width=320,
                                                                 height=450,
                                                                 border_width=1,
                                                                 )

        self.mapConfigOptionsTabFrame.grid(row=0,
                                           column=0,
                                           ipady=100,
                                           ipadx=75,
                                           padx=25,
                                           pady=100,
                                           sticky="w",
                                           )

        self.mapConfigMaplistTabFrame = MapConfigMaplistFrame(self.tab("Map Config"),
                                                              fg_color="#1E1E1E",
                                                              bg_color="#1E1E1E",
                                                              width=320,
                                                              height=450,
                                                              border_width=1,
                                                              )

        self.mapConfigMaplistTabFrame.grid(row=0,
                                           column=0,
                                           ipady=50,
                                           padx=25,
                                           pady=100,
                                           sticky="ne",
                                           )

        #####################SERVER CONFIG
        self.serverConfigMainLabel = ctk.CTkLabel(master=self.tab("Server Config"),
                                                  text="BF3 Server Fun-Bot Configuration Tool (WIP/NON-FUNCTIONAL)",
                                                  font=("Segoe UI", 24),
                                                  text_color="#FFFFFF",
                                                  anchor="center"
                                                  )

        self.serverConfigMainLabel.grid(row=0,
                                        column=0,
                                        #ipady=50,
                                        padx=95,
                                        pady=100,
                                        sticky="n",
                                        )
        self.serverConfigFrame = BF3FunBotConfigFrame(self.tab("Server Config"),
                                                      fg_color="#1E1E1E",
                                                      bg_color="#1E1E1E",
                                                      width=320,
                                                      height=450,
                                                      border_width=1,
                                                      )
        self.serverConfigFrame.grid(row=0,
                                   column=0,
                                   padx=25,
                                   pady=200,
                                   sticky="n",
                                   )

class BF3FunBotConfigFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.settings_definition = ""
        self.bot_config_definition = ""
        self.new_server_config_button = ctk.CTkButton(self,
                                                     text="New Server Config",
                                                     text_color="#FFFFFF",
                                                     height=30,
                                                     width=225,
                                                     font=("Segoe UI", 14),
                                                     command=self.init_new_server_config,
                                                     state="enabled",
                                                      anchor="center"
                                                     )
        self.new_server_config_button.grid(row=0,
                                          column=0,
                                          padx=25,
                                          pady=25,
                                          sticky="ew",
                                          )
        self.new_server_config_window = None

    def open_new_server_config_window(self):
        if self.new_server_config_window is None or not self.new_server_config_window.winfo_exists():
            self.new_server_config_window = NewBF3ServerConfigWindow(self)
            self.new_server_config_window.grab_set()
            self.new_server_config_window.focus_set()
        else:
            self.new_server_config_window.focus_set()

    def init_new_server_config(self):
        try:
            with open("bf3-reference-settings/settings-definition.json", "r", encoding="utf-8") as f:
                self.settings_definition = json.load(f)
                f.close()
        except Exception:
            messagebox.showerror("Error", "Failed to load settings definition file.")
        try:
            with open("bf3-reference-settings/Config.json", "r", encoding="utf-8") as f:
                self.bot_config_definition = json.load(f)
                f.close()
        except Exception:
            messagebox.showerror("Error", "Failed to load bot config definition file.")

        self.open_new_server_config_window()





class NewBF3ServerConfigWindow(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.title("New BF3 Server Config")
        self.geometry("1000x700")
        self.resizable(False, False)
        self.configure(bg="#2C2C2C")
        self.grid_columnconfigure((0, 1), weight=1)  # Configure two columns

        # Load Config JSON
        with open("bf3-reference-settings/Config.json", "r") as file:
            self.config_data = json.load(file)["Config"]

        # Create a scrollable frame
        self.scrollable_frame = ctk.CTkScrollableFrame(self, fg_color="#2C2C2C", width=950, height=650)
        self.scrollable_frame.grid(row=1, column=0, padx=20, pady=20, columnspan=2, sticky="nsew")

        # Add export button
        self.export_button = ctk.CTkButton(
            self,
            text="Export Config",
            text_color="#FFFFFF",
            font=("Segoe UI", 14),
            height=30,
            width=200,
            fg_color="#3A3A3A",
            command=self.export_to_files
        )
        self.export_button.grid(row=0, column=1, padx=20, pady=10, sticky="ne")  # Position at the top-right corner

        # Generate labels and dropdowns for each config entry
        self.generate_config_elements()

    def generate_config_elements(self):
        """Generate a label and dropdown/entry field for each key in the config."""
        column_count = 2  # Number of columns
        row, column = 0, 0  # Initialize row and column

        for key, value in self.config_data.items():
            # Label
            label = ctk.CTkLabel(self.scrollable_frame, text=key, font=("Segoe UI", 14), text_color="#FFFFFF", anchor="w")
            label.grid(row=row, column=column * 2, padx=10, pady=5, sticky="w")  # Use even column for labels

            # Dropdown or Entry
            if isinstance(value, bool):  # Boolean fields as dropdowns
                option_menu = ctk.CTkOptionMenu(self.scrollable_frame, values=["True", "False"], fg_color="#3A3A3A", text_color="#FFFFFF",
                                                command=lambda v, k=key: self.update_config_value(k, v))
                option_menu.set(str(value))  # Set the initial value
                option_menu.grid(row=row, column=column * 2 + 1, padx=10, pady=5, sticky="e")  # Use odd column for inputs

            elif isinstance(value, (int, float)):  # Numeric fields as entry widgets
                entry = ctk.CTkEntry(self.scrollable_frame, fg_color="#3A3A3A", text_color="#FFFFFF")
                entry.insert(0, value)  # Set the initial value
                entry.grid(row=row, column=column * 2 + 1, padx=10, pady=5, sticky="e")
                entry.bind("<FocusOut>", lambda e, k=key, widget=entry: self.update_numeric_value(k, widget))

            elif isinstance(value, str):  # Strings as Entry widgets
                entry = ctk.CTkEntry(self.scrollable_frame, fg_color="#3A3A3A", text_color="#FFFFFF")
                entry.insert(0, value)  # Set the initial value
                entry.grid(row=row, column=column * 2 + 1, padx=10, pady=5, sticky="e")
                entry.bind("<FocusOut>", lambda e, k=key, widget=entry: self.update_config_value(k, widget.get()))

            else:  # Other types use a generic text field
                entry = ctk.CTkEntry(self.scrollable_frame, fg_color="#3A3A3A", text_color="#FFFFFF")
                entry.insert(0, str(value))  # Set the initial value
                entry.grid(row=row, column=column * 2 + 1, padx=10, pady=5, sticky="e")
                entry.bind("<FocusOut>", lambda e, k=key, widget=entry: self.update_config_value(k, widget.get()))

            # Update row and column for two columns
            column += 1
            if column >= column_count:  # Move to the next row after two entries
                row += 1
                column = 0

    def update_config_value(self, key, value):
        """Update the config dictionary with the new value."""
        if isinstance(self.config_data[key], bool):  # Handle boolean conversion
            self.config_data[key] = value == "True"
        else:
            self.config_data[key] = value
        print(f"{key} updated to {value}")

    def update_numeric_value(self, key, widget):
        """Update numeric config values and validate input."""
        try:
            value = float(widget.get())
            if isinstance(self.config_data[key], int):  # Preserve integer type
                value = int(value)
            self.config_data[key] = value
            print(f"{key} updated to {value}")
        except ValueError:
            print(f"Invalid input for {key}, resetting value.")
            widget.delete(0, "end")
            widget.insert(0, self.config_data[key])  # Reset to previous value

    def export_to_files(self):
        """Export the current config data to JSON and Lua files."""
        # Step 1: Export as JSON
        export_dir = "user-generated/fun-bot config"
        lua_export_dir = os.path.join(export_dir, "lua")
        os.makedirs(export_dir, exist_ok=True)  # Create directories if they don't exist
        os.makedirs(lua_export_dir, exist_ok=True)

        json_file_path = os.path.join(export_dir, "Config.json")
        lua_file_path = os.path.join(lua_export_dir, "Config.lua")

        try:
            # Save as JSON
            with open(json_file_path, "w", encoding="utf-8") as json_file:
                json.dump({"Config": self.config_data}, json_file, indent=4)

            # Save as Lua
            lua_content = self.convert_to_lua_format(self.config_data)
            with open(lua_file_path, "w", encoding="utf-8") as lua_file:
                lua_file.write(lua_content)

            messagebox.showinfo("Export Successful", f"Configuration exported to:\n{json_file_path}\nand\n{lua_file_path}")
        except Exception as e:
            messagebox.showerror("Export Failed", f"Failed to export configuration:\n{str(e)}")

    def convert_to_lua_format(self, config_data):
        """Convert JSON config data to Lua format."""
        lua_lines = [
            "-- This file is autogenerated. Changes made here might be overwritten.\n\n",
            "---@class Config\n",
            "Config = {\n"
        ]

        for key, value in config_data.items():
            if isinstance(value, str) and value not in ["true", "false"] and value != "null":  # Format strings
                lua_lines.append(f"\t{key} = \"{value}\",\n")
            elif isinstance(value, bool):  # Format booleans
                lua_lines.append(f"\t{key} = {'true' if value else 'false'},\n")
            elif value == "null": # Convert null to nil
                lua_lines.append(f"\t{key} = {'nil'},\n")
            else:  # Format other types (numbers, etc.)
                lua_lines.append(f"\t{key} = {value},\n")

        lua_lines.append("}\n")
        return "".join(lua_lines)


##################MAP CONFIG FRAME
class MapConfigOptionsTabFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.numRounds = 1
        selected_map = ctk.StringVar(value="")
        selected_mode = ctk.StringVar(value="")
        global ui_maplist
        self.mapSelectLabel = ctk.CTkLabel(self,
                                           text="Map:",
                                           font=("Segoe UI", 14),
                                           text_color="#FFFFFF",
                                           height=30,
                                           bg_color="#1E1E1E",
                                           )

        self.mapSelectLabel.grid(row=0,
                                 column=0,
                                 padx=25,
                                 pady=15,
                                 sticky="nw",
                                 )

        self.select_map = ctk.CTkOptionMenu(self,
                                            text_color="#FFFFFF",
                                            height=30,
                                            width=225,
                                            font=("Segoe UI", 14),
                                            values=[m['name'] for m in maps],
                                            command=self.update_compatible_modes,
                                            variable=selected_map,
                                            )

        self.select_map.grid(row=0,
                             column=0,
                             padx=25,
                             pady=45,
                             sticky="nw",
                             )

        self.modeSelectLabel = ctk.CTkLabel(self,
                                            text="Game Mode:",
                                            font=("Segoe UI", 14),
                                            text_color="#FFFFFF",
                                            height=30,
                                            )

        self.modeSelectLabel.grid(row=0,
                                  column=0,
                                  padx=25,
                                  pady=85,
                                  sticky="nw",
                                  )

        self.select_mode = ctk.CTkOptionMenu(self,
                                             text_color="#FFFFFF",
                                             height=30,
                                             width=225,
                                             font=("Segoe UI", 14),
                                             values=[m['name'] for m in modes],
                                             variable=selected_mode,
                                             )

        self.select_mode.grid(row=0,
                              column=0,
                              padx=25,
                              pady=115,
                              sticky="nw",
                              )

        self.roundSelectLabel = ctk.CTkLabel(self,
                                             text=f"Number of Rounds: {self.numRounds}",
                                             font=("Segoe UI", 14),
                                             text_color="#FFFFFF",
                                             height=30,
                                             )

        self.roundSelectLabel.grid(row=0,
                                   column=0,
                                   padx=25,
                                   pady=155,
                                   sticky="nw",
                                   )

        self.select_rounds = ctk.CTkSlider(self,
                                           from_=1,
                                           to=10,
                                           number_of_steps=10,
                                           command=self.update_rounds_label,
                                           )

        self.select_rounds.set(self.numRounds)

        self.select_rounds.grid(row=0,
                                column=0,
                                padx=25,
                                pady=185,
                                sticky="nw",
                                )

        self.add_to_serverlist_button = ctk.CTkButton(self,
                                                     text="Add to Serverlist",
                                                     text_color="#FFFFFF",
                                                     height=30,
                                                     width=225,
                                                     font=("Segoe UI", 14),
                                                     command=self.add_to_serverlist,
                                                     state="enabled",
                                                     )

        self.add_to_serverlist_button.grid(row=0,
                                        column=0,
                                        padx=25,
                                        pady=225,
                                        sticky="nw",
                                        )

        self.remove_map_button = ctk.CTkButton(self,
                                                     text="Remove last map from ServerList",
                                                     text_color="#FFFFFF",
                                                     height=30,
                                                     width=225,
                                                     font=("Segoe UI", 14),
                                                     command=self.remove_from_serverlist,
                                                     state="enabled",
                                                     )

        self.remove_map_button.grid(row=0,
                                        column=0,
                                        padx=25,
                                        pady=265,
                                        sticky="nw",
                                        )

        self.export_to_file_button = ctk.CTkButton(self,
                                                     text="Export to MapList.txt",
                                                     text_color="#FFFFFF",
                                                     height=30,
                                                     width=225,
                                                     font=("Segoe UI", 14),
                                                     command=self.export_to_file,
                                                     state="enabled",
                                                     )

        self.export_to_file_button.grid(row=0,
                                        column=0,
                                        padx=25,
                                        pady=305,
                                        sticky="nw",
                                        )

        self.import_from_file_button = ctk.CTkButton(self,
                                                     text="Import from File",
                                                     text_color="#FFFFFF",
                                                     height=30,
                                                     width=225,
                                                     font=("Segoe UI", 14),
                                                     command=self.load_map_file,
                                                     state="enabled",
                                                     )

        self.import_from_file_button.grid(row=0,
                                        column=0,
                                        padx=25,
                                        pady=345,
                                        sticky="nw",
                                        )

    def update_rounds_label(self, value):
        value = int(value)
        self.roundSelectLabel.configure(text=f"Number of Rounds: {value}")

    def update_compatible_modes(self, value, **kwargs):
        selected_map = value

        for m in maps:
            if m['name'] == selected_map:
                self.select_mode.configure(values=[i['name'] for i in m['modes']])
                self.select_mode.set(m['modes'][0]['name'])
                return
            else:
                self.select_mode.configure(values=[i['name'] for i in modes])
                continue

    def add_to_serverlist(self):
        selected_map = self.select_map.get()
        selected_mode = self.select_mode.get()
        num_rounds = self.select_rounds.get()
        global maplist
        global ui_maplist

        if maplist == "":
            maplist = ctk.StringVar(value=maplist)
        selected_map_id = str([i["mapID"] for i in maps if i["name"] == selected_map])
        selected_mode_id = str([i["modeID"] for i in modes if i["name"] == selected_mode])

        map_to_add = selected_map_id.strip("['']") + " " + selected_mode_id.strip("['']") + " " + str(int(num_rounds)) + "\n"
        maplist.set(maplist.get() + map_to_add)

        w = MapConfigMaplistFrame(self)
        if ui_maplist == "" or not isinstance(ui_maplist, ctk.StringVar):
            ui_maplist = ctk.StringVar(value=ui_maplist)

        ui_maplist.set(ui_maplist.get() + selected_map + \
                             " --- " + selected_mode + \
                             " --- " + str(int(num_rounds)) + "\n")

        w.mapList.configure(textvariable=ui_maplist)
        w.mapList.configure(text=ui_maplist)
        w.mapList.update()

    def remove_from_serverlist(self):
        global maplist
        global ui_maplist
        if maplist == "":
            maplist = ctk.StringVar(value=maplist)
            ui_maplist = ctk.StringVar(value=ui_maplist)
        if maplist.get() == "":
            return
        else:
            maplist.set(maplist.get().split("\n", 1)[1])
            ui_maplist.set(ui_maplist.get().split("\n", 1)[1])
        w = MapConfigMaplistFrame(self)
        w.mapList.configure(textvariable=ui_maplist)
        w.mapList.configure(text=ui_maplist)
        w.mapList.update()

    def export_to_file(self):
        global maplist

        if maplist == "":
            maplist = ctk.StringVar(value=maplist)
        if maplist.get() == "":
            return
        else:
            with open("MapList.txt", "w") as f:
                f.write(maplist.get())
                f.close()
                messagebox.showinfo("Success", "MapList.txt has been exported successfully.")

    def load_map_file(self):
        global maplist
        global ui_maplist
        if not isinstance(ui_maplist, ctk.StringVar):
            ui_maplist = ctk.StringVar(value="")
        ui_maplist.set("")

        with open("MapList.txt", "r") as f:
            maplist = f.read()
            f.close()
            messagebox.showinfo("Success", "MapList.txt has been imported successfully.")
        maplist = ctk.StringVar(value=maplist)
        maplist.set(value=maplist.get())

        temp_s = ""
        imaplist = maplist.get().split("\n")
        w = MapConfigMaplistFrame(self)

        for i in imaplist:
            if i == "":
                continue
            else:
                ui_mapname = i.split(" ")[0]

                ui_mapmode = i.split(" ")[1]

                ui_maprounds = i.split(" ")[2]

                try:
                    if ui_mapname in [m['mapID'] for m in maps] and ui_mapmode in [m['modeID'] for m in modes] and ui_maprounds.isdigit():
                        temp_s += "".join([s['name'] for s in maps if s['mapID'] == ui_mapname]).strip("[""]") + \
                                        " --- " + "".join([s['name'] for s in modes if s['modeID'] == ui_mapmode]).strip("[""]") + \
                                        " --- " + ui_maprounds + "\n"

                except Exception:
                    messagebox.showerror("Error", "Invalid Maplist File")
            ui_maplist.set(value=temp_s)
            w.mapList.update()
        ui_maplist.set(value=temp_s)

        w.mapList.configure(textvariable=ui_maplist)
        w.mapList.configure(text=ui_maplist)
        w.mapList.update()

##################Maplist Frame
class MapConfigMaplistFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        global maplist
        global ui_maplist

        self.mapSelectLabel = ctk.CTkLabel(self,
                                           text="Map List:",
                                           font=("Segoe UI", 14),
                                           text_color="#FFFFFF",
                                           height=30,
                                           bg_color="#1E1E1E",
                                           )

        self.mapSelectLabel.grid(row=0,
                                 column=0,
                                 padx=25,
                                 pady=15,
                                 sticky="nw",
                                 )

        if maplist == "":
            maplist = ctk.StringVar(value=maplist)
        if ui_maplist == "":
            ui_maplist = ctk.StringVar(value=ui_maplist)

        self.mapList = ctk.CTkLabel(self,
                                      font=("Segoe UI", 10),
                                      text_color="#FFFFFF",
                                      height=400,
                                      width=320,
                                      bg_color="#1E1E1E",
                                      fg_color="#2C2C2C",
                                      textvariable=ui_maplist,
                                      text="",
                                      anchor="nw",
                                      )

        self.mapList.grid(row=0,
                          column=0,
                          padx=25,
                          pady=100,
                          ipadx=50,
                          sticky="",
                          )


app = AppCore()
app.mainloop()