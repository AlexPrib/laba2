import csv
import os


class Iter:
    def __init__(self):

        self.counter = 0
        self.file_name = "dataset.csv"

    def __next__(self) -> tuple:

        if os.path.exists(self.file_name):
            with open(self.file_name, "r", encoding="utf-8") as csvfile:
                arr = list(csv.reader(csvfile, delimiter=","))

                if self.counter == len(arr):
                    raise StopIteration

                elif self.counter < len(arr):
                    self.counter += 1
                    output = (
                        arr[self.counter - 1][0],
                        arr[self.counter - 1][1],
                        arr[self.counter - 1][2],
                        arr[self.counter - 1][3],
                        arr[self.counter - 1][4],
                        arr[self.counter - 1][5],
                        arr[self.counter - 1][6],
                    )
                    return output
        else:
            raise FileNotFoundError


class YXiter:
    def __init__(self):

        self.counter = 0
        self.X = "divide_data_output//X.csv"
        self.Y = "divide_data_output//Y.csv"

    def __next__(self) -> tuple:

        if os.path.exists(self.X) and os.path.exists(self.Y):

            with open(self.X, "r", encoding="utf-8") as csvfile:
                arr = list(csv.reader(csvfile, delimiter=","))

            if self.counter == len(arr):
                raise StopIteration

            elif self.counter < len(arr):
                self.counter += 1
                with open(self.X, "r", encoding="utf-8") as csvfilex:

                    arr_x = list(csv.reader(csvfilex, delimiter=","))
                    date = arr_x[self.counter][0]

                with open(self.Y, "r", encoding="utf-8") as csvfiley:

                    arr_y = list(csv.reader(csvfiley, delimiter=","))
                    output = (
                        date,
                        arr_y[self.counter - 1][0],
                        arr_y[self.counter - 1][1],
                        arr_y[self.counter - 1][2],
                        arr_y[self.counter - 1][3],
                        arr_y[self.counter - 1][4],
                        arr_y[self.counter - 1][5],
                    )
                    return output
            else:
                raise FileNotFoundError


class WeekIter:
    def __init__(self):

        self.file_name = "data_to_weeks_output"
        self.counter = 0
        self.data = []

        if os.path.exists(self.file_name):

            for root, dirs, files in os.walk(self.file_name):
                for file in files:

                    with open(
                        os.path.join(self.file_name, file), "r", encoding="utf-8"
                    ) as csvfile:
                        dates = list(csv.reader(csvfile, delimiter=","))

                        for i in range(len(dates)):
                            self.data.append(dates[i])
        else:
            raise FileNotFoundError

    def __next__(self) -> tuple:

        if self.counter == len(self.data):
            raise StopIteration

        elif self.counter < len(self.data):
            self.counter += 1
            output = (
                self.data[self.counter - 1][0],
                self.data[self.counter - 1][1],
                self.data[self.counter - 1][2],
                self.data[self.counter - 1][3],
                self.data[self.counter - 1][4],
                self.data[self.counter - 1][5],
                self.data[self.counter - 1][6],
            )
            return output


class YearIter:
    def __init__(self):

        self.file_name = "data_to_years_output"
        self.counter = 0
        self.data = []

        if os.path.exists(self.file_name):

            for root, dirs, files in os.walk(self.file_name):
                for file in files:

                    with open(
                        os.path.join(self.file_name, file), "r", encoding="utf-8"
                    ) as csvfile:
                        dates = list(csv.reader(csvfile, delimiter=","))

                        for i in range(len(dates)):
                            self.data.append(dates[i])
        else:
            raise FileNotFoundError

    def __next__(self) -> tuple:

        if self.counter == len(self.data):
            raise StopIteration

        elif self.counter < len(self.data):
            self.counter += 1
            output = (
                self.data[self.counter - 1][0],
                self.data[self.counter - 1][1],
                self.data[self.counter - 1][2],
                self.data[self.counter - 1][3],
                self.data[self.counter - 1][4],
                self.data[self.counter - 1][5],
                self.data[self.counter - 1][6],
            )
            return output


obj = YearIter()
while True:
    print(next(obj))
