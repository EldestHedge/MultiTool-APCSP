def TempConverter():
	def TemperatureScript():
		print ("[1] Know Celsius, Find Fahrenheit")
		print ("[2] Know Celsius, Find Kelvin")
		print ("[3] Know Fahrenheit, Find Celsius")
		print ("[4] Know Fahrenheit, Find Kelvin")
		print ("[5] Know Kelvin, Find Celsius")
		print ("[6] Know Kelvin, Find Fahrenheit")
		print ("[7] Back to Main Menu")

	TemperatureScript()
	print ("")
	
	TempInput = int(input("Select an option: "))

	if TempInput == 1:
		#insert Celsius to Fahrenheit
		CTemp = float(input("Degrees Celsius: "))
		Far = CTemp * 1.8 + 32

		print (str(CTemp) + " degrees Celsius = " + str(Far) + " degrees Fahrenheit")
		
	if TempInput == 2:
		#insert Celsius to Kelvin
		CTemp = float(input("Degrees Celsius: "))
		Kel = CTemp + 273.15

		print (str(CTemp) + " degrees Celsius = " + str(Kel) + " degrees Kelvin")

	if TempInput == 3:
		#insert Fahrenheit to Celsius
		FTemp = float(input("Degrees Fahrenheit: "))
		Cel = (FTemp - 32) / 1.8

		print (str(FTemp) + " degrees Fahrenheit = " + str(Cel) + " degrees Celsius")

	if TempInput == 4:
		#insert Fahrenheit to Kelvin
		FTemp = float(input("Degrees Fahrenheit: "))
		Kel = (FTemp + 495.67) * (5/9)

		print (str(FTemp) + " degrees Fahrenheit = " + str(Kel) + " degrees Kelvin")

	if TempInput == 5:
		#insert Kelvin to Celsius
		KTemp = float(input("Degrees Kelvin: "))
		Cel = KTemp - 273.15
		
		print (str(KTemp) + " degrees Kelvin = " + str(Cel) + " degrees Celsius")

	if TempInput == 6:
		#insert Kelvin to Fahrenheit
		KTemp = float(input("Degrees Kelvin: "))
		Far = KTemp * 1.8 - 495.67

		print (str(KTemp) + " degrees Kelvin = " + str(Far) + " degrees Fahrenheit")

	if TempInput == 7:
		#BackButton
		os.system('cls')
        Main()
        MainMenu.MMenu()


TempConverter()