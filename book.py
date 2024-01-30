import csv
import pandas as pd 


class Book:

    
    def __init__(self, name , number_page, date_chap, price, dis_count, subject):
        self.name = name
        self.number_page = number_page
        self.date_chap = date_chap
        self.price = price
        self.dis_count = dis_count
        self.subject = subject

    def __str__(self):
        return f"Book(name: {self.name}, number_page: {self.number_page}, date_chap: {self.date_chap}, price: {self.price}, dis_count: {self.dis_count}, subject {self.subject})"
book_list = []
while True:
    print('1 : add book')
    print('2 : remove book')
    print('3 : updte book name ')
    print('4 : show book')
    print('5 : search name book')
    print('6 : search price book')
    print('7 : updte book subject ')
    print('8 : exit')
    choice = input("please chose a number: ")
    if choice == '1':
        e_name = input('enter_name :')
        e_number_page = input('enter_number_page :')
        e_date_chap = input('enter_date_chap :')
        e_price = input('enter_price :')
        e_dis_count = input('enter_dis_count :')
        e_subject = input('enter_subject :')


        new_book = Book(e_name, e_number_page, e_date_chap, e_price, e_dis_count, e_subject)

        fields = ['name', 'number_page', 'date_chap', 'price', 'dis_count', 'subject']
        
        book_list.append(new_book)


        with open('book_name.csv', 'w') as file_book:
                writer = csv.DictWriter(file_book, fieldnames=fields)
                writer.writeheader()
                for book in book_list:
                    writer.writerow(vars(book))

    elif choice == '2':
        book_name_to_remove = input("the name for remove: ")
        data = pd.read_csv('book_name.csv')

        index_to_remove = data[data['name'] == book_name_to_remove].index
        data = data.drop(index_to_remove)
        data.to_csv('book_name.csv', index=False)

    elif choice == '3':
        book_name_to_update = input("Enter the name of the book: ")
        new_book_name = input("Enter the new name of the book to update: ")
        new_subject = input("Enter the new subject: ")
      
        data = pd.read_csv('book_name.csv')
        if any(data['name'] == book_name_to_update):

            if 'subject' not in data.columns:
                data['subject'] = ''
            data.loc[data['name'] == book_name_to_update, 'name'] = new_book_name
            data.loc[data['name'] == book_name_to_update, 'subject'] = new_subject
        
            data.to_csv('book_name.csv', index=False)  

    elif choice == '4':
        data = pd.read_csv('book_name.csv')
        print(data)
    elif choice == '5':
        book_name = input("Enter the name of the book: ")
        data = pd.read_csv('book_name.csv')
        search_result = data[data['name'].str.contains(book_name)]
        print(search_result)
    elif choice == '6':
        book_price = input("Enter the price of the book: ")
        data = pd.read_csv('book_name.csv')
        search_result = data[data['price']== float(book_price)]
        print(search_result)

    elif choice == '7':
        book_name_to_update = input("Enter the name of the book: ")
        new_subject = input("Enter the new subject: ")
      
        data = pd.read_csv('book_name.csv')
        if any(data['name'] == book_name_to_update):
            data.loc[data['name'] == book_name_to_update, 'subject'] = new_subject
        
            data.to_csv('book_name.csv', index=False)
    elif choice == '8':
        break  

