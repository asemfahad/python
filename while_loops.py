num_of_triess = 0
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