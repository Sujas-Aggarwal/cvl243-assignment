class bcolors:
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
        print(bcolors.WARNING + text + bcolors.ENDC)
    def printError(text):
        print(bcolors.FAIL + text + bcolors.ENDC)
    def printSuccess(text):
        print(bcolors.OKGREEN + text + bcolors.ENDC)
    def printInfo(text):
        print(bcolors.OKBLUE + text + bcolors.ENDC)
    def printHeader(text):
        print(bcolors.HEADER + text + bcolors.ENDC)
    def printCyan(text):
        print(bcolors.OKCYAN + text + bcolors.ENDC)
    def printBold(text):
        print(bcolors.BOLD + text + bcolors.ENDC)
    def printUnderline(text):
        print(bcolors.UNDERLINE + text + bcolors.ENDC)
#---------------------------------------------------

# Prompts -
class prompts:
    inputLength = 'Enter the length of the beam (meters): '
    inputWidth = 'Enter the width of the beam (meters): '
    inputHeight = 'Enter the height of the beam (meters): '
    inputLoad = 'Enter the load on the beam (kN): '
    inputMaterial = 'Enter the material of the beam: '
    inputSupport = 'Enter the type of support: '
    numberError = 'Please enter a valid number.'
    infoText = '\
Hello, I am Sujas Kumar Aggarwal, 2022CE11047. This is my submission for CVL243 Assignment. \n\
This python programme is made to conduct flexural sectional analysis for a flanged and singly reinforced beam.\n\
This programme will ask you for the following details: \n\
1. Length of the beam (meters) \n\
2. Width of the beam (meters) \n\
3. Height of the beam (meters) \n\
4. Load on the beam (kN) \n\
5. Material of the beam \n\
6. Type of support \n\
After entering these details, the programme will calculate the following: \n\
1. Area of the beam \n\
2. Moment of Inertia of the beam \n\
3. Maximum Bending Stress \n'
    helpText = 'Note: Enter "exit" to quit or "help" to see options.'
    def programmeInput(prompt=""):
        bcolors.printBold(prompt)
        a = input()
        if a == 'exit':
            exit()
        if a == 'help':
            bcolors.printInfo(prompts.infoText)
            return prompts.programmeInput()
        return a
    def takeNumericInput(prompt,additionCheck = lambda x: True):
        a = prompts.programmeInput(prompt)
        if (not a.isnumeric()) and additionCheck(a):
            bcolors.printError(prompts.numberError)
            bcolors.printInfo(prompts.helpText)
            return prompts.takeNumericInput(prompt)
        else:
            a = int(a)
        return a
#---------------------------------------------------
lenBeam = prompts.takeNumericInput(prompts.inputLength)
widthBeam = prompts.takeNumericInput(prompts.inputWidth)
heightBeam = prompts.takeNumericInput(prompts.inputHeight)
loadBeam = prompts.takeNumericInput(prompts.inputLoad)
materialBeam = prompts.takeNumericInput(prompts.inputMaterial)
supportBeam = prompts.takeNumericInput(prompts.inputSupport)
bcolors.printSuccess('Beam Details:')
print('Length: ' + str(lenBeam) + ' meters')
print('Width: ' + str(widthBeam) + ' meters')
print('Height: ' + str(heightBeam) + ' meters')
print('Load: ' + str(loadBeam) + ' kN')
print('Material: ' + str(materialBeam))
print('Support: ' + str(supportBeam))
bcolors.printInfo('Beam Details have been recorded.')
bcolors.printInfo('Calculating...')