# You can test your functions here if you like

import q1
import q2
import q3

# Write your final program below:

print("Let's solve the Towers of Hanoi puzzle! How many disks? ")
disk_number = q2.prompt_for_1_to_9()
print(q3.solve_hanoi(int(disk_number), 1, 3))