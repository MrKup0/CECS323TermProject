import sqlalchemy.sql.functions
from db_connection import Session, engine
from Keys import Key
from Doors import Door
from Rooms import Room
from Hooks import Hook
from Issued_Keys import IssuedKey
from Employees import Employee

def menu(): # Pres order
  print("[1] Create a new Key") # Jacob
  print("[2] Request Access") # Angel
  print("[3] Check Room Access") # Jacob
  print("[4] Delete a Key") # Angel
  print("[5] Delete Employee") # Jacob
  print("[6] Add new Door") # Angel
  print("[7] Change Request") # Jacob
  print("[8] Lost key") # Angel
  print("[9] Log room access") # Jacob
  print("[0] Quit")

def io_Menu():
  menu()
  option = int(input("Enter your choice "))

  # Create new key
  if option == 1:
    room_choice = int(input("Which ROOM should the key be made for?: "))
    door_choice = input("Which DOOR should the key be for?: ")

    with Session() as sess:
      try:
        door = sess.query(Key).filter_by(room_number=room_choice, door_name=door_choice)
        useable_hooks = sess.query(Hook).filter(Hook.hook_id.not_in(door))
      except:
        print("Could not find correlating door")
        return 0

      if len(useable_hooks) == 0:
        print("Too many key's exist for that door; cannot issuse a new one")
      else:
        new_key = Key(door[0], useable_hooks[0])
        sess.add(new_key)
        useable_hooks[0].add_key(new_key)
        door.add_key(new_key)
        print("New Key Created")
        sess.commit()
    return 0
  # Create request
  elif option == 2:
    room_requested = input("Which room would you like access to? ")
    employee_id = input("Please input your employee id: ")

    with Session as sess:
      try:
        queried_employee = sess.query(Employee).filter_by(employee_id=employee_id)
        queried_room = sess.query(Room).filter_by(room_number=room_requested)
        new_request = Request(queried_employee[0], queried_room[0])

        sess.add(new_request)
        queried_employee[0].create_request(new_request)
        queried_room[0].add_request(new_request)
      except:
        print("Failed to create request")
      else:
        sess.commit()
        print("Request created! Please await approval")
    return 0

  # Get employee room access
  elif option == 3:
    employee_id = input("Which employee would you like to check acess for?")
    with Session() as sess:
      # An employee has access to a room iff they have a valid key
      # So check their issued keys, then check the rooms the hooks open
      posessed_keys: [IssuedKey] = sess.query(IssuedKey).filter_by(employee_id=employee_id, is_valid=True)

      if len(posessed_keys) == 0:
        print("Employee cannot open any doors")
        return 0

      iso_keys = sess.query(Key).filter(Key.hook_id.in_(posessed_keys))
      processed_doors = []
      for key in iso_keys:
        if key.room_number not in processed_doors:
          print("Employee has access to: " + key.room_number)
          processed_doors.append(key.room_number)
    return 0

  # Delete a key
  elif option == 4:
    with Session() as sess:
      valid_keys = sess.query(Key).all()
      for key in valid_keys:
        print(key)
      print("Above are valid keys; select one to delete\n")
      hook = input("Hook_id: ")
      room_number = input("room_number: ")
      door_name = input("door_name: ")
      try:
        specific_key = sess.query(Key).filter_by(hook_id=hook, room_number=room_number, door_name=door_name)
        sess.delete(specific_key)
      except:
        print("Could not make changes, double check input")
      else:
        sess.commit()
    return 0

  # Delete employee
  elif option == 5:
    with Session() as sess:
      employees = sess.query(Employee).all()
      for emp in employees:
        print(emp)
      print("Select from the above employees, which to remove")
      fired_guy = input("Enter the employee number: ")

      try:
        sess.delete(sess.query(Employee).filter_by(emplyee_id=fired_guy))
      except:
        print("An error occured, " + fired_guy + " could not be removed")
      else:
        sess.commit()
        print("Employee removed!")
    return 0

  # Add new door
  elif option == 6:
    with Session as sess:
      rooms = sess.query(Room).all()
      for r in rooms:
        print(r)
      room_alter = input("Enter the room number you wish to add a door too: ")
      new_name = input("What should this door be called? ")
      try:
        parent_room = sess.query(Room).filter_by(room_number=room_alter)
        new_door = Door(parent_room[0], new_name)
        sess.add(new_door)
        parent_room.add_door(new_door)
      except:
        print("There was an issue locating room number " + room_alter)
      else:
        sess.commit()
        print("New door has been added!")
    return 0

  # Change request
  elif option == 7:
    with Session() as sess:
      employees = sess.query(Employee).all()
      for emp in employees:
        print(emp)

      sel = input("Please enter the employee number who's requests you wish to view: ")
      try:
        active_requests = sess.query(Requests).filter_by(employee_id=sel)
        if len(active_requests) == 0:
          print("Employee has no logged requests!")
          return 0

        for i in active_requests:
          print("Request for room: " + i.room_number)

      except:
        print("Could not find employee with id=" + sel)
        return 0

      request = input("Which room request would you like to alter?")

      try:
        queried_request = sess.query(Request).filter_by(employee_id=sel, room_number=request)
        date = queried_request[0].request_date
        if len(queried_request) > 1:
          for i in queried_request:
            print(i.room_number + "; on " + i.request_date)
          date = input("Employee has made several requests for that room, please indicate which date you wish to alter: ")
      except:
        print("Could not find specifed room")
        return 0

      try:
        new_guy = input("Please enter the new employee you wish the request to be made for: ")
        sess.query(Request).filter_by(employee_id=sel, room_number=request, request_date=date)\
          .update({Request.employee_id:new_guy}, syncronize_session=False)
      except:
        print("Could not alter table")
        return 0
      else:
        sess.commit()
        print("Updated employee request")

  # Log Lost Key
  elif option == 8:
    id = input("Please enter your id: ")
    room = input("Please input what room key you lost: ")

    with Session() as sess:
      try:
        lost_key = sess.query(IssuedKey).filter_by(employee_id=id, requested_room=room)
        if not lost_key[0].is_valid:
          print("This key has already been returned, no sweat")
          return
        else:
          sess.query(Employee).filter_by(employee_id=id).update({Employee.amount_owed:Employee.amount_owed + 20}, synchronize_session=False)
      except:
        print("Could not find specific key, please check you have been issued a key for that room")
      else:
        print("Thank you for reporting the loss, a new key has been issued and you have been charged")
    return 0

  # Log Room Access
  elif option == 9:
    with Session as sess:
      rooms = ses.query(Room).all()
      for i in rooms:
        print(i.room_number)
      query_room = input("From the above rooms, which would you like to check acess to: ")

      try:
        acsess = sess.query(IssuedKey).join(Key).filter(Key.room_number==query_room)
        listed = []
        for i in acsess:
          if i not in listed:
            print("Employee: "+i.employee_id+" has access")
            listed.append(i)
      except:
        print("Could not find anyone with access")
    return 0

  # exit condition
  elif option == 0:
    return 1
  else:
    print("Something went wrong parsing!")
    return 2
