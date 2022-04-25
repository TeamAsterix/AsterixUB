import os


def __list_all_plugins():
    """load plugins"""
    import glob
    from os.path import basename, dirname, isfile

    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_plugins = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    return all_plugins


PLUGINS = sorted(__list_all_plugins())
__all__ = PLUGINS + ["PLUGINS"]
