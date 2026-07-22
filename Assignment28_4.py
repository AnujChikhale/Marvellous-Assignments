original_file = open("Demo.txt", "r")
copy_file = open("copy.txt", "w")

original_data = original_file.read()
copy_file.write(original_data)

original_file.close()
copy_file.close()