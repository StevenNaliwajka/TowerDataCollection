from Codebase.Generic_VENV_Manger.venv_util import VENVUtil
from Codebase.Pathing.get_project_root import get_project_root


def run():
    VENVUtil.run_with_venv(get_project_root(), get_project_root)

if __name__ == '__main__':
    run()