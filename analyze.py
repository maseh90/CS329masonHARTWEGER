import numpy
import matplotlib.pyplot
targetAngles = numpy.load("data/targetAngles.npy")
backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
matplotlib.pyplot.plot(backLegSensorValues,linewidth=4)
matplotlib.pyplot.plot(frontLegSensorValues)
matplotlib.pyplot.plot(targetAngles)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
print(backLegSensorValues)
