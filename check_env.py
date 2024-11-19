import sys
import os

def check_environment() -> None:
    """
    Check whether running in virtual environment or conda environment.

    Returns:
        None
    """
    try:
        if 'CONDA_PREFIX' in os.environ:
            print("You are in a conda environment.")
        elif hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
            print("You are in a virtual environment (venv).")
        else:
            print("You are not in any virtual environment.")
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    check_environment()
