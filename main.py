# this is the main file, the one you have to execute to launch the project

from tkinter import filedialog
import os

# ask the user the path of the directory he wants to have stats on
path = filedialog.askdirectory(initialdir="../", title="Open a folder")

# TODO: vérifier la compatibilité avec d'autres OS


def analyse_files_of_folder(path_folder_to_analyse):
    nb_files_by_type = {}
    size_files_by_type = {}  # in bytes
    size_folders = {}

    # create the folder keys (only immediate folder)
    list_folders = os.listdir(path_folder_to_analyse)
    for folder in list_folders:
        if os.path.isdir(path_folder_to_analyse + "/" + folder):
            size_folders[folder] = 0

    for file in os.listdir(path_folder_to_analyse):
        extension = os.path.splitext(file)[1]
        extension_present = False
        for key in nb_files_by_type.keys():
            if key == extension:
                nb_files_by_type[extension] += 1
                size_files_by_type[extension] += os.path.getsize(path_folder_to_analyse + "/" + file)
                extension_present = True
                break

        if not extension_present:
            nb_files_by_type[extension] = 1
            size_files_by_type[extension] = os.path.getsize(path_folder_to_analyse + "/" + file)

    return nb_files_by_type, size_files_by_type, size_folders


if path != "":  # otherwise the user did not select a folder
    nb_files_by_type, size_files_by_type, size_folders = analyse_files_of_folder(path)
    print("Result of the analysis: \n\n")
    for key in nb_files_by_type.keys():
        if key == "":
            print(f"Number of files with no extension: {nb_files_by_type[key]}")

        else:
            print(f"Number of {key} files: {nb_files_by_type[key]}")

    print("\n\n")
    for key in size_files_by_type.keys():
        if key == "":
            print(f"Size of the files with no extension: {nb_files_by_type[key]}")

        else:
            print(f"Size of {key} files: {size_files_by_type[key]}")

    print("\n\n")
    for folder in size_folders.keys():
        print(f"Size of {folder} folder: {size_folders[folder]}")
