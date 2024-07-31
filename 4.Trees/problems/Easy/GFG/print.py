from termcolor import colored
def printed(*argv):
    for i in argv:
        print(colored(i, "red", "on_black", attrs=['bold']))
    # print("\n")
