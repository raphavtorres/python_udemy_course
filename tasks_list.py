import os

tasks_list = []
trash_list = []


def list_tasks():
    print("\nTASKS:")
    print(*tasks_list, sep='\n')
    print()


def undo_task():
    if len(tasks_list) != 0:
        trash_list.append(tasks_list[-1])
        tasks_list.pop(-1)
    else:
        print("No tasks to undo")


def redo_task():
    if len(trash_list) != 0 and trash_list[-1] not in tasks_list:
        tasks_list.append(trash_list[-1])
        trash_list.pop(-1)
    else:
        print("No tasks to redo")


def perm_delete():
    ...


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
        print('deleting')
    else:
        tasks_list.append(user_input)


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
