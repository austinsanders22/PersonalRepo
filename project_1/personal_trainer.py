# Packages - pandas was used for alternative script.
import random
import pandas as pd

class Athlete():
    """Class stores basic information on the user. Physical and health
    information is used for creating plans in other classes."""

    # Initializing function to start the user's profile.
    def __init__(self, name = "", age = '', height = '', weight = '',
    gender = ''):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender
        self.diet_goals = 'start'
        self.choose = 'start'
        self.health_goals = 'start'
        self.lifting_goals = 'start'
        self.activity = 'start'
        self.running_goals = 'start'

class Weights():
    """Class stores user's weightlifting goals and creates a personalized
    weightlifting plan."""

    # Initializing function to store user's lifting style.
    def __init__(self, lifting_goals = ''):
        self.trainingplan = lifting_goals

    # Controller function within the class.
    def weight_manage(self):
        Weights.train_plan(self)

    # Function creates lifting plan based on user input
    def train_plan(self):
        # Set training programs
        days = ['SUN', 'MON', 'TUES', 'WED', 'THURS', 'FRI', 'SAT']
        body_build = [['Rest', 'Push-Strength', 'Pull-Strength', 'Legs',
                       'Push-Hypertrophy', 'Pull-Hyptertophy', 'Legs'],
                      ['', 'Bench 5x5', 'Bent-over rows 4x8', 'Leg press 5x10',
                       'Mil Press 3x10', 'Wt Pull-ups 5x5', 'Squat 4x5'],
                      ['', 'Mil Press 4x8', '1-arm Rows 3x10','RDLs 4x10',
                      'Dec Bench 3x8', 'T-Bar Rows 3x12','1 Leg RDL 3x10'],
                      ['','DB Inc Bench', 'Pull-downs', '1 Leg Sqt',
                      'Chest Flies', 'Seated Rows', 'KB Swings'],
                      ['','Chest Flies', '1 Arm DB curls', 'KB Swings',
                      'Shoulder Flies', 'Hammer Curls', 'Calf Raises'],
                      ['', 'Tricep Exten', 'Hammer Curls', 'Calf raises',
                      'Tri Ext', '1 Arm DB curls', 'GDH']]

        power_lift = [['Rest', 'B Squat 5x5', 'Rest', 'F Squat 3x3', 'Rest',
                      'Deadlift 5x3', 'Rest'],
                      ['', 'Bench 5x5', '', 'Mil Press 5x5', '', 'B Squat 5x3', ''],
                      ['', 'Deadlift 3x3', '', 'RDLs 4x8', '','Bench 4x8', ''],
                      ['','1 Leg RDL', '',  'Dips', '', 'KB Swings', ''],
                      ['','DB Inc Bench', '', 'KB Swings', '', 'Pull-ups', ''],
                      ['', 'Core', '', 'Core', '', 'Core', '']]

        olympic_lift = [['Rest', 'Clean 3x3', 'Rest', 'Snatch 3x3', 'Rest',
                        'Clean/Jerk 5x3', 'Rest'],
                        ['', 'Snatch 3x3', '', 'Fr Squat 5x5', '', 'B Squat 5x3', ''],
                        ['', 'Push Press 5x5', '', 'Jerk 3x3', '','KB Snatch', ''],
                        ['','1 Leg RDL', '',  'Dips', '', 'KB Swings', ''],
                        ['','KB Swings', '', 'KB Swings', '', 'Pull-ups', ''],
                        ['', 'Core', '', 'Core', '', 'Core', '']]

        days_header = ("%-5s  %-20s %-20s  %-10s  %-20s %-20s  %-10s" %
                          (days[0],
                           days[1],
                           days[2],
                           days[3],
                           days[4],
                           days[5],
                           days[6]))

        # Creates plan based on user's weightlifting style
        if self.lifting_goals == '1':
            print("Your weekly bodybuilding split is below! Weight is not \
as important. Work low weights for high reps! You should leave the \
gym with a massive pump every day!")
            print(days_header)
            print('-' * 120)
            for item in body_build:
                bodybuilding = ("%-5s  %-20s %-20s  %-15s  %-20s %-20s  %-10s" %
                                (item[0],
                                item[1],
                                item[2],
                                item[3],
                                item[4],
                                item[5],
                                item[6]))
                print(bodybuilding)
        if self.lifting_goals == '2':
            print("Your weekly power lift split is below! Build up in weight \
each week. Start light the first week and then add 5-10lbs every week after.")
            print(days_header)
            print('-' * 120)
            for item in power_lift:
                power = ("%-5s  %-20s %-20s  %-15s  %-20s %-20s  %-10s" %
                                (item[0],
                                item[1],
                                item[2],
                                item[3],
                                item[4],
                                item[5],
                                item[6]))
                print(power)
        if self.lifting_goals == '3':
            print("Your weekly olympic lift split is below! Build up in weight \
each week. Start light the first week and then add 5-10lbs every week after.")
            print(days_header)
            print('-' * 120)
            for item in olympic_lift:
                olym = ("%-5s  %-20s %-20s  %-15s  %-20s %-20s  %-10s" %
                                (item[0],
                                item[1],
                                item[2],
                                item[3],
                                item[4],
                                item[5],
                                item[6]))
                print(olym)
        next = 'baseline'
        while next != '':
            next = input("Your weightlifting plan is above! Press enter-key to go back to home: ")
        Journey.manage_profile(self)

