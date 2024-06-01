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
        self.files_by_type_go = {}
        self.sub_folders = []  # immediate sub folder not go
        self.nb_folders_go = 0
        self.nb_files_go = 0
        self.nb_files = 0
        self.size = 0

    def merge_dicts(self, dict_to_merge_from):
        for key in dict_to_merge_from.keys():
            if key in self.files_by_type_go.keys():  # optimization ?

                self.files_by_type_go[key] = (self.files_by_type_go[key][0] + dict_to_merge_from[key][0],
                                              self.files_by_type_go[key][1] + dict_to_merge_from[key][1])

                # quite ugly, need to change

            else:
                self.files_by_type_go[key] = dict_to_merge_from[key]