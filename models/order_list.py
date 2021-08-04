from models.order import *
from models.book import *

book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 750)
book2 = Book("Harry Potter and the Chamber of Secrets", "J.K. Rowling", 750)
book3 = Book("Harry Potter and the Prisoner of Azkaban", "J.K. Rowling", 750)

order1 = Order("John O'Neil", "2 August 2021", book1, book1.price)
order2 = Order("Sean O'Grady", "3 August 2020", book1, book1.price)
order3 = Order("Carrie Potter", "4 August 2019", book1, book1.price)
orders =[order1, order2, order3]