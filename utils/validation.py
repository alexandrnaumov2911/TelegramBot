def validation_integer(value: str):

    if '-' in value and '.' in value:
        value1 = value[1:].split('.')
        if value1[0].isdigit() and value[1].isdigit():
            return True
        else:
            return False

    elif '-' in value:
        if value[1:].isdigit():
            return True
        else:
            return False


    elif '.' in value:
        value1 = value.split('.')
        if value1[0].isdigit() and value1[1].isdigit():
            return True
        else:
            return False


    else:
        if value.isdigit():
            return True
        else:
            return False

def validation_operation(operation: str):
    if operation in ['+', '-', '/', '*']:
        return True
    return False