from main_window import MainWindow
import pickle
import structlog as sl

logger = sl.get_logger()


def Save(mw: MainWindow) -> MainWindow:
    """
    :param mw: The MainWindow object from the application.
    :return: The same MainWindow object being returned after hosts array saved.
    """
    try:
        with open(".sacred/main_window.pickle", "wb") as pickle_management:
            pickle.dump(mw.host_array, pickle_management, pickle.HIGHEST_PROTOCOL)
    except Exception as e:
        logger.error(f"Error In Save Manager Save: {e}")
        raise e
    return mw


def Load(mw: MainWindow) -> MainWindow:
    try:
        with open(".sacred/main_window.pickle", "rb") as pickle_management:
            mw.host_array = pickle.load(pickle_management)
    except Exception as e:
        logger.error(f"Error In Save Manager Load: {e}")
        raise e
    return mw


def Delete(mw: MainWindow) -> MainWindow:
    try:
        mw.host_array = None
    except Exception as e:
        logger.error(f"Error In Save Manager Delete: {e}")
        raise e
    return mw
