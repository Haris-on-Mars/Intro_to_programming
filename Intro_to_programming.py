# #def multiply_by_three(input_var):
#     output_var = input_var * 3
#     return output_var
# output_var=multiply_by_three(97)
# #print(output_var)


# def divide_by_two_and_multiply_by_4(input_variable):
#     output_variable=(input_variable/2)*4
#     return output_variable
# output_variable=divide_by_two_and_multiply_by_4(10)
# print(output_variable)

# Number_of_hours=40
# Rate_per_hour=10
# Tax=0.12
# Gross_pay=(Rate_per_hour*Number_of_hours)
# Tax_on_Salary=(Gross_pay*Tax)
# Net_pay=(Gross_pay-Tax_on_Salary)
# print(Net_pay)
# print(Net_pay*4.00)

#Function with mutiple arguments

def calculate_net_pay(hours_worked, hourly_rate, tax_rate):
    """
    Calculates the net pay after tax deductions based on hours worked, hourly rate, and tax rate.

    Args:
        hours_worked (float): The number of hours worked.
        hourly_rate (float): The pay rate per hour.
        tax_rate (float): The tax rate to be applied (as a decimal, e.g., 0.2 for 20%).

    Returns:
        float: The net pay after tax deductions.
    """
    gross_pay = hours_worked * hourly_rate
    tax_on_salary = gross_pay * tax_rate
    net_pay = gross_pay - tax_on_salary
    return net_pay

# # Example usage
# hours_worked = 40
# hourly_rate = 24
# tax_rate = 0.22
# net_pay = calculate_net_pay(hours_worked, hourly_rate, tax_rate)
# print(net_pay)

#Function with no arguments

def nikal_bsdk():
    output = "Tu nikal bsdk_madarchod"
    return output

# Example usage
# result = nikal_bsdk()
# print(nikal_bsdk())

def get_expected_cost(bedroom, bathroom):
    """
    Calculate the expected cost of a house beased on the number of bedroom & bathrooms.
    
    Agruments:
        each bedroom adds $30,000 to the cost,
        each bathroom adds $10,000 to the cost.
    
    Returns:
        The expected cost if the house. 

    """
    get_expected_cost = (bedroom * 30000) + (bathroom * 10000)
    return get_expected_cost

# Example_usage
# bedroom = 1
# bathroom = 1

# expected_cost = get_expected_cost(3, 2)

# print(expected_cost)

#Data types:
# 1. String
# 2. Integer
# 3. Float
# 4. Boolean
# 5. List
# 6. Tuple
# 7. Dictionary
# 8. Set


# x = "1.20252645"
# print(type(x))
# print(x)

# Convert string to float
# x_float = float(x)
# print(type(x_float))
# print(x_float)

# x = 1.20252645
# print(type(x))
# y = int(x)
# print(type(y))
# print(round(y, 2))  # Rounding to 2 decimal placesy


# x = "984231894.554984"
# y = "987984654897"
# multiply_x_by_True = x * True
# multiply_x_by_False = x * False 


# multiply_y_by_True = y * True
# multiply_y_by_False = y * False


# print(multiply_x_by_True)

# print(multiply_x_by_False)

# print(multiply_y_by_True)

# print(multiply_y_by_False)

#Data_type_examples

#Exercise 1:

def get_expected_cost(bedroom, bathroom, basement):
    """
    Calculate the expected cost of a house based on the number of bedrooms, bathrooms, and basements.

    Args:
        bedroom (int): Number of bedrooms.
        bathroom (int): Number of bathrooms.
        basement (Boolean): Number of basements.

    Returns:
        int: The expected cost of the house.
    """

    get_expected_cost = 80000 + (bedroom * 30000) + (bathroom * 10000)
    if basement >= True:
        get_expected_cost = 80000 + (bedroom * 30000) + (bathroom * 10000) + (basement * 40000)
    if basement == False:
        get_expected_cost = 80000 + (bedroom * 30000) + (bathroom * 10000)
    return get_expected_cost

# Example usage
# bedroom = 0 
# bathroom = 0
# basement = 0
# expected_cost = get_expected_cost(0, 0, True)
# print(expected_cost)

# Example 2:

