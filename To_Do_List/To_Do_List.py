list_of_tasks=[]
def addtask():
    task_input = input()
    status = 'pending'
    list_of_tasks.append({'Task Name':task_input,'Task Status': status})
def displaytask():
    print('To------------- Do ---------------List')
    s=1
    for i in list_of_tasks:
        print(f'{s}.{i}')
        s = s+1
    print('\n--------------------------------')
def updatestatus():
    print('choose index of list')
    user= int(input())
    list_of_tasks[user-1]['Task Status']='completed'
    print('Task updated succesfully')
if __name__=='__main__':
    while True:
        print('1.Add task\n2.Display Task\n3.Update Task Status\n4.Exit')
        print('Enter your choice')
        user_input = int(input())
        if user_input == 1:
            addtask()
            print('task added')
        elif user_input ==2:
            displaytask()
        elif user_input ==3:
            displaytask()
            updatestatus()
        elif user_input ==4:
            print('Thank you ')
            break
        else:
            print('please enter a right choice')
            continue
        