from tkinter import StringVar, messagebox

import customtkinter as ctk
from PIL.ImageTk import PhotoImage

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
        self.grid_rowconfigure(2, weight=1)

        self.top_menu_frame = TopMenuFrame(self,
                                           fg_color="#1E1E1E",
                                           bg_color="#1E1E1E",
                                           width=900,
                                           height=115,
                                           )

        self.top_menu_frame.grid(row=0,
                                 column=0,
                                 rowspan=2,
                                 sticky="new",
                                 )

        self.main_content_tabview = MainContentTabView(self, fg_color="#2C2C2C", bg_color="#1E1E1E")
        self.main_content_tabview.grid(row=2,
                                       column=0,
                                       sticky="nsew",
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
                                              )

        self.menu_icon_button.grid(row=0,
                                   column=0,
                                   rowspan=2,
                                   padx=15,
                                   sticky="w",
                                   )

        self.top_menu_title_label = ctk.CTkLabel(master=master,
                                                 text="Mod Configuration Tool",
                                                 font=("Segoe UI", 32),
                                                 fg_color="#1E1E1E",
                                                 text_color="#FFFFFF",
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
                                     sticky="new",
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
                                           ipady=275,
                                           ipadx=75,
                                           padx=25,
                                           pady=125,
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
                                           pady=125,
                                           sticky="ne",
                                           )

        #####################SERVER CONFIG
        self.serverConfigMainLabel = ctk.CTkLabel(master=self.tab("Server Config"),
                                                  text="BF3 Server Configuration Tool (COMING SOON)",
                                                  font=("Segoe UI", 24),
                                                  text_color="#FFFFFF",
                                                  )

        self.serverConfigMainLabel.grid(row=0,
                                        column=0,
                                        padx=175,
                                        pady=15,
                                        sticky="new",
                                        )


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
                                            width=205,
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
                                             width=205,
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
                                                     width=205,
                                                     font=("Segoe UI", 14),
                                                     command=self.add_to_serverlist,
                                                     state="enabled",
                                                     )

        self.add_to_serverlist_button.grid(row=0,
                                        column=0,
                                        padx=25,
                                        pady=215,
                                        sticky="nw",
                                        )

        self.remove_map_button = ctk.CTkButton(self,
                                                     text="Remove last map from Serverlist",
                                                     text_color="#FFFFFF",
                                                     height=30,
                                                     width=205,
                                                     font=("Segoe UI", 14),
                                                     command=self.remove_from_serverlist,
                                                     state="enabled",
                                                     )

        self.remove_map_button.grid(row=0,
                                        column=0,
                                        padx=25,
                                        pady=255,
                                        sticky="nw",
                                        )

        self.export_to_file_button = ctk.CTkButton(self,
                                                     text="Export to ServerList.txt",
                                                     text_color="#FFFFFF",
                                                     height=30,
                                                     width=205,
                                                     font=("Segoe UI", 14),
                                                     command=self.export_to_file,
                                                     state="enabled",
                                                     )

        self.export_to_file_button.grid(row=0,
                                        column=0,
                                        padx=25,
                                        pady=295,
                                        sticky="nw",
                                        )

        self.import_from_file_button = ctk.CTkButton(self,
                                                     text="Import from File",
                                                     text_color="#FFFFFF",
                                                     height=30,
                                                     width=205,
                                                     font=("Segoe UI", 14),
                                                     command=self.load_map_file,
                                                     state="enabled",
                                                     )

        self.import_from_file_button.grid(row=0,
                                        column=0,
                                        padx=25,
                                        pady=335,
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
            with open("ServerList.txt", "w") as f:
                f.write(maplist.get())
                f.close()
                messagebox.showinfo("Success", "ServerList.txt has been exported successfully.")

    def load_map_file(self):
        global maplist
        global ui_maplist
        if not isinstance(ui_maplist, ctk.StringVar):
            ui_maplist = ctk.StringVar(value="")
        ui_maplist.set("")

        with open("ServerList.txt", "r") as f:
            maplist = f.read()
            f.close()
            messagebox.showinfo("Success", "ServerList.txt has been imported successfully.")
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
