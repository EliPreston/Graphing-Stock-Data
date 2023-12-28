import requests
import sys
import dontpushme.key as my_api_key
import functions.pickle_data as pickle_data


def getAVData(time_specifier: str):
    
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    # url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=IBM&apikey='+my_api_key.__key__

    try:
        f_tickers = open('data/tsx_tickers.txt', 'r')
        f_error = open('data/tickers_w_errors.txt', 'a')
    except Exception as e:
        print("=> Error opening tsx_tickers.txt - check if this file exists in the specified path")
        print("=> Error: {}".format(e))
        sys.exit(1)
   
    count = 0
    for symbol in f_tickers:
        try:
            count += 1
            if ('.' in symbol):
                f_error.write(symbol)
            else:
                symbol = symbol.replace('\n', '')
                
                if (time_specifier == "monthly"):
                    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=TSX:'+symbol+'&apikey='+my_api_key.__key__
                    success = pickle_data.pickleData(time_specifier, url, symbol)
                    if (success == -1):
                        print("Daily request limit reached")
                        print("Tickers processed before limit reached: {}".format(count-1))
                        return
                
                # elif (time_specifier == "daily"):
                    # url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSX:'+symbol+'&apikey='+my_api_key.__key__
                    # print(url)
                    # success = pickle_data.pickleData(url, symbol)
                    # if (success == -1):
                    #     print("Daily request limit reached")
                    #     print("Tickers processed before limit reached: {}".format(count-1))
                    #     return
        except Exception as e:
            print("=> Error with request for ticker {}: {}".format(symbol, e))
            return
    f_tickers.close()
    f_error.close()


def tsxActiveStocks():
    print("\nUpdating tsx_tickers.txt......")

    try:
        url = 'https://www.tsx.com/json/company-directory/search/tsx/%5E*'
        r = requests.get(url)
        data = r.json()
    except Exception as e:
        print("=> Error accessing TSX directory:\n {}".format(e))
        sys.exit(2)

    try:
        f = open('data/tsx_tickers.txt', 'w')
    except Exception as e:
        print("=> Error writing to tsx_tickers.txt")
        print("=> Error: {}".format(e))
        sys.exit(3)
     
    for stock in data['results']:
        try:    
            f.write(stock['symbol']+"\n")
        except Exception as e:
            print("=> Error writing stock ticker to file:\n {}".format(e))
            sys.exit(4)
    f.close()
    
    print("=> All active/current TSX tickers written to ./data/tsx_tickers.txt\n")








# ************DUMP***************

    # 2. https://pypi.org/project/Yahoo-ticker-downloader/


    # 3.
    # import csv
    # CSV_URL = 'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey='+my_key

    # with requests.Session() as s:
    #     download = s.get(CSV_URL)
    #     decoded_content = download.content.decode('utf-8')
    #     cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    #     my_list = list(cr)

        # ['symbol', 'name', 'exchange', 'assetType', 'ipoDate', 'delistingDate', 'status']
        # for row in my_list:
        #     print(row)

        
    # try:
    #     symbol = 'IBM'
    #     symbol = symbol.replace('\n', '')
    #     url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=IBM&apikey=demo'
    #     pickle_data.pickleData(url, symbol)
    # except Exception as e:
    #     print("=> Error with request for ticker {}: {}".format(symbol, e))      