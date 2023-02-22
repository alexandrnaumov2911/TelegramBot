import re


def validation_2(value: str):
    r = re.compile(r'-?\d+(\.(\d+))?')
    if re.match(r, value):
        try:
            if '.' in value:
                float(value)
            else:
                int(value)
            return True
        except Exception as e:
            print(f'Упало {e}')
    return False
