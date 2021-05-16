class flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passenger= []
    def add_passenger(self,name):
        if not self.open_seats():
            return False
        self.passenger.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passenger)

flight=flight(2)

people=["minkle","sachin","suraj","prabal"]
for person in people:
        success= flight.add_passenger(person)
        if success:
            print(f"add {person} to flight succesfully.")
        else:
            print(f"no available seats for that {person}")

