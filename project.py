#My python project will calculate the amount to #be collected at the end of a number of 
# years by customers who save at a bank. The saving is based on a capital that will be 
# accruing a given percentage compound interest. The compound interest can vary based 
# on the number of years the customer is saving his capital.

import numpy as np

#function to calculate the time required to make a specific amount of money
def compute_period(amount,interest):
    final_amount=float(input(f"""Enter the amount of money you wish to receive 
    at the end of your investment: """))
    t=(np.log((final_amount/amount))/np.log((1+interest)))
    print(f"""
    It will take {round(t,2)} years to make {final_amount} GHS from an initial deposit of {amount} GHS
    at a simple interest rate of {interest*100}%
    """)

#The user needs to enter the initial deposit
print(f"""
You are welcome to International Bank's interest calculator
-----------------------------------------------------------
""")
principal=float(input("Enter the initial deposit in Cedis (GHS): "))

#here the user enters the time/period of investment
while True:
    try:
        time=input(f"""
        For how many years do you want to save the deposit
        with the bank without withdrawing? The longer the 
        period the more you earn on your investment!!!
        ************************************************
        """)
        #convert the input to float type
        time=float(time)
        #test the 
        if time<2 and time>=1:
            rate=0.02
            print(f"""Your estimated return will be
            {round(principal*(1+rate)**time,2)} GHS
            after saving for {time} years
            """)
            print(f"""Do you rather want to know how long it will take you to get
            a specific return ? YES/NO
            """)
            do_reverse=input("Enter y for YES and n for NO: ")
            if do_reverse=="y":
                compute_period(principal,rate)
        elif time>=2 and time<5:
            rate=0.04
            print(f"""Your estimated return will be
            {round(principal*(1+rate)**time,2)}  GHS
            after saving for {time} years
            """)
            print(f"""Do you rather want to know how long it will take you to get
            a specific return ? YES/NO
            """)
            do_reverse=input("Enter y for YES and n for NO: ")
            if do_reverse=="y":
                compute_period(principal,rate)
        elif time>=5 and time<8:
            rate=0.06
            print(f"""Your estimated return will be
            {round(principal*(1+rate)**time,2)} GHS
            after saving for {time} years
            """)
            print(f"""Do you rather want to know how long it will take you to get
            a specific return ? YES/NO
            """)
            do_reverse=input("Enter y for YES and n for NO: ")
            if do_reverse=="y":
                compute_period(principal,rate)
        elif time>=8 and time<11:
            rate=0.07
            print(f"""Your estimated return will be
            {round(principal*(1+rate)**time,2)} GHS
            after saving for {time} years
            """)
            print(f"""Do you rather want to know how long it will take you to get
            a specific return ? YES/NO
            """)
            do_reverse=input("Enter y for YES and n for NO: ")
            if do_reverse=="y":
                compute_period(principal,rate)
        elif time>=11:
            rate=0.1
            print(f"""Your estimated return will be
            {round(principal*(1+rate)**time,2)} GHS
            after saving for {time} years
            """)
            print(f"""Do you rather want to know how long it will take you to get
            a specific return ? YES/NO
            """)
            do_reverse=input("Enter y for YES and n for NO: ")
            if do_reverse=="y":
                compute_period(principal,rate)
        else:
            print(f"OOops!!!!! For you to enjoy an interest rate you must leave the deposit for at least 1 year!!!")
    except:
        while True:
            try:
                time_type=type(time)
                if (time_type=="float") is False:
                    time_input=input(f"""Please enter the number of years 
                    you wish to save your deposit without withdrawing
                    ******************************************************
                    """)
                    time=float(time_input)
                    if time<2 and time>=1:
                        rate=0.02
                        print(f"""Your estimated return will be
                        {round(principal*(1+rate)**time,2)} GHS
                        after saving for {time} years
                        """)
                        print(f"""Do you rather want to know how long it will take you to get
                        a specific return ? YES/NO
                        """)
                        do_reverse=input("Enter y for YES and n for NO")
                        if do_reverse=="y":
                            compute_period(principal,rate)
                    elif time>=2 and time<5:
                        rate=0.04
                        print(f"""Your estimated return will be
                        {round(principal*(1+rate)**time,2)}  GHS
                        after saving for {time} years
                        """)
                    elif time>=5 and time<8:
                        rate=0.06
                        print(f"""Your estimated return will be
                        {round(principal*(1+rate)**time,2)} GHS
                        after saving for {time} years
                        """)
                    elif time>=8 and time<11:
                        rate=0.07
                        print(f"""Your estimated return will be
                        {round(principal*(1+rate)**time,2)} GHS
                        after saving for {time} years
                        """)
                    elif time>=11:
                        rate=0.1
                        print(f"""Your estimated return will be
                        {round(principal*(1+rate)**time,2)} GHS
                        after saving for {time} years
                        """)
                    else:
                        print(f"OOops!!!!! For you to enjoy an interest rate you must leave the deposit for at least 1 year!!!")
                else:
                    time_input=input(f"""
                    Please enter the number of years 
                    you wish to save your deposit without withdrawing
                    ******************************************************
                    """)
                    time=float(time_input)
                    if time<2 and time>=1:
                        rate=0.02
                        print(f"""Your estimated return will be
                        {round(principal*(1+rate)**time,2)} GHS
                        after saving for {time} years
                        """)
                        print(f"""Do you rather want to know how long it will take you to get
                        a specific return ? YES/NO
                        """)
                        do_reverse=input("Enter y for YES and n for NO")
                        if do_reverse=="y":
                            compute_period(principal,rate)
                    elif time>=2 and time<5:
                        rate=0.04
                        print(f"""Your estimated return will be
                        {round(principal*(1+rate)**time,2)}  GHS
                        after saving for {time} years
                        """)
                    elif time>=5 and time<8:
                        rate=0.06
                        print(f"""Your estimated return will be
                        {round(principal*(1+rate)**time,2)} GHS
                        after saving for {time} years
                        """)
                    elif time>=8 and time<11:
                        rate=0.07
                        print(f"""Your estimated return will be
                        {round(principal*(1+rate)**time,2)} GHS
                        after saving for {time} years
                        """)
                    elif time>=11:
                        rate=0.1
                        print(f"""Your estimated return will be
                        {round(principal*(1+rate)**time,2)} GHS
                        after saving for {time} years
                        """)
                    else:
                        print(f"OOops!!!!! For you to enjoy an interest rate you must leave the deposit for at least 1 year!!!")
            except ValueError:
                print("Enter a number")  
    