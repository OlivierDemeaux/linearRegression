import csv
import sys

def error(err):
	print(err)
	sys.exit()

def gradientDescent(data):
	m = len(data['km'])
	theta0 = 0
	theta1 = 0
	learning_rate = 1
	cost = None
	old_cost = None
	while (old_cost is None or round(old_cost, 2) != round(cost, 2)):
		j = 0
		tmp0 = 0
		tmp1 = 0
		old_cost = cost
		cost = 0
		while (j < m):
			x = data['km'][j]
			y = data['price'][j]
			guess = theta1 * x + theta0
			cost += pow(guess - y, 2)
			tmp0 += guess - y
			tmp1 += (guess - y) * x
			j += 1
		cost *= (1 / float(2 * m))
		theta0 -= (1 / float(learning_rate)) * (1 / float(m)) * tmp0
		theta1 -= (1 / float(learning_rate)) * (1 / float(m)) * tmp1
		learning_rate += 1
	return (theta0, theta1)

def scale(data, min, max):
	i = 0
	div = float(max - min)
	if (div == 0):
		div = float(1)
	while (i < len(data['km'])):
	    data['km'][i] = (data['km'][i] - min) / div
	    i += 1
	return data

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        error('python train.py [file]')
    filename = sys.argv[1]
    km = []
    price = []
    data = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if (line_count != 0):
                km.append(int(row[0]))
                price.append(int(row[1]))
            line_count += 1
    data = {}
    data['km'] = km
    data['price'] = price
    if (len(data) < 1):
        error('No data in file')
    min = min(data['km'])
    max = max(data['km'])
    print(data)
    print(min)
    print(max)
    data = scale(data, min, max)
    t0, t1 = gradientDescent(data)
    print(t0)
    print(t1)
