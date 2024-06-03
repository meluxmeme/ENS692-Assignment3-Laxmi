# school_data.py
# AUTHOR NAME
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022
## Declare any global variables needed to store the data here


# You may add your own additional classes, functions, variables, etc.


def main():
    print("ENSF 692 School Enrollment Statistics")
    
   
    # Print Stage 1 requirements here
    array1 = np.stack((year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022))
    reshapedArray = array1.reshape(10,20,3)
    school_name ={
        1224: 'Centennial High School',
        1679: 'Robert Thirsk School',
        9626: 'Louise Dean School',
        9806: 'Queen Elizabeth High School',
        9813: 'Forest Lawn High School',
        9815: 'Crescent Heights High School',
        9816: 'Western Canada High School',
        9823: 'Central Memorial High School',
        9825: 'James Fowler High School',
        9826: 'Ernest Manning High School',
        9829: 'William Aberhart High School',
        9830: 'National Sport School',
        9836: 'Henry Wise Wood High School',
        9847: 'Bowness High School',
        9850: 'Lord Beaverbrook High School',
        9856: 'Jack James High School',
        9857: 'Sir Winston Churchill High School',
        9858: 'Dr. E. P. Scarlett High School',
        9860: 'John G Diefenbaker High School',
        9865: 'Lester B. Pearson High School'
    }
    schoolcode =[school_name.keys()]
    print(schoolcode)
    userdata = input("Enter school name or code")
    if userdata.isdigit() and int(userdata) in school_name:
       print(f"The school name for code {userdata} is {school_name[int(userdata)]}")
       indexof =list(school_name.keys()).index(int(userdata))
       #print(indexof)
       # userdata.index()
    #    schoolcode =[school_name.keys()]
    #    print(schoolcode)
    elif userdata in school_name.values():
        print(f"The code for school {userdata} is {list(school_name.keys())[list(school_name.values()).index(userdata)]}")
    else:
        print("School or code not found.")



    grad_10_mean = np.mean(reshapedArray[0:10, indexof, 0])
    print("Mean enrollment for Grade 10 across all years " + str( grad_10_mean))

    grad_11_mean = np.mean(reshapedArray[0:10, indexof, 1])
    print("Mean enrollment for Grade 11 across all years " + str( grad_11_mean))

    grad_12_mean = np.mean(reshapedArray[0:10, indexof, 2])
    print("Mean enrollment for Grade 12 across all years" + str( grad_12_mean))
    
    highest_enrollment = np.max(reshapedArray[0:10, indexof, ::])
    print("Highest enrollment for a single grade within the entire time period :" + str(int(highest_enrollment)))
    

    lowest_enrollment = np.min(reshapedArray[0:10, indexof, ::])
    print("Highest enrollment for a single grade within the entire time period :" + str(int(lowest_enrollment)))


   
    print("Total enrollment for 2013 : " + str(int(np.sum(reshapedArray[0, indexof, ::]))) )
    print("Total enrollment for 2014 : " + str(int(np.sum(reshapedArray[1, indexof, ::]))))
    print("Total enrollment for 2015 : " + str(int(np.sum(reshapedArray[2, indexof, ::])) ))
    print("Total enrollment for 2016 : " + str(int(np.sum(reshapedArray[3, indexof, ::])) ))
    print("Total enrollment for 2017 : " + str(int(np.sum(reshapedArray[4, indexof, ::])) ))
    print("Total enrollment for 2018 : " + str(int(np.sum(reshapedArray[5, indexof, ::])) ))
    print("Total enrollment for 2019 : " + str(int(np.sum(reshapedArray[6, indexof, ::])) ))
    print("Total enrollment for 2020 : " + str(int(np.sum(reshapedArray[7, indexof, ::])) ))
    print("Total enrollment for 2021 : " + str(int(np.sum(reshapedArray[8, indexof, ::])) ))
    print("Total enrollment for 2022 : " + str(int(np.sum(reshapedArray[9, indexof, ::])) ))
    print("Total ten year enrollment : " + str(int(np.sum(reshapedArray[::, indexof, ::])) ))
    print("Mean total year enrollment over ten years : " + str((int(reshapedArray[::, indexof, ::].sum())/10) ))
    
    mask = reshapedArray[::, indexof, ::] > 500

# Apply mask to find elements greater than 500
    elements_gt_500 = reshapedArray[::, indexof, ::][mask]

# Calculate median of elements greater than 500
    median_gt_500 = np.median(elements_gt_500)
    #enroll_over_500 = reshapedArray[::, indexof, ::]>500
    print("For all enrollment over 500, median is : " + str(int (median_gt_500)))

    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")


if __name__ == '__main__':
    main()

