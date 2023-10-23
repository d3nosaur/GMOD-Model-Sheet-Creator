import os
import csv

# path to the collection of addons
COLLECTION_PATH = ""


# find all *.mdl files in the collection path
def search_folder(path) -> list[str]:
    mdl_files = []

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".mdl"):
                mdl_files.append(file)

    return mdl_files


def save_to_csv(filename, data: dict[str, list[str]]):
    with open(filename, "w") as file:
        writer = csv.writer(file)

        addon_name_list = list(data.keys())

        writer.writerow(addon_name_list)

        for i in range(len(data[addon_name_list[0]])):
            row = []

            for addon_name in addon_name_list:
                # make sure data[addon_name[i]] exists
                if len(data[addon_name]) > i:
                    row.append(data[addon_name][i])
                else:
                    row.append("")

            writer.writerow(row)



def main():
    addon_data = {}

    for folder in os.listdir(COLLECTION_PATH):
        mdl_files = search_folder(os.path.join(COLLECTION_PATH, folder))

        addon_data[folder] = mdl_files

    save_to_csv("model_data.csv", addon_data)

if __name__ == "__main__":
    main()
