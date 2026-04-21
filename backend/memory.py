service/memory.py(Context Awareness)

memory = {}

def store(user_id, key, value):
    if user_id not in memory:
        memory[user_id] = {}

    memory[user_id][key] = value


def get(user_id):
    return memory.get(user_id, {})
