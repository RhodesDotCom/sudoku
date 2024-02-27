import re

#prefix - letters, numbers, underscores, dots and dashes
#domain - letters, numbers, dashes and at least 1 dot
regex = '^[\w.-]+[@][a-zA-Z0-9.]+[.][a-zA-Z]{2,}$'

email = 'nat_h---a-n.n.rhodes@.f.dfADSd.coM'

print(re.search(regex, email))
if re.search(regex, email):
    print('valid')
else:
    print('invalid')