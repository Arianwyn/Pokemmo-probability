def programa():
    donnatorstatus = input("Do you have donnator status? (yes/no): ")
    shinycharm = input("Do you have shiny charm? (yes/no): ")

    x = input("Number of encounters:")

    def probabilidad(x):
        if donnatorstatus == "no":
            if shinycharm == "yes":
                return int(x) * 100 / 27000
            if shinycharm == "no":
                  return int(x) * 100 / 30000
        if donnatorstatus == "yes":
             if shinycharm == "yes":
                 return int(x) * 100 / 24000
             if shinycharm == "no":
                return int(x) *100 / 27000


    a = probabilidad(x)
    print("Your chances of getting a shiny are:", a, "%")

    close = input("Are you done? (yes/no):")
    if close == "yes":
        print("Good bye")
    if close == "no":
         programa()
programa()
