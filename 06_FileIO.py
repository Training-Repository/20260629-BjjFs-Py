import sys

def demo_sys():
    print("Hi")

    print(sys.argv)
    print(sys.path)
    print(sys.version)

# demo_sys()

import os

def demo_os():
    current_dir = os.getcwd()
    print(f"{current_dir = }")

    new_dir = os.path.join(current_dir, "demo_dir")
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
        print(f"\nDirectory 'demo_dir' created at [{new_dir}].")
    else:
        print(f"\nDirectory 'demo_dir' already exists at [{new_dir}].")

    print("\nFiles and directories in the current directory:")
    for item in os.listdir():
        print(f"\t{item}")

    new_file_path = os.path.join(new_dir, "demo_file.txt")

    second_file_path = os.path.join(new_dir, "demo_file_2.txt")

    ## Version 1
    # file = open(new_file_path, mode="w")
    # file.write("This is a demo file")
    # file.close()

    ## Version 2
    # try:
    #     file = open(new_file_path, mode="w")
    #     file.write("This is a demo file")
    # finally:
    #     file.close()
    
    ## Version 3
    with open(new_file_path, mode="w") as file:
        file.write("This is a demo file\n")
        file.write("Second line\n")
        file.writelines(["Third line\n", "Fourth line\n", "Fifth Line\n"])
        
    ## Reading the file
    with open(new_file_path) as file:
        data = file.readlines()
        print(f"Read the data -> {data}")
        filtered = [line    for line in data      if 'f' in line.lower() ]
        filtered_2 = list(filter((lambda x: 'f' in x.lower()), data))
        print(f"{filtered = }")
        print(f"{filtered_2 = }")
        with open(second_file_path, "w") as outFile:
            outFile.writelines(filtered)

        
    print("="*40)
    with open(second_file_path) as file:
        data  = file.read()
        print(data)
    print("="*40)

    with open(new_file_path) as file:
        data = file.read()
        print(data)

    ## Cleanup
    if os.path.exists(new_file_path):
        os.remove(new_file_path)

    if os.path.exists(second_file_path):
        os.remove(second_file_path)

    if os.path.exists(new_dir):
        os.rmdir(new_dir)

    print("Cleanup completed!!")
demo_os()