class Cardio():
    """Class creates a running plan for the user and calculates their
    heart rate training zones."""

    # Initializing function to store user's running goals and age.
    def __init__(self, running_goals = '', age = 0):
        self.running_goals = running_goals
        self.age = age

    # Controller function within the class.
    def cardio_manage(self):
        car1 = input("Which aspect of cardio do you want to see "
        "(enter 1 or 2): \n1 - Running Plan \n2 - My Heart Rate Zones\n ")
        if car1 == "2":
            Cardio.HR_zones(self)
        if car1 == "1":
            Cardio.cardio_plan(self)

    # Function creates running plan based on user input
    def cardio_plan(self):
        # Set running programs
        days = ['WEEK','SUN', 'MON', 'TUES', 'WED', 'THURS', 'FRI', 'SAT']
        ten_k = [['1', 'Rest', '3 mi Z1/2', '8x400m', 'Rest', '3 mi Fast', 'Rest', '4 mi Z1/2'],
                        ['2', '', '3 mi Z1/2', '4x800m', '', '3 mi Fast', '', '5 mi Z1/2'],
                        ['3', '', '3 mi Z1/2', '8x400m', '', '4 mi Fast', '', '6 mi Z1/2'],
                        ['4', '', '3 mi Z1/2', '4x800m', '', '5 mi Fast', '', '7 mi Z1/2'],
                        ['5', '', '3 mi Z1/2', '8x400m', '', '6 mi Fast', '', '8 mi Z1/2'],
                        ['6', '', '3 mi Z1/2', '4x800m', '', '3 mi Z1/2', '', '6.2 mi Fast']]

        half_mar = [['1', 'Rest', '3 mi Z1/2', '8x400m', 'Rest', '4 mi Fast', 'Rest', '6 mi Z1/2'],
                        ['2', '', '4 mi Z1/2', '4x800m', '', '5 mi Fast', '', '8 mi Z1/2'],
                        ['3', '', '5 mi Z1/2', '10x400m', '', '5 mi Fast', '', '10 mi Z1/2'],
                        ['4', '', '6 mi Z1/2', '5x800m', '', '6 mi Fast', '', '12 mi Z1/2'],
                        ['5', '', '6 mi Z1/2', '12x400m', '', '6 mi Fast', '', '8 mi Z1/2'],
                        ['6', '', '3 mi Z1/2', 'Rest', '', '2 mi Z1/2', '', '13.1 mi Fast']]

        full_mar = [['1', 'Rest', '6 mi Z1/2', '4x800m', 'Rest', '6 mi Fast', 'Rest', '14 mi Z1/2'],
                        ['2', '', '8 mi Z1/2', '5x800m', '', '7 mi Fast', '', '16 mi Z1/2'],
                        ['3', '', '8 mi Z1/2', '6x800m', '', '8 mi Fast', '', '18 mi Z1/2'],
                        ['4', '', '8 mi Z1/2', '7x800m', '', '10 mi Fast', '', '20 mi Z1/1'],
                        ['5', '', '9 mi Z1/2', '8x800m', '', '8 mi Fast', '', '8 mi Z1/2'],
                        ['6', '', '3 mi Z1/2', 'Rest', '', '2 mi Z1/2', '', '26.2 mi Fast']]

        days_header = ("%-4s %-4s  %-20s %-20s  %-10s  %-20s %-20s  %-10s" %
                          (days[0],
                           days[1],
                           days[2],
                           days[3],
                           days[4],
                           days[5],
                           days[6],
                           days[7]))

         # Creates running plan based on user's running goal
        if self.running_goals == '1':
            print("Your 6-week 10K plan is below! This is a great \
beginner's plan.")
            print(days_header)
            print('-' * 120)
            for item in ten_k:
                ten = ("%-4s %-4s  %-20s %-20s  %-10s  %-20s %-20s  %-10s" %
                                (item[0],
                                item[1],
                                item[2],
                                item[3],
                                item[4],
                                item[5],
                                item[6],
                                item[7]))
                print(ten)
        if self.running_goals == '2':
            print("Your 6-week half-marathon plan is below! Ensure that you\
 feel comfortable running 6-7 miles before you start!")
            print(days_header)
            print('-' * 120)
            for item in half_mar:
                half = ("%-4s %-4s  %-20s %-20s  %-10s  %-20s %-20s  %-10s" %
                                (item[0],
                                item[1],
                                item[2],
                                item[3],
                                item[4],
                                item[5],
                                item[6],
                                item[7]))
                print(half)
        if self.running_goals == '3':
            print("Your 6-week marathon plan is below! You should be \
comfortable running up to 12 miles before starting this. Start with the \
10K and/or half-marathon plan first if you need to build up.")
            print(days_header)
            print('-' * 120)
            for item in full_mar:
                full = ("%-4s %-4s  %-20s %-20s  %-10s  %-20s %-20s  %-10s" %
                                (item[0],
                                item[1],
                                item[2],
                                item[3],
                                item[4],
                                item[5],
                                item[6],
                                item[7]))
                print(full)
        next = 'baseline'
        while next != '':
            next = input("Your running plan is above! Press enter-key to go back to home: ")
        Journey.manage_profile(self)

    # Function determines the heart rate training zones for the user.
    def HR_zones(self):
        self.max_HR = (220 - self.age)
        self.zone_one = "Zone 1: " + str(round(self.max_HR*.68)) + " - " +\
                        str(round(self.max_HR*.73))
        self.zone_two = "Zone 2: " + str(round(self.max_HR*.73)) + " - " +\
                        str(round(self.max_HR*.80))
        self.zone_three = "Zone 3: " + str(round(self.max_HR*.80)) + " - " +\
                        str(round(self.max_HR*.87))
        self.zone_four = "Zone 4: " + str(round(self.max_HR*.87)) + " - " +\
                        str(round(self.max_HR*.93))
        self.zone_five = "Zone 5: " + str(round(self.max_HR*.93)) + " - " +\
                        str(round(self.max_HR))
        self.HR_zones = [self.zone_one, self.zone_two, self.zone_three,\
                        self.zone_four, self.zone_five]
        print(*self.HR_zones, sep = "\n")
        next = 'baseline'
        while next != '':
            next = input("Your heart rate zones are above! Press enter-key to go back to home: ")
        Journey.manage_profile(self)

class Nutrition():
    """Class takes basic user information and creates a diet plan,
    calculates macros, and BMI."""

    # Initializing function to store user's basic info for calculating
    # nutrition plan.
    def __init__(self, age = 0, height = 0, weight = 0, diet = '', goals = ''):
        self.dietgoals = diet
        self.goals = goals
        self.height = height
        self.weight = weight
        self.age = age

    # Controller function within the class.
    def nutrition_manage(self):
        nutr = input("What do you want to see (enter 1, 2, or 3):"
        "\n1 - Diet Plan \n2 - Recommended Macros \n3 - BMI\n")
        if nutr == "1":
             Nutrition.diet_plan(self)
        if nutr == "2":
             Nutrition.calc_macros(self)
        if nutr == "3":
             Nutrition.bmi_calc(self)

    # Function lists information about the user selected diet.
    def diet_plan(self):
        self.keto = "The ketogenic diet a high-fat, high-protein, low-carbohydrate \
diet that forces the body to burn fat for an energy source as oppposed to \
carbohydrates. When your body consumes high amounts of fats and low amounts of \
carbohyrdrates, your body goes into a process call ketosis. During ketosis, \
fatty acids replace glucose as your body's fueling source. Ignore your macros - \
ensure you eat less than 50 grams of carbohyrates a day. Here are the main \
components of a Keto diet: \nMeat\nEggs\nCheese\nSeafood\nNuts\nLow-Carb Veggies\n"
        self.paleo = "The paleo diet is an all natural, whole-food diet designed \
to make humans eat diets similar to humans of the hunter and gatherer ages. The \
diet is supposed to simulate a diet that the human body is evolved to eat. The \
diet is composed of foods of the earth and limits processed and artifical foods.\
\nFollow your macros and eat these foods:\
\nMeat\nEggs\nVegetables\nFruit\nNuts\nSeafood\n"
        self.flexible = "EAT WHATEVER YOU WANT. Just make sure your diet \
matches your macros count!"
        if self.diet_goals == '1':
            self.dietplan = self.paleo
        if self.diet_goals == '2':
            self.dietplan = self.keto
        if self.diet_goals == '3':
            self.dietplan = self.flexible
        print(self.dietplan)
        next = 'baseline'
        while next != '':
            next = input("Your diet plan is above! Press enter-key to go back to home: ")
        Journey.manage_profile(self)

    # Function calculates the user's BMI.
    def bmi_calc(self):
        self.weight_kg = self.weight*.4536
        self.height_m = self.height*.0254
        self.BMI = round(self.weight_kg/(self.height_m**2))
        print("BMI: ", self.BMI)
        next = 'baseline'
        while next != '':
            next = input("Your BMI is above! BMI is an outdated metric "
            "for evaluating physical health. Find a bod pod or other body "
            "fat measuring system to get a better idea of your muscle to "
            "fat ratio. Press enter-key to go back to home: ")
        Journey.manage_profile(self)

    # Function calculates the user's daily macros based on height, weight,
    # age, goals, and activity level.
    def calc_macros(self):
        self.BMR = 655 + (4.35*self.weight) + (4.7*self.height) - (4.7-self.age)
        if self.activity == '1':
            self.activity_adj = 1.2
        if self.activity == '2':
            self.activity_adj = 1.375
        if self.activity == '3':
            self.activity_adj = 1.55
        if self.activity == '4':
            self.activity_adj = 1.725
        self.calories = self.BMR * self.activity_adj
        if self.health_goals == '1':
            self.calories -= self.calories*.2
            self.macro_plan = [.2, .42, .38]
        elif self.health_goals == '2':
            self.calories += self.calories*.1
            self.macro_plan = [.3, .4, .3]
        elif self.health_goals == '3':
            self.macro_plan = [.25, .5, .25]
        self.fat = (self.macro_plan[0]*self.calories)/9
        self.carbs = (self.macro_plan[1]*self.calories)/4
        self.protein = (self.macro_plan[2]*self.calories)/4
        self.macros = ["Grams of fat: " + str(round(self.fat)),
        "Grams of carbohydrates: " + str(round(self.carbs)),
        "Grams of protein: " + str(round(self.protein))]
        print(*self.macros, sep="\n")
        print("Consume this ratio of macronutrients! Don't forget that \
alcohol counts. Every 4 calories of alcohol should count as 1 carb gram.")
        print("Total number of calories: ", round(self.calories))
        next = 'baseline'
        while next != '':
            next = input("Your macros are above! Press enter-key to go back to home: ")
        Journey.manage_profile(self)

