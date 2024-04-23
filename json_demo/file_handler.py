import json
def read_data_from_json(file_path):
    try:
        fileobj = open(file_path, 'r')
        data = json.load(fileobj)
    except Exception as e:
        print(e)
        return []
    else:
        return data



def read_data_from_file(file_path):
    try:
        with open(file_path, 'r') as fileobj:
            val  = fileobj.read()
            return val
    except Exception as e:
        return False

def save_data_to_file(file_path, val):
    try:
        with open(file_path, 'w') as fileobj:
            fileobj.write(str(val))
            return True
    except Exception as e:
        return False

def save_data_to_json(file_path, data):
    old_books = read_data_from_json(file_path)
    # print(f"old book, {old_books}")
    old_books.append(data)
    try:
        with open(file_path, 'w') as fileobj:
            json.dump(old_books, fileobj)
            return True
    except Exception as e:
        print("eeeee")
        return False



if __name__ == '__main__':
    res = read_data_from_json('books.json')
    print(res)
