# User input module

def yes_or_no(question):
    reply = str(input(question + ' (y/N): ')).lower().strip()
    if reply[0] == 'y':
        return True
    return False
