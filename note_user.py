# class 활용 예제
from notebook import NoteBook
from notebook import Note

new_note = Note()
new_note.write_content("Don't cry. because I'm happy")

quote_book = NoteBook("The Quote Book")
quote_book.add_note(new_note)
quote_book.add_note(new_note)
quote_book.add_note(new_note)
quote_book.add_note(new_note)
quote_book.add_note(new_note)

print(quote_book.get_number_of_pages())

# quote_book.add_note(Note("Hellow, world"))
# quote_book.add_note(Note("Hellow, world"))
# quote_book.add_note(Note("Hellow, world"))

# print(quote_book.get_number_of_pages())

my_note = quote_book.remove_note(10)
print(my_note)
# my_note = quote_book.remove_note(1)
# print(my_note)
