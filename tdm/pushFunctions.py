import os


# function to read file overviews

def overviewList(fileDirectory):
    overviews = []

    for file_name in os.listdir(fileDirectory):
        file_path = os.path.join(fileDirectory, file_name)
        if os.path.isfile(file_path):
            try:
                with open(file_path, "r", encoding='utf-8') as file:
                    content = file.read(100)
                    overviews.append(content)
            except UnicodeDecodeError:
                continue

    return overviews


# function to read files
def contentsList(fileDirectory_):
    character_list = []

    for file_name in os.listdir(fileDirectory_):
        file_path = os.path.join(fileDirectory_, file_name)
        if os.path.isfile(file_path):
            try:
                with open(file_path, "r", encoding='utf-8') as file:
                    content = file.read()
                    character_list.append(content)
            except UnicodeDecodeError:
                continue

    return character_list
