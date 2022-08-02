def read_text_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.read()
    print("data")