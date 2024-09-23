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
    inputWidth = 'Enter the width of the beam (mm): '
    inputDepth = 'Enter the depth of the beam (mm): '
    inputWebWidth = 'Enter the web width of the beam (mm): '
    inputEffectiveDepth = 'Enter the effective depth of the beam (mm): '
    inputFlexuralRigidity = 'Enter the flexural rigidity of the beam (GN-m^2): '
    inputDiameterReinforcement = 'Enter the diameter of the reinforcement (mm): '
    inputNumberReinforcement = 'Enter the number of reinforcement: '
    tShape = lambda x: f'\
 <--------- W = {x[0]}mm ----------->\n\
|---------------------------------|    ^             ^\n\
|                                 |    |             |\n\
|                                 |    |             |\n\
|                                 |    |             |\n\
|                                 |    |             |\n\
|                                 |    |             |\n\
|----------             ----------|  D = {x[1]}mm    ED = {x[3]}mm\n\
          |             |              |             |\n\
          |             |              |             |\n\
          |             |              |             |\n\
          |             |              |             |\n\
          |             |              |             |\n\
          |  *   *   *  |              |             -\n\
          |             |              |      \n\
          |             |              |      \n\
          |             |              |      \n\
          ---------------              -     \n\
         <- WW = {x[2]}mm ->\n'
    iShape = lambda x: f'\
 <--------- W = {x[0]}mm ----------->\n\
|---------------------------------|     ^             ^\n\
|                                 |     |             |\n\
|                                 |     |             |\n\
|                                 |     |             |\n\
|                                 |     |             |\n\
|-------                   -------|     |             |\n\
        |                 |             |             |\n\
        |                 |        D = {x[1]}mm    ED = {x[2]}mm\n\
        |                 |             |             |\n\
        |                 |             |             |\n\
|-------                   -------|     |             |\n\
|                                 |     |             |\n\
|            *   *   *            |     |             -\n\
|                                 |     |             \n\
|                                 |     |             \n\
|---------------------------------|     -             \n\
         <- WW = {x[2]}mm ->\n'
    lShape = lambda x: f'\
 <--------- W = {x[0]}mm ------->\n\
-------------------------------|         ^             ^\n\
|                              |         |             |\n\
|                              |         |             |\n\
|                              |         |             |\n\
|                              |         |             |\n\
|                              |         |             |\n\
|                              |         |             |\n\
|                  ------------|         |             |\n\
|                  |                 D = {x[1]}mm  ED = {x[2]}mm\n\
|                  |                     |             |\n\
|                  |                     |             |\n\
|    *    *    *   |                     |             -\n\
|                  |                     |             \n\
|                  |                     |             \n\
|                  |                     |             \n\
--------------------                     -             \n\
<-  WW = {x[2]}mm  ->\n'
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
5. Flexural Rigidity (GN-m^2)  \n\
6. Diameter of Reinforcement (mm)\n\
7. Number of Reinforcement \n\
After entering these details, the programme will calculate the following: \n\
1. Location of Neutral Axis \n\
2. Ultimate bending Moment of the Beam\n\
3. Reinforcement Type i.e OverReinforced \n'
    helpText = 'Note: Enter "exit" to quit or "help" to know more.'
    def programmeInput(prompt=""):
        rainbow.printBold(prompt)
        a = input() or None
        if a == 'exit':
            exit()
        if a == 'help':
            rainbow.printWarning(prompts.infoText)
            return prompts.programmeInput(prompt)
        return a
    def validateInput(prompt,checks = lambda x: True,errorMessage = 'Please enter a valid input.',canBeEmpty = False,preValue = None):
        if not preValue == None:
            rainbow.printCyan(f'Default Value: {preValue}')
        a = prompts.programmeInput(prompt)
        if a==None:
            a = preValue
        if (a==None) and canBeEmpty:
            return a
        elif (a==None) and not canBeEmpty:
            rainbow.printError(errorMessage)
            rainbow.printInfo(prompts.helpText)
            return prompts.validateInput(prompt,checks,errorMessage,canBeEmpty,preValue=preValue)
        if not (checks(a) and not a==None):
            rainbow.printError(errorMessage)
            rainbow.printInfo(prompts.helpText)
            return prompts.validateInput(prompt,checks,errorMessage,canBeEmpty,preValue=preValue)
        return a
