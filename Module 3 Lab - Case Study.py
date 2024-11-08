# Define a base class to represent any kind of vehicle
class Vehicle:
    def __init__(self, vehicle_type="car"):
        # Assume "car" as the default type of vehicle
        self.vehicle_type = vehicle_type

# Define a class specifically for cars (or other automobiles)
class Automobile(Vehicle):
    def __init__(self, manufacturing_year, brand, model_name, number_of_doors, roof_type):
        # Initialize the base class with the default vehicle type
        super().__init__()
        
        # Set up the details specific to the car
        self.manufacturing_year = manufacturing_year
        self.brand = brand
        self.model_name = model_name
        self.number_of_doors = number_of_doors
        self.roof_type = roof_type

    # Method to display all the information about the car
    def show_vehicle_info(self):
        print("\nHere are the details for your vehicle:")
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.manufacturing_year}")
        print(f"Make: {self.brand}")
        print(f"Model: {self.model_name}")
        print(f"Number of doors: {self.number_of_doors}")
        print(f"Type of roof: {self.roof_type}")
        print("\nThank you for sharing your car details with us!")

# Let's start the process of gathering details about the car
print("Hello! Let's gather some details about your car so we can document it properly.")

# Collect the car details from the user
year = input("First, what year was your car manufactured? (e.g., 2022): ")
make = input("Great! What brand or make is your car? (e.g., Toyota): ")
model = input("And the model name? (e.g., Corolla): ")
doors = input("How many doors does your car have? Please enter 2 or 4: ")
roof = input("Lastly, what type of roof does your car have? (solid or sun roof): ")

# Create an Automobile instance using the provided details
user_car = Automobile(year, make, model, doors, roof)

# Display the collected car information in a friendly way
user_car.show_vehicle_info()