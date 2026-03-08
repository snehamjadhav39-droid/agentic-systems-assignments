class StudentMarks:
    def last_three_average(self, Marks):
        input_list=Marks[-3:]
        print(input_list)
        total_marks=sum(input_list)
        average_marks=total_marks/3
        print("Average Marks : ", average_marks)

# Taking input from user
marks_input = input("Enter marks separated by spaces: ")

# Convert input into a list of integers
marks_list = [int(x) for x in marks_input.split()]
    
s1=StudentMarks()


s1.last_three_average(marks_list)
