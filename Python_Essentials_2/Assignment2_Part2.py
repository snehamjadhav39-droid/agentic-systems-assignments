class StudentScores:
    def highest_last_two(self, Marks):
        try:
            if len(self.Marks) < 2:
                raise ValueError("List has less than 3 marks. Cannot calculate average.")

            input_list=Marks[-2:]
            print(input_list)
            for i in input_list:
                if i>input_list[1]:
                    print("Highest Score among the two is : ", i)
                else:
                    print("Highest Score among the two is : ", input_list[1])
        except:
            print("Not enough marks to find the highest value")

# Taking input from user
marks_input = input("Enter marks separated by spaces: ")

# Convert input into a list of integers
marks_list = [int(x) for x in marks_input.split()]
    
s1=StudentScores()
s1.highest_last_two(marks_list)
