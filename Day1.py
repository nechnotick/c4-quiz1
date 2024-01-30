"""
@author: Neo Namane
"""

fruits = ["apple", "banana", "orange"]
size =[1, 2, 3]
fs = {
 'fruits':fruits,
 'size': size     
 }

df = pd.DataFrame(fs)
print(df)