def get_todos(filepath = "todos.txt"):
    with open(filepath ,'r') as file_local:
            local_todos = file_local.readlines()
    return local_todos

# for update only
def write_todos(todos_local,filepath = "todos.txt"):
    with open(filepath,'w') as file:
        file.writelines(todos_local)


# python practise/experiments/test/