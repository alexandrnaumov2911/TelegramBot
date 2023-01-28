"""
Нужно дополнить код таким образом, чтобы он вывел все адреса в алфавитном порядке и в формате имя_пользователя@домен.
"""

from utils import ReName
emails = {'mgu.edu': ['andrei_servo', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
              'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
              'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
              'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
      	      'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
      	      'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
print(sorted(ReName(emails)))
