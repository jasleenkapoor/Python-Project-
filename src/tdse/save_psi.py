#parameters: array of np.square(np.abs(psi_list),a string that will separate the data, a file name for text file, True for axis, false for no axis
def writetxt(array,filename,spacedwith,txtaxis):# a function that takes the inputted array and outputs it, in the form of a text document, with an optional axis
    ''' Returns a textfile with all data points of psi for every time and space imcrement
    
    Parameters
    - - - - - - -
    array : multidimensional array
    
    filename: str
        name of textfile
    
    spacedwith: str
        Seperates all data points in the outputed txt file.
    
    txtaxis: Boolean
        Displays txt file axis to show time and space outputs.'''

    with open(filename, 'w') as file: #opens the file. 
        if txtaxis ==True:        
            file.writelines(" Psi in Time-->") 
            file.writelines("\n")
            file.writelines("Psi in Space")
            file.writelines("\n")
            file.writelines("|")
            file.writelines("\n")
            file.writelines("|")
            file.writelines("\n")
            file.writelines("\/")
            file.writelines("\n")
            for i in array:
                for j in i:
                    print(j)
                    file.write(str(j))
                    file.write(spacedwith)
                file.writelines("\n")
        return
