import os
import json

path_file = '..\\aula_udemy\\task_list_using_json\\tasks_json.json'


def create_obj(tasks_list, trash_list):
    return {'task_list': tasks_list, 'trash_list': trash_list}


def write_json(obj):
    with open(path_file, 'w', encoding='utf8') as file:
        json.dump(obj, file)


def read_json():
    with open(path_file, 'r', encoding='utf8') as file:
        tasks = json.load(file)
    return tasks


def list_tasks(tasks_list):
    print("\nTASKS:")
    print(*tasks_list, sep='\n')
    print()


def task_not_in_list(task, list):
    if task not in list:
        return True
    return False


def list_len_nonzero(list):
    if len(list) != 0:
        return True
    return False


def undo_task(tasks_list, trash_list):
    if list_len_nonzero(tasks_list):
        trash_list.append(tasks_list[-1])
        tasks_list.pop()
    else:
        print("No tasks to undo")


def redo_task(trash_list, tasks_list):
    if list_len_nonzero(trash_list) and \
            task_not_in_list(trash_list[-1], tasks_list):
        tasks_list.append(trash_list[-1])
        trash_list.pop()
    else:
        print("No tasks to redo")


def get_task_delete_position(task, tasks_list):
    task_position = tasks_list.index(task)
    return task_position


def perm_delete(tasks_list):
    task = input('Task name: ')
    if not task_not_in_list(task, tasks_list):
        t_pos = get_task_delete_position(task, tasks_list)
        tasks_list.pop(t_pos)
    else:
        print("Value not in list")


def test_user_input(user_input, tasks_list, trash_list, tasks):
    if user_input == 'list':
        list_tasks(tasks_list)
        # read_json
    elif user_input == 'undo':
        undo_task(tasks_list, trash_list)
    elif user_input == 'redo':
        redo_task(trash_list, tasks_list)
    elif user_input == 'clear':
        os.system('cls')
    elif user_input == 'delete':
        perm_delete(tasks_list)
    elif task_not_in_list(user_input, tasks_list):
        tasks_list.append(user_input)
    else:
        print("Value already in list")
    write_json(create_obj(tasks_list, trash_list))
