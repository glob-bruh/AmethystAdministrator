from main_window import MainWindow
from networkPinger import pinger, icmpPingSend
from servicesManager import ServiceManagementWindow, ServiceManagementAddServiceWindow
from editHost import EditHostWindow
from canvasController import hostCanvas
import pyarrow.feather as feather


class SaveManager:
    def __int__(self):
        self.skeleton_for_now = None
