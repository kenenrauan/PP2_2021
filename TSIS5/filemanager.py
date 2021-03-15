import os
cwd = os.getcwd()
uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])

def choose_dir_process():
    global cwd
    print("Your current directory path: ", cwd)
    print("Select the process:")
    print("1. Rename the directory")
    print("2. Show me number of files")
    print("3. Show me number of directories")
    print("4. Show me content of directory")
    print("5. Add file to the directory")
    print("6. Add new directory to the directory")
    print("7. Open dir")
    print("8. Open file")
    process = int(input('Input: '))
    dir_process(process)

def dir_process(process):
    global cwd
    if process == 1:
        current_name = os.path.basename()
        new_name = input("Write new name: ")
        os.chdir(os.path.dirname(cwd))
        os.rename(current_name, new_name)
    elif process == 2:
        print (len([i for i in os.listdir(cwd) if os.path.isfile(i)]))
    elif process == 3:
        print (len([i for i in os.listdir(cwd) if os.path.isdir(i)]))
    elif process == 4:
        print(os.listdir(cwd))
    elif process == 5:
        file_name = input("Write file name: ")
        with open(file_name, 'w+') as f:
            print('File', file_name, 'Created')
    elif process == 6:
        dir_name = input("Write new directory: ")
        os.mkdir(cwd+dir_name+'/')
        print("Directory", dir_name, " Created")
    elif process == 7:
        print("Choose the dir: ")
        print([i for i in os.listdir(cwd) if os.path.isdir(i)])
        new_dir = input("Name of directory: ")
        cwd += '/' + new_dir
        print(cwd)
    elif process == 8:
        print("Choose the file: ")
        print([i for i in os.listdir(cwd) if os.path.isfile(i)])
        new_file = input("Name of file: ")
        cwd += '/' + new_file
        choose_file_process()
    choose_dir_process()

def choose_file_process():
    global cwd
    print("Your current File path: ", cwd)
    print("1. Delete file")
    print("2. Rename file")
    print("3. Add content to the file")
    print("4. Rewrite content to the file")
    print("5. Return to the parent directory")
    process = int(input('Input: '))
    file_process(process)

def file_process(process):
    global cwd
    file_name = os.path.basename(cwd)
    if process == 1:
        os.remove(file_name)
    elif process == 2:
        new_name = input("Write new name of file: ")
        os.rename(file_name, new_name)
    elif process == 3:
        with open(cwd, "r") as f:
            content = f.read()
        new_content = input("Add new content: ")
        with open(cwd, "w") as f:
            f.write(content+new_content)
    elif process == 4:
        new_content = input("Rewrite the content: ")
        with open(cwd, "w") as f:
            f.write(new_content)
    elif process == 5:
        uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])
        cwd = uppath(cwd, 1)
        choose_dir_process()
    choose_file_process()
        
while True:
    choose_dir_process()