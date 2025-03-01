from Codebase.Generic_VENV_Manger.generic_venv_manager.venv_util import VENVUtil
from Codebase.Paths.get_project_root import get_project_root
import sys

def setup():
    VENVUtil.setup_venv(get_project_root())

if __name__ == "__main__":
    setup()
