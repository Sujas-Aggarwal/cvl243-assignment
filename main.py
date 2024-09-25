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
    inputCGrade= 'Enter the Concrete Grade (MPa): '
    inputSGrade = 'Enter the Reinforcement Grade (MPa): '
    inputWebWidth = 'Enter the web width of the beam (mm): '
    inputDepthFlang = 'Enter the Flang Depth of the beam (mm): '
    inputEffectiveDepth = 'Enter the effective depth of the beam (mm): '
    inputFlexuralRigidity = 'Enter the flexural rigidity of the beam (GN-m^2): '
    inputDiameterReinforcement = 'Enter the diameter of the reinforcement (mm): '
    inputNumberReinforcement = 'Enter the number of reinforcement: '
    tShape = lambda x: f'\
 <--------- W = {x[0]}mm ----------->\n\
|---------------------------------|    ^             ^                  ^\n\
|                                 |    |             |                  |\n\
|                                 |    |             |                  |\n\
|                                 |    |             |              DF = {x[4]}mm\n\
|                                 |    |             |                  |\n\
|                                 |    |             |                  |\n\
|----------             ----------|  D = {x[1]}mm    ED = {x[3]}mm      -\n\
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
|---------------------------------|     ^             ^       ^\n\
|                                 |     |             |       |\n\
|                                 |     |             |       |\n\
|                                 |     |             |   DF = {x[4]}mm\n\
|                                 |     |             |       |\n\
|-------                   -------|     |             |       -\n\
        |                 |             |             |\n\
        |                 |        D = {x[1]}mm    ED = {x[3]}mm\n\
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
-------------------------------|         ^             ^          ^\n\
|                              |         |             |          |\n\
|                              |         |             |          |\n\
|                              |         |             |        DF = {x[4]}mm\n\
|                              |         |             |          |\n\
|                              |         |             |          |\n\
|                              |         |             |          |\n\
|                  ------------|         |             |          -\n\
|                  |                 D = {x[1]}mm  ED = {x[3]}mm\n\
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
    typeOfBeam = 0
    width = 0
    grade = 0
    cGrade = 0
    sGrade = 0
    depth = 0
    webWidth = 0
    depthFlang = 0
    effectiveDepth = 0
    flexuralRigidity = 0
    diameterReinforcement = 0
    numberReinforcement = 0
    def __init__(self,width,depth,cGrade,sGrade,webWidth,depthFlang,effectiveDepth,flexuralRigidity,diameterReinforcement,numberReinforcement,typeOfBeam):
        self.width = int(width)
        self.depth = int(depth)
        self.webWidth = int(webWidth)
        self.depthFlang = int(depthFlang)
        self.effectiveDepth = int(effectiveDepth)
        self.flexuralRigidity = int(flexuralRigidity)
        self.diameterReinforcement = int(diameterReinforcement)
        self.numberReinforcement = int(numberReinforcement)
        self.typeOfBeam = int(typeOfBeam)
        self.cGrade = int(cGrade)
        self.sGrade = int(sGrade)
        self.isOverReinforced = False
        
    def areaBeam(self):
        if (self.typeOfBeam==1):
            return self.depthFlang*self.width + (self.depth-self.depthFlang)*self.webWidth
        elif (self.typeOfBeam==2):
            return 2*self.depthFlang*self.width + (self.depth-2*self.depthFlang)*self.webWidth
        return self.depthFlang*self.width + (self.depth-self.depthFlang)*self.webWidth
    def areaReinforcement(self):
        return (3.14159*(self.diameterReinforcement**2)/4)*self.numberReinforcement
    def reinforcementRatio(self):
        return self.areaReinforcement()/self.areaBeam()
    def isUnderReinforced(self):
        if self.reinforcementRatio() > 0.04:
            self.isOverReinforced = True
    def neutralAxisDepth(self):
        Ast = self.areaReinforcement()
        fck = self.cGrade  # characteristic strength of concrete
        fy = self.sGrade  # yield strength of steel
        
        if self.isOverReinforced:
            # Over-reinforced condition (concrete crushes before steel yields)
            return (fy * Ast - 0.447 * fck * (self.width - self.webWidth) * self.depthFlang) / (0.362 * fck * self.webWidth)
        else:
            # Under-reinforced condition (steel yields before concrete crushes)
            xu_max = 0.48 * self.effectiveDepth  # Maximum neutral axis depth for under-reinforced section
            xu = fy * Ast / (0.36 * fck * self.width)
            return min(xu, xu_max)
    def ultimateBendingMoment(self):
        Ast = self.areaReinforcement()
        fck = self.cGrade
        fy = self.sGrade
        d = self.effectiveDepth
        
        xu = self.neutralAxisDepth()  # Neutral axis depth
        if self.isOverReinforced:
            return (self.sGrade*self.areaReinforcement()-0.447*self.cGrade*(self.width-self.webWidth)*self.depthFlang)/(0.362*self.cGrade*self.webWidth)
        
        z = d - 0.42 * xu  # Lever arm
        
        # Calculate ultimate moment capacity using IS 456: 2000
        Mu = 0.87 * fy * Ast * z / 1e6  # Convert to kNm
        return Mu
    
    def display(self):
        self.isUnderReinforced()
        rainbow.printHeader('\n---------Results--------')
        rainbow.printInfo(f'Area of the Beam:\033[0m {self.areaBeam()}mm^2')
        rainbow.printInfo(f'Area of the Reinforcement:\033[0m {self.areaReinforcement()}mm^2')
        rainbow.printInfo(f'Reinforcement Ratio:\033[0m {self.reinforcementRatio()}')
        rainbow.printInfo(f'Neutral Axis Depth:\033[0m {self.neutralAxisDepth()}mm')
        rainbow.printInfo(f'Ultimate Bending Moment:\033[0m {self.ultimateBendingMoment()}N-m^2')
        if self.isOverReinforced:
            rainbow.printWarning('The Beam is Over Reinforced.')
        else:
            rainbow.printWarning('The Beam is Under Reinforced.')
        return
    def saveCSV(self):
        serialNumber = 1
        try:
            with open('results.csv','r') as f:
                #read the last line
                serialNumber = int(f.readlines()[-1].split(',')[0]) + 1
                pass
            with open('results.csv','a') as f:
                f.write(f'{serialNumber},{"T Shape" if self.typeOfBeam==1 else "I Shape" if self.typeOfBeam==2 else "L Shape"},{self.width},{self.depth},{self.cGrade},{self.sGrade},{self.webWidth},{self.depthFlang},{self.effectiveDepth},{self.flexuralRigidity},{self.diameterReinforcement},{self.numberReinforcement},{self.areaBeam()},{self.areaReinforcement()},{self.neutralAxisDepth()},{self.ultimateBendingMoment()},{"OverReinforced" if self.isOverReinforced else "UnderReinforced"}\n')
        except FileNotFoundError:
            with open('results.csv','w') as f:
                f.write('S. No.,Type of Beam,Width (mm),Depth (mm),Concrete Grade (MPa),Steel Grade (MPa),Web Width (mm),Flang Depth (mm),Effective Depth (mm),Flexural Rigidity (GN-m^2),Reinforcement Diameter (mm),Number of Reinforcement,Area of Beam (mm^2),Area of Reinforcement (mm^2),Neutral Axis Depth (mm),Ultimate Bending Moment (N-m^2),Type of Reinforcement\n')
                f.write(f'{serialNumber},{"T Shape" if self.typeOfBeam==1 else "I Shape" if self.typeOfBeam==2 else "L Shape"},{self.width},{self.depth},{self.cGrade},{self.sGrade},{self.webWidth},{self.depthFlang},{self.effectiveDepth},{self.flexuralRigidity},{self.diameterReinforcement},{self.numberReinforcement},{self.areaBeam()},{self.areaReinforcement()},{self.neutralAxisDepth()},{self.ultimateBendingMoment()},{"OverReinforced" if self.isOverReinforced else "UnderReinforced"}\n')
        except Exception as e:
            rainbow.printError("Some Error Occured, Please Delete 'results.csv' file if it already exists and try again.")
