#parameters: array of np.square(np.abs(psi_list),a string that will seperate the data, a file name for txt, Ture for axis, Talse for no axis
def writetxt(array,filename,spacedwith,txtaxis):# a function that takes the inputed array and outputs it in the form of a txt document, with an optional axis
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