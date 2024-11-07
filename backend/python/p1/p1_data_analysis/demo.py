import pandas as pd
import pandas_datareader as pdr # remote access data reader
import matplotlib as mat
import matplotlib.pyplot as plt
import datetime  # datetime is an object that you can call classes like date and time. those class then have their own functions

def get_requirements():
    print("\nDeveloper: Logan Moecher")

    print("\nProgram Requirements"
        +"\n1. Run demo.py")

    print("\nProgram Requirements:")
    print("\n1. Run demo.py"

        +"\n2. If errors, more than likely missing installations."
        +"\n3. Test Python Package installer: pip freeze"
        +"\n4. Research how to do the following installations: \n"
        +"\ta. pandas (only if mising)\n"
        +"\tb. pandas-datareader (only if missing)\n"
        +"\tc. matplot\n"

        +"\n5. Create at least three functions.\n"

        +"\ta. main(): calls at least two other functions.\n"
        +"\tb. get_requirements(): displays the program requirements.\n"
        +"\tc. data_analysis(): displays the following data.\n")

def data_analysis():
    start = datetime.datetime(2010, 1, 1)
    end = datetime.date.today()

    # read data into Pandas dataframe
    df = pdr.DataReader('XOM', 'yahoo', start, end) #remote data access

# convert to pandas module from DataReader
#df1 = pd.DataFrame.from_records(df) #put information into a pandas DataFrame
    print("Print number of records")
    print(df.shape[0])
    print()

    print("print columns")
    print(df.columns)
    print()

    print("Print dataframe")
    print(df[0:60])
    print(df.shape)
    print()

    print('Print first 5 lines')
    print(df[0:5])
    print()

    print('Print last 5 lines')
    print(df[-6:-1])
    print()

    print('Print first 2 lines')
    print(df[0:2])
    print()

    print('Print last 2 lines')
    print(df[-3:-1])

    #Plot using matplotlib.pyplot class
    plt.style.use('ggplot')
    df['High'].plot()
    df['Adj Close'].plot()
    plt.legend()
    plt.show()

