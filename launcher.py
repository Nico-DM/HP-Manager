import threading
import time
import sys


def start_flask():
    from Back.app import create_app
    app = create_app()
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)


def start_gui():
    import Front.main


if __name__ == "__main__":
    if getattr(sys, 'frozen', False):
        import multiprocessing
        multiprocessing.freeze_support()

    flask_thread = threading.Thread(target=start_flask, daemon=True)
    flask_thread.start()

    time.sleep(1.5)

    start_gui()
