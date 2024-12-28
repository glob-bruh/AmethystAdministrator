from main_window import MainWindow

if __name__ == "__main__":
    window_instance = MainWindow()
    window_instance.initGui(window_instance.window_main, 20)
    window_instance.window_main.mainloop()
