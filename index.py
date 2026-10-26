name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}, you are {age} years old.")

rectangle_length = input("Enter the length of the rectangle: ")
rectangle_width = input("Enter the width of the rectangle: ")
calculated_area = int(rectangle_length) * int(rectangle_width)
print(f"The area of the rectangle is: {calculated_area}")

temperature_celsius = input("Enter the temperature in Celsius: ")
temperature_fahrenheit = (float(temperature_celsius) * 9/5) + 32
print(f"The temperature in Fahrenheit is: {temperature_fahrenheit:.2f}")