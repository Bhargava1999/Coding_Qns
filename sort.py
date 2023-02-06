#Sort 0's 1's 2's
#logic-1

inp="012012012012012"
out=""
temp=""
for i in inp:
    if i =='0':
        out=i+out
    elif i =='1':
        out=out+i
    else:
        temp=temp+i
out=out+temp
print(out)

#time complexity: O(N)
