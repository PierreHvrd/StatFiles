# this is the main file, the one you have to execute to launch the project

from tkinter import filedialog
import os
from Folder import Folder

# ask the user the path of the directory he wants to have stats on
# path = filedialog.askdirectory(initialdir="../", title="Open a folder")

# TODO: vérifier la compatibilité avec d'autres OS
# TODO: comprendre la différence entre 'Taille' et 'Sur Disque'

path = "C:/Users/pierr/OneDrive/Documents/ZetaTest"


def analyse_files_of_folder(path_folder_to_analyse):
    current_folder = Folder(path_folder_to_analyse)

    # locally
    for file in os.listdir(path_folder_to_analyse):
        path_of_potential_file = path_folder_to_analyse + "/" + file
        if os.path.isfile(path_of_potential_file):
            extension = os.path.splitext(file)[1]
            extension_present = False
            size_of_current_file = os.path.getsize(path_of_potential_file)
            for key in current_folder.files_by_type.keys():
                if key == extension:
                    current_folder.files_by_type[extension] = (current_folder.files_by_type[extension][0] + 1,
                                                               current_folder.files_by_type[extension][0] +
                                                               size_of_current_file)

                    extension_present = True
                    break

            if not extension_present:
                current_folder.files_by_type[extension] = (1, size_of_current_file)

            # update the current_folder stats
            current_folder.size += size_of_current_file
            current_folder.nb_files += 1
            current_folder.size_go += size_of_current_file
            current_folder.nb_files_go += 1

    # globally
    list_folders = os.listdir(path_folder_to_analyse)
    for folder in list_folders:
        potential_folder_path = path_folder_to_analyse + "/" + folder

        if os.path.isdir(potential_folder_path):
            sub_folder = analyse_files_of_folder(potential_folder_path)
            current_folder.sub_folders.append(sub_folder)
            current_folder.nb_folders_go += 1

    return current_folder


if path != "":  # otherwise the user did not select a folder
    main_folder = analyse_files_of_folder(path)
    main_folder.count_sub_directories()

    print("\nResults of the analysis: \n\n")
    print("Global results:\n")
    print(f"Path: {main_folder.path}")
    print(f"Size (globally): {main_folder.size_go}")
    print(f"Number of files (globally): {main_folder.nb_files_go}")
    print(f"Number of folders (globally): {main_folder.nb_folders_go}")

    print("\nLocal results: \n")
    my_list = [local_folder.path for local_folder in main_folder.sub_folders]
    print(f"Sub-folders (locally): {my_list}")
    print(f"Number of folders: {len(main_folder.sub_folders)}")
    print(f"Number of files in this folder (locally): {main_folder.nb_files}")

    print("\n\n")
    for key in main_folder.files_by_type.keys():
        if key == "":
            print(f"Size of the files with no extension: {main_folder.files_by_type[key]}")

        else:
            print(f"Size of {key} files: {main_folder.files_by_type[key]}")
