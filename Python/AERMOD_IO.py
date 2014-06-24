# Importing Libraries
import os
import AERMOD_FUNC as AFUN
import subprocess
import time

'''AUTOMATICALLY RUN AERMOD FROM COMMAND LINE
# then wait 5 seconds for results. Once the
# results are generated, the .PLOT file
# will be opened and the data will be extracted
# and saved in NUMPY and/or MATLAB format. 
# Next, the "AERMOD" folder will be stored in the
# simulation Files location.'''

# **************** USER INPUTS ****************

#File Names 
PFL_name = 'CinWil2005.PFL'
SFC_name = 'CinWil2005.SFC'
PLOT_name = 'GE_PLOT.PLOTtest' # taken from '.inp' file

#Output Value Locations
rows = [9,14]
column = 3


#Combined Sensitivity Analysis (SEE README FOR DETAILS)
#? yes - 1; no - 0
CMBDSens = 1

#Matlab Export?
matlabexport = True

waittime = 8 # seconds (Depends on CPU Speed)










# **************** *********** ****************
# DO NOT CHANGE ANYTHING BELOW THIS LINE


# Point to "Untouched" file Directory
BASEFILESDIR = os.getcwd()
ORIGLOC = '/BASEFILES/'
FUTLOC = '/AERMOD/'
SIMOUTLOC = '/SensitivityOutputs/'
SENSLOC = '/SensitivityInputs/'


# Opening .PFL File
try:
    PFL_delta = AFUN.openinpfile(BASEFILESDIR + ORIGLOC + PFL_name)
except:
    print "COULD NOT READ or FIND PFL FILE \n Please Place PFL File in BASEFILES Folder"
    
# Opening .SFC File
try:
    SFC_delta = AFUN.openinpfile(BASEFILESDIR + ORIGLOC + SFC_name)
except:
    print "COULD NOT READ or FIND SFC FILE \n Please Place SFC File in BASEFILES Folder"

SimulationDataOutput = []
# Create Loop for modifying each of the parameters... 
if CMBDSens == 0:       
    PFLSENSLISTVALS = AFUN.openinpfile(BASEFILESDIR + SENSLOC + 'SensPFL.txt')
    SFCSENSLISTVALS = AFUN.openinpfile(BASEFILESDIR + SENSLOC + 'SensSFC.txt')
    
    ################### Part 1: PFL
    try:
        os.remove(BASEFILESDIR+FUTLOC+PFL_name)
    except:
        pass
    #copy SFC file
    AFUN.INP_write(AFUN.openinpfile(BASEFILESDIR + ORIGLOC + SFC_name),BASEFILESDIR+FUTLOC+SFC_name)
    #change and copy PFL file
    if len(PFLSENSLISTVALS[0])>0:
        for ind,val in enumerate(PFLSENSLISTVALS):
            #print ind
            tempa = AFUN.openinpfile(BASEFILESDIR + ORIGLOC + PFL_name)
            tempa[int(val[0])-1][int(val[1])-1]=val[2]
            AFUN.INP_write(tempa,BASEFILESDIR+FUTLOC+PFL_name)        
            os.chdir(BASEFILESDIR + FUTLOC)
            subprocess.call(BASEFILESDIR + FUTLOC + 'AERMOD.exe')
            time.sleep(waittime)
            os.chdir(BASEFILESDIR+'/')
            temp_array = []
            for valprime in AFUN.openinpfile(BASEFILESDIR + FUTLOC + PLOT_name)[rows[0]-1:rows[1]]:
                temp_array.append(float(valprime[column-1]))
            
            SimulationDataOutput.append(temp_array)
            del tempa
            os.remove(BASEFILESDIR+FUTLOC+PFL_name)
        ################### Part 2: SFC
        try:
            os.remove(BASEFILESDIR+FUTLOC+SFC_name)
        except:
            pass        
    #copy PFL file
    AFUN.INP_write(AFUN.openinpfile(BASEFILESDIR + ORIGLOC + PFL_name),BASEFILESDIR+FUTLOC+PFL_name)
    #change and copy the SFC file
    if len(SFCSENSLISTVALS[0])>0:
        for ind,val in enumerate(SFCSENSLISTVALS):
            #print ind
            tempa = AFUN.openinpfile(BASEFILESDIR + ORIGLOC + SFC_name)
            tempa[int(val[0])-1][int(val[1])-1]=val[2]
            AFUN.INP_write(tempa,BASEFILESDIR+FUTLOC+SFC_name)
            os.chdir(BASEFILESDIR + FUTLOC)
            subprocess.call(BASEFILESDIR + FUTLOC + 'AERMOD.exe')
            time.sleep(waittime)
            os.chdir(BASEFILESDIR+'/')
            temp_array = []
            for valprime in AFUN.openinpfile(BASEFILESDIR + FUTLOC + PLOT_name)[rows[0]-1:rows[1]]:
                temp_array.append(float(valprime[column-1]))
            
            SimulationDataOutput.append(temp_array)
            del tempa
            os.remove(BASEFILESDIR+FUTLOC+SFC_name)
    try:        
        os.remove(BASEFILESDIR+FUTLOC+PFL_name)
    except:
        pass
    try:        
        os.remove(BASEFILESDIR+FUTLOC+SFC_name)
    except:
        pass    


elif CMBDSens == 1:
    COMBOSENSLISTVALS = AFUN.openinpfile(BASEFILESDIR + SENSLOC + 'SensPFLaSFC.txt')
    for ind,val in enumerate(COMBOSENSLISTVALS):
        if len(val) % 4 > 0:
            print 'Check line ' + str(ind+1) + ' in SensPFLaSFC.txt: SIMULATION SKIPPED!'
            temp_array = [0]*(rows[1]+1-rows[0])
            SimulationDataOutput.append(temp_array)
        else:
            #print 'hello'
            tempa = AFUN.openinpfile(BASEFILESDIR + ORIGLOC + PFL_name)
            tempb = AFUN.openinpfile(BASEFILESDIR + ORIGLOC + SFC_name)
            for i in range(len(val)/4):
                #print i, val[i*4]
                if val[i*4] in 'PFL':
                    tempa[int(val[i*4+1])-1][int(val[i*4+2])-1]=val[i*4+3]
                    #print tempa
                elif val[i*4] in 'SFC':
                    tempb[int(val[i*4+1])-1][int(val[i*4+2])-1]=val[i*4+3]
                    #print tempb
                    
            # moving/writing files                    
            AFUN.INP_write(tempa,BASEFILESDIR+FUTLOC+PFL_name)
            AFUN.INP_write(tempb,BASEFILESDIR+FUTLOC+SFC_name)
            os.chdir(BASEFILESDIR + FUTLOC)
            subprocess.call(BASEFILESDIR + FUTLOC + 'AERMOD.exe')
            time.sleep(waittime)
            os.chdir(BASEFILESDIR+'/')
            temp_array = []
            for valprime in AFUN.openinpfile(BASEFILESDIR + FUTLOC + PLOT_name)[rows[0]-1:rows[1]]:
                temp_array.append(float(valprime[column-1]))

            SimulationDataOutput.append(temp_array)                    
            del tempa
            del tempb
            os.remove(BASEFILESDIR+FUTLOC+PFL_name)
            os.remove(BASEFILESDIR+FUTLOC+SFC_name)    





if matlabexport == True:

    import numpy, scipy.io
    arr = numpy.array(SimulationDataOutput)
    scipy.io.savemat(os.getcwd()+SIMOUTLOC+'SENSRESULTS.mat', mdict={'arr': arr})
















































    
