import numpy
import matplotlib.pyplot
backLegSensorValues = numpy.load("data/data_file.npy")
matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.show()
print(backLegSensorValues)
