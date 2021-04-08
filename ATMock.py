import datetime
import random


now = datetime.datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))

customerdata = {}


def bank():
    print('Welcome to Zuri Bank, where customer is king.\n')

    selectedOption = False

    while selectedOption == False:

        prompt = (input('Are you an account holder? Yes/No? Type q to quit: \n').lower().title())
        if prompt == 'Yes':
            selectedOption == True
            login()


        elif prompt == 'No':
            selectedOption == True
            register()
        else:
            exit()


def register():
    print('Kindly fill in your details to open an account. \n')

    #Requirements for account opening
    email = input('Email address?: \n')
    phone_number = int(input('Phone number?: \n'))
    first_name = input('What is your first name?: \n')
    middle_name = input('What is your middle name? \n')
    last_name = input('What is your last name?: \n')


    full_name = (first_name + ' ' + middle_name + ' ' + last_name)  # This outputs the customer's full name.
    accountNumber = generateAccountNumber()  #New account generation
    customerdata[accountNumber] = [first_name, middle_name, last_name, email, phone_number]


    userLogin = input('New username: \n')

    if userLogin in customerdata:
        print('\n Username already exists.\n')
    else:
        userPassword = input('New Password: \n')
        customerdata[userLogin] = userPassword

    print('Thank you for choosing us. Welcome %s, your account has successfully been created.' % full_name)
    print('== === ==== ===== ==== ===')
    print('Your account number is: %d' % accountNumber)
    print('== === ==== ===== ==== ===')

    login()

def login():
    print('===Login to your account===')
    accountNumberFromUser =int(input('Enter your account number: \n'))
    password = input('Enter your password: \n')
    transaction()

    isSuccessfulLogin = False

    while isSuccessfulLogin == False:


        for accountNumber, userDetails in customerdata.items():
            if accountNumber == accountNumberFromUser:
                if userDetails[3] == password:
                    isSuccessfulLogin = True

        print('Invalid account or password')



    transaction(userDetails)



def transaction():

    selectedOption = int(input('What would you like to do?: \n1.Withdrawal\n2.Deposit\n3.Complaint\n4.Logout \n'))

    if selectedOption == 1:
        withdrawal()
    elif selectedOption == 2:
        deposit()
    elif selectedOption == 3:
        complaint()
    elif selectedOption == 4:
        exit()

    else:
        print('Invalid option selected.')


def withdrawal():
    balance = 5000000
    withdrawal = int(input('How much would you like to withdraw?:  '))
    if withdrawal > 0:
        print('Your current balance is' + ' ' + str(balance - withdrawal))
        print('Please take your cash')

    keep_going = False
    while keep_going == False:

        another_transaction = (input('Would you like to perform another transaction?: Yes/No \n').lower().title())
        if another_transaction == 'Yes':
            keep_going == True
            transaction()
        else:
            print('Thank you for banking with us.')
            exit()


def deposit():
    balance = 5000000
    deposit = int(input('How much would you like to deposit?: '))
    if deposit > 0:
        currentBalance = (balance + deposit)
        print('Current Balance  : %d' % currentBalance)

        keep_going = False
        while keep_going == False:

            another_transaction = (input('Would you like to perform another transaction?: Yes/No \n').lower().title())
            if another_transaction == 'Yes':
                keep_going == True
                transaction()
            else:
                print('Thank you for banking with us.')
                exit()

def complaint():
    complaint = int(
        input('What issue will you like to report? \n1.Dispense Error\n2.Insufficient Funds\n3.Staff Attitude \n:'))
    if complaint < 4:
        print('Thank you for contacting us.Kindly visit the nearest branch for a resolution.')

        keep_going = False
        while keep_going == False:

            another_transaction = (input('Would you like to perform another transaction?: Yes/No \n').lower().title())
            if another_transaction == 'Yes':
                keep_going == True
                transaction()
            else:
                print('Thank you for banking with us.')
                exit()


    else:
        print('Invalid option selected, try again later')

    exit()



def generateAccountNumber():

    return random.randrange(1111111111,9999999999)



bank()
