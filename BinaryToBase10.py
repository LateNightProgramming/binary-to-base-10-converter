def main():
    inp = ""
    inplist = []
    mathlist = []
    additionvar = 1
    selectvar = 0
    question = ""
    inpneg = ""
    output = "base 10 ="
    while inpneg != 1 and inpneg != 0 and inpneg != "1 (negative)" and inpneg != "0 (positive)":
        try:
            inpneg = int(input("is the number positive or negative (1 for negative, 0 for positive) "))
        except:
            print("bruh")
            main()
        if inpneg != 1 and inpneg != 0 and inpneg != "1 (negative)" and inpneg != "0 (positive)":
            print("come on man")
        else:
            if inpneg == 1:
                print("the number is negative")
                inpneg = "1 (negative)"
                output += " -"
            elif inpneg == 0:
                print("the number is positive")
                inpneg = "o (positive)"
    while inp != "end":
        inp = input("input a bit").lower()
        if inp == "1" or inp == "0":
            inplist.append(inp)
            mathlist.append(0)
        elif inp == "end":
            print("creation finished")
        else:
            print("what")
    print("value =")
    print(inpneg)
    for x in inplist:
        print(x)
    for y in range(len(inplist)):
        mathlist[len(inplist) - 1 - selectvar] += additionvar
        additionvar *= 2
        selectvar += 1
    selectvar = len(inplist)-1
    base10output = 0
    for z in range(len(inplist)):
        if inplist[selectvar]=="1":
            base10output += mathlist[selectvar]
        selectvar -= 1
    base10output = str(base10output)
    if base10output == 0:
        output = output.rstrip("-")
    print(output, end=base10output)
    while question != "yes":
        question = input("\ndo you wish to restart? ").lower()
        if question == "yes":
            print("restarting...")
            main()
        elif question == "no":
            print("program finished")
            quit()
        else:
            print("please input yes or no")
main()
