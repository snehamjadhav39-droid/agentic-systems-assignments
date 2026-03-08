#Create a class called StudentMarks which does the following:

#Takes a list of marks as input while creating the object.
#Create a method called last_three_avg() which:
#Finds the average of the last three marks using negative indexing. If the list has less than 3 marks, handle it using exception handling and print:
#Not enough marks to calculate average


class StudentMarks:
    def last_three_average(self, Marks):
        try:
            if len(self.Marks) < 3:
                raise ValueError("List has less than 3 marks. Cannot calculate average.")

            input_list=Marks[-3:]
            print(input_list)
            total_marks=sum(input_list)
            average_marks=total_marks/3
            print("Average Marks : ", average_marks)
        except:
            print("Not enough marks to calculate average")

# Taking input from user
marks_input = input("Enter marks separated by spaces: ")

# Convert input into a list of integers
marks_list = [int(x) for x in marks_input.split()]
    
s1=StudentMarks()


s1.last_three_average(marks_list)
