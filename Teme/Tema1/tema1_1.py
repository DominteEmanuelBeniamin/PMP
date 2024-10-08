import csv
import random
import os

print("Directorul de lucru curent:", os.getcwd())

os.chdir('/home/dominteemanuelbeniamin/Documents/GitHub/PMP/Teme/Tema1/')

def sample_students(file_path, num_samples):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) 
        students = [row for row in reader if row[1].lower() == 'nu']  
        
    if num_samples > len(students):
        raise ValueError("Numărul de eșantioane cerut este mai mare decât numărul de studenți disponibili.")
        
    selected_students = random.sample(students, num_samples)
    for student in selected_students:
        print(student)

file_path = 'Lista_Studenti.csv'
num_samples = 2
sample_students(file_path, num_samples)
