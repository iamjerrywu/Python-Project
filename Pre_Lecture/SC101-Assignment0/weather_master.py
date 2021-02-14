"""
File: weather_master.py
Name: sheng-hao wu
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment Handout.

"""

def main():
	input_temp_list = []
	cold_days = 0
	str_input_temp, int_input_temp = None, None
	quit_value = -100  # quit value can be customized

	print("stanCode \"Weather Master 4.0\"!")
	while int_input_temp != quit_value:
		# user enter temperature in string type
		str_input_temp = input("Next Temperature: (or " + str(quit_value) + " to quit)?")
		# error handling, check data's validness
		try:
			# those cannot be converted from string->integer, would be considered as invalid data type
			int(str_input_temp)
		except:
			# if invalid data type, re-enter data again and skip rest of processing code
			print("invalid temperature data, please enter again!")
			continue
		# convert to integger type
		int_input_temp = int(str_input_temp)
		# record temp except quit value, and record cold days as well
		if int_input_temp != -100:
			input_temp_list.append(int_input_temp)
			if int_input_temp < 16:
				cold_days += 1

	# print out highest / lowest / average temp. and cold days
	if len(input_temp_list) > 0:
		print("Highest temperature =", max(input_temp_list))
		print("Lowest temperature = ", min(input_temp_list))
		print("Average = ", sum(input_temp_list) / len(input_temp_list))
		print(cold_days, " colde day(s)")
	# if no valid temp. data, print this
	else:
		print("No temperatures were entered.")

###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
