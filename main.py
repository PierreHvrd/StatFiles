# this is the main file, the one you have to execute to launch the project

from tkinter import filedialog
import os
import matplotlib.pyplot as plt
from Folder import Folder
from show_in_proper_unit import show_in_proper_unit
import copy

# ask the user the path of the directory he wants to have stats on

path = filedialog.askdirectory(initialdir="../", title="Open a folder")

# TODO: vérifier la compatibilité avec d'autres OS

# path = "C:/Users/pierr/OneDrive/Documents/ZetaTest"


def analyse_files_of_folder(path_folder_to_analyse):
    current_folder = Folder(path_folder_to_analyse)

    # globally
    list_folders = os.listdir(path_folder_to_analyse)
    for folder in list_folders:
        potential_folder_path = path_folder_to_analyse + "/" + folder

        if os.path.isdir(potential_folder_path):
            sub_folder = analyse_files_of_folder(potential_folder_path)
            current_folder.sub_folders.append(sub_folder)
            current_folder.nb_folders_go += 1

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
                                                               current_folder.files_by_type[extension][1] +
                                                               size_of_current_file)

                    extension_present = True
                    break

            if not extension_present:
                current_folder.files_by_type[extension] = (1, size_of_current_file)

            # update the current_folder stats
            current_folder.size += size_of_current_file
            current_folder.nb_files += 1

    # set the global stats to the local stats (before counting the sub folder)
    current_folder.size_go = current_folder.size
    current_folder.nb_folders_go = len(current_folder.sub_folders)
    current_folder.nb_files_go = current_folder.nb_files
    current_folder.files_by_type_go = copy.deepcopy(current_folder.files_by_type)

    # update the global stats
    for sub_folder in current_folder.sub_folders:
        current_folder.size_go += sub_folder.size_go
        current_folder.nb_files_go += sub_folder.nb_files_go
        current_folder.nb_folders_go += sub_folder.nb_folders_go
        current_folder.merge_dicts(sub_folder.files_by_type_go)

    return current_folder


if path != "":  # otherwise the user did not select a folder
    # print the results
    main_folder = analyse_files_of_folder(path)
    proper_unit_size_go, name_unit_size_go = show_in_proper_unit(main_folder.size_go)
    proper_unit_nb_files_go, name_unit_nb_files_go = show_in_proper_unit(main_folder.nb_files_go)


    """
    DO NOT SHOW IN THE PIE CHART, SHOW NEXT TO IT
    
    
    print("\nResults of the analysis: \n\n")
    print("Global results:\n")
    print(f"Path: {main_folder.path}")
    print(f"Size (globally): {proper_unit_size_go} {name_unit_size_go}")
    print(f"Number of files (globally): {main_folder.nb_files_go}")
    print(f"Number of folders (globally): {main_folder.nb_folders_go}")
    
    SAME BUT LOCAL (add switch global/local)
    print("\nLocal results: \n")
    my_list = [local_folder.path for local_folder in main_folder.sub_folders]
    print(f"Sub-folders (locally): {my_list}")
    print(f"Number of folders: {len(main_folder.sub_folders)}")
    print(f"Number of files in this folder (locally): {main_folder.nb_files}")
    
    
    """
    data_files_local = []
    data_files_local_label = []
    for key in main_folder.files_by_type.keys():
        if key == "":
            data_files_local.append(main_folder.files_by_type[key])
            data_files_local_label.append("No extension")

        else:
            data_files_local.append(main_folder.files_by_type[key])
            data_files_local_label.append(key)

    stats_files = main_folder.generate_files_stats()
    data_files_by_type = []
    data_files_by_type_label = []
    other_percentage = 0

    for key in stats_files.keys():
        if stats_files[key] > 2:
            if key == "":
                data_files_by_type.append(stats_files[key])
                data_files_by_type_label.append("No extension")

            else:
                data_files_by_type.append(stats_files[key])
                data_files_by_type_label.append(key)

        else:
            other_percentage += stats_files[key]

    data_files_by_type_label.append("Others")
    data_files_by_type.append(other_percentage)

    # explode the biggest value
    max_value = max(data_files_by_type)
    max_index = data_files_by_type.index(max_value)
    explode_value = tuple([0 if i != max_index else 0.1 for i in range(len(data_files_by_type))])

    plt.pie(data_files_by_type, labels=data_files_by_type_label, startangle=90, shadow=True, autopct='%.2f%%',
            explode=explode_value)
    plt.title = f"Stats for folder : {os.path.basename(os.path.normpath(path))}"
    plt.axis("equal")

    plt.show()
