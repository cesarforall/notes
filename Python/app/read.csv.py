import csv


def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        header = next(reader)
        # print(header)

        data = []

        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)

        print(data[2])
        return data


"""
    for row in reader:
      print('-' * 40)
      print(row)
"""


if __name__ == '__main__':
    read_csv('./app/world_population.csv')
