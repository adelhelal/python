# Python
- Interpreted language "scripting" (code executed line by line)
- PEP - Python Enhancement Proposals - style guide
- PIP - Python Installer Package `pip install package`
  - PyPI.org - Python Package Index
- Python VM
  - CPython - interpreter and compiler - compiles Python code into bytecode before interpreting it
  - Python Memory Manager - manages memory of object and data structures in a private heap
    - "Stack frames" are allocated on the heap 
- Python special characters
  - `_identifier` -  (protected) non-public methods and instance variables
  - `__identifier` - (private) "mangled" to _ClassName__identifier to prevent access outside class or name clashes with subclass
  - `__method__()` - magic methods or dunder methods - invoked internally by Python on types e.g. int.__add__(int) used for int + int 
- Namespaces and Variable Scope
  - Built-In
  - Global
  - Enclosing
  - Local
- Pickling (Serializing) with `pickle.dump()` and `pickle.load()`
- REST API - Flask vs Django (realpython.com/api-integration-in-python)  
- Decorators
```
def lowercase_decorator(function):
   def wrapper():
       func = function()
       string_lowercase = func.lower()
       return string_lowercase
   return wrapper

@lowercase_decorator
def hello():
   return 'Hello World'   
```

## Machine Learning
### Libraries
- Numpy - multidimentional array (python)
- Pandas - data analysis with data frames / two-dimentional data structures (roes and columns)
```python
import pandas
data = pandas.read_csv('data.csv')
```
- MatPlotLib - two-dimentional plotting library for graphs
- Scikit-learn - decision trees / neural networks etc
```python
# train and test model
from sklearn.model_selection import train_test_split
input_train, input_test, output_train, output_test = train_test_split(data['input_column'], data['output_column'], test_size=0.2)
# make prediction
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(input_train, output_train)
predictions = model.predict(input_test)
# evaluate
from sklearn.metrics import accuracy_score
score = accuracy_score(output_test, predictions) # assert expected vs actual = score from 0-1
# persist model
sklearn.externals.joblib.dump(model, 'persisted_model.joblib')
model = sklearn.externals.joblib.load('persisted_model.joblib')
predictions = model.predict(input_test)
```

### Tools
- Anaconda for Jupyter
    - `$ jupyter notebook` > New > "Python 3" notebook
- Sample data
    - kaggle.com