def cost_of_project(engraving, solid_gold, gold_plated):
    """
    Calculate the cost of a project based on engraving and solid gold.

    Args:
        engraving (str): the project includes engraving. each engraving unit add $7 to the cost on gold plated and $10 to the cost on solid gold.
        solid_gold (bool): the project is made of solid gold.

    Returns:
        int: The total cost of the project.
    """
    total_cost = (gold_plated * 50) + (solid_gold * 100) + (len(engraving) * 7 if gold_plated else len(engraving) * 10)
    if gold_plated == True and solid_gold == False:
        total_cost = (gold_plated * 50) + (len(engraving) * 7)
    elif solid_gold == True and gold_plated == False:
        total_cost = (solid_gold * 100) + (len(engraving) * 10)
    return total_cost

# Example usage
# engraving = "Muhammad Haris"
# solid_gold = True
# gold_plated = False

# print(cost_of_project("Subhan Sheikh", True, False))



def cost_of_project(engraving, solid_gold, gold_plated):
    """
    Calculate the cost of a project based on engraving and solid gold.

    Args:
        engraving (str): the project includes engraving. each engraving unit add $7 to the cost on gold plated and $10 to the cost on solid gold.
        solid_gold (bool): the project is made of solid gold.

    Returns:
        int: The total cost of the project.
    """
    total_cost = (gold_plated * 50) + (solid_gold * 100) + (len(engraving) * 7 if gold_plated else len(engraving) * 10)
    if gold_plated == True and solid_gold == False:
        total_cost = (gold_plated * 50) + (len(engraving) * 7)
    elif solid_gold == True and gold_plated == False:
        total_cost = (solid_gold * 100) + (len(engraving) * 10)
    return total_cost

# Example usage
# engraving = "Muhammad Haris"
# solid_gold = True
# gold_plated = False

# print(cost_of_project("Mansoor Ahmed Bhatti", False, True))

tour = 90000
train_tickets_for_one_side = 31000
Bus_tickets_for_one_side = 20000
Hotel_in_Islamabad = 5000
Nights_in_Islamabad = 2
Days_in_Islamabad = 1
rent_a_car_in_Islamabad = 10000
total_cost = (tour + (train_tickets_for_one_side * 2) + (Bus_tickets_for_one_side * 2) + (Hotel_in_Islamabad * Nights_in_Islamabad) + (Days_in_Islamabad * rent_a_car_in_Islamabad))
# print(total_cost)

#Condition & Conditional Statements

#we_are_defining_the_function_to_evaluate_the body_Temperature

def evaluate_body_temperature(temperature):

    message = "Normal_temperature"

    if temperature > 38:
        message = "Fever!"
    return message

# Example usage
# temperature = 37

# print(evaluate_body_temperature(1))


def evaluate_body_temperature(temperature):

    if temperature > 38:
        message = "Fever!!"
    else:
        message = "Normal_temperature"
    return message

def evaluate_body_temperature_with_adv_features(temperature):

    if temperature > 38:
        message = "Fever"
    elif temperature > 35:
        message  = "Normal Temperature"
    else:
        message = "Low Temperature"
    return message

# print(evaluate_body_temperature_with_adv_features(35.1))

# Example - Calculations¶
# In the examples so far, conditional statements were used to decide how to set the values of variables. But you can also use conditional statements to perform different calculations.

# In this next example, say you live in a country with only two tax brackets. Everyone earning less than 12,000 pays 25% in taxes, and anyone earning 12,000 or more pays 30%. The function below calculates how much tax is owed.

def calculate_tax(income):

    if income < 12000:
        tax = income * 0.25
    else:
        tax = income * 0.30
    return tax

# Example usage
# income = 15000

# print(calculate_tax(50000))

# Appendix: Conditional Statements

def add_three_or_eight(input_variable):

    if input_variable < 10:
        output_variable = input_variable + 3
    else:
        output_variable = input_variable + 8
    return output_variable

# Example usage
# input_variable = 5

# print(add_three_or_eight(10.00000000000000000000000000000000000000000000000000001))

# Example - Multiple "elif" statements¶
# So far, you have seen "elif" used only once in a function. But there's no limit to the number of "elif" statements you can use. For instance, the next block of code calculates the dose of medication (in milliliters) to give to a child, based on weight (in kilograms).

