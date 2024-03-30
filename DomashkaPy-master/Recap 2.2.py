import os
from pathlib import Path


class NoData(Exception):
    pass


class DataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.filename = Path(file_path).name
        self.data = self._read_data()

    def _read_data(self):
        with open(self.file_path, 'r') as file:
            data = file.read().strip().split(',')
            if not data:
                raise NoData("The file contains no data")
            return list(map(float, data))

    def total_samples(self):
        return len(self.data)

    def average(self):
        return sum(self.data) / len(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else:
            return sorted_data[n // 2]

    def max_value(self):
        return max(self.data)

    def min_value(self):
        return min(self.data)

    def create_report(self):
        report = f"Report for {self.filename}\n"
        report += f"samples: {self.total_samples()}\n"
        report += f"average: {self.average():.2f}\n"
        report += f"median: {self.median():.2f}\n"
        report += f"max: {self.max_value():.2f}\n"
        report += f"min: {self.min_value():.2f}"
        return report



data_file = "random_data.txt"
da = DataAnalyzer(data_file)

report = da.create_report()
print(report)

assert da.total_samples() == 20
assert da.average() == 49.35
assert da.median() == 47.5
assert da.max_value() == 94
assert da.min_value() == 4

report = da.create_report()
print(report)

expected_report = (
    "Report for random_data.txt\n"
    "samples: 20\n"
    "average: 49.35\n"
    "median: 47.50\n"
    "max: 94.00\n"
    "min: 4.00"
)
assert report == expected_report