class Recovery():
    """Class provides recommendations to user on sleep and
    recovery activities."""

    # Controller function within the class.
    def recov_manage(self):
        recov = input("What would you like to see (enter 1 or 2):"
        "\n1 - Sleep Plan \n2 - Rehab Plan\n")
        if recov == '1':
            Recovery.sleep_plan(self)
        if recov == '2':
            Recovery.rehab_plan(self)

    def sleep_plan(self):
        self.sleepplan = "I recommend getting 7-9 hours of sleep every night. \
Avoid the following within 2 hours of sleep:\nalcohol \ntobacco \ncaffeine \nsugar\
\nblue light \n\nReading and stretching before bed will enhance sleep and \
optimize recovery."
        print(self.sleepplan)
        next = 'baseline'
        while next != '':
            next = input("Your sleep recommendations are above! Press enter-key to go back to home: ")
        Journey.manage_profile(self)

    def rehab_plan(self):
        self.rehabplan = "Incorporate 1 of the followings activities 3-5 times \
a week: \n30 minutes of yoga \n30 minutes of stretching \n60 minutedeep tissue \
massage\n"
        print(self.rehabplan)
        next = 'baseline'
        while next != '':
            next = input("Your rehab plan is above! Press enter-key to go back to home: ")
        Journey.manage_profile(self)

