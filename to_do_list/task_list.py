import os

tasks_list = []
trash_list = []


def list_tasks():
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


def undo_task():
    """ if len(tasks_list) != 0: """
    if list_len_nonzero(tasks_list):
        trash_list.append(tasks_list[-1])
        tasks_list.pop()
    else:
        print("No tasks to undo")


def redo_task():
    if list_len_nonzero(trash_list) and \
            task_not_in_list(trash_list[-1], tasks_list):
        tasks_list.append(trash_list[-1])
        trash_list.pop()
    else:
        print("No tasks to redo")


def get_task_delete_position(task):
    task_position = tasks_list.index(task)
    return task_position


def perm_delete():
    task = input('Task name: ')
    if not task_not_in_list(task, tasks_list):
        t_pos = get_task_delete_position(task)
        tasks_list.pop(t_pos)
    else:
        print("Value not in list")


def test_user_input(user_input):
    if user_input == 'list':
        list_tasks()
    elif user_input == 'undo':
        undo_task()
    elif user_input == 'redo':
        redo_task()
    elif user_input == 'clear':
        os.system('cls')
    elif user_input == 'delete':
        perm_delete()
    elif task_not_in_list(user_input, tasks_list):
        tasks_list.append(user_input)
    else:
        print("Value already in list")


def main():
    while True:
        print(f'{tasks_list=}\n{trash_list=}')
        print("Commands: list, undo, redo, clear, delete, exit")
        try:
            user_input = input("Type a task or command >> ").lower().strip()
        except ValueError:
            print('invalid input...')
            continue
        if user_input == 'exit':
            break
        test_user_input(user_input)


if __name__ == '__main__':
    main()
