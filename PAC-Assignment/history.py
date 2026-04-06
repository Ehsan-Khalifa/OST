history = []

def record(operation, result):
    history.append({"operation": operation, "result": result})

def show_history():
    for i, entry in enumerate(history, 1):
        print(f"{i}. {entry['operation']} = {entry['result']}")
