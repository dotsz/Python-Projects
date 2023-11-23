import q1
import q2
import q3
import q5
import q6

# Write any test code below
print(q1.num_letters("something", "s"))  # 1
print(q1.num_letters("mississippi", "s"))  # 4
print(q1.num_letters("miSsiSsippi", "S"))  # 4
print(q2.num_letters("mississippi", "si"))  # 8
print(q2.num_letters("mississippi", "ss"))  # 4
print(q2.num_letters("mississippi", ""))  # 0
print(q2.num_letters("", "s"))  # 0
print("")
print(q3.num_vowels("reAdY"))  # 3
print(q3.num_vowels("psychOlogy"))  # 4
print(q3.num_vowels("aeioUy"))  # 6
print(q3.num_vowels("aeiyyOu"))  # 7
print(q3.num_vowels("ympt"))  # 1
print(q3.num_vowels("wrYly"))  # 2
print(q3.num_vowels("Yesterday"))  #4
print("")
print(q5.shift("abcdef", 1))  # "fabcde"
print(q5.shift("abcdef", 4))  # "cdefab"
print(q5.shift("abcdef", 0))  # "abcdef"
print(q5.shift("abcdef", -1))  # "bcdefa"
print(q5.shift("abcdef", 7))  # "fabcde"
print("")
print(q6.cipher("Hello, world!", 1))  # Gdkkn, vnqkc!
print(q6.cipher("Hello, world!", 0))  # Hello, world!
print(q6.cipher("Hello, world!", -1))  # Ifmmp, xpsme!
print(q6.cipher("Hello, world!", 3))  # Ebiil, tloia!
print(q6.cipher("Hello, world!", 123))  # Olssv, dvysk!
print(q6.cipher("Hello, world!",
                234))  # Hello, world! (since 234 is a multiple of 26)
