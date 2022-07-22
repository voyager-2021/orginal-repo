# importing modules
import os

#making warning (Y/n)
put = input("Are you sure want restart pc (Y/n): ")

if put == 'y':
    os.system('shutdown /r /t 0')
elif put == 'Y':
    os.system('shutdown /r /t 0')
elif put == 'n':
    exit()
elif put == 'N':
    exit()
else:
    exit()
