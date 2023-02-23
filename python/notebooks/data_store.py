# encoding: utf-8


class DataStore:
    """
    Store of measurements and times
    """

    def __init__(self):
        self.times = []
        self.measurements = []

    def add_measurement(self, date, value):
        """
        Add the given value to the data store

        :param date: Date of the measurement
        :type date: str

        :param value: Value to add
        :type value: int or float
        """

        self.measurements.append(value)
        self.times.append(date)

    def print_measurements(self):
        """
        print the measurements and times
        """

        for time, value in zip(self.times, self.measurements):
            print(time, value)

    def get_max(self):
        """
        get the maximum value togtehr with the given timestep for tha value
        """
        
        return max(self.measurements)

    def get_min(self):
        """
        get the minimum value togtehr with the given timestep for tha value
        """
        
        return min(self.measurements)

    def get_mean(self):
        """
        get the mean value togtehr with the given timestep for tha value
        """
        mean = sum(self.measurements)/len(self.measurements)
        
        return mean

class TemperatureStore(DataStore):

    def add_measurement(self, date, value):
        
        # convert to kelvin
        value += 272.15
        
        self.measurements.append(value)
        self.times.append(date)

class AccumulatingStore(DataStore):

    def __init__(self):
        super().__init__()
        self.accumulation = []
      
    def add_measurement(self, date, value):

        super().add_measurement(date, value)

        # set a 0 value for the case where this is the first measurement
        last_acc = 0

        # Get the last accumulated value if we already have some
        if self.accumulation:
            last_acc = self.accumulation[-1]

            # add the accumulated value
            self.accumulation.append(last_acc + value)