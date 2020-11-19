sistemas = ['windows', 'macos', 'linux', 'solaris', 'ios']

a_file = open("exec2_output_joafl.txt", "w")
text = "=== exec2 joao lopes ===\n"
print(text, file=a_file)

print("*** for ***")
print("*** for ***", file=a_file)
for x in sistemas:
	if (x != 'solaris'):
		str = "ciclo one: " + x
		print(str)
		print(str, file=a_file) 


print("\n\n*** while ***")
print("\n\n*** while ***", file=a_file)
count = 0
while (count < len(sistemas)):
	if (sistemas[count] != 'solaris'):
		str = "ciclo two: " + sistemas[count]
		print(str)
		print(str, file=a_file)
	count = count + 1

a_file.close()