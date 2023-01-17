class SENSOR:
  def __init__(self,inputName,data):
    self.linkName = inputName
    self.values = data
  def Get_Value(self):
    return pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
