import pandas as pd
from sklearn import linear_model
import tkinter as tk 

df = pd.read_csv("E:/tinkter taturiol/Python-tkinter-based-stock-prediction-application-using-Multiple-Linear-Regression-master/HDFC.csv")

X = df[['Open','Close']] # here we have 2 variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets
Y = df['Turnover']

# with sklearn
regr = linear_model.LinearRegression()
regr.fit(X, Y)
print(regr.score(X, Y))

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

# tkinter GUI
root= tk.Tk()
root.title("Stock price predication\n")

canvas1 = tk.Canvas(root, width = 500, height = 300)
canvas1.pack()

# with sklearn
Intercept_result = ('Intercept: ', regr.intercept_)
label_Intercept = tk.Label(root, text=Intercept_result, justify = 'center')
canvas1.create_window(260, 220, window=label_Intercept)

# with sklearn
Coefficients_result  = ('Coefficients: ', regr.coef_)
label_Coefficients = tk.Label(root, text=Coefficients_result, justify = 'center')
canvas1.create_window(260, 240, window=label_Coefficients)

# New_Interest_Rate label and input box
label1 = tk.Label(root, text='Open price rate: \n')
canvas1.create_window(120, 100, window=label1)

entry1 = tk.Entry (root) # create 1st entry box
canvas1.create_window(270, 100, window=entry1)

# New_Unemployment_Rate label and input box
label2 = tk.Label(root, text='Close price  rate: \n')
canvas1.create_window(120, 120, window=label2)

entry2 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 120, window=entry2)

def values(): 
    global Open #our 1st input variable
    Open = float(entry1.get()) 
    
    global Close #our 2nd input variable
    Close = float(entry2.get()) 
    
    Prediction_result  = ('Predicted Stock Turnover: ', regr.predict([[Open ,Close]]))
    label_Prediction = tk.Label(root, text= Prediction_result, bg='red')
    canvas1.create_window(260, 280, window=label_Prediction)
    
button1 = tk.Button (root, text='Predict Stock Turnover Price',command=values, bg='red') # button to call the 'values' command above 
canvas1.create_window(270, 150, window=button1)
 

root.mainloop()
