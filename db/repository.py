from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def show_all_books(self):
        pass

    @abstractmethod
    def add_book(self, **kwargs):
        pass

    @abstractmethod
    def update_book(self, **kwargs):
        pass

    @abstractmethod
    def delete_book(self, index):
        pass

    @abstractmethod
    def show_authors(self):
        pass

    @abstractmethod
    def add_author(self, **kwargs):
        pass

    @abstractmethod
    def find_book(self, **kwargs):
        pass

    def get_book_by_exact_name(self, **kwargs):
        pass
