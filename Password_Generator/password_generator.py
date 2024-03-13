import random
import string
def password_gen():
    print('Enter the complexity of password-: Easy, Medium or Hard')
    complexity  = input().capitalize()
    print('Enter the desired length of password')
    len_of_password = int(input())
    a=[]
    if complexity == 'Hard':
        randomkey = string.ascii_lowercase + string.digits + string.punctuation
        for i in range(len_of_password):
            s = random.choice(randomkey)# for choosing random keys
            a.append(s)# appending it to a list
        generated_password = ''.join(a)
        print(generated_password)
    elif complexity =='Medium':
        randomkey = string.ascii_lowercase + string.digits
        for i in range(len_of_password):
            s = random.choice(randomkey)
            a.append(s)
        generated_password = ''.join(a)
        print(generated_password)
    elif complexity =='Easy':
        randomkey = string.ascii_lowercase
        for i in range(len_of_password):
            s = random.choice(randomkey)
            a.append(s)
        generated_password = ''.join(a)
        print(generated_password)
    else:
        print('Enter a right choice')
if __name__== '__main__':
    password_gen()