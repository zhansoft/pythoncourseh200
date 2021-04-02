import sqlite3

dog = sqlite3.connect("example1.db")
c = dog.cursor()
r = [('c','a'),('a','b'), ('a','e'),('c','d'),
          ('c','f'),('f','g'), ('f','h'),('h','j'),
          ('h','i')]

c.execute('DROP TABLE IF EXISTS G')
c.execute('''CREATE TABLE G (Parent, Child)''')

c.executemany('INSERT INTO G VALUES (?,?)', r)


dog.commit()


q = lambda a, b: "SELECT G.Parent FROM G, (SELECT G.Parent, G.Child FROM G WHERE G.Child = '{0}') WHERE G.Child = '{1}'".format(a,b)  #TO DO: Implement Lambda function

print(c.execute(q('b','e')).fetchall())
print(c.execute(q('h','g')).fetchall())
print(c.execute(q('e','a')).fetchall())

dog.close()