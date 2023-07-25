# Commission Variables
SQL = 30.30
SAL = 71.43
Booking = 100

sql_input = int(input("How many SQL's do you have this month?: "))
sal_input = int(input("How many SAL's do you have this month?: "))
booking_input = int(input("How many Bookings do you have this month?: "))

total_commission = (sql_input * SQL) + (sal_input * SAL) + (booking_input * Booking)
total_commission = float(total_commission)

# Total Pay Variables
total_pay = (1390*2) + total_commission

def get_commission():
    print(f"Your total commission for the month is ${total_commission}.")

def get_paycheck():
    print(f"Your total pay for the month is ${total_pay}.")

while True:
    user_input = input("Would you like to see your commission or total pay?: ")
    user_input = user_input.strip()
    match user_input:
        case 'commission':
            get_commission()
        case 'total pay':
            get_paycheck()

