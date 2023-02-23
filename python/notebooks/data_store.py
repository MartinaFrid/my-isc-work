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

    # def __init__(self):
    #     super().__init__() # for this class we 
      
    def add_measurement(self, date, value):
        """
        Add measurement to the accumulation

        :param date: Date of measurement
        :param value: Measurement value
        """

        self.times.append(date)
        
        last_measurement = 0

        # Get the last measurement if we already have some
        if self.measurements:
            last_measurement = self.measurements[-1]

        # add the accumulated value
        self.measurements.append(last_measurement + value)