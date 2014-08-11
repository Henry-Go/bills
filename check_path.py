import json
import os.path

"""
This module will look for `~/.pwds/passwords.pwd` and Check
if exists, if not it will create it, otherwise just print
a `file exists` comment.
"""

# TODO
# - Check if folder is writable
# - Check if file is writable
# - Append an example

pwd_path = '~/.pwds/'
pwd_filename = 'passwords.pwd'
pwd_fullpath = pwd_path + pwd_filename

# check if file already exist
file_exist = os.path.isfile(pwd_fullpath)
# check if dir already exist
dir_exist = os.path.exists(pwd_path)
print (dir_exist)
print (file_exist)
bill_example = { 
    'date': 'today',
    'desc': 'lorem ipsum',
    'amount': 150
}

if not dir_exist:
    print('creating dir...')
    os.makedirs(pwd_path)
    if not file_exist:
        branding_str = "Document used to store passwords for the pwd tool"
        file = open(pwd_fullpath, 'w')
        file.write(branding_str)
        file.write({'bills': bill_example})
    else:
        print('File already exist')
else:
    file = open(pwd_fullpath, 'r')
    for line in file:
        print(line)

# Insert new bill 
file = open(pwd_fullpath, 'r+')
file.write('electric_bill: {"one": 123, "two": 234234}')
for linei in file:
    print(line)
