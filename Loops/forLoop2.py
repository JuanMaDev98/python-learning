numbers = [1,2,5,10,3,0,4,45]
x = None
y = 0

# Iterate through numbers list
for i in numbers:
    if x == None:
        x = i
    # Find the maximum value
    if i > x:
        x = i

# Iterate through numbers list again
for i in numbers:
    # Increment y by 1
    y += 1
    # If current number is not the maximum value, skip to the next iteration
    if i != x:
        continue    
    # Break out of the loop when the maximum value is found
    break
    
# Print the position and value of the maximum number
print("El mayor valor se encuentra en la posición",y, "y es",x) 