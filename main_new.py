"""
-------------------------------------------------
AMETHYST ADMINISTRATOR
https://github.com/glob-bruh/AmthystAdministrator
All content licensed under BSD-3
-------------------------------------------------
main - MAIN PYTHON FILE:
-------------------------------------------------
This file is the first thing executed. 
-------------------------------------------------
"""

from main_window import MainWindow

if __name__ == "__main__":
    window_instance = MainWindow()
    window_instance.initGui(window_instance.window_main, 20)
    window_instance.window_main.mainloop()
