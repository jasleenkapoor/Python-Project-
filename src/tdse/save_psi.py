#parameters: array of np.square(np.abs(psi_list),a string that will separate the data, a file name for text file, True for axis, false for no axis
def writetxt(array,filename,spacedwith,txtaxis):# a function that takes the inputted array and outputs it, in the form of a text document, with an optional axis
    with open(filename, 'w') as file:
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
