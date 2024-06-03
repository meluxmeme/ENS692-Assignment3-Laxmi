# school_data.py
# AUTHOR NAME
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here


# You may add your own additional classes, functions, variables, etc.


def main():
    print("ENSF 692 School Enrollment Statistics")
    
   # print(data)
    # Print Stage 1 requirements here
    array1 = np.stack((year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022))
    reshapedArray = array1.reshape(10,20,3)

    CenSchool_grad_10 = reshapedArray[0:10, 0, 0]
    print(CenSchool_grad_10)
    print(CenSchool_grad_10.mean())

    CenSchool_grad_11 = reshapedArray[0:10, 0, 1]
    print(CenSchool_grad_11)
    print(CenSchool_grad_11.mean())
    
    CenSchool_grad_12 = reshapedArray[0:10, 0, 2]
    print(CenSchool_grad_12)
    print(CenSchool_grad_12.mean())
    
    # Prompt for user input
    #userData =input("Either enter school name or school code")

    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")


if __name__ == '__main__':
    main()

