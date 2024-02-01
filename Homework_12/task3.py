class Bus:
    def __init__(self, speed, max_seating_capacity, max_speed):
        self.speed = speed
        self.max_seating_capacity = max_seating_capacity
        self.max_speed = max_speed
        self.passenger_list = []
        self.available_seats = max_seating_capacity
        self.seats_in_bus = {}

    def embark(self, *passengers):
        for passenger in passengers:
            if self.available_seats > 0:
                self.passenger_list.append(passenger)
                self.seats_in_bus[self.max_seating_capacity - self.available_seats + 1] = passenger
                self.available_seats -= 1
            else:
                print("No available seats on the bus.")

    def disembark(self, *passengers):
        for passenger in passengers:
            removed_passengers = [p for p in self.passenger_list if p == passenger]
            if removed_passengers:
                for p in removed_passengers:
                    self.passenger_list.remove(p)
                    seat = list(self.seats_in_bus.keys())[list(self.seats_in_bus.values()).index(p)]
                    self.seats_in_bus.pop(seat, None)
                    self.available_seats += 1
                self._update_seats_in_bus()
            else:
                print(f"Passenger {passenger} not found on the bus.")

    def _update_seats_in_bus(self):
        self.seats_in_bus = {i + 1: passenger for i, passenger in enumerate(self.passenger_list)}

    def increase_speed(self, value):
        self.speed = min(self.speed + value, self.max_speed)

    def decrease_speed(self, value):
        self.speed = max(self.speed - value, 0)

    def __contains__(self, passenger):
        return passenger in self.passenger_list

    def __iadd__(self, passenger):
        self.embark(passenger)
        return self

    def __isub__(self, passenger):
        self.disembark(passenger)
        return self


if __name__ == "__main__":
    bus = Bus(60, 3, 80)
    bus.embark("Ivanov", "Petrov", "Ivanov")
    print(bus.passenger_list)
    print(bus.available_seats)
    print(bus.seats_in_bus)

    bus.disembark("Ivanov")
    print(bus.passenger_list)
    print(bus.available_seats)
    print(bus.seats_in_bus)

    bus.increase_speed(20)
    print(bus.speed)

    bus.decrease_speed(50)
    print(bus.speed)

    name = "Ivanov"
    if name in bus:
        print(f"{name} is on the bus")
    else:
        print("Passenger not found")

    bus += "Smirnov"
    print(bus.passenger_list)
    print(bus.seats_in_bus)
    bus -= "Ivanov"
    print(bus.passenger_list)
    print(bus.seats_in_bus)
