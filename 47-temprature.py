
def convertTemperature(celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """

        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00

        l=[Kelvin, Fahrenheit]

        return l


ans=convertTemperature(-40)
print(ans)