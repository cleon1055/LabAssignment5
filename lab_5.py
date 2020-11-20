
"""
The program will translate a sentence captured as user input.
We first read the in text file textese.txt.
Then from the text file, we create a list of strings from each line
in the text file.
Then we create a dictionary off the list. 
Once the text file has been read into memeory, we close the file. 

We then define a fuction for translating which involves splitting the user
input (sentence) into an array of strings ("enjoy the excellent band tonight") 
["enjoy. "the", "excellent", "band", "tonight"]

Once we have the array of strings representing the user's input sentence, we 
loop through each words to find the key mathcing the word and returns back the 
value assigned to each key word in the dictionary.

After each word is translated, we then
Print out the translated sentence to the user. 

"""

""" 
main():
    set sentence = input()
    set dictionary  = translate()
    trasnlate(sentence, dictionary):

trasnlate(sentence, dictionary):
    words = for each of the word in the sentence
    for each word, translate the word
    print translated sentence to user

create_dictionary():
    read in textese.txt
    create list = each line from file
    close the file
    create a dict off the list
    return the dict

main()

"""

def main():
    sentence = input("Enter the sentence: ")
    dictionary = create_dictionary("textese.txt")
    translate(sentence, dictionary)

def create_dictionary(txt_file):
    infile = open(txt_file, "r")
    words = [word.rstrip() for word in infile]
    infile.close()
    return dict([word.split(",") for word in words])

def translate(sentence, dictionary):
    words = sentence.split() 
    for word in words:
        print(dictionary.get(word, word), " ", end="") 

main()