#---------------------------------------------------
def main(shape=None,width=None,depth=None,cGrade = None,sGrade = None,webWidth=None,depthFlang=None,effectiveDepth=None,flexuralRigidity=None,diameterReinforcement=None,numberReinforcement=None):

    shape = prompts.validateInput(prompts.allTogether, lambda x: x.isnumeric() and int(x) in [1,2,3],preValue=shape)
    width = prompts.validateInput(prompts.inputWidth, lambda x: x.isnumeric() and int(x)>0,preValue=width)
    depth = prompts.validateInput(prompts.inputDepth, lambda x: x.isnumeric() and int(x)>0,preValue=depth)
    cGrade = prompts.validateInput(prompts.inputCGrade, lambda x: x.isnumeric() and int(x)>0,preValue=cGrade)
    sGrade = prompts.validateInput(prompts.inputSGrade, lambda x: x.isnumeric() and int(x)>0,preValue=sGrade)
    webWidth = prompts.validateInput(prompts.inputWebWidth, lambda x: x.isnumeric() and int(x)>0 and int(x)<=int(width),preValue=webWidth)
    depthFlang = prompts.validateInput(prompts.inputDepthFlang, lambda x: x.isnumeric() and int(x)>0 and int(x)<=int(depth),preValue=depthFlang)
    effectiveDepth = prompts.validateInput(prompts.inputEffectiveDepth, lambda x: x.isnumeric() and int(x)>0 and int(x)<=int(depth),preValue=effectiveDepth)
    flexuralRigidity = prompts.validateInput(prompts.inputFlexuralRigidity, lambda x: x.isnumeric() and int(x)>0,preValue=flexuralRigidity)
    diameterReinforcement = prompts.validateInput(prompts.inputDiameterReinforcement, lambda x: x.isnumeric() and int(x)>0,preValue=diameterReinforcement)
    numberReinforcement = prompts.validateInput(prompts.inputNumberReinforcement, lambda x: x.isnumeric() and int(x)>0,preValue=numberReinforcement)
    if int(shape)==1:
        rainbow.printBold(prompts.tShape([width,depth,webWidth,effectiveDepth,depthFlang]))
    elif int(shape)==2:
        rainbow.printBold(prompts.iShape([width,depth,webWidth,effectiveDepth,depthFlang]))
    elif int(shape)==3:
        rainbow.printBold(prompts.lShape([width,depth,webWidth,effectiveDepth,depthFlang]))
    rainbow.printInfo(f'Width of the beam:\033[0m {width}mm')
    rainbow.printInfo(f'Depth of the beam:\033[0m {depth}mm')
    rainbow.printInfo(f'Grade of Concrete: \033[0m{cGrade}MPa')
    rainbow.printInfo(f'Grade of Steel: \033[0m{sGrade}MPa')
    rainbow.printInfo(f'Web Width of the beam:\033[0m {webWidth}mm')
    rainbow.printInfo(f'Depth Flang of the beam:\033[0m {depthFlang}mm')
    rainbow.printInfo(f'Effective Depth of the beam: \033[0m{effectiveDepth}mm')
    rainbow.printInfo(f'Flexural Rigidity of the beam: \033[0m{flexuralRigidity}GN-m^2')
    rainbow.printInfo(f'Diameter of the Reinforcement: \033[0m{diameterReinforcement}mm')
    rainbow.printInfo(f'Number of Reinforcement:\033[0m {numberReinforcement}')

    confirm = prompts.validateInput('Are the inputs correct? (y/n): ', lambda x: x in ['y','n'],canBeEmpty=True)
    if confirm == 'n':
        rainbow.printError('Please enter the inputs again.')
        main(shape,width,depth,cGrade,sGrade,webWidth,depthFlang,effectiveDepth,flexuralRigidity,diameterReinforcement,numberReinforcement)
    solution = solve(width,depth,cGrade,sGrade,webWidth,depthFlang,effectiveDepth,flexuralRigidity,diameterReinforcement,numberReinforcement,shape)
    rainbow.printSuccess('The inputs have been successfully confirmed.')
    solution.display()
    confirmCSV = prompts.validateInput('Do you want to save the results in a CSV file? (y/n): ', lambda x: x in ['y','n'],canBeEmpty=True)
    if not confirmCSV == 'n':
        solution.saveCSV()
        rainbow.printSuccess('The results have been saved in the CSV file in the current directory.')
    return
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