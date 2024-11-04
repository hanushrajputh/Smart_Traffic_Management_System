class TrafficData:
    def __init__(self):
        """Initialize a traffic data storage."""
        self.data = {}

    def add_vehicle(self, vehicle_id, vehicle):
        """Add a vehicle to the traffic data."""
        self.data[vehicle_id] = vehicle

    def get_vehicle(self, vehicle_id):
        """Retrieve a vehicle by its ID."""
        return self.data.get(vehicle_id)
