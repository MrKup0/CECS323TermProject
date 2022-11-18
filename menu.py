def menu():
  print("[1] menu option 1")
  print("[2] menu option 2")
  print("[3] menu option 3")
  print("[4] menu option 4")
  print("[5] menu option 5")
  print("[6] menu option 6")
  print("[7] menu option 7")
  print("[8] menu option 8")
  print("[9] menu option 9")
  print("[0] menu option quit")

menu()
option = int(input("Enter your choice: "))

while option != 0:
  if option == 1:
    #Selecting this option will create a key or replace said key
    key_amount = 0
    option_choice = string(input("Do you wish to create a new key yes or no."))
    if option_choice = "yes":
      print("creating key")
      key_amount += 1 
      return keys(hook_id, room_number, door_name) 
    else:
      print("have a good day")
      return 0

  elif option == 2:
    room_request = string(create_request)

  elif option == 4:
    id_confirmation = int(input("Please input your employee id: "))
    if id_confirmation == employee_id:
      key_confirmation = int(input("Please input the key number lost: "))
      if key_confirmation == hook_id:
        print("lost key confirmed")
        return true
      else:
        print("key not found")
        return false

  elif option == 5:
    remove(employee_id)

  elif option == 6:
    remove(issued_key)
    