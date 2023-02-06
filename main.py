import os
import time


def file_tree_1(dir_path: str, level: int = 0):
    """
    function for creating file tree.
    dir_path - current directory path,
    level - level of nesting.
    """
    for p in os.listdir(dir_path):
        new_path = os.path.join(dir_path, p)
        # print(f'{str(level * " ")}  {new_path} {str(level)}')
        new_level = level
        if os.path.isdir(new_path):
            # print('folder')
            level += 1
            file_tree_1(new_path, level)
        level = new_level


def file_tree_2(dir_path: str):
    """
    function for creating file tree.
    dir_path - current directory path.
    """
    for p, v, s in os.walk(dir_path):
        print(f'{p} {v} {s}')


def show_time(func_names: list, dir_path: str):
    """
    Show the current working time of each function
    in the list.
    f_name - list of functions names
    dir_path - current directory path
    """
    for func in func_names:
        start = time.time()
        func(dir_path)
        end = time.time()
        print(f'Time {end - start}')


if __name__ == '__main__':
    func_list = [file_tree_1, file_tree_2]
    dir_name = '.'
    show_time(func_list, dir_name)
    
    print("Hello world") 
    print("Hello world")         