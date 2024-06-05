# school_data.py
# AUTHOR NAME: Laxmi Paudel
#
# A terminal-based application for computing and printing statistics based on given input.



import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

class School:
    def __init__(self, data, school_names):
        """
        Initialize the SchoolEnrollment class with data and school names.

        :param data: List of yearly enrollment data.
        :param array3D : 3D array of the given data
        :param school_names: Dictionary mapping school codes to school names.
        :param school_codes: make a list of school codes.
        :grad_10_data: array of all grade 10 data
        :grad_11_data: array of all grade 11 data
        :grad_12_data: array of all grade 12 data
        """
        self.array3D = np.stack(data).reshape(10, 20, 3)
        self.school_names = school_names
        self.school_codes = list(school_names.keys())
        self.grad_10_data = self.array3D[:,:,0]
        self.grad_11_data = self.array3D[:,:,1]
        self.grad_12_data = self.array3D[:,:,2]

    def get_school_code(self, userdata):
        """
        Get the school code from the user input, which could be a code or a name.

        :param userdata: User input which could be a school code or name.
        :return: School code if found, otherwise raise value error.
        """
        if userdata.isdigit() and int(userdata) in self.school_names:
            return int(userdata)
        elif userdata in self.school_names.values():
            return self.school_codes[list(self.school_names.values()).index(userdata)]
        else:
            raise ValueError("Invalid input, Enter valid school name or code")


    def compute_statforASchool(self, school_code):
        """
        Compute and print statistics for the given school code.

        :param school_code: School code to compute statistics for, 
        :index: find the index of school code in a school_code list and calculate statistics based on the index.
        """
        print("\n***Requested School Statistics***\n")

        index = self.school_codes.index(school_code)
        print(f"\nSchool Name: {self.school_names[school_code]}, School Code: {school_code}:\n")

        # calculate the mean of each grade, highest and lowest enrollment of the entire period of the requested school using fancy indexing
        grad_10_mean = int(np.nanmean(self.array3D[:, index, 0]))
        grad_11_mean = int(np.nanmean(self.array3D[:, index, 1]))
        grad_12_mean = int(np.nanmean(self.array3D[:, index, 2]))
        highest_enrollment = int(np.nanmax(self.array3D[:, index, :]))
        lowest_enrollment = int(np.nanmin(self.array3D[:, index, :]))

        print(f"Mean enrollment for Grade 10 across all years: {grad_10_mean}")
        print(f"Mean enrollment for Grade 11 across all years: {grad_11_mean}")
        print(f"Mean enrollment for Grade 12 across all years: {grad_12_mean}")
        print(f"Highest enrollment for a single grade within the entire time period: {highest_enrollment}")
        print(f"Lowest enrollment for a single grade within the entire time period: {lowest_enrollment}")

        #use for loop to calculate and print total enrollment of each year of the requested school.
        for year in range(10):  
            print(f"Total enrollment for {2013 + year}: {int(np.sum(self.array3D[year, index, :]))}")
        # calculate total ten year enrollment and mean of that and print values
        total_ten_year_enrollment = np.sum(self.array3D[:, index, :])
        mean_ten_year_enrollment = np.sum(self.array3D[:, index, :]/10)

        print(f"Total ten year enrollment: {int(total_ten_year_enrollment)}")
        print(f"Mean total enrollment over 10 years: {int(mean_ten_year_enrollment)}")

        #checking either values are greatert than 500 or not, use array masking for that and calculate median of that values
        mask = self.array3D[:, index, :] > 500
        elements_gt_500 = self.array3D[:, index, :][mask]
        if elements_gt_500.size > 0:
            median_gt_500 = int(np.nanmedian(elements_gt_500))
            print(f"For all enrollment over 500, median is: {median_gt_500}")
        else:
            print("No enrollment data over 500.")

    def compute_statforallSchool(self):

        """Compute and print required statistics for ALL School.
        :mean_2013 mean of total enrollment of year 2012
        :mean_2022 mean of total enrollment of year 2022
        """
        print("\n***General Statistics for All Schools***\n")
        mean_2013 = int(np.nanmean(self.array3D[1, : :]))
        mean_2022 = int(np.nanmean(self.array3D[9, : :]))

        print(f"Mean enrollment in 2013 :  {mean_2013}")
        print(f"Mean enrollment in 2012 :  {mean_2022}")
        #calculate total graduating of the year 2022 and print value on the same line
        print(f"Total graduating year class of 2022 :  {int(np.nansum(self.array3D[9, :, 2]))}")
        #calculate highest enrollment of all grades and schools and print value on the same line
        print(f"Highest enrollment for a single grade :  {int(np.nanmax(self.array3D[:, :, :]))}")
        #calculate lowest enrollment of all grades and schools and print value on the same line
        print(f"Lowest enrollment for a single grade :  {int(np.nanmin(self.array3D[:, :, :]))}")

def main():
    print("ENSF 692 School Enrollment Statistics")
    #data initialization
    data = [year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022]

    """ dictionary mapping school code to name from given dataset Assignment3Data.csv """
    school_names = {
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
     
     #initialize the class object with data of 10 different year.
    enrollment = School(data, school_names)
    print(f"Shape of full data array :  {(np.stack(enrollment.array3D).reshape(10, 20, 3)).shape}")
    #run the code until user-input is valid, if user data is invalid throws a valueerror and prompt user to reenter 
    while True:
        try:
            userdata = input("Please enter the high school code or name : ")
            school_code = enrollment.get_school_code(userdata)
            if school_code in school_names:
                enrollment.compute_statforASchool(school_code)
                enrollment.compute_statforallSchool()
            break
        except ValueError as e:
            print(e)
if __name__ == '__main__':
    main()

