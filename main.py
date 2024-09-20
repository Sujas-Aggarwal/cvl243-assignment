from sys import argv
class rainbow:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    def printWarning(text):
        print(rainbow.WARNING + text + rainbow.ENDC)
    def printError(text):
        print(rainbow.FAIL + text + rainbow.ENDC)
    def printSuccess(text):
        print(rainbow.OKGREEN + text + rainbow.ENDC)
    def printInfo(text):
        print(rainbow.OKBLUE + text + rainbow.ENDC)
    def printHeader(text):
        print(rainbow.HEADER + text + rainbow.ENDC)
    def printCyan(text):
        print(rainbow.OKCYAN + text + rainbow.ENDC)
    def printBold(text):
        print(rainbow.BOLD + text + rainbow.ENDC)
    def printUnderline(text):
        print(rainbow.UNDERLINE + text + rainbow.ENDC)
#---------------------------------------------------

# Prompts -
class prompts:
    inputLength = 'Enter the length of the beam (meters): '
    inputWidth = 'Enter the width of the beam (meters): '
    inputHeight = 'Enter the height of the beam (meters): '
    inputLoad = 'Enter the load on the beam (kN): '
    inputMaterial = 'Enter the material of the beam: '
    inputSupport = 'Enter the type of support: '
    tShape = '\
|-----------------|\n\
|                 |\n\
|                 |\n\
|----         ----|\n\
     |       |\n\
     |       |\n\
     |       |\n\
     ---------\n'
    iShape ='\
|-----------------|\n\
|                 |\n\
|                 |\n\
|----         ----|\n\
     |       |\n\
     |       |\n\
     |       |\n\
|----         ----|\n\
|                 |\n\
|                 |\n\
|-----------------|\n'
    lShape ='\
------------------|\n\
|                 |\n\
|                 |\n\
|       ----------|\n\
|       |\n\
|       |\n\
|       |\n\
|       |\n\
|       |\n\
---------\n'
    allTogether = '\
1) |-----------------|       2) |-----------------|      3) ------------------|\n\
   |                 |          |                 |         |                 |\n\
   |                 |          |                 |         |                 |\n\
   |----         ----|          |----         ----|         |       ----------|\n\
        |       |                    |       |              |       |\n\
        |       |                    |       |              |       |\n\
        |       |                    |       |              |       |\n\
        ---------               |----         ----|         |       |\n\
                                |                 |         |       |\n\
                                |                 |         |       |\n\
                                |-----------------|         ---------\n\
     1) T Shaped Beam             2) I Shaped Beam          3) L Shaped Beam\n\n\
Please enter the number of the shape you want to analyse: '
    numberError = 'Please enter a valid number.'
    infoText = '\n\
Hello, I am \033[1mSujas Kumar Aggarwal\033[0m\033[93m,2022CE11047.\nThis is my submission for CVL243 Assignment. \n\
This python programme is made to conduct flexural sectional analysis for a flanged and singly reinforced beam.\n\
This programme will ask you for the following details: \n\
0. Shape of the Beam i.e I\n\
1. Width of The Beam (mm) \n\
2. Web Width of the beam (mm) \n\
3. Depth of the beam (mm) \n\
4. Effective Depth (mm) \n\
5. Flexural Rigidity (N-m^2)  \n\
6. Diameter of Reinforcement (mm)\n\
7. Number of Reinforcement \n\
After entering these details, the programme will calculate the following: \n\
1. Location of Neutral Axis \n\
2. Ultimate bending Moment of the Beam\n\
3. Reinforcement Type i.e OverReinforced \n'
    helpText = 'Note: Enter "exit" to quit or "help" to know more.'
    def programmeInput(prompt=""):
        rainbow.printBold(prompt)
        a = input() or " "
        if a == 'exit':
            exit()
        if a == 'help':
            rainbow.printWarning(prompts.infoText)
            return prompts.programmeInput(prompt)
        return a
    def validateInput(prompt,checks = lambda x: True,errorMessage = 'Please enter a valid input.',canBeEmpty = False):
        a = prompts.programmeInput(prompt)
        if (a==" ") and canBeEmpty:
            return " "
        if checks(a) and not a==" ":
            a = int(a)
        else:
            rainbow.printError(errorMessage)
            rainbow.printInfo(prompts.helpText)
            return prompts.validateInput(prompt,checks,errorMessage)
        return a
#---------------------------------------------------
# lenBeam = prompts.validateInput(prompts.inputLength)
def main():

    shape = prompts.validateInput(prompts.allTogether, lambda x: x.isnumeric() and x in ['1','2','3'])
if __name__=="__main__":
    if len(argv)>1:
        if argv[1] == '--help':
            rainbow.printWarning(prompts.infoText)
            exit()
    try:
        main()
    except Exception as e:
        rainbow.printError("Unfortunately, Some Unforseen Erorr Occured. Please try again.")