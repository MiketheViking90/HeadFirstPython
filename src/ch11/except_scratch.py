import sys

def show_ecp():
    try:
        with open('myfile.txt') as fh:
            file_data = fh.read()
        print(file_data)
    except FileNotFoundError:
        print("file not found")
    except:
        print("some other error occured")

def exc_info_try():
    try:
        1/0
    except:
        err = sys.exc_info()
        for e in err:
            print(e)

def exc_info_try_2():
    try:
        1 / 0
    except Exception as exc:
        print(type(exc))

exc_info_try_2()