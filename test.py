import numpy as np
#import csv
#fields= ["time", "space", "psi"]
#rows = [ ['Nikhil', 'COE', '2', '9.0'], 
#         ['Sanchit', 'COE', '2', '9.1'], 
#         ['Aditya', 'IT', '2', '9.3'], 
#         ['Sagar', 'SE', '1', '9.5'], 
#         ['Prateek', 'MCE', '3', '7.8'], 
#         ['Sahil', 'EP', '2', '9.1']] 
#
#filename='test out put.txt'
#with open(filename, 'w') as csvfile:
#    csvwriter = csv.writer(csvfile) 
#        
#    # writing the fields 
#    csvwriter.writerow(fields) 
#        
#    # writing the data rows 
#    csvwriter.writerows(rows)


t_array=np.array([0,1,2,3,4,7,6,7,8,9])
x_array=np.array([0,1,2,3,4,5,6,7,8,9])
psi_list=np.array([1,2,1,4,1,2,2,1,9,4])

        
def writetxt(array1,array2,array3,spacedwith):
    fullarray = np.array([array1,array2,array3])
    fullarray = np.swapaxes(fullarray,0,1)
    with open('test output.txt', 'w') as fd:
        fd.writelines("Time Space Psi")
        fd.writelines("\n")  
        for j in array1:
            for i in fullarray[j,]:
                fd.writelines(str(i))
                fd.writelines(spacedwith)
            fd.writelines("\n")
        return
writetxt(t_array,x_array,psi_list," ")
        
#            if len(array1)!=len(array2):
#        return print("array lenths don't match")