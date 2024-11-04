class Vehicle:
    def __init__(self, vehicle_id, location):
        """Initialize a vehicle with an ID and initial location."""
        self.vehicle_id = vehicle_id
        self.location = location

    def move(self, new_location):
        """Move the vehicle to a new location."""
        self.location = new_location
