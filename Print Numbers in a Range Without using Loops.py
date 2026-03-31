def func(num, temp=1):
   
    if(temp==num+1):
        return True
        
    print(temp)
    return func(num,temp+1)
    

n=int(input("Enter the number: "))
func(n)

''''
Recursion is not just a loop; it is a stack of tasks. When a function calls itself, the current execution is "paused" and placed on the Call Stack.
Stack Memory: A dedicated area in RAM that follows LIFO (Last-In, First-Out) logic.
Stack Frame: Each "pause" creates a frame containing the local variables (like upper) and a "bookmark" (Instruction Pointer) showing where to restart.
Variables defined inside a recursive function are RESET every time the function calls itself. To keep a 'running total' or 'counter,' I must pass that variable as an argument in the function call.
''''