class Buddy():
    """Class helps find the user a training partner."""

    # Function allows user to select a training partner or get one at random.
    def pick_buddy(self):
        buddies = ["Arnold Schwarzenegger", "Eddie Hall", "Fitness Marshall",
         "Thor", "Matt Fraser", "Tia-Clair Toomey", \
                   "Katrin Davidsdottir"]
        bud = input("Do you want to (enter 1 or 2): "
        "\n1 - Pick your training partner\n2 - Get a training partner at random\n")
        if bud == '1':
            print(*buddies, sep="\n")
            pick = input("Who do you select?\n")
            if pick not in buddies:
                print("Sorry! You spelled the name incorrectly. You get a "
                "random training partner.")
                self.randbud = random.randint(0, len(buddies)-1)
                self.buddy = buddies[self.randbud]
            else:
                self.buddy = buddies[(buddies.index(pick))]
        if bud == '2':
            self.randbud = random.randint(0, len(buddies)-1)
            self.buddy = buddies[self.randbud]
        print("It is time to get to work! You have a beast of a partner.",
        self.buddy, "is ready to put you through the gauntlet!")
        next = 'baseline'
        while next != '':
            next = input("Your workout buddy is above! Press enter-key to go back to home: ")
        Journey.manage_profile(self)

class Journey():
    """Managing class for the entire program."""

    # Function collects basic user info that will remain in place for
    # entire program.
    def collect_health(self):
        print("Hello! Welcome to the Virtual Personal Trainer (VPT)!")
        print("Our goal is to be your one stop shop for all your fitness needs.")
        print("Please start by entering your basic information and answering a few questions.")
        print("We will create a physical baseline first and then you can manage your profile.")
        self.name = input("What is your name? ")
        while self.age.isnumeric() == False:
            self.age = input("What is your age? ")
            if self.age.isnumeric() == False:
                print("Please input your age numerically!!!")
        self.age = int(self.age)
        while self.height.isnumeric() == False:
            self.height = input("How tall are you? (in inches) ")
            if self.height.isnumeric() == False:
                print("Please input your height in inches as a number!!!")
        self.height = int(self.height)
        while self.weight.isnumeric() == False:
            self.weight = input("How much do you weigh? (in pounds) ")
            if self.weight.isnumeric() == False:
                print("Please input your weight in pounds as a number!!!")
        self.weight = int(self.weight)
        Journey.profile_info(self)

    # Function runs through the user's profile and allows them to input
    # their goals and desired types of training.
    # After the user inputs information, the user can explore their plans
    # in the other classes.
    # Once the user returns, if the user wants to change profile, they will be
    # diverted to this function to updated training preferences.
    def profile_info(self):
        self.diet_goals = 'start'
        self.choose = 'start'
        self.health_goals = 'start'
        self.lifting_goals = 'start'
        self.activity = 'start'
        self.running_goals = 'start'
        while self.lifting_goals not in {"1", "2", "3"}:
            self.lifting_goals = input("Which weightlifting style do you enjoy"
            " \n(enter 1, 2, or 3): \n1 - Bodybuilding  \n2 - Powerlifting"
            " \n3 - Olympic lifting \n")
            if self.lifting_goals not in {"1", "2", "3"}:
                print("Please enter a valid response (1, 2, or 3)")
        while self.activity not in {"1", "2", "3", "4"}:
            self.activity = input("How many days a week do you currently "
            "conduct heavy, strenuous exercise \n(enter 1, 2, 3, or 4):"
            " \n1 - 0-1 Days \n2 - 2-3 Days \n3 - 4-5 Days \n4 - 6-7 Days\n")
            if self.activity not in {"1", "2", "3", "4"}:
                print("Please enter a valid response (1, 2, 3, or 4)")
        while self.running_goals not in {"1", "2", "3"}:
            self.running_goals = input("What's your goal running distance "
            "\n(enter 1, 2, or 3): \n1 - 6.2 miles \n2 - 13.1 miles "
            "\n3 - 26.2 miles\n")
            if self.running_goals not in {"1", "2", "3"}:
                print("Please enter a valid response (1, 2, or 3)")
        while self.health_goals not in {"1", "2", "3"}:
            self.health_goals = input("What are your health goals"
            "\n(enter 1, 2, or 3):\n1 - Cut fat\n2 - Gain Mass\n3 - Perform\n")
            if self.health_goals not in {"1", "2", "3"}:
                print("Please enter a valid response (1, 2, or 3)")
        while self.diet_goals not in {"1", "2", "3"}:
            self.diet_goals = input("What kind of diet do you want to follow "
            "\n(enter 1, 2, or 3): \n1 - Paleo\n2 - Keto\n3 - Flexible\n")
            if self.diet_goals not in {"1", "2", "3"}:
                print("Please enter a valid response (1, 2, or 3)")
        self.choose = "start"
        while self.choose not in {"1", "2", "3", "4", "5", "quit", "6"}:
            self.choose = input("Congrats! We have created a weightlifting, "
            "running, and nutrition plan based on your information and goals!"
            "\nWhich plans would you like to explore "
            "\n(enter 1, 2, 3, 4, 5, 6, or 'quit' to end program):"
            "\n1 - Weightlifting \n2 - Cardio \n3 - Nutrition \n4 - Recovery"
            "\n5 - Training Buddy\n6 - Change Profile\n")
            if self.choose == "1":
                Weights.weight_manage(self)
            if self.choose == "2":
                Cardio.cardio_manage(self)
            if self.choose == "3":
                Nutrition.nutrition_manage(self)
            if self.choose == "4":
                Recovery.recov_manage(self)
            if self.choose == "5":
                Buddy.pick_buddy(self)
            if self.choose == "6":
                Journey.profile_info(self)
            if self.choose not in {"1", "2", "3", "4", "5", "6", "quit"}:
                print("Please enter one of the following numbers as a response "
                "- 1, 2, 3, 4, 5, 6, or quit")

    # Function helps the user determine what they want to look at next in the
    # program.
    # User has option to quit or change profile information.
    def manage_profile(self):
        self.choose = "start"
        while self.choose not in {"1", "2", "3", "4", "5", "quit", "6"}:
            self.choose = input("Which plans would you like to explore next "
            "(enter 1, 2, 3, 4, 5, 6, or 'quit' to end program):"
            "\n1 - Weightlifting \n2 - Cardio \n3 - Nutrition \n4 - Recovery"
            "\n5 - Training Buddy\n6 - Change Profile Information\n")
            if self.choose == "1":
                Weights.weight_manage(self)
            if self.choose == "2":
                Cardio.cardio_manage(self)
            if self.choose == "3":
                Nutrition.nutrition_manage(self)
            if self.choose == "4":
                Recovery.recov_manage(self)
            if self.choose == "5":
                Buddy.pick_buddy(self)
            if self.choose == "6":
                Journey.profile_info(self)
            if self.choose not in {"1", "2", "3", "4", "5","6", "quit"}:
                print("Please enter one of the following numbers as a "
                "response - 1, 2, 3, 4, 5, 6, or 'quit'")

## Runs the script from command line.
me = Athlete()
Journey.collect_health(me)
