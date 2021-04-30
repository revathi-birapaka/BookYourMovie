print("Welcome to BookYourMovie.com", "\n")


Row = int(input("Enter the number of rows:\n"))
Seats = int(input("Enter the number of seats in each row:\n"))
choice = 10
Booked_seats = 0
cost_of_ticket = 0
Total_Income = 0
Total_num_of_seats = Row*Seats
Ticket_booked_by_Person = [[None for j in range(Seats)] for i in range(Row)]

class pattern:

  @staticmethod
  def draw_pattern():
    pattern_of_seats = {}
    for i in range(Row):
      row_of_seats = {}
      for j in range(Seats):
        row_of_seats[str(j+1)] = 'S'
      pattern_of_seats[str(i)] = row_of_seats
    return pattern_of_seats


  @staticmethod
  def find_percentage():
    percentage = ((Booked_seats/Total_num_of_seats)*100)
    return percentage


class_call = pattern
sequence_of_pattern = class_call.draw_pattern()


while choice != 0:
  print("\n 1. Show the seats\n 2. Buy a ticket\n 3. Statistics\n 4. Show booked tickets user info\n 0. Exit")
  choice = int(input("Select your choice: "))
  if choice == 1:
    if Seats < 10:
      for seat in range(Seats):
          print(seat, end=' ')
      print(Seats)
    else:
      for seat in range(10):
        print(seat, end=' ')
      for seat in range(10, Seats):
        print(seat, end=' ')
      print(Seats)
    if Seats < 10:
      for num in sequence_of_pattern.keys():
        print(int(num)+1, end=' ')
        for no in sequence_of_pattern[num].values():
          print(no, end=' ')
        print()
    else:
        count_num = 0
        for num in sequence_of_pattern.keys():
          if int(list(sequence_of_pattern.keys())[count_num]) < 9:
            print(int(num)+1,end=' ')
          else:
            print(int(num)+1,end=' ')
          count_key = 0
          for no in sequence_of_pattern[num].values():
            if int(list(sequence_of_pattern[num].keys())[count_key]) <= 10:
              print(no, end=' ')
            else:
              print(no, end=' ')
            count_key += 1
          count_num += 1
          print()
        print('Vacant Seats = ' , Total_num_of_seats - Booked_seats)
        print()

        
  elif choice == 2:
    Row_number = int(input("Select the row:\n"))
    Column_number = int(input("Select the column:\n"))
    if Row_number in range(1, Row+1) and Column_number in range(1, Seats+1):
      if sequence_of_pattern[str(Row_number-1)][str(Column_number)] == "S":
        if Row*Seats <= 60:
          cost_of_ticket = 10
        elif Row_number <= int(Row/2):
              cost_of_ticket = 10
        else:
          cost_of_ticket = 8
        print("Cost of the ticket is -> ",'$', cost_of_ticket)
        Response = input("Enter yes if you want to book else no if you want to stop: \n")
        details_of_Person = {}
        if Response == "yes":
            details_of_Person["Name"] = input("Enter your Name -> ")
            details_of_Person["Gender"] = input("Enter your Gender -> ")
            details_of_Person["Age"] = input("Enter your Age -> ")
            details_of_Person["Phone_Number"] = input("Enter your Phone Number -> ")
            details_of_Person["Cost_of_Ticket"] = cost_of_ticket
            sequence_of_pattern[str(Row_number-1)][str(Column_number)] = "B"
            Booked_seats += 1
            Total_Income = (cost_of_ticket*Total_num_of_seats)

        else:
            continue
        Ticket_booked_by_Person[Row_number-1][Column_number-1] = details_of_Person
        print("Booked Successfully!!")
     
      else:
        print("The seat you have chosen is already booked")
      
    else: 
      Response == "no"
      print("Invalid input")
       
  elif choice == 3:
    print("Number of purchased Tickets -> ",Booked_seats)
    print("Percentage -> ",class_call.find_percentage())
    print("Current Income -> ", '$',cost_of_ticket)
    print("Total Income -> ", '$',Total_Income)
    print()

  elif choice == 4:
    Enter_row_num = int(input("Enter Row number -> \n"))
    Enter_column_num = int(input("Enter Column number -> \n"))
    if Enter_row_num in range(1,Row+1) and Enter_column_num in range(1,Seats+1):
      if sequence_of_pattern[str(Enter_row_num - 1)][str(Enter_column_num)] == 'B':
        Person = Ticket_booked_by_Person[Enter_row_num - 1][Enter_column_num - 1]
        print("Name -> ", Person["Name"])
        print("Gender -> ", Person["Gender"])
        print("Age -> ", Person["Age"])
        print("Cost_of_Ticket -> ", '$', Person['Cost_of_Ticket'])
        print("Phone Number -> ", Person["Phone_Number"])
      else:
          print()
          print("This Seat is Vacant")  
    
    else:
      print()
      print("Invalid Input")
   
  else:
    print()
    print("Exit")    

