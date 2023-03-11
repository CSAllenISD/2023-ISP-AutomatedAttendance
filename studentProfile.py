import pandas as pd

#This is just a model for each student profile that will be stored in the database via the API
name = 'firstName' + ' ' + 'lastName'
data = {'firstName': ['Oliver'], 'lastName': ['Hankins'], 'contactInformation': ['{name}@student.allenisd.org'], 'Picture': ['{firstName}_{lastName}.jpg']}

df = pd.DataFrame(data)
df.head()
