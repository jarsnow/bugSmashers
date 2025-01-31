import sqlite3

# first step, connect to a database file (.db)
# also creates the file if it isn't found
connection = sqlite3.connect('py_database.db')

# next step is to create a cursor
# a cursor can execute sqlite statements, which you can fetch info from later
cursor = connection.cursor()

# sql statement to make a table (if it's not already there)
make_table = '''
    CREATE TABLE IF NOT EXISTS Students (
        FirstName TEXT,
        LastName TEXT,
        Birthday DATE,
        HoursSleptIn348 INTEGER );
    '''

# execute the command above on the database
# executions are like github commits
cursor.execute(make_table)

# sql statement to add a user to a database
add_john = "INSERT INTO Students VALUES ('John', 'Rader', 2005-04-01, 25);"
# values for every column is needed at time of insertion!

# what if I don't have values for a user,
# or just don't want to specify all the values right now?
# different formatting for strings allowed by python, useful for sql queries
add_andrew = ("INSERT "
              "INTO Students(FirstName, LastName, HoursSleptIn348) "  # notice, Birthday is not specified here
              "VALUES ('Andrew', 'Huang', 90);")

# no user has been added to the database yet!
# execute command (to do things for real)
cursor.execute(add_john)
cursor.execute(add_andrew)

# let's check to see that we actually did things
# sql command to get ALL information from the Students table
result = cursor.execute("SELECT * FROM Students;")

# get information back from the result, then print it
print(result.fetchall())

# save your changes!
# mentioned earlier that 'executes' are like github commits sql commits are like github pushes
# commit takes all the stored execute queries, then modifies the database file
connection.commit()

# good practice to close your open connections (in any scenario, not just sql)
connection.close()
