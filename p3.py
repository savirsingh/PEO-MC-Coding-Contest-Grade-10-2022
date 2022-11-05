a=int(input())
d=int(input())
n=int(input())

nums=[]

for i in range(n):
    nums.append(a)
    a+=d

print(sum(nums))