#---------------------------------------------------
#Solving Algorithms -
class solve:
    def tSolver(width,depth,webWidth,effectiveDepth,flexuralRigidity,diameterReinforcement,numberReinforcement):
        pass
    def iSolver(width,depth,webWidth,effectiveDepth,flexuralRigidity,diameterReinforcement,numberReinforcement):
        pass
    def lSolver(width,depth,webWidth,effectiveDepth,flexuralRigidity,diameterReinforcement,numberReinforcement):
        pass
#---------------------------------------------------
def main(shape=None,width=None,depth=None,webWidth=None,effectiveDepth=None,flexuralRigidity=None,diameterReinforcement=None,numberReinforcement=None):

    shape = prompts.validateInput(prompts.allTogether, lambda x: x.isnumeric() and int(x) in [1,2,3],preValue=shape)
    width = prompts.validateInput(prompts.inputWidth, lambda x: x.isnumeric() and int(x)>0,preValue=width)
    depth = prompts.validateInput(prompts.inputDepth, lambda x: x.isnumeric() and int(x)>0,preValue=depth)
    webWidth = prompts.validateInput(prompts.inputWebWidth, lambda x: x.isnumeric() and int(x)>0,preValue=webWidth)
    effectiveDepth = prompts.validateInput(prompts.inputEffectiveDepth, lambda x: x.isnumeric() and int(x)>0,preValue=effectiveDepth)
    flexuralRigidity = prompts.validateInput(prompts.inputFlexuralRigidity, lambda x: x.isnumeric() and int(x)>0,preValue=flexuralRigidity)
    diameterReinforcement = prompts.validateInput(prompts.inputDiameterReinforcement, lambda x: x.isnumeric() and int(x)>0,preValue=diameterReinforcement)
    numberReinforcement = prompts.validateInput(prompts.inputNumberReinforcement, lambda x: x.isnumeric() and int(x)>0,preValue=numberReinforcement)
    if int(shape)==1:
        rainbow.printBold(prompts.tShape([width,depth,webWidth,effectiveDepth]))
    elif int(shape)==2:
        rainbow.printBold(prompts.iShape([width,depth,webWidth]))
    elif int(shape)==3:
        rainbow.printBold(prompts.lShape([width,depth,effectiveDepth]))
    rainbow.printInfo(f'Width of the beam:\033[0m {width}mm')
    rainbow.printInfo(f'Depth of the beam:\033[0m {depth}mm')
    rainbow.printInfo(f'Web Width of the beam:\033[0m {webWidth}mm')
    rainbow.printInfo(f'Effective Depth of the beam: \033[0m{effectiveDepth}mm')
    rainbow.printInfo(f'Flexural Rigidity of the beam: \033[0m{flexuralRigidity}GN-m^2')
    rainbow.printInfo(f'Diameter of the Reinforcement: \033[0m{diameterReinforcement}mm')
    rainbow.printInfo(f'Number of Reinforcement:\033[0m {numberReinforcement}')
    rainbow.printInfo(f'Shape of the Beam: \033[0m{shape}')
    confirm = prompts.validateInput('Are the inputs correct? (y/n): ', lambda x: x in ['y','n'],canBeEmpty=True)
    if confirm == 'n':
        rainbow.printError('Please enter the inputs again.')
        main(shape,width,depth,webWidth,effectiveDepth,flexuralRigidity,diameterReinforcement,numberReinforcement)
    else:
        rainbow.printSuccess('The inputs have been successfully confirmed.')

if __name__=="__main__":
    try:
        rainbow.printHeader('Flexural Sectional Analysis')
        rainbow.printWarning(prompts.infoText)
        rainbow.printInfo(prompts.helpText)
        main()
    except Exception as e:
        try:
            print(e)
        except:
            pass
        rainbow.printError("Unfortunately, Some Unforseen Erorr Occured. Please try again.")