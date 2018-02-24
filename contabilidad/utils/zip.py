from django.conf import settings
import os
import zipfile
log = settings.LOG


def unzip(zip_path, working_path):
    zip_ref = zipfile.ZipFile(zip_path, 'r')
    zip_ref.extractall(working_path)
    zip_ref.close()


def get_files(path):
    if os.path.exists(path):
        return os.listdir(path)
    return []


def get_folder_name(path):
    exclude = ['__MACOSX']
    file_name = ""
    log.debug("searching in %s", path)
    if os.path.exists(path):
        folders = [name for name in os.listdir(path) if name not in exclude]
        # print("FOLDERS: {}".format(folders))
        file_name = folders[0] if len(folders) > 0 else ""
        log.debug("file name %s", file_name)
        # print("FILE NAME: {}".format(file_name))
    return "{}/{}".format(path, file_name)
