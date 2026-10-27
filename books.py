from dataclasses import dataclass


@dataclass(frozen=True)
class Book:
    title: str
    author: str


books_to_read = [
    Book(title="三体", author="刘慈欣"),
    Book(title="活着", author="余华"),
    Book(title="百年孤独", author="加西亚·马尔克斯"),
]


if __name__ == "__main__":
    for book in books_to_read:
        print(f"{book.title} - {book.author}")
