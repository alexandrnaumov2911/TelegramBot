import re
ip = '255.255.255.254'

pattern = re.compile(r'((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$')

reg = re.search(pattern, ip)

if reg:
    print(reg.group(0))
    print('ip адрес верный')
else:
    print('Неккоректный ip адрес')