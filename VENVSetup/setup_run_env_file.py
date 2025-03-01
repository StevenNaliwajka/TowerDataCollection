import os

from ..VENVCodeBase.VENVPathing.get_venv_root import get_venv_root
from ..VENVCodeBase.VENVSupport.copy_file_and_rename import copy_file_and_rename
from ..VENVCodeBase.VENVPathing.get_venv_example_folder import get_venv_example_folder


def setup_run_env_file(old_path, new_path):
    # Perform the copy operation
    copy_file_and_rename(old_path, new_path)


if __name__ == "__main__":
    example_folder = get_venv_example_folder()
    old_path = os.path.join(example_folder, "run_env_var.example.json")
    root_folder = get_venv_root()
    new_path = os.path.join(root_folder, "run_env_var.json")
    setup_run_env_file(old_path, new_path)