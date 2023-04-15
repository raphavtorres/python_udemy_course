from functions import test_user_input, write_json, create_obj, read_json


def main():
    tasks = read_json()
    if tasks == {}:
        tasks = create_obj([], [])
    write_json(tasks)

    tasks_list = tasks.get('task_list')
    trash_list = tasks.get('trash_list')

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
        test_user_input(user_input, tasks_list, trash_list, tasks)


if __name__ == '__main__':
    main()
