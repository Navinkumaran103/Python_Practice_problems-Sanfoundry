Binary to Gray Code:
n=int(input("Enter the binary: "), 2)
b= n>>1
gray= n ^ b
print(bin(gray)[2:])
Single-Bit Transitions
"Gray Code: Also called 'Reflected Binary.' 
Its primary goal is error prevention by ensuring only one bit state changes between consecutive numbers

