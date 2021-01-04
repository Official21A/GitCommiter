import os
import datetime


local_path = "/Cache/record.data"


def cache_init():
    if not os.path.exists(local_path):
        with open(local_path, "w") as file:
            file.writelines([f'$Cache Created : {datetime.datetime.now()}'])


def cache_up(string):
    with open(local_path, "r") as file:
        lines = file.readlines()
    with open(local_path, "w") as file:
        new_lines = [line for line in lines if line != "&"+string]
        file.writelines(new_lines)
        file.write(f'\n&{string}')


def cache_in():
    with open(local_path, "r") as file:
        lines = file.readlines()
        new_lines = [line for line in lines if line.startswith("&")]
    return new_lines


def cache_clear():
    with open(local_path, "w") as file:
        file.writelines([f'$Cache Created : {datetime.datetime.now()}'])