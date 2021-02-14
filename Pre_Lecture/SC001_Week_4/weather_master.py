"""
File: weather_master.py
Name: Sheng-Hao Wu
-------------------------------
This file belongs to SC101 pre-lecture assignment problem1
Description: Design a weather forecaster capable of processing temp. data
    - input: temp. data ( or "quit_value(-100) to exit)"
    - output:
        if valid datas entered, show:
            1. highest temp.
            2. lowest temp.
            3. average temp,
            4. cold days amount (<16C temp.)
        else
            show:"no temperatures were entered"
"""
def weather():
    input_temp_list = []
    cold_days = 0
    str_input_temp, int_input_temp = None, None
    quit_value = -100  # quit value can be customized

    print("stanCode \"Weather Master 4.0\"!")
    while int_input_temp!=quit_value:
        # user enter temperature in string type
        str_input_temp = input("Next Temperature: (or " + str(quit_value) + " to quit)?")
        # error handling, check data's validness
        try:
            #those cannot be converted from string->integer, would be considered as invalid data type
            int(str_input_temp)
        except:
            #if invalid data type, re-enter data again and skip rest of processing code
            print("invalid temperature data, please enter again!")
            continue
        #convert to integger type
        int_input_temp = int(str_input_temp)
        # record temp except quit value, and record cold days as well
        if int_input_temp != -100:
            input_temp_list.append(int_input_temp)
            if int_input_temp < 16:
                cold_days+=1

    # print out highest / lowest / average temp. and cold days
    if len(input_temp_list) > 0:
        print("Highest temperature =", max(input_temp_list))
        print("Lowest temperature = ", min(input_temp_list))
        print("Average = ", sum(input_temp_list)/len(input_temp_list))
        print(cold_days," colde day(s)")
    #if no valid temp. data, print this
    else:
        print("No temperatures were entered.")

weather()

