# 5. Count the number of words in a sentence.

s = "my name is Harshit Shrimali"
count = 1
for i in s :
  if i == " ":
    count += 1

print(f"Number of words in string : {count}")