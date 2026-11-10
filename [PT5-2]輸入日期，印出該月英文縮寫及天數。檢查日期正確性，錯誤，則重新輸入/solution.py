while True:
  m = int(input("Month:"))
  d = int(input("Day:"))

  D = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  M = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']


  if (m >= 13) or (m <= 0):
    print("*** Wrong Date!")
    print("-----------------")
    continue
  elif (d <= 0) or (d > D[m-1]):
    print("*** Wrong Date!")
    print("-----------------")
    continue
  else:
    print("=====================")
    print(f"*** Month {M[m-1]}:{D[m-1]} days")
    break