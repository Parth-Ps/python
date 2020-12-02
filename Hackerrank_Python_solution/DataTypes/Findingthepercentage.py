'''
Title     : Finding the percentage
Subdomain : Data Types
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
n = int(input())
ar = {}
for i in range(0, n):
    s = input()
    ss = s.split(" ")
    n = ss[0]
    m1 = float(ss[1])
    m2 = float(ss[2])
    m3 = float(ss[3])
    m_avg = (m1 + m2 + m3) / 3.0
    ar[n] = "%.2f" % m_avg
s_name = input()
print(ar[s_name])
'''
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()

    query_scores = student_marks[query_name]
    print("{0:.2f}".format(sum(query_scores) / (len(query_scores))))
