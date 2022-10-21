#########################################
# Project   : CSV to ARFF converter     #
# Created   : 20/10/22                  #
# Author    : Boran T.                  #
# Reason    : Why Not                   #
#########################################

# Importing library
import pandas as pd
import numpy as np

def main():

    def arff(breast):
        #this code line for getting the name of file
        head, sep, tail = file_name.partition('.')
    
        print('[INFO] -- Convertion -> [Started]')

        #open file in w+ mode
        f = open(f"{head}.arff",'w+')
    
        f.write(f'@relation {head}\n')

        # what's the datatype of the columns
        for name in breast.head(0):
            if 'Unnamed: 32' == name:
                breast.drop('Unnamed: 32', axis=1, inplace=True)
                continue
            f.write(f'@attribute\t  \'{name}\' ')
        
            if breast[f"{name}"].dtype == np.int64:
                f.write('\tinteger')
        
            elif breast[f"{name}"].dtype == np.float64:
                f.write('\tnumeric')
        
            elif breast[f"{name}"].dtype == np.object0:
                f.write(f'\t{breast[f"{name}"].unique()}')

            elif breast[f"{name}"].dtype == np.str0:
                f.write(f'\tstring')

            f.write('\n')

        # how many instances in excel write as comment
        f.write(f'@data\n%\n% Instances ({len(breast.axes[0])}):\n%\n')

        # this part is for writing datas
        for row in range(1,len(breast.axes[0])):
            for_comma = len(breast.iloc[row])
            count = 0
            for name in breast.iloc[row].tolist():
                count +=1 

                f.write(f'{name}')
            
                if count == for_comma:
                    continue
                else:
                    f.write(', ')
           
            f.write('\n')
    
        f.close()
        print('[INFO] -- Convertion -> [Ended]')



    # for file input and diff. excel extensions
    file_name = str(input('Please Enter excel file name: '))
    if 'csv' in file_name:
        breast = pd.read_csv(file_name)
        arff(breast)
    elif 'xlsx' in file_name:
        breast =  pd.read_excel(file_name)
        arff(breast)
    else:
        print('[Error] -- file you\'ve entered is not in correct format')


# inorder to work with main
if __name__ == "__main__":
    main()