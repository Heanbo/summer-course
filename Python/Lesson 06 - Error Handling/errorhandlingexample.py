from area import rect_area

try:
    len = float(input("Enter the length:  "))
    wid = float(input("Enter the width:  "))
    rect_area(len, wid)
except ValueError:
    print("There was a Value Error.")
#except ZeroDivisionError:
#    print("System cannot divide by 0.")
except:
    print("There was an error")
else:
    print("Executed without any Errors")
finally:
    print("This always runs")

print("There was no crash")