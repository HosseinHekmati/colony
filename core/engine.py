import subprocess
from colony.utils.config import load_config
from colony.core.manager import run_colony


def start_debug_panel():
    try:
        subprocess.Popen(
            ["x-terminal-emulator", "-e", "python3 -m colony.debug.debug_panel"]
        )
    except Exception:
        print("[WARNING] Could not launch debug panel.")


def start_colony():
    config = load_config()

    if config.get("debug", False):
        start_debug_panel()

    run_colony()
