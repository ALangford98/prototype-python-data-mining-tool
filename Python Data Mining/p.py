import csv
import pandas as pd
import numpy as np
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter as tk

# file = pd.read_csv('All_sales.csv')
# df = pd.DataFrame(file)
# month1 = df.head(89)
# month12 = df.head(89)
# m1SALES = sum(month1['SALES QUANTITY'])
# m12SALES = sum(month12['SALES QUANTITY'])

# data = [m1SALES, m12SALES]
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# period = ['First Month', 'Last Month']
# ax.bar(period,data)
# plt.xlabel("PERIOD")
# plt.ylabel("SALES QUANTITY")
# percChange = (m12SALES - m1SALES) / m1SALES *100

# plt.show()
# print(round(percChange, 1),'percent increase in items sold')

# salesAmt = pd.read_csv('SalesAmount.csv')
# fig, ax = plt.subplots(figsize=(20, 6))
# ax.plot(salesAmt['DATE'], salesAmt['SALES AMOUNT'])

# QuantitySales = pd.read_csv('SalesQuantityProducts.csv')
# fig, x = plt.subplots(figsize=(910, 6))
# x.plot(QuantitySales['PRODUCT DESCRIPTION'], QuantitySales['SALES QUANTITY'])


# salesAmt = pd.read_csv('SalesQuantity.csv')
# fig, ax = plt.subplots(figsize=(20, 6))
# ax.bar(salesAmt['DATE'], salesAmt['SALES QUANTITY'])


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.salesQt = tk.Button(self, text="Sales Quantity")
        self.salesQt.pack(side="top")
        self.salesQt["command"] = self.salesQ

        self.salesAm = tk.Button(self, text="Sales Amount by Quantity")
        self.salesAm.pack(side="top")
        self.salesAm["command"] = self.salesA

        self.salesAmount = tk.Button(self, text="Sales Amount")
        self.salesAmount.pack(side="top")
        self.salesAmount["command"] = self.salesQu

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        
    def salesQ(self):
        QuantitySales = pd.read_csv('SalesQuantityProducts.csv')
        fig, x = plt.subplots(figsize=(910, 6))
        x.plot(QuantitySales['PRODUCT DESCRIPTION'], QuantitySales['SALES QUANTITY'])
        plt.show()

    def salesA(self):
        salesAmt = pd.read_csv('SalesAmount.csv')
        fig, ax = plt.subplots(figsize=(20, 6))
        ax.bar(salesAmt['DATE'], salesAmt['SALES AMOUNT'])
        plt.show()

    def salesQu(self):
        salesAmount = pd.read_csv('SalesQuantity.csv')
        fig, a = plt.subplots(figsize=(20, 6))
        a.plot(salesAmount['DATE'], salesAmount['SALES QUANTITY'])
        plt.show()

root = tk.Tk()
app = Application(master=root)
app.mainloop()





