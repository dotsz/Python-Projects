base = 3000  # in cm  - "," symbol doesn't work as thousand separator
height = 1000  # in cm - "," symbol doesn't work as thousand separator
volume = 1 / 3 * base**2 * height  # added * in between 1/3 and base so it can multiply.
# Added ** operator to exponentiate base to 2

print(
    "The volume of a square pyramid with base " + str(base) +
    "cm and height " + str(height) + "cm is " + str(volume) + "cm^3"
)  # converted base, height, and volume variables into string to be able to concatenate.
# It would be a runtime error if I don't add the string 'str()' conversion before concatenation -
# As the error would occur when it attempts to concatenate non-string data type.
