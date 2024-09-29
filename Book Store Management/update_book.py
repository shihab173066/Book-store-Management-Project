def update_book(all_books):
    search_item = input("Enter title or ISBN or Author's name for Update book: ")
    
    matching_books = []
    
    for index, book in enumerate(all_books):
        if(search_item.lower() in book["title"].lower() or search_item.lower() in book["authors"].lower() or search_item.lower() in book["isbn"]):
            matching_books.append((index, book))
            
            print (f"{len(matching_books)}. Title: {book['title']} - Authors: {book['authors']} - ISBN: {book['isbn']} - Price: {book['price']} - Quantity: {book['quantity']}")
            
    if not matching_books:
        print("No books found to update ")
        return all_books
    
    try:
        selected_index = int(input("Enter the Index number of the book which you want to update: "))
        
        if selected_index <= 0:
            raise IndexError
        
        book_index = matching_books [selected_index - 1] [0]
        book_to_update = all_books [book_index]
        
        print("What do you want to update?")
        print("1. Title")
        print("2. Authors")
        print("3. ISBN")
        print("4. Year")
        print("5. Price")
        print("6. Quantity")
        
        update_choice = input("Enter your choice: ")
        
        if update_choice == "1":
            book_to_update['title'] = input("Enter new title: ")
        elif update_choice == "2":
            book_to_update['authors'] = input("Enter new authors: ")
        elif update_choice == "3":
            book_to_update['isbn'] = input("Enter new ISBN: ")
        elif update_choice == "4":
            book_to_update['year'] = input("Enter new year: ")
        elif update_choice == "5":
            book_to_update['price'] = float(input("Enter new price: "))
        elif update_choice == "6":
            book_to_update['quantity'] = int(input("Enter new quantity: "))
        else:
            print("Invalid choice")
        
        print(f"'{book_to_update['title']}' has been updated.")
        
    except(IndexError, ValueError):
        print("Invalid Input")
        
    return all_books