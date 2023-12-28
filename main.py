import sys
import functions.get_data as get_data
import functions.pickle_data as pickle_data
import functions.plot_data as plot_data


'''
Helper functions for main
'''

# Prompts used for what option/process they want to preform
# and performs that branch of processes
def chooseOption() -> None:
    print("Options: ")
    print("1 => Unpickle data (raw) \n2 => Plot data")
    perform_analysis = input("Which calculation should be done? ")
    
    match perform_analysis.lower():
        case '1':
            time_specifier = input("Get monthly or daily stock data? (monthly/daily) ")
            chosen_ticker = input("Enter ticker: ")
            ticker_data = pickle_data.unPickleMyData(time_specifier.lower(), chosen_ticker.upper())
            return

        case '2':
            time_specifier = input("Get monthly or daily stock data? (monthly/daily) ")
            chosen_ticker = input("Enter ticker: ")
            plot_data.plotMyData(time_specifier.lower(), chosen_ticker.upper())
            return

        case 'q' | 'e':
            print("quitting/exiting...")
        case _:
            print("Invalid option... exiting...")
            sys.exit(1)

# Checks command line arguments.
# Main can be called with up to 3 CLAs, all either 1 or 0
# These arguments just skip having to enter 'n' (no) to the
# program asking if you want to re-retrieve all tickers and
# pickle all the data from AlphaVantage
def checkCLAs() -> None:

    validArgs = [False, False, False]
    if (len(sys.argv) > 1):
        
        try:
            match sys.argv[1]:
                case '1':
                    validArgs[0] = True
                    print("Updating TSX active stocks (local) list")
                    get_data.tsxActiveStocks()
                case '0':
                    validArgs[0] = True
                case _:
                    validArgs[0] = False    
        except Exception as e:
            print("Error thrown: {}".format(e))       
        
        try:
            match sys.argv[2]:
                case '1':
                    validArgs[1] = True
                    print("Retrieving & pickle-ing AlphaVantage data")
                    time_specifier = input("Get monthly or daily stock data? (monthly/daily) ")
                    get_data.getAVData(time_specifier)
                case '0':
                    validArgs[1] = True
                case _:
                    validArgs[1] = False
        except Exception as e:
            print("Error thrown: {}".format(e))       
    
        try:
            match sys.argv[3]:
                case '1':
                    validArgs[2] = True
                    chooseOption()
                case '0':
                    validArgs[2] = True
                case _:
                    validArgs[2] = False
        except Exception as e:
            print("Error thrown: {}".format(e))

        # try:
        #     if (sys.argv[3] == '1'):
        #         validArgs[2] = True
        #         chooseOption()
        #     elif (sys.argv[3] == '0'):
        #         validArgs[2] = True
        # except Exception as e:
        #     print(e)
        #     validArgs[2] = False


    if ((validArgs[0] == False) or (validArgs[1] == False) or (validArgs[2] == False)):
        print("One or more arguments passed are invalid/incorrect, only 0 or 1 are acceptable.\n")

    # if (validArgs[0] == False):
    #     update_active_stocks = input("Get most recent list of active TSX stocks? [y/n] ")
    #     match update_active_stocks.lower():
    #         case "y":
    #             get_data.tsxActiveStocks()
    #         case "n":
    #             print("Continuing...\n\n")
    #         case _:
    #             print("Invalid option, continue with program or ctr+c and start again.\n")

    # if (validArgs[1] == False):
    #     pickle_all_data = input("Pickle TSX data from alphavantage? [y/n] ")
    #     match pickle_all_data.lower():
    #         case "y":
    #             get_data.getAVData()
    #         case "n":
    #             print("Continuing...\n\n")
    #         case _:
    #             print("Invalid option, continue with program or ctr+c and start again.\n")
    
    # if (validArgs[2] == False):
    #     chooseOption()
    

'''
Main
'''
if __name__ == "__main__":
    print("Running....\n")
    
    checkCLAs()
    
    

