"""
Нужно дополнить код таким образом, чтобы он вывел все адреса в алфавитном порядке и в формате имя_пользователя@домен.
"""

emails = {'mgu.edu': ['andrei_servo', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
              'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
              'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
              'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
      	      'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
       	      'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}


list1 = [values + '@' + key for key, v in emails.items() for values in v]
print('''
'''.join(sorted(list1)))




