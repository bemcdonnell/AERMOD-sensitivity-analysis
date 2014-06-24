# This script writes an input file.

def INP_write(lines, directory_file_output):
    with open(directory_file_output, 'w') as inp_file:
        try:
            #print 'here'
            for line in lines:
                #inp_file.writelines('\t'.join(line) + '\n')# for i in line)
                inp_file.write('\t'.join(line) + '\n')# for i in line)
        except:
            print 'Writing to INP Failed'
            inp_file.close()
            
    inp_file.close()
# setup to return file building errors




def retrieve_section_simulation(lines,mx_split = -1):
    temp = []
    for line in lines:
            if not line.startswith(';'):
                temp.append(line.split(None,mx_split))
    return temp   

##def runAERMOD(executefile):
##    execfile(

def openinpfile(loc):
    with open(loc,'r') as fldat:
        lines = fldat.read().splitlines()
    fldat.close()
    output = retrieve_section_simulation(lines)
    return output


def copy_file(path):
    '''copy_file(string)

    Import the needed functions.
    Assert that the path is a file.
    Return all file data.'''
    from os.path import basename, isfile
    assert isfile(path)
    return (basename(path), file(path, 'rb', 0).read())

def paste_file(file_object, path):
    '''paste_file(tuple, string)

    Import needed functions.
    Assert that the path is a directory.
    Create all file data.'''
    from os.path import isdir, join
    assert isdir(path)
    file(join(path, file_object[0]), 'wb', 0).write(file_object[1])
