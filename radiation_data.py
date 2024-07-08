# Initial radiation data values for five locations
City_Center = [22, 16, 20, 31, 28]
Industrial_Zone = [35, 32, 30, 37, 40]
Residential_District = [15, 12, 18, 20, 14]
Rural_Outskirts = [9, 13, 16, 14, 7]
Downtown = [25, 18, 22, 21, 26]


# define the function to calculate the average radiation of a location
def avg_radiation(location):
    total_sum = 0
    for value in range(len(location)):
        total_sum += location[value]
    avg = total_sum / len(location)
    return avg


# define the function to calculate the standard deviation of the radiation of a location
def std_dev_radiation(location):
    std_dev_sum = 0
    for value in range(len(location)):
        std_dev_sum += (location[value] - avg_radiation(location)) ** 2
    std_dev = (std_dev_sum / len(location)) ** 0.5
    return std_dev

# create a dictionary for the locations to allow easy checking for if a user input is valid


locations = {
    "City_Center": City_Center,
    "Industrial_Zone": Industrial_Zone,
    "Residential_District": Residential_District,
    "Rural_Outskirts": Rural_Outskirts,
    "Downtown": Downtown
}

# create a function to get the location wanted from a user

def get_location():
    location_name = input("Choose one of: City_Center, Industrial_Zone, Residential_District, Rural_Outskirts, Downtown\n")
    if location_name in locations:
        return location_name
    else:
        print("Invalid location name. Try again.")
        return None

# creating a blank user input

user_input = ""

# creating the loop allowing infinite user inputs until the user chooses to end the inputs
# also give user the information as to what commands are valid

while user_input.lower() != "end this program":
    user_input = input("""Which of the following would you like to do for a location's radiation value:
                        Calculate Average
                        Calculate Standard Deviation 
                        See values
                        Add value
                        Remove value
                        End this program\n""")

# create the command to print the average radiation of a location based on the user command

    if user_input.lower() == "calculate average":
        location_name = get_location()
        if location_name:
            print("Average radiation:", avg_radiation(locations[location_name]))

# create the command to print the standard deviation of radiation of a location based on the user command

    elif user_input.lower() == "calculate standard deviation":
        location_name = get_location()
        if location_name:
            print("Standard deviation of radiation:", std_dev_radiation(locations[location_name]))

# create the command to show values for radiation of a location

    elif user_input.lower() == "see values":
        location_name = get_location()
        if location_name:
            print("Values:", locations[location_name])

    # create the command to add a value for radiation of a location

    elif user_input.lower() == "add value":
        location_name = get_location()
        if location_name:
            try:
                value_to_add = int(input("Enter the value to add: "))
                locations[location_name].append(value_to_add)
                print("Value added. Updated values:", locations[location_name])
            except ValueError:
                print("Invalid value. Please enter an integer.")

    # create the command to remove a value for radiation of a location

    elif user_input.lower() == "remove value":
        location_name = get_location()
        if location_name:
            try:
                value_to_remove = int(input("Enter the value to remove: "))
                if value_to_remove in locations[location_name]:
                    locations[location_name].remove(value_to_remove)
                    print("Value removed. Updated values:", locations[location_name])
                else:
                    print("Value not found in the list. Try again.")
            except ValueError:
                print("Invalid value. Please enter an integer.")

# create the command to terminate the program

    elif user_input.lower() == "end this program":
        print("Ending the program.")
        break

# ensure the user knows that they have entered an incorrect command

    else:
        print("Try again")
