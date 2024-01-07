f=open('students_new.txt','r',encoding='utf-8')

students=[]
for student in f:
        z=student.split(';')
        id= int (z[0])
        var= int (z[2])
        grup=(z[3])
        name = z [1]
        students.append({'id':id,'full_name':name,'var':var,'grup':grup})
for student in students:
        print(student)
  
f.close()
