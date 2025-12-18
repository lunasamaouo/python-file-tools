import os

folder_path = "text_folder"  # 替换为你的文件夹路径

files = os.listdir(folder_path)

print("当前文件夹中的文件有：")
for file in files:
    print(file)
