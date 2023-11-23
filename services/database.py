import pyodbc

server = 'DESKTOP-UTVRFMC\SQL'
database = 'crud_python'
#username = 'DESKTOP-UTVRFMC\João Saraiva'
#password = '00000000'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
cursor = cnxn.cursor()