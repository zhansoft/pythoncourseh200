def appendicitis(lst):
    summation = 0
    for i in lst:
        summation += int(i)
    if summation == 3:
        return True
    elif len(lst) == 5:
        return False


if __name__ == "__main__":
    list_values = []
    symptoms = ["abdominal pain", "nausea", "vomiting", "fever", "loss of appetite"]
    for i in range(len(symptoms)):
        condition = "Do you have " +  symptoms[i] + ": " + " 1/0"
        valInput = input(condition)
        list_values += valInput
        if appendicitis(list_values):
            print("Appendicitis")
            break
    if not appendicitis(list_values):
        print("No Appendicitis")

    
