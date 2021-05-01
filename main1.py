class Bookyourmovie:
    title = "Welcome to BookYourMovie.com"

    def mainmenu(self):
        response = True
        while response:
          print("Enter your Choice:")
          self.choice = int(input("\n 1. Show the seats\n 2. Buy a ticket\n 3. Statistics\n 4. Show booked tickets user info\n 0. Exit\n"))
          if self.choice == 0:
            response = False
            self.exit()
          elif self.choice == 1:
            self.show_the_seats()
          elif self.choice == 2:
            self.buy_a_ticket()
          elif self.choice == 3:
            self.statistics()
          elif self.choice == 4:
            self.user_info()
          else:
              print("\n Your choice is Invalid")

    def __init__(self):
        self.row_num = int(input("Enter the number of rows -> \n"))
        self.col_num = int(input("Enter the number of seats in each row -> \n"))
        self.total_no_of_seats = (self.row_num * self.col_num)
        self.current_income = 0
        self.total_income = 0
        self.details_of_user = {}
        self.pattern_of_seats = []
        self.count_of_seats = 0
  
        #pattern
        for x in range(self.row_num):
            i = []
            for y in range(self.col_num):
                i.append("S")
            self.pattern_of_seats.append(i)
        print(end=' ')

    def show_the_seats(self):
      print("\nCinema :\n")
      i = 0
      j = 0
      print(end=' ')
      for y in range(1, self.col_num + 1):
          j +=1
          print(j, end=' ')
      print()  
      for x in self.pattern_of_seats:
          i += 1
          print(i, end=' ')
          print(' '.join(x), sep=' ')

    def buy_a_ticket(self):
      x = int(input("Enter the row number -> \n"))
      y = int(input("Enter the column number -> \n"))
      if self.total_no_of_seats < 60:
        self.cost_of_ticket = 10
        print("Cost of ticket is 10$")
      elif x > self.row_num/2:
        self.cost_of_ticket = 8
        print("Cost of ticket is 8$")
      elif x < self.row_num/2:
        self.cost_of_ticket = 10
        print("Cost of ticket is 10$")
      elif self.pattern_of_seats[x-1][y-1] == "B":
        print("This seat is booked by someone else")
        self.mainmenu()
      Response = input("Enter yes if you want to book else no if you want to stop: \n")

      if Response == "yes":
        dict_details_of_user = {}
        Name_of_user = input("Enter your Name -> ")
        Gender_of_user = input("Enter your Gender -> ")
        Age_of_user = input("Enter your Age -> ")
        Mobile_Num_of_user = input("Enter your Mobile Num -> ")
        self.row_num_1 = x - 1
        self.col_num_1 = y - 1
        self.pattern_of_seats[self.row_num_1][self.col_num_1] = "B"
        self.count_of_seats += 1
        self.current_income = (self.current_income+self.cost_of_ticket)
        dict_details_of_user[(self.row_num_1+1),(self.col_num_1+1)] = list((Name_of_user,Gender_of_user,Age_of_user,Mobile_Num_of_user, self.cost_of_ticket))
        self.details_of_user.update(dict_details_of_user)
        print("Ticket Booked Successfully!!!")
      else:
        print("Please try again")

    def Income_Gain(self):
      if self.total_no_of_seats < 60:
        self.total_income = self.total_no_of_seats*10
      elif self.total_no_of_seats >= 60:
        for i in range(0,int(self.row_num/2)):
            value_1 = int(self.row_num/2)*self.col_num*10
        for j in range(int(self.row_num/2),self.row_num):
            value_2 = int(self.row_num/2)*self.col_num*8
        self.total_income = (value_1+value_2)
        return self.total_income

    def statistics(self):
      self.percentage = (self.count_of_seats/self.total_no_of_seats)*100
      print("Number of purchased tickets -> ",self.count_of_seats)
      print("Percentage -> ","{:.2f}".format(self.percentage),"%")
      print("Current Income -> ",'$',self.current_income)
      print("Total Income -> ",'$',self.Income_Gain())

    def user_info(self):
      self.test_x = int(input("Enter the row number -> "))
      self.test_y = int(input("Enter the column number ->"))
      if self.pattern_of_seats[self.test_x-1][self.test_y-1] == 'B':
          Person = self.details_of_user[(self.test_x,self.test_y)]
          print('Name -> ',Person[0])
          print('Gender ->',Person[1])
          print('Age ->',Person[2])
          print('Mobile Num ->',Person[3])
      else:
          print("This seat is vacant!!")

    def exit(self):
        return None

Bym_obj = Bookyourmovie()
Bym_obj.mainmenu()

