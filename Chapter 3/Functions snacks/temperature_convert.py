def temperature_converter(temp_value, unit = 'C', threshold = 0):
	if unit == 'C':
		converted_temp_value = (temp_value * 9/5) + 32
	else:
		converted_temp_value = (temp_value - 32) * 5/9

	if converted_temp_value > threshold:
		return "Cold advisory"
	else:
		return "Heat alert"

print(temperature_converter(35, 'C', 180))
 