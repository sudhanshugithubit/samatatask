def generate_fibonacci(n):
    if n <= 0:
        return "Please enter a positive integer."
    
    fibonacci_sequence = []
    
    if n >= 1:
        fibonacci_sequence.append(0)
    if n >= 2:
        fibonacci_sequence.append(1)
    
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    
    return fibonacci_sequence

def greet():
    try:
        n = int(input("Enter the number of terms: "))
        
        fibonacci_sequence = generate_fibonacci(n)
        print("Fibonacci sequence:")
        print(fibonacci_sequence)
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    greet()