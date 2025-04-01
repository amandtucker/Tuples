Books = ['English','Computer programming', 'Oracle','VB.Net']
print(type(Books))
print (Books)
Books[1]='Mathematics'
print(Books[1:3])
print(Books[-3:-2])
#List packing 
Book1, Book2, Book3, Book4 = Books
print(Book1)

del Books [1]
print(Books)

Books.remove('VB.Net')
print(Books)

print(Books.pop(1))
print(Books)

