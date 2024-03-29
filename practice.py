text = input("Enter a paragraph/text: ")
#tokenization 
individual_words = text.split()
print(individual_words)
#tracking number of occurences of each word
word_count = []

for word in individual_words:
    #indicating that we haven't found the word in the word_count yet
    found = False
    #iterating over every item in the word_count
    for item in word_count:
        #if word found in word_count in item[0], increment the count 
        if word == item[0]:
            item[1] += 1
            #found is set to True bcoz word is found in word_count, exist inner loop
            found = True
            break
    #if word not found in word_count, then it is it's 1st occurrence. Hence append it to word_count 
    if not found:
        word_count.append([word,1])
#iterating over each item in the word_count list to print
for item in word_count:
    print(f"{item[0]} : {item[1]}")
   