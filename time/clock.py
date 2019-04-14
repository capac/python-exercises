import datetime
print("Enter a number between 0 and 2359 to represent the time: ", end="")

tm = input()

date = str(datetime.time(hour=int(tm[:-2]), minute=int(tm[-2:])))

t = ':'.join(date.split(' ')[-1].split(':')[:2])
hr = int(date.split(' ')[-1].split(':')[:2][0])
print(hr)

if hr >= 0 and hr < 4:
    print("You should be sleeping")

elif hr >= 4 and hr < 12:
    print("Good Morning!")

elif hr >= 12 and hr < 17:
    print("Good afternoon")

elif hr >= 17 and hr < 22:
    print("Good Evening!")

elif hr >= 22 and hr < 24:
    print("Good Night!")
else:
    print("?")
