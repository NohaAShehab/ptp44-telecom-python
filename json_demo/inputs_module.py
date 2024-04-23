from file_handler import read_data_from_file, save_data_to_file
def ask_for_int(message='Please enter a number'):
    while True:
        try:
            num= int(input(message))
        except Exception as e :
            print("please enter valid number")
        else:
            if num > 0:
                return num
            print("---- no of pages must be greater than zero")



def ask_for_string(message='Please enter a string'):
    while True:
        input_str = input(message)
        if input_str and not input_str.isspace():
            return input_str
        print("---- name mustn't be empty or spaces")




import time
def generate_id():
    id = round(time.time())
    print(id)

def generate_id_from_file():
    id = read_data_from_file("count")
    if id.isdigit():
        id = int(id) +1
        save_data_to_file('count',id)
        return id
    return False

if __name__ == '__main__':
    generate_id()












