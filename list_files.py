import os

folder_path = "test_folder"

files = os.listdir(folder_path)

print("当前文件夹中的文件有：")

for file in files:
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        file_name, file_ext = os.path.splitext(file)
        print(f"文件名：{file_name}，文件类型：{file_ext}")


