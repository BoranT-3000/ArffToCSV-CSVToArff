#########################################
# Project   : ARFF to CSV converter     #
# Created   : 21/10/22                  #
# Author    : Boran T.                  #
# Reason    : Why Not                   #
#########################################

# # # importing libraries
import os
import shutil
import pandas as pd
# https://github.com/haloboy777/arfftocsv


file_name = str(input('please enter arff extension file name: '))

# # Getting all the arff files from the current directory
files = [arff for arff in os.listdir('.') if arff.endswith(".arff")]

if file_name in files:
    original = file_name
    target = r'copy.txt'
    shutil.copyfile(original, target)

    # listing directories
    print ("The dir is: %s"%os.listdir(os.getcwd()))

    headers = []
    datas =[]
    row_content = []

    with open(target) as fp:
        print("[INFO] -> Data is collecting!")
        line_count = len(fp.readlines())
        print('[INFO] -> Total lines:', line_count)
        count = 0
        percentageSign = 0
        
        fp.seek(0) 
        Lines = fp.readlines()
        for line in Lines:
            count += 1
            if "@ATTRIBUTE" in line or "@attribute" in line:
                header = line.split()
                headers.append(header[1])
            elif "%" in line:
                percentageSign+=1
                continue
            elif "@data" in line or "@DATA" in line:
                continue
            elif "@relation" in line or "@relation" in line:
                continue
            else:
                replace_line = line.replace(',',' ').replace('\n','')
                data = replace_line.split()
                datas.append(data)

        # print(headers)
        # print(percentageSign)
        # print(datas)


    with open(target, 'w') as fp:
        lengthofheaders = len(headers)
        count = 0
        for name in headers:
            count +=1 
            name = str(name).replace('\'','')
            fp.write(f'{name}')

            # her hangi bir conversion hatası burdan çıkabilir 
            # çünkü sonda bir coma eksik şekilde yaptım
            if count == lengthofheaders:
                continue
            else:
                fp.write(',')
        fp.write("\n")
        

        # write datas to txt file
        for two in datas:
            data = str(two).replace("[","").replace("]","").replace("\'","")
            # print(f'{data}\n')
            fp.write(f'{str(data)}\n')


    # to get file name inorder to convert it to csv
    get_name_of_file = os.path.basename(target)
    read_file = pd.read_csv (target)
    read_file.to_csv (f'{os.path.splitext(file_name)[0]}.csv', index=None)


    # # inorder to delete file after conversion to csv
    if os.path.exists("copy.txt"):
        os.remove("copy.txt")
        print('[INFO] -> Copied file is deleted')
    else:
        print("[ERROR] -> The file does not exist")


    print('[INFO] -> Conversion Completed')
    # listing directories
    print ("The dir is after conversion: %s"%os.listdir(os.getcwd()))

else:
    print('File is not exist in the current dir.')


    
