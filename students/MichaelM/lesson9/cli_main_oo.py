# !/usr/bin/env python3
# wk: cd C:\Users\v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson9
# mo: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson9
# hm: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson9

# git add cli_main.py_oo.py
# git add mailroom_classes_oo.py
# git add test_mailroom_oo.py

# git commit cli_main.py_oo.py
# git commit mailroom_classes_oo.py
# git commit test_mailroom_oo.py

# git push
# goto https://github.com/geekwriter2/Self_Paced-Online/tree/master/students/MichaelM/lesson9/
# click Pull request > new pull request


from lesson9 import mailroom_classes_oo as mr
import importlib

importlib.reload(mr)
import os

usr_directory = "{}/tmp/".format(os.getcwd())


# >> Menu Selection
def main(prompt, menu):
    while True:
        distinct_donor_list = dc.distinct_donor_list()
        response = input(prompt)
        if response.lower() not in menu:
            print(f"'{response}' not available. Please make a valid choice.\n")
        elif response.lower() in menu:
            if response.lower() == "ty":
                user_response_ty = input(
                    "- type 'list' to view a list of donors\n- type 'new' to "
                    "add a donor to the list\n- type in an existing donor to add a new donation >> ")
                if user_response_ty == "list":
                    for item in distinct_donor_list:
                        print(f"{item.title()}")
                elif user_response_ty == "new":
                    first = input("first name? >> ").lower()
                    last = input("last name? >> ").lower()

                    # validate integers and non-negative numbers
                    while True:
                        try:
                            while True:
                                donation = float(input("Donation amount? >> "))
                                if donation > 0:
                                    break
                                elif donation == "True":
                                    pass
                            break
                        except ValueError:
                            print("Please enter valid numbers")
                    d = mr.Donor(first, last)
                    dc.add_donation(d.name, donation)
                    letter = d.donor_letters("new", d.first, donation, 0.0)
                    print(letter)
                elif user_response_ty.title() in distinct_donor_list:
                    # jacob astor
                    donor = user_response_ty.title()
                    print(f"{donor} found.")
                    d = mr.Donor()

                    # validate integers and non-negative numbers
                    while True:
                        try:
                            while True:
                                donation = float(input("Donation amount? >> "))
                                if donation > 0:
                                    break
                                elif donation == "True":
                                    pass
                            break
                        except ValueError:
                            print("Please enter valid numbers")
                    dc.add_donation(donor, donation)
                    sum_amt = float(dc.donor_total(donor))
                    print("{0:,.2f} added to {1}'s total. "
                          "{1}'s total contribution is ${2:,.2f}".format(donation,
                                                                         donor,
                                                                         sum_amt))
                    letter = d.donor_letters("existing_donor", donor, donation, sum_amt)
                    print()
                    print(letter)
            elif response.lower() == "cr":
                summed_donor_list = dc.sum_donors()
                print("{name:<40}{total_donation:<20}{donation_cnt:<30}{ave_donation:}".format(
                    name=dc.esteemed_donors_headers[0],
                    total_donation=dc.esteemed_donors_headers[1],
                    donation_cnt=dc.esteemed_donors_headers[2],
                    ave_donation=dc.esteemed_donors_headers[3]))
                tmp_donor_list = sorted(summed_donor_list, key=lambda x: x[1], reverse=True)
                [print("{name:<40}${total_donation:<20}{donation_cnt:<30}${ave_donation:}".format(name=row[0],
                                                                                                  total_donation=row[1],
                                                                                                  donation_cnt=row[2],
                                                                                                  ave_donation=row[3])
                       ) for row in tmp_donor_list]
            elif response.lower() == "s":
                dc.print_letters(usr_directory)
            elif response.lower() == "q":
                break


# >> Main Prompt
main_prompt = ("\n\n-Main Menu-\n"
               "Do you want to:\n"
               "Send a Thank You -ty\n"
               "Create a Report -cr\n"
               "Send Thank You Letters - s\n"
               "Quit -q\n"
               " >> ")

# >> Main Menu
main_menu = {"cr", "q", "s", "ty"}
if __name__ == "__main__":

    # start by initiallizing the datacollection class and building a dataset of donors
    d1 = mr.Donor("jacob", "astor")
    d2 = mr.Donor("alan", "rufus, 1st lord of richmond")
    d3 = mr.Donor("henry", "ford")
    d4 = mr.Donor("cornelius", "vanderbilt")
    d5 = mr.Donor("jakob", "fugger")
    dc = mr.DonorCollection()
    dc.add_donation(d1.name, 10.0)
    dc.add_donation(d1.name, 100.0)
    dc.add_donation(d1.name, 1000.0)
    dc.add_donation(d1.name, 10000.0)
    dc.add_donation(d2.name, 10.0)
    dc.add_donation(d2.name, 100.0)
    dc.add_donation(d2.name, 1000.0)
    dc.add_donation(d3.name, 10.0)
    dc.add_donation(d3.name, 100.0)
    dc.add_donation(d4.name, 10.0)
    dc.add_donation(d5.name, 10.0)

    # run input
    main(main_prompt, main_menu)
