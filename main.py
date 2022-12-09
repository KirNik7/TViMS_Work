import csv
import math
import numpy as np
import matplotlib.pyplot as plt


def read_csv(filename):
    with open(filename, 'r') as f:
        next(f)
        reader = csv.reader(f)
        return list(reader)


def write_csv(filename, data):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def sum_values(data):
    sum_values = 0
    for i in range(len(data)):
        sum_values += int(data[i][1])
    return sum_values


# building a histogram
def build_histogram(data, num_bins):
    plt.hist(data, num_bins)
    plt.show()


def main():
    data = read_csv('W9.csv')

    # sort data in ascending order
    data.sort(key=lambda x: int(x[1]))

    # find min and max
    min_value = int(data[0][1])
    max_value = int(data[-1][1])

    # find the range
    range_value = max_value - min_value

    # find the number of classes
    num_classes = int(1 + 3.3 * math.log10(len(data)))

    # find the class width
    class_width = range_value / num_classes

    # vector containing the midpoints of the grouping intervals
    midpoints = []
    for i in range(num_classes):
        midpoints.append(min_value + (class_width / 2) + (i * class_width))

    # calculation of the sample average
    sample_average = sum_values(data) / len(data)

    # calculation of median
    if len(data) % 2 == 0:
        median = (int(data[len(data) // 2][1]) + int(data[len(data) // 2 - 1][1])) / 2
    else:
        median = int(data[len(data) // 2][1])

    # calculation of sample variance
    sample_variance = np.var([int(x[1]) for x in data])

    # calculation of sample standard deviation
    sample_standard_deviation = np.std([int(x[1]) for x in data])

    # calculation of sample moment of 3 and 4 orders
    new_data = [i**3 for i in data]
    sample_moment_3 = sum_values(new_data) / len(new_data)
    new_data = [i**4 for i in data]
    sample_moment_4 = sum_values(new_data) / len(new_data)

    # calculation of selective excess
    selective_excess = sample_moment_3 / (sample_standard_deviation ** 3)

    # calculation of the coefficient of asymmetry
    coefficient_of_asymmetry = sample_moment_3 / (sample_standard_deviation ** 3)

    write_csv('W9_new.csv', data)

    print('Min: ', min_value)
    print('Max: ', max_value)
    print('Range: ', range_value)
    print('Number of classes: ', num_classes)
    print('Class width: ', class_width)
    print('Vector containing the midpoints of the grouping intervals:')
    for i in range(len(midpoints)):
        print(midpoints[i], end=' ')
    print()
    print('Sample average: ', sample_average)
    print('Median: ', median)
    print('Sample variance: ', sample_variance)
    print('Sample standard deviation: ', sample_standard_deviation)
    print('Sample moment of 3 orders: ', sample_moment_3)
    print('Sample moment of 4 orders: ', sample_moment_4)
    print('Selective excess: ', selective_excess)
    print('Coefficient of asymmetry: ', coefficient_of_asymmetry)

    build_histogram([int(x[1]) for x in data], num_classes)


if __name__ == '__main__':
    main()
