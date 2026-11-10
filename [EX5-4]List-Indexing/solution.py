m = int(input("Mouth:"))

if (m == 1):
    print("*** Month 1 : 31 days")
elif (m == 2):
    print("*** Month 2 : 28 days")
elif (m == 3):
    print("*** Month 3 : 31 days")
elif (m == 4):
    print("*** Month 4 : 30 days")
elif (m == 5):
    print("*** Month 5 : 31 days")
elif (m == 6):
    print("*** Month 6 : 30 days")
elif (m == 7):
    print("*** Month 7 : 31 days")
elif (m == 8):
    print("*** Month 8 : 31 days")
elif (m == 9):
    print("*** Month 9 : 30 days")
elif (m == 10):
    print("*** Month 10 : 31 days")
elif (m == 11):
    print("*** Month 11 : 30 days")
else:
    print("*** Month 12 : 31 days")

print("==================================")

if (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
  print("+++ Mouth %d : 31 days"% m)
elif (m==4 or m==6 or m==9 or m==11):
  print("+++ Mouth %d : 30 days"% m)
else:
  print("+++ Mouth 2 : 28 days")

print("==================================")

if (m==2):
  print("### Mouth 2 : 28 days")
elif (m==4 or m==6 or m==9 or m==11):
  print("### Mouth %d : 30 days"% m)
else:
  print("### Mouth %d : 31 days"% m)

print("==================================")

D = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
M = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
print("=== Mouth %s : %d days"% (M[m-1], D[m-1]))