from abc import ABC, abstractmethod

class Vehicle:
    def __init__(self, vehicle_id, license_plate, owner_name):
        self._vehicle_id = vehicle_id
        self.__license_plate = license_plate  # private
        self.__owner_name = owner_name        # private

    def get_license_plate(self):
        return self.__license_plate

    def get_owner_name(self):
        return self.__owner_name

    def get_vehicle_id(self):
        return self._vehicle_id

    def display(self):
        print(f"Vehicle ID: {self._vehicle_id}")

    def calculate_parking_fee(self, hours):
        raise NotImplementedError("Override in subclass")

class Bike(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, helmet_required=True):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.helmet_required = helmet_required

    def display(self):
        print(f"Bike → ID: {self.get_vehicle_id()}, Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Helmet: {self.helmet_required}")

    def calculate_parking_fee(self, hours):
        return 20 * hours

class Car(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, seats=4):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.seats = seats

    def display(self):
        print(f"Car → ID: {self.get_vehicle_id()}, Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Seats: {self.seats}")

    def calculate_parking_fee(self, hours):
        return 50 * hours

class SUV(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, four_wheel_drive=True):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.four_wheel_drive = four_wheel_drive

    def display(self):
        print(f"SUV → ID: {self.get_vehicle_id()}, Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, 4WD: {self.four_wheel_drive}")

    def calculate_parking_fee(self, hours):
        return 70 * hours

class Truck(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, max_load_capacity=1000):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.max_load_capacity = max_load_capacity

    def display(self):
        print(f"Truck → ID: {self.get_vehicle_id()}, Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Max Load: {self.max_load_capacity} kg")

    def calculate_parking_fee(self, hours):
        return 100 * hours


class ParkingSpot:
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.__size = size  # private
        self.__occupied = False
        self.__vehicle = None

    def is_occupied(self):
        return self.__occupied

    def assign_vehicle(self, vehicle):
        if self.__occupied:
            return False

        # Size restrictions
        if isinstance(vehicle, Bike) and self.__size in ["S", "M", "L", "XL"]:
            pass
        elif isinstance(vehicle, Car) and self.__size in ["M", "L", "XL"]:
            pass
        elif isinstance(vehicle, SUV) and self.__size in ["L", "XL"]:
            pass
        elif isinstance(vehicle, Truck) and self.__size == "XL":
            pass
        else:
            return False

        self.__vehicle = vehicle
        self.__occupied = True
        return True

    def remove_vehicle(self):
        if not self.__occupied:
            return None
        vehicle = self.__vehicle
        self.__vehicle = None
        self.__occupied = False
        return vehicle

    def show_status(self):
        if self.__occupied:
            print(f"Spot {self.spot_id} ({self.__size}): Occupied by {type(self.__vehicle).__name__} ({self.__vehicle.get_license_plate()})")
        else:
            print(f"Spot {self.spot_id} ({self.__size}): Empty")

    def get_vehicle(self):
        return self.__vehicle

class ParkingLot:
    def __init__(self, name):
        self.name = name
        self.spots = []
        print(f"\nParking Lot '{self.name}' Created.")

    def add_spot(self, spot):
        self.spots.append(spot)

    def show_spots(self):
        print("\n--- Parking Spot Status ---")
        for spot in self.spots:
            spot.show_status()

    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if not spot.is_occupied() and spot.assign_vehicle(vehicle):
                print(f"{type(vehicle).__name__} parked in Spot {spot.spot_id}")
                return True
        print(f"No suitable spot found for {type(vehicle).__name__}")
        return False

    def unpark_vehicle(self, vehicle, hours):
        for spot in self.spots:
            if spot.get_vehicle() == vehicle:
                removed = spot.remove_vehicle()
                if removed:
                    fee = removed.calculate_parking_fee(hours)
                    print(f"\nUnparked {type(removed).__name__} ({removed.get_license_plate()}) from Spot {spot.spot_id}")
                    print(f"Parking Fee = ₹{fee}")

                    # Simulating payment (for demo purposes, always using CashPayment)
                    payment_method = CashPayment()
                    payment_method.process_payment(fee)

                    return True
        print("Vehicle not found in parking lot.")
        return False

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} in Cash.")

class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} using Card.")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via UPI.")


lot = ParkingLot("CityMall Parking")
lot.add_spot(ParkingSpot(1, "S"))
lot.add_spot(ParkingSpot(2, "M"))
lot.add_spot(ParkingSpot(3, "M"))
lot.add_spot(ParkingSpot(4, "L"))
lot.add_spot(ParkingSpot(5, "XL"))
bike1 = Bike("B101", "TS01AB1234", "Rahul", True)
car1 = Car("C201", "TS05CD5678", "Priya", 5)
suv1 = SUV("S301", "TS09EF9012", "Anjali", True)
truck1 = Truck("T401", "TS11XY4455", "Ravi", 12)
print("\n--- Display Vehicles ---")
for v in [bike1, car1, suv1, truck1]:
    v.display()
print("\n--- Parking Vehicles ---")
lot.park_vehicle(bike1)
lot.park_vehicle(car1)
lot.park_vehicle(suv1)
lot.park_vehicle(truck1)
lot.show_spots()
print("\n--- Unparking Car after 3 hours ---")
lot.unpark_vehicle(car1, hours=3)
lot.show_spots()
