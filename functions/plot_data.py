import json
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui


from collections import deque
from PyQt6 import QtWidgets

import functions.pickle_data as pickle_data


# https://pyqtgraph.readthedocs.io/en/latest/getting_started/plotting.html
# https://www.pythonguis.com/tutorials/plotting-pyqtgraph/


class GraphWindow():
    def __init__(self, ticker: str, x_vals: list, y_vals: list) -> None:
        
        
        # create plot window object
        plt = pg.plot()
        plt.setGeometry(100, 100, 1000, 700)
        
        # showing x and y grids
        plt.showGrid(x = True, y = True)
        
        # adding legend
        plt.addLegend()
        
        # set properties of the label for y axis
        plt.setLabel('left', 'Vertical Values', units ='y')
        
        # set properties of the label for x axis
        plt.setLabel('bottom', 'Horizontal Values', units ='s')

        m = [i for i in range(len(x_vals))]
        m_labels = [
            # Generate a list of tuples (x_value, x_label)
            (m[i], x_vals[i])
            for i in range(len(x_vals)) 
        ]
        
        # setting horizontal range
        plt.setXRange(0, len(x_vals))
        
        # setting vertical range
        plt.setYRange(0, max(y_vals) + 5)
        
        # setting window title
        plt.setWindowTitle(ticker)
        
        # ploting line in green color
        line1 = plt.plot(m, y_vals, pen ='g', labels=m_labels, symbol ='x', symbolPen ='g',
                                symbolBrush = 0.2, name ='monthly closes')
        plt.getPlotItem().getAxis('bottom').setTicks([m_labels])



def plotMyData(time_specifier: str, ticker: str) -> tuple:

    ticker_data = pickle_data.unPickleMyData(time_specifier, ticker)

    match time_specifier:
        case "monthly":

            month_dict = ticker_data['Monthly Adjusted Time Series']
            
            x_vals = deque()
            y_vals = np.array([])
            
            for month in month_dict:
                x_vals.appendleft(month)
                # y_vals = np.append(y_vals, float(month_dict[month]['4. close']))
                y_vals = np.concatenate(([float(month_dict[month]['4. close'])], y_vals))
            x_vals = list(x_vals)
            


            test = GraphWindow(ticker, x_vals, y_vals)
            QtGui.QGuiApplication.exec()
            
            # print(type(x_vals))
            # print(type(y_vals))
            return x_vals, y_vals

            
        # case "daily":
        #     day_dict = ticker_data[]
    
    return


