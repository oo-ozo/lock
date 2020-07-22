import style
from os import system

#system("pkg install figlet")
print(style.color('green'))
style.big("made by")
print(style.color('red'))
style.big("Tricker")
print(style.square("locker", "blue"))
print(style.color('white'))

print(style.line())
system("bash lock.sh")

print(style.color('green'))
print("Please Exit Termux and enter again :)")
print(style.color('white'))


