S = input()

B_order = []
for i in range(len(S)):
    if S[i] == 'B':
        B_order.append(i)

K_order = []
R_order = []
for i in range(len(S)):
    if S[i] == 'K':
        K_order.append(i)
    elif S[i] == 'R':
        R_order.append(i)

if (B_order[0]+B_order[1]) % 2 != 0 and (B_order[0] * B_order[1]) % 2 == 0:
    if R_order[0] <= K_order[0] <= R_order[1]:
        print('Yes')
    else:
        print('No')
else:
    print('No')
