import sqlalchemy.sql.functions
from db_connection import Session, engine
from Keys import Key
from Doors import Door
from Rooms import Room
from Hooks import Hook
from Issued_Keys import IssuedKey
from Employees import Employee

def menu():
  print("[1] Create a new Key")
  print("[2] Request Access")
  print("[3] Check Room Access")
  print("[4] Delete a Key")
  print("[5] Delete Employee :(")
  print("[6] Add new Door")
  print("[7] Change Request")
  print("[8] Lost key :(")
  #print("[9] menu option 9")
  print("[0] menu option quit")

def io_Menu():
  menu()
  option = int(input("Enter your choice: "))

  if option == 1:
    #Selecting this option will create a key or replace said key
    option_choice = string(input("Do you wish to create a new key yes or no."))
    if option_choice == "yes":
      print("creating key")
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


def foo():
  menu()
  option = int(input("Enter your choice "))

  # Create new key
  if option == 1:
    room_choice: int = int(input("Which ROOM should the key be made for?: "))
    door_choice: str = input("Which DOOR should the key be for?: ")

    with Session() as sess:
      door: [Door] = sess.query(Key).filter_by(room_number=room_choice, door_name=door_choice)
      useable_hooks: [Hook] = sess.query(Hook).filter(Hook.hook_id.not_in(door))

      if len(useable_hooks) == 0:
        print("Too many key's exist for that door; cannot issuse a new one")
      else:
        new_key = Key(door[0], useable_hooks[0])
        sess.add(new_key)
        useable_hooks[0].add_key(new_key)
        door.add_key(new_key)
        print("New Key Created")
        sess.commit()

  # Create request
  elif option == 2:
    room_requested = input("Which room would you like access to? ")
    employee_id = input("Please input your employee id: ")

    with Session as sess:
      try: # would be more debug friendly with filter if statements
        queried_employee: [Employee] = sess.query(Employee).filter_by(employee_id=employee_id)
        queried_room: [Room] = sess.query(Room).filter_by(room_number=room_requested)
        new_request = Request(queried_employee[0], queried_room[0])

        sess.add(new_request)
        queried_employee[0].create_request(new_request)
        queried_room[0].add_request(new_request)
        sess.commit()
        print("Request created! Please await approval")
      except:
        #sess.abort()
        print("Failed to create request")

  # Get employee room access
  elif option == 3:
    employee_id = input("Which employee would you like to check acess for?")
    with Session() as sess:
      # An employee has access to a room iff they have a valid key
      # So check their issued keys, then check the rooms the hooks open
      posessed_keys: [IssuedKey] = sess.query(IssuedKey).filter_by(employee_id=employee_id, is_valid=True)

      if len(posessed_keys) == 0:
        print("Employee cannot open any doors")
        return

      iso_keys: [Key] = sess.query(Key).filter(Key.hook_id.in_(posessed_keys))
      processed_doors = []
      for key in iso_keys:
        if key.room_number not in processed_doors:
          print("Employee has access to: " + key.room_number)
          processed_doors.append(key.room_number)

  # Delete a key
  elif option == 4:
    with Session() as sess:
      fuck = sess.query(Key).all
      for shit in fuck:
        print(shit)
  # Delete employee
  elif option == 5:
    return
  # Add new door
  elif option == 6:
    return
  # Change request
  elif option == 7:
    return
  # exit condition
  elif option == 0:
    return 1
  else:
    print("Something went wrong parsing!")
    return 2
