import csv as csv
import numpy as np

csv_file = csv.reader(open('../data/train.csv', 'rb'))
header = csv_file.next()

data = []
for row in csv_file:
	data.append(row)
data = np.array(data)
print data

number_passengers = np.size(data[0::,1].astype(np.float))
number_survived = np.sum(data[0::,1].astype(np.int))
proportion_survivors = number_survived / number_passengers

women_only_stats = data[0::,4] == "female"
men_only_stats = data[0::,4] != "female"

women_onboard = data[women_only_stats,1].astype(np.float)
men_onboard = data[men_only_stats,1].astype(np.float)

proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)

print 'Proportion of women who survived is %s' % proportion_women_survived
print 'Proportion of men who survived is %s' % proportion_men_survived

test_file = csv.reader(open('../data/test.csv', 'rb'))
header = test_file.next()

prediction_file = csv.writer(open('../results/genderbasedmodel.csv', 'wb'))

prediction_file.writerow(["PassengerId", "Survived"])
for row in test_file:
	if row[3] == 'female':
		prediction_file.writerow([row[0], '1'])
	else:
		prediction_file.writerow([row[0], '0'])
prediction_file.close()