def get_todos(filepath="todos.txt"):
    """Takes filepath and fetches data from file, then returns it as a list"""
    with open(filepath, 'r') as todo_file:
        items = todo_file.readlines()
    return items


def save_todos(items, filepath="todos.txt"):
    """Takes items as argument and saves them to file at provided filepath"""
    with open(filepath, 'w') as file:
        file.writelines(items)


def display_todos():
    """Displays list of todos with ordernumber and capitalized items"""
    items = get_todos()
    # List comprehension
    # items = [item.strip('\n') for item in items]

    for index, item in enumerate(items):
        item = item.strip('\n')
        print(f'{index + 1}. {item.capitalize()}')


def remove_item(item):
    """Removes provided item from todos file"""
    items = get_todos()
    index = items.index(item)
    items.pop(index)
    save_todos(items)
    return get_todos()
