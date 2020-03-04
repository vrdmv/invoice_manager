import os

def create_workdir():
    """Create a current working directory.
    (works across all operating systems)"""

    work_dir = os.path.join("C:\\", "Invoice Manager",
                            "Work environment")
    if not os.path.exists(work_dir):
        os.makedirs(work_dir)
    work_dir_str = str(work_dir)
    return work_dir_str


def create_archive():
    """Create a current working directory.
    (works across all operating systems)"""

    archive_dir = os.path.join("C:\\", "Invoice Manager",
                               "Archive")
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    archive_dir_str = str(archive_dir)
    return archive_dir_str