total_bill =float(input("Enter the total bill: "))
paid_bill =float(input("Enter the bill you paid: "))

if total_bill < paid_bill :
    print("The change is:", paid_bill - total_bill)
elif total_bill > paid_bill :
    print("You have to pay:" ,total_bill - paid_bill)
elif total_bill == paid_bill :
    print("No Due Amount")
else :
    print("Somethings went wrong")