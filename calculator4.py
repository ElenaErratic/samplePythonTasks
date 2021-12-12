def calculate():
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
    if y == 'M':
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
        check(x, y, oper)
        print("Yeah... division by zero. Smart move...")

      else:
        check(x, y, oper)
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
          answer_1 = input()
          if answer_1 == 'y':
            M = result
            break
          elif answer_1 == 'n':
            break
  
        while True:
          print("Do you want to continue calculations? (y / n):")
          answer_2 = input()
          if answer_2 == 'y':
            break
          elif answer_2 == 'n':
            break
  
        if answer_2 == 'n':
          break    

        if oper == "/" and y == 0:
          print("Yeah... division by zero. Smart move...")
          

def check(x, y, oper):
  msg = ""
  msg_6 = " ... lazy"
  msg_7 = " ... very lazy"
  msg_8 = " ... very, very lazy"
  msg_9 = "You are"
  if is_one_digit(x) == True and is_one_digit(y) == True:
    msg += msg_6
  
  if (x == 1 or y == 1) and oper =="*":
    msg += msg_7
  if (x == 0 or y == 0) and (oper =="*" or oper =="+" or oper =="-"):
    msg += msg_8
  if msg !="":
    msg = msg_9 + msg
    print(msg)

  
def is_one_digit(v):
  if v > -10 and v < 10 and v == int(v):
    return True
  else:
    return False
  


calculate()
