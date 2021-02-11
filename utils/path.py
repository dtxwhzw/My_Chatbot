import os


def get_root_path():
    root_path, _ = os.path.split(__file__)
    root_path = os.path.dirname(root_path)
    return root_path

def get_config_path():
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../conf"))
    return config_path

def get_data_path():
    return os.path.join(
        get_root_path(), 'data'
    )


if __name__ == '__main__':
    print(get_data_path())