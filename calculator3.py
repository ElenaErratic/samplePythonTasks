def calculator()
  M = 0
  while True:
    print("Enter an equation")
    calc = input()
    calc = calc.split()
    x = calc[0]
    y = calc[2]
    oper = calc[1]
    if x == 'M':
      x = M
    elif y == 'M':
      y = M

    try:
      x = float(x)
      y = float(y)
    except ValueError:
      print("Do you even know what numbers are? Stay focused!")

    else:

      if oper not in ('+', '-', '*', '/'):
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
      elif oper == "/" and y == 0:
        print("Yeah... division by zero. Smart move...")
      else:
        if oper == "+":
          result = x + y
          print(result)
        elif oper == "-":
          result = x - y
          print(result)
        elif oper == "*":
          result = x * y
          print(result)
        elif oper == "/" and y != 0:
          result = x / y
          print(result)

        while True:
          print("Do you want to store the result? (y / n):")
          answer = input()
          if answer == 'y':
            M = result
            break
          elif answer == 'n':
            break

        while True:
          print("Do you want to continue calculations? (y / n):")
          answer = input()
          if answer == 'y':
            break
          elif answer == 'n':
            break

      if answer == 'n':
        break    

