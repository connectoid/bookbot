BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050


book: dict[int, str] = {}

def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    ends = [',', '.', '!', ':', ';', '?']
    if start+size < len(text) and text[start+size] == text[start+size-1] == '.':
        part_string = text[start:start + size]
        part_string = part_string[:-2]
    else:
        part_string = text[start:start + size]
    while part_string[-1] not in ends:
        part_string = part_string[:-1]
    
    part_size = len(part_string)
    return part_string, part_size

def prepare_book(path):
    start = 0
    page_number = 1
    with open(path) as f:
        text = f.read()
        while start < len(text):
            page, part_size = _get_part_text(text, start, PAGE_SIZE)
            book[page_number] = page.lstrip()
            start = start + part_size + 1
            page_number += 1

prepare_book(BOOK_PATH)
