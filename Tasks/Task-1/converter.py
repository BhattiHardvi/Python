# Datatype Converter Program

# Take user input and convert it into int, float, str, and bool using type casting constructors.
#  Display datatype before and after conversion.

a = int(input("enter a value: "))
print("Before Conversion:", type(a))

b = int(a)
c = float(a)
d = str(a)
e = bool(a)

print("After Conversion:")

print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))