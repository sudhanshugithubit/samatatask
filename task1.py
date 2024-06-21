def calculate_area(length, width):
    if length == width:
        return "This is a square!"
    else:
        return length * width

def sudhanshu():
    try:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        
        result = calculate_area(length, width)
        print(result)
    except ValueError:
        print("Please enter valid numerical values for length and width.")


if __name__ == "__main__":
    sudhanshu()