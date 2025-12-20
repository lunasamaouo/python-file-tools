import os
import shutil

source_folder = "test_folder"
 
txt_folder = os.path.join(source_folder, "txt") # 创建txt文件夹路径
jpg_folder = os.path.join(source_folder, "jpg") # 创建jpg文件夹路径
other_folder = os.path.join(source_folder, "other") # 创建other文件夹路径

os.makedirs(txt_folder, exist_ok=True)# 创建txt文件夹
os.makedirs(jpg_folder, exist_ok=True)
os.makedirs(other_folder, exist_ok=True)


folder_path = "test_folder"

files = os.listdir(folder_path)

print("当前文件夹中的文件有：")

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if not os.path.isfile(file_path):
        continue

    file_name, file_ext = os.path.splitext(file)

    if file_ext == ".txt":
        target_folder = txt_folder
    elif file_ext == ".jpg":
        target_folder = jpg_folder
    else:
        target_folder = other_folder

    target_path = os.path.join(target_folder, file)
    shutil.move(file_path, target_path)

    print(f"已移动文件：{file} → {target_folder}")
        


