import re
import csv

with open('file_to_read.txt', 'r') as file:
    content = file.read()

    text = str(content.replace("\n", " ")).replace("'", " ")

    mixed_words_list = text.split(" ")

    words_list = [re.sub(r'[^a-zA-Z0-9àèéìòù]', '', word).lower() for word in mixed_words_list]
    words_list = [word for word in words_list  if word]
    words_list .sort()

    unique_words = []
    length = []
    occurrence = []

    for word in words_list :
        freq = words_list .count(word)

        if word in unique_words:
            continue
        else:
            unique_words.append(word)
            length.append(len(word))
            occurrence.append(freq)

    total_list = [(unique_words[i], length[i], occurrence[i]) for i in range(min(len(unique_words), len(length), len(occurrence)))]

    with open('words.csv', 'w', newline='') as df:
        title_row = ['word', 'length', 'freq']
        writer = csv.writer(df)
        writer.writerow(title_row)
        writer.writerows(total_list)
