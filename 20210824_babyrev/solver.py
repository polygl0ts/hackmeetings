from string import ascii_uppercase, ascii_lowercase

check = [0x5f,0x40,0x5a,0x15,0x75,0x45,0x62,0x53,0x75,0x46,0x52,0x43,0x5f,0x75,0x50,0x52,0x75,0x5f,0x5c,0x4f]

# Reverse memfrob() XOR
decrypted_check = []
for c in check:
    decrypted_check.append(c^42)



# Finds the number of shifts for each position
def find_shifts():
    shifts = []
    for i in range(20):
        a = 4*i
        while(True):
            if is_prime(a):
                shifts.append(a % 26)
                break;
            a += 1
    return shifts

# Returns True if n is prime, else returns False
def is_prime(n):
    if n > 1:
        # check for factors
        for i in range(2,n):
            if (n % i) == 0:
                return False
        else:
            return True

        # if input number is less than
        # or equal to 1, it is not prime
    else:
        return False


shifts = find_shifts()

flag = "corctf{"

for i in range(20):
    c = decrypted_check[i]
    if c >= 65 and c <= 90 :
        flag += ascii_uppercase[(c - 65 - shifts[i]) % 26]
    elif c >= 97 and c <= 122:
        flag += ascii_lowercase[(c - 97 - shifts[i]) % 26]
    else: 
        flag+=(chr(c))
flag += "}"

print(flag)

