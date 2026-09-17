def main():
  Ans = 0

  try:
    print("Inside try block")
    print("Enter first number :")
    No1 = int(input())
  
    print("Enter second number :")
    No2 = int(input())
  
    Ans = No1/No2

  except ZeroDivisionError as zobj:
    print("Inside zobj")

  except Valueerror as vobj:
    print("Inside vobj")

  except Exception as eobj:
    print("Inside eobj")

  finally:
    print("Inside finally")

 
    

  print("Division is :",Ans)

if __name__ == "__main__":
  main()4