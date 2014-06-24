AERMOD Sensitivity Analysis Code v0.1 -- BRYANT E. MCDONNELL -- 11/12/13
Contact: bemcdonnell(a.t.) gmail.com


Prerequisites: Python 2.7
- Installation File is available at python.org .
- Then install NUMPY and SCIPY toolkits for Python..
- Windows Machine

_________________________________________________________________________________________
Script Details: AERMOD_IO.py

This Python Script was written to conduct a sensitivity analysis on AERMOD inputs and collects user defined data from the AERMOD output files. The script was originally created for a friend of mine to run several iterations of AERMOD with different input parameters and then export the data to MATLAB.  That basically summarizes the capabilities of the program. If you have any interest in taking this further, please feel free to do so. 

CHECKLIST:

The user should place *.PFL, and *.SFC files into the "BASEFILES" folder.

The user should place *.inp, and ALL other files associated with running AERMOD in the AERMOD folder.

AERMOD.exe should be placed into the AERMOD folder.

"Right-click" on the AERMOD_IO.py and choose edit with IDLE

The user should specify the rows and column to extract data from the *.out file.

_________________________________________________________________________________________

There are two options to run a sensitivity analysis...A single parameter sensitivity or multiple parameter sensitivity...

------------------------------------------
SINGLE VALUE SENSITIVITY:

Conceptually, using the 'SensPFL.txt' and 'SensSFC.txt' files, the user specifies the row number, column item number, and the "NEW" value for the sensitivity analysis. Each row is a separate simulation. 

The below technique would be used if the user would like to conduct a single value sensitivity analysis where only ONE value from EITHER the PFL or SFC file would be changed. The program will conduct a sensitivity on then PFL changes... then on the SFC changes.

METHOD 1: Vary one parameter in either PFL or SFC


For example: in 'SensPFL.txt', the file should look like this:
1 3 37.2
2 4 51.0
3 3 69.0

row 2, item 4 will be replaced as 51.0

-- and -- 

For example: in 'SensSFC.txt', the file should look like this:
4 3 37.2
4 4 51.0
4 5 -69.0

------------------------------------------
MULTIPLE VALUE SENSITIVITY

If the user would like to conduct a combination sensitivity analysis where each simulation would see changes to both a PFL and an SFC parameters, the user would setup the 'SensPFLaSFC.txt' with multiple statements in each row. As before, each row represents a simulation

METHOD 2: Vary multiple parameters in each simulation

for example:
PFL 1 3 37.2 PFL 2 4 51.0 SFC 4 3 37.2 SFC 4 5 51.0
PFL 1 3 37.2 PFL 2 4 51.0 SFC 4 3 37.2
PFL 2 4 51.0 SFC 4 3 37.2
PFL 1 3 37.2 PFL 2 4 51.0

-for the first simulation: In the PFL file, two items will be modified and in the SFC file, two items will be modified.The modified numbers must be written in one continuous row. 

-for the second simulation: In the PFL file, two items will be modified and in the SFC file, one item will be modified.The modified numbers must be written in one continuous row.
 
-for the third simulation: In the PFL file, one item will be modified and in the SFC file, one item will be modified.The modified numbers must be written in one continuous row. 

-for the forth simulation: In the PFL file, two items will be modified and in the SFC file, no items will be modified.The modified numbers must be written in one continuous row. 

_________________________________________________________________________________________
Once all the inputs are established correctly, and you have every file in the correct location, execute the AERMOD_IO.py script by pressing "F5"

Your data output should be visible in SensitivityOutputs as a MATLAB file
