

import csv

from matplotlib import pyplot


fd = open("data.csv", "r")

csv_data = csv.reader(fd, delimiter=',')

data = []

for row in csv_data:
    data.append(row)

data.pop(0)

print(data)




pyplot.plot(

    data,
    linestyle = "none",
    marker = "o",
    color = "green",
    markersize = 10,
    )



pyplot.xlim(0, 10)
pyplot.ylim(0, 10)
pyplot.title("Linear regression")

pyplot.show()





fd.close()
