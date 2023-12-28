# Graphing-Stock-Data
## A little side project using AlphaVantage's stock API, pickle/cpickle, and Pyqtgraph
Not finished, but a fun mini project to play around with

### Main Function(s)
- Requesting/retreiving the the Toronto Stock Exchange's (TSX) active trading ticker symbols and storing these strings in a text file locally
- Requesting/retrieving data from AlphaVantage in JSON form
- Convertin, or "pickling", the data from JSON/python dict. (an arbitrary Python object) into a series of bytes and storing that in a binary file locally
- Accessing, or "unpickling", the binary file of a specifc ticker symbol and graphing the data using Pyqtgraph