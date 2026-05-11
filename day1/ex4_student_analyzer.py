def analyze_students(students):
    averages = []
    for name , score in students.items():
        average = sum(score) / len(score)
        if average >= 15:
            print(f"{name}: average= {average:.2f} - Great Job!")
        else:
            print(f"{name}: average= {average:.2f} - Keep Trying!")
        averages.append(average) 
    if not students:
        print("No students found" )
        return None
    else:
        return f"Class average: {sum(averages) / len(averages):.2f}"

students = {
    "Zelda": [18, 19, 20],
    "Link": [12, 14, 13],
    "Ganondorf": [9, 10, 8],
    "Mario": [20, 20, 19],
    "Sonic": [15, 14, 16]
}


print(analyze_students(students))


    
