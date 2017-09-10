''' Creating dictionary from list
a=[0.232,0,0.435,3453,0,1213]
b=[]
c=[]
for i in range(len(x)):
    if x[i]!=0:
        b.append(i)
        c.append(x[i])
d={'inds':b,'vals':c}
print(d)'''


''' Group By Dict
def decompress_vector(d,n=None):
    p=max(max(d['inds'])+1,n)
    b=[]
    c=d['inds']
    z=d['vals']
    for i in range(p):
        l=[]
        for j in range(len(d['inds'])):
            if c[j]==i:
                l.append(z[j])
        b.append(sum(l))
            
    return(b)

d={'inds':[1,2,3,2,4],'vals':[2,4,3,5,1]}
x=decompress_vector(d)
x
'''

''' Find Common Inds 

def find_common_inds(d1,d2):
    a=d1['inds']
    b=d2['inds']
    n1=len(a)
    n2=len(b)
    c=set()
    for i in range(n1):
        for j in range(n2):
            if a[i]==b[j]:
                c.add(a[i])
                break
    return(list(c))

d1 = {'inds': [9, 9, 1, 9, 3, 1], 'vals': [0.28, 0.84, 0.71, 0.03, 0.04, 0.75]}
d2 = {'inds': [0, 9, 9, 1, 3, 3, 9], 'vals': [0.26, 0.06, 0.46, 0.58, 0.42, 0.21, 0.53, 0.76]}
print(find_common_inds(d1,d2))
'''

grades = [
    # First line is descriptive header. Subsequent lines hold data
    ['Student', 'Exam 1', 'Exam 2', 'Exam 3'],
    ['Thorny', '100', '90', '80'],
    ['Mac', '88', '99', '111'],
    ['Farva', '45', '56', '67'],
    ['Rabbit', '59', '61', '67'],
    ['Ursula', '73', '79', '83'],
    ['Foster', '89', '97', '101']
]

''' assignments like student names
assignments=[]
for i in range(1,4):
    assignments.append(grades[0][i])
print(assignments)
'''

''' Dictionary
grade_lists=dict()
for i in range(1,7):
    d1={grades[i][0]:[int(x) for x in (grades[i][1:4])]}
    grade_lists.update(dict)
print(grade_lists)
print(type(grade_lists))
'''

''' Dictionary in a dictionary
grade_dicts=dict()
for i in range(1,7):
    d2=dict()
    for j in range(1,4):
        d3={grades[0][j]:int(grades[i][j])}
        d2.update(d3)
    grade_dicts.update({grades[i][0]:d2})
print(grade_dicts)
'''

'''average grades per sutudent
avg_grades_by_student_test=dict()
for i in range(1,7):
    x=[int(x) for x in (grades[i][1:4])]
    x=sum(x)/3
    d1={grades[i][0]:x}
    avg_grades_by_student_test.update(d1)
print(avg_grades_by_student_test)
'''

''' grades by assignment
grades_by_assignment=dict()
for j in range(1,4):
    l=[]
    for i in range(1,7):
        l.append(int(grades[i][j]))
    grades_by_assignment.update({'Exam '+str(j):l})
print(grades_by_assignment['Exam1']==)
'''
'''
avg_grades_by_assignment=dict()
for j in range(1,4):
    l=[]
    for i in range(1,7):
        l.append(int(grades[i][j]))
    l=sum(l)/6
    avg_grades_by_assignment.update({'Exam '+str(j):l})
print(avg_grades_by_assignment)
'''
'''Rank'''


avg_grades_by_student=dict()
for i in range(1,7):
    x=[int(x) for x in (grades[i][1:4])]
    x=int(sum(x)/3)
    d1={grades[i][0]:x}
    avg_grades_by_student.update(d1)
avg_grades_by_student=sorted(avg_grades_by_student.items(), key=lambda value:value[1], reverse=True)
rank=[]
for i in range(0,6):
    rank.append(avg_grades_by_student[i][0])

# `rank_test`: Test cell
print(rank)
print("\n=== Ranking ===")
for i, s in enumerate(rank):
    print("{}. {}: {}".format(i+1, s, avg_grades_by_student[s]))

