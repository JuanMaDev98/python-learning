
#Puedes usar este código para saber exactamente que error es por el que salta el try except

try:
    res = 190 / 0
except Exception as error:
    # handle the exception
    print("An exception occurred:", error) # An exception occurred: division by zero

try:
  print("Here's variable x:", x)
except Exception as error:
  print("An error occurred:", error) # An error occurred: name 'x' is not defined
  
  
#Este codigo se usa para retornar la exception que levanta
  
try:
    res = 190 / 0
except Exception as error:
    # handle the exception
    print("An exception occurred:", type(error).__name__) # An exception occurred: ZeroDivisionError

try:
  print("Here's variable x:", x)
except Exception as error:
  print("An error occurred:", type(error).__name__) # An error occurred: NameError

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  