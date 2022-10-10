'''
required = []
s_list = []
s = input()
k = int(input())
y = len(s)
z = int(y/3)

for i in s:
    s_list.append(i)

reversed = s_list[::-1]    # s_list = ['A', 'A', 'B', 'C', 'A', 'A', 'A', 'D', 'A']
reversed = s_list[::-1]  # reversed = ['A', 'D', 'A', 'A', 'A', 'C', 'B', 'A', 'A']

while reversed :
    for i in range(z):
        popped = reversed.pop()
        required.append(popped)
    rewards = (set(required))
    rewardl = list(rewards)
    answer = ''.join(rewardl)
    print(answer)

    del required[0:z]'''



# t = number of test cases
# n = number of participants
# k = number of problems in the contest
# 
t = int(input("Enter the number of test cases: "))

for i in range(t):

    nk = input("enter no. of participants and problem: ")
    lnk = nk.split()
    nn = lnk[0]
    mk = input("enter marks for each problem individually: ")
    lmk = mk.split()
    for j in lmk:
        jin = int(j)
        

    for i in range(nn):
        mn1 = input()



    