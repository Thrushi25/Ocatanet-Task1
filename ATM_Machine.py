import time
print("Please enter your card number")
time.sleep(4)
password= 2525
pin = int(input("enter your atm pin number"))
balance=8000
if pin == password:
  while True:
    print("""
    1 == balance
    2 == deposit balance
    3 == withdraw balance
    4 == exit
    """
    )
    try:
      choice=int(input("please enter your choice"))
    except:
      print("please enter the valid choice")
    if choice == 1:
      print(f"your current balance is {balance}")
    if choice == 2:
      deposit_amount = int(input("please enter your deposit amount"))
      balance+=deposit_amount
      print(f"{deposit_amount} is credited too your account")
      print(f"your updated balance is {balance}")
    if choice == 3:
      withdraw_amount = int(input("please enter your deposit amount"))
      balance-=withdraw_amount
      print(f"{withdraw_amount} is debited too your account")
      print(f"your updated balance is {balance}")
    if choice == 4:
      break
else:
  print("your enter the wrong pin,please try again")