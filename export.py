import pandas as pd

import sys

def export(file, company) :
    # making data frame from csv file
    data = pd.read_csv(file, index_col="SYMBOL")

    # retrieving row by loc method
    first = data.loc[company]
    print(first)

    df = pd.DataFrame(first)

    # STEP 3 : OUTPUT directory location for all the .csv files obtained
    df.to_csv('/Users/nex/Desktop/companydir/' + company + '.csv')

if __name__ == '__main__':
    # STEP 1 : Please pass your file path here -> This will consists of all the companies that you wish to generate .csv files from
    f = open('/Users/nihantg/Desktop/company.txt')
    i=0
    for readline in f:
        values = readline.split("\n")
        print(values[0])

        # STEP 2 : This is the combined.csv file path (Please define yours)
        export("/Users/nex/Downloads/combined.csv", values[0])

