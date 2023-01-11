import csv
import string

all_lyrics = []

#grab all the lyrics into one big list
#can also insert any txt file with words and the program will still function
with open('tswift_lyrics.txt') as all_songs:
    
    for line in all_songs.readlines():
        all_lyrics.append(line)


lines_list = []

#split the  lyrics up into a list of lines
for line in all_lyrics:
    lines_list.append(line.split())


words_list = []

#split the lines into a list of words
for sentence in lines_list:
    for word in sentence:
        words_list.append(word)


cleaned_words = []

#remove any punctuation from the words
for word in words_list:
    clean_word = word.translate(str.maketrans('', '', string.punctuation))
    cleaned_words.append(clean_word.lower())


word_dict = {}

#get the count of each word and store in the word_dict dictionary
for word in cleaned_words:
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

temp_dict = {}


#write the result to a csv file for further analysis in excel or google sheets
with open('words_count.csv','w') as output_csv:
    fields = ['word','count']
    output_writer = csv.DictWriter(output_csv,fieldnames=fields)
    output_writer.writeheader()
    for key,value in word_dict.items():
        temp_dict['word'] = key
        temp_dict['count'] = value
        output_writer.writerow(temp_dict)


