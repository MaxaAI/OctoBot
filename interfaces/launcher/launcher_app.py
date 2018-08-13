import os
from tkinter.ttk import Progressbar, Label

from config.cst import PROJECT_NAME
from interfaces.app_util import TkApp
from interfaces.launcher import LAUNCHER_VERSION, launcher_controller


class LauncherApp(TkApp):
    PROGRESS_MIN = 0
    PROGRESS_MAX = 100

    def __init__(self):
        self.window_title = f"{PROJECT_NAME} - Launcher"
        self.progress = None
        self.progress_label = None

        super().__init__()

    def create_components(self):
        # buttons
        self.progress = Progressbar(self.window, orient="horizontal",
                                    length=200, mode="determinate")
        self.progress.pack()
        self.progress_label = Label(self.window, text=f"{self.PROGRESS_MIN}%")
        self.progress_label.pack()
        self.progress["value"] = self.PROGRESS_MIN
        self.progress["maximum"] = self.PROGRESS_MAX

    def inc_progress(self, inc_size, to_max=False):
        if to_max:
            self.progress["value"] = self.PROGRESS_MAX
            self.progress_label["text"] = f"{self.PROGRESS_MAX}%"
        else:
            self.progress["value"] += inc_size
            self.progress_label["text"] = f"{round(self.progress['value'], 2)}%"

    @staticmethod
    def close_callback():
        os._exit(0)

    def start_app(self):
        self.window.mainloop()

    def stop(self):
        self.window.quit()


def start_launcher(args):
    if args.version:
        print(LAUNCHER_VERSION)
    else:
        if args.update:
            pass
        elif args.update_launcher:
            pass
        else:
            installer_app = LauncherApp()
            installer = launcher_controller.Launcher(installer_app)
