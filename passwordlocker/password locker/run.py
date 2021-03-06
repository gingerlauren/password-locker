#!/usr/bin/env python3
from passlock import Credential
from passlock import UserData
import random
import string
import time
import pyperclip
def create_creds(uname, password):
    '''
    function that creates new credentials
    '''
    new_cred = Credential(uname,password)
    return new_cred


def save_creds(credential):
    '''
    function that saves credentials
    '''
    credential.save_creds()




def check_existing_cred(uname):
    '''
    function to test if credentials exist
    '''
    return Credential.creds_exist(uname)

def authenticate_creds(uname, passwrd):
    '''
    '''
    return Credential.authenticate_creds(uname,passwrd)

def user_data(acc_name,acc_username, acc_password):
    '''
    Function to authenticate and log in a user
    '''
    data = UserData(acc_name, acc_username, acc_password)
    return data


def create_new_data(mydata):
    '''
    Function that creates new data to save user password
    '''
    mydata.create_password()


def show_data():
    '''
    function to display the data
    '''
    return UserData.show_user_data()



def copy_password(acc_name):
    '''
    function to copy password to the clipboard
    '''
    my_password = UserData.show_user_data(acc_name)
    pyperclip.copy(my_password.acc_password)

def data_exist(acc_name):
    '''
    Function to check if the data exists
    '''
    return UserData.data_exists(acc_name)


def find_user_data(acc_name):
        '''
        function that finds user data by acc_name
        '''

        return UserData.find_by_acc_name(acc_name)





def generate_password(pass_length):
    '''
    Function that generates a random password
    '''

    password_list = []
    generated_password = random.sample(string.ascii_lowercase + string.digits + string.ascii_uppercase,pass_length)
    password_list.append(''.join(generated_password))
    return password_list





def main():
        print("Hello, welcome to password locker!, What is your name?")
        user_name = input('Name:')
        print(f'hello {user_name}. what would you like to do?')
        print('\n')
        while True:
            print("Use the following short short codes : cc - create a new account, lg - log in , ex - exit")
            short_code = input().lower()

            if short_code == 'cc':
                            print("New Account")
                            print("-"*10)

                            print ("username ....")
                            uname = input()

                            print("password ...")
                            password = input()

                            print("confirm password ...")
                            password = input()
                            save_creds(create_creds(uname,password)) # create and save credentials
                            print ('\n')
                            print(f"Your new account with username : '{uname}' and password '{password}' has been successfully created")
                            print ('\n')


            elif short_code == "lg":
                            print("Enter username and password to login:")
                            print("-"*50)
                            uname = input("Username: ")
                            passwrd = input("Password: ")
                            passwrd = input("confirm Password: ")
                            log_in = authenticate_creds(uname, passwrd)
                            if log_in==0:
                                print("\n")
                                print("Invalid username and/or password")             

                                print("-"*25)
                            elif log_in!=0:
                                print("\n")
                                print(f"Welcome {log_in.uname}! What would you like to do?")


                                while True:
                                    print("Use the following short short codes : ap - add new password, cp - copy a  password , lp - view you passwords, ex - exit")
                                    shrt_code= input()  
                                    if shrt_code== "ap":
                                        print("Enter account name such as facebook, instagram or Gmail:.......")
                                        acc_name = input()
                                        print(f"Enter username account for {acc_name}.......")
                                        acc_username = input()
                                        print("What is you preferred password length?")
                                        pass_length = int(input("Password length:"))
                                        acc_password = generate_password(pass_length)
                                        create_new_data(user_data(acc_name, acc_username, acc_password))
                                        print("\nHold on tight....")
                                        time.sleep(1.0)
                                        print("\n")
                                        print(f"Generated  password for {acc_name} is {acc_password}")
                                        print(".."*10)

                                    elif shrt_code =="cp":
                                        print("Enter the account name of  password you want to copy")
                                        get_name = (input("acc name : "))
                                        if data_exist(get_name):
                                            pyperclip.copy(acc_password)
                                            print("\n")
                                            print(f"Password for  {acc_name} successfully copied to clipboard, go ahead and paste it")
                                        else:
                                            print("You do not have any passwords yet")
                                            print("--"*10)



                                    elif shrt_code == "lp":
                                        if show_data():
                                            print('\n')
                                            for data in  show_data():
                                                print(f"{data.acc_name}------> {data.acc_password}")
                                                print('\n')

                                    elif shrt_code == "ex":
                                        print(f"Bye{log_in.uname}")







if __name__=='__main__':
    main()