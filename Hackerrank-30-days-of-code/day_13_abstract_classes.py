from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):

    def __init__(self, _title, _author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self):
        pass


class MyBook(Book):

    def __init__(self, _title, _author, _price):
        super().__init__(_title, _author)
        self.price = _price

    def display(self):
        print("Title: {0}\nAuthor: {1}\nPrice: {2}".format(self.title, self.author, self.price))


if __name__ == '__main__':
    title = input()
    author = input()
    price = int(input())
    new_novel = MyBook(title, author, price)
    new_novel.display()