def get_doseage(weight):

    if weight < 5.2:
        dosage = 1.25
    elif weight < 7.9:
        dosage = 2.5
    elif weight < 10.4:
        dosage = 3.75
    elif weight < 15.9:
        dosage = 5
    elif weight <21.2:
        dosage = 7.5
    else:
        dosage = 10
    return dosage


# Example usage
# print(get_doseage(22.1))

#Question 1

def get_grade(score):

    if score >=90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >=60:
        grade = "D"
    else:
        grade = "F"
    return grade

# Example usage
# score = 85

# print(get_grade(70))

# Question 2

def cost_of_project(engraving, solid_gold):
    if solid_gold == True:
        total_cost = len(engraving) * 10 + 100
    else:
        total_cost = len(engraving) * 7 + 50
    return total_cost

example_usage = cost_of_project("Muhammad Haris", True)

# print(cost_of_project("Muhammad Haris Farooqui", True))

# Question 3

def get_water_bill(num_gallons):
    if num_gallons <= 8000:
        bill = 5 * (num_gallons / 1000)
    elif num_gallons <= 22000:
        bill = 6 * (num_gallons / 1000)
    elif num_gallons <= 30000:
        bill = 7 * (num_gallons / 1000) 
    else:
        bill = 10 * (num_gallons / 1000)
    return bill

# Example usage
# num_gallons = 15000

# print(get_water_bill (3000000))

# Question 4

def get_phone_bill(gb):
    if gb <= 15:
        bill = 100
    else:
        bill = round(100 + ((gb - 15) * 100)) 
    return bill

# Example usage
# gb = 20  

# print(get_phone_bill(2000))


flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"
# print(type(flowers))
# print(flowers)

flowers_list = ["pink primrose","hard-leaved pocket orchid","canterbury bells","sweet pea","english marigold","tiger lily","moon orchid","bird of paradise","monkshood","globe thistle"]

# print(type(flowers_list))
# print(flowers_list)

# print(len(flowers_list))

# print("first_value:", flowers_list[1])


# print("6th_value:", flowers_list[6])


# print("Last_value:", flowers_list[-1])

# print("first_three_values:", flowers_list[:3], "last_two_values:", flowers_list[-2:])

flowers_list.remove("monkshood")

# print(flowers_list)

# flowers_list.append("black_rose")

# print(flowers_list)


hardcover_sales = [139, 128, 172, 139, 191, 168, 170]

# print(len(hardcover_sales))
# print(min(hardcover_sales))
# print(max(hardcover_sales))

# print(sum(hardcover_sales[:5])/5)

# Question 1

menu = ['stewed meat with onions', 'bean soup', 'risotto with trout and shrimp','fish soup with cream and onion', 'gyro']

menu.remove('bean soup')
# print(menu)

menu.append('roasted beet salad')
# print(menu)


# Question 2

num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159,
                 141, 148, 132, 147, 168, 153, 170, 161, 148, 152,
                 141, 151, 131, 149, 164, 163, 143, 143, 166, 171]

avg_first_seven = sum(num_customers[:7])/7
avg_last_seven = sum(num_customers[-7:])/7
max_month = max(num_customers)
min_month = min(num_customers)

# print(avg_first_seven)
# print(avg_last_seven)
# print(max_month)
# print(min_month)

# Question 3

flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"

# print(flowers.split(","))

# alphabet = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z"

# print(alphabet.split("."))

address = "Mr. H. Potter,The cupboard under the Stairs,4 Privet Drive,Little Whinging,Surrey"
# print(address.split(","))

alphabet = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

alphabet_x = [x==10 for x in alphabet]
# print(alphabet_x)

ratings = [1, 2, 3, 4, 5, 4, 5, 1]
def percentage_liked(ratings):
    people_liked = [x>=4 for x in ratings]
    percentage_liked = (people_liked.count(True) / len(ratings))
    return percentage_liked

# print(percentage_liked(ratings))


# Question 5

num_users = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]

def percentage_growth(num_users, yrs_ago):
    growth = ((num_users[len(num_users)-1]) - (num_users[len(num_users) - yrs_ago - 1])) / (num_users[len(num_users) - yrs_ago - 1])
    return growth

# print(percentage_growth(num_users, 10))
