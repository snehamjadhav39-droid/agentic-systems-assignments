def validate_and_score_resumes(student_info):
    print(type(student_info))
    student_data = student_info
    if student_data['experience_years'] < 0 or not student_data['skills']:
        raise TypeError("Not a Valid Exp Input")
    elif not isinstance(student_data['name'], str) or not student_data['name']:
        raise TypeError("Not a Valid Name Input")
    else:
        print(student_data)

        
Student_1 = {'name': 'Alice', 'experience_years': 5, 'skills': ['Python', 'SQL'], 'has_degree': True}
Student_2 = {'name': 'Bob', 'experience_years': -1, 'skills': ['Java'], 'has_degree': False}
Student_3 = {'name': 'Carol', 'experience_years': 3, 'skills': [], 'has_degree': False}
Student_4 = {'name': 'Dave', 'experience_years': 7, 'skills': ['Python', 'ML', 'SQL'], 'has_degree': False}
validate_and_score_resumes(Student_1)
validate_and_score_resumes(Student_2)
validate_and_score_resumes(Student_3)
validate_and_score_resumes(Student_4)
