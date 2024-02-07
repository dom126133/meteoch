import pandas as pd
from datetime import datetime, timedelta

class Threshold_pc:
    def __init__(self, data):
        self.data = data
        self.begin_time = data['time'].min()
        self.end_time = data['time'].max()

    def begin_time(self):
        return self.begin_time

    def end_time(self):
        return self.end_time

    def _calculate(self, time, threshold):
        values = self.data.loc[(self.data['time'] >= time) & (self.data['time'] < time + timedelta(days=1))]
        
        tn = values.min()
        tx = values.max()
        tmean = values.mean()
        tmedian = values.median()
        
        # generate a dataframe containing min, max, mean and median
        # drop first row with iloc
        result = pd.concat([tn,tx,tmean,tmedian], axis=1).iloc[1:, :]
        result = result.rename(columns={0:'min', 1:'max', 2:'mean', 3:'median'})

        # Accessing all the values less than threshold 
        # counting them and return % value
        # count number of values and divide by the number of rows
        no_under_threshold = result.loc[result['min'] <= threshold, 'min'].count()
        no_total = result['min'].count()
        pc_tn = no_under_threshold / no_total *100
        return [f"{time:%Y-%m-%d}", f"{no_under_threshold}/{no_total}", f"{pc_tn:.0f} %"]

    def pc(self, threshold):
        time = self.begin_time
        result = []
        while time < self.end_time:
            result.append(self._calculate(time, threshold))
            time = time + timedelta(days=1)
        return result