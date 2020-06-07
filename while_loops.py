"""num_of_triess = 0
while num_of_triess < 3 :
    username = input('please enter your user name : ')
    password = input('please enter your password : ')

    if username == 'fadi' and password =='123':
        print('welcome')
        num_of_triess = 0
        exit()
    else:
        print('error')
        num_of_triess +=1
        print('you have : ' + str( 3- num_of_triess ) + 'left')



a = 0
b = 0
while a < 4:
    a+=1
    b=0
    while b < 4 :
        b+=1
        print(a,b)
    
for a in range(1,5):
    for b in range(1,5):
        print(a,b)
print(list(range(0,2000000+500000,5000)))


for letter in "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhonhhhhhhhhhht":
    if not(letter == "h"):
        print(letter)
y = 10 
while y > 0:
    y-=1
    if y == 5:
      continue
    print(y)     
print('bye')

start = int(input('Enter the starting number : '))
end = int(input('How High shoyld i go : '))
print('number \t\t square')
print('-------------------------')

while start <= end:
    square = start **2
    print(start,"\t\t",square)
    start+=1
print('number \t\t square')
print('-------------------------')
for i in range(start,end+1):
    square = i **2
    print(i,'\t\t',square)"""
size = int(input('please enter how many colms :'))
for r in range(size):
    for c in range((r+1)**2):
        print('*', end = '')
    print()    
while size > 0:
    for c in range(size**2):
        print('*',end= '')
    size-=1
    print()