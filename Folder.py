# this file contains the code for the folder class

class Folder:
    def __init__(self, path):
        """
        go means global which mens in this folder and all the sub-folders
        :param path:
        """
        self.path = path
        self.size_go = 0
        self.files_by_type = {}  # Ex: 'extension': (nb_of_files, size_of_files) ONLY in this folder
        self.sub_folders = []  # immediate sub folder not go
        self.nb_folders_go = 0
        self.nb_files_go = 0
        self.nb_files = 0
        self.size = 0

    def count_sub_directories(self):
        for folder in self.sub_folders:
            folder.count_sub_directories()
            self.nb_files_go += folder.nb_files
            self.nb_folders_go += len(folder.sub_folders)
            self.size_go += folder.size
