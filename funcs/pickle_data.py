try:
  import cPickle as pickle
except:
  import pickle

import requests
import sys
import json

def pickleData(time_specifier: str, url: str, ticker: str) -> int:
    print("\nRequesting data....")
    try:
        print('=> ' + url[:-16] + '****************' + '\n')
        data = requests.get(url).json()
        if (len(data) == 1):
            return -1
    except Exception as e:
        print("Error with url:\n{}".format(e))
        sys.exit(5)
# https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=TSX:HBD&apikey=9YJCBV2T3359UNA2
    print("Pickling data.......")

    if (time_specifier == "monthly"):
        try:
            fileNameMonthly = 'stockdata/pickled_data_monthly/pickled_data_monthly_'+ticker+'.bin'
            pickleFile = open(fileNameMonthly, 'wb')
            pickledData = pickle.dumps(data)
            pickleFile.write(pickledData)
            pickleFile.close()
        except Exception as e:
            print("Error pickling data:\n{}".format(e))
            sys.exit(6)
    
    # elif (time_specifier == "daily"):
    #     try:
    #         fileNameDaily = 'stockdata/pickled_data_daily/pickled_data_daily_'+ticker+'.bin'
    #         pickleFile = open(fileNameDaily, 'wb')
    #         pickledData = pickle.dumps(data)
    #         pickleFile.write(pickledData)
    #         pickleFile.close()
    #     except Exception as e:
    #         print("Error pickling data:\n{}".format(e))
    #         sys.exit(6)
    
    print("=> Data pickled in {}....\n\n".format(fileNameMonthly))
    return 1

# Accesses binary file associated with "ticker", retrieves/converts binary 
# data into human-readable format. Returns data (dictionary)
def unPickleMyData(time_specifier: str, ticker: str) -> dict:
    print("Unpickling data....")
    
    if (time_specifier == "monthly"):
        try:
            pickledFile = open('stockdata/pickled_data_monthly/pickled_data_monthly_'+ticker+'.bin', 'rb')
            data = pickle.load(pickledFile)
            # print(data)
            pickledFile.close()
            
        except Exception as e:
            print("Error unpickling data:\n{}".format(e))
            sys.exit(7)
    # elif (time_specifier == "daily"):
    #     try:
    #         pickledFile = open('stockdata/pickled_data_daily/pickled_data_daily_'+ticker+'.bin', 'rb')
    #         data = pickle.load(pickledFile)
    #         print(data)
    #         pickledFile.close()
            
    #     except Exception as e:
    #         print("Error unpickling data:\n{}".format(e))
    #         sys.exit(7)

    print("=> Data unpickled without error....\n")
    return data
    

