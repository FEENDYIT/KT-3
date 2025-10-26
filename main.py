import csv
import re

def clean_text(text):

    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', text).strip()

def get_books(filename):

    with open(filename, encoding='utf-8', newline='') as f:
        reader = csv.reader(f, delimiter='|')
        rows = list(reader)

        data = rows[1:]
        parse_row = lambda r: [            r,
            clean_text(r[1]),
            clean_text(r[2]),
            int(r[3]),
            round(float(r[4]), 2)
        ]
        return list(map(parse_row, data))

def filtered_books(books, keyword):

    keyword = keyword.lower()
    filtered = filter(lambda b: keyword in b[1].lower(), books)
    transform = lambda b: [b, f"{b[1]}, {b[2]}", b[3], b[4]]
    return list(map(transform, filtered))

def calculate_totals(filtered_books_list):

    return list(map(lambda b: (b, round(b[2] * b[3], 2)), filtered_books_list))

if __name__ == '__main__':
    filename = 'books.csv'
    books = get_books(filename)

    filtered = filtered_books(books, 'python')

    totals = calculate_totals(filtered)

    print('')
    print(books[:3])
    print('\n')
    print(filtered[:3])
    print('\n')
    print(totals[:3])