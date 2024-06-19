#geeks for geeks

def PalinArray(arr ,n):
    def reverse_integer(n):
    # Handle negative numbers
        sign = -1 if n < 0 else 1
        n = abs(n)
    
    # Convert to string, reverse, and convert back to integer
        reversed_int = int(str(n)[::-1])
    
        return sign * reversed_int
    # Code here
    i = 0
    while i!=n:
        if arr[i] == reverse_integer(arr[i]):
            i+=1
        else:
            return 0
    return 1
