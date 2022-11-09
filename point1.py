import csv
import os


def divide_data(file_name: str) -> None:
    """script that will split the original csv file into an X.csv and Y.csv file
    Args:
        file_name: Path to file
    Raises:
        TypeError: No such file exists
    """

    if os.path.exists(file_name):

        if not os.path.exists('divide_data_output'):
            os.mkdir('divide_data_output')

        with open(file_name, 'r', encoding='utf-8') as csvfile:
            reader_object = list(csv.reader(csvfile, delimiter=","))
            with open('divide_data_output//X.csv', 'w', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, lineterminator='\n')
                for elements in reader_object:
                    writer = csv.writer(csvfile, lineterminator='\n')
                    writer.writerow([str(elements[0])])
            with open('divide_data_output//Y.csv', 'w', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, lineterminator='\n')
                for elements in reader_object:
                    writer = csv.writer(csvfile, lineterminator='\n')
                    writer.writerow((
                        elements[1], elements[2], elements[3], elements[4], elements[5], elements[6],))
    else:
        raise FileNotFoundError

if __name__ == '__main__':
    try:
        file_name = 'dataset.csv'
        divide_data(file_name)

    except FileNotFoundError:
        print('No such file exists!')