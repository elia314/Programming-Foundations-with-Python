import urllib.request


def read_text():
    quotes = open("/Users/eliaahadi/Google Drive/Online_Courses/Udacity/FullStackWeb_NanoDegreePlus/Lesson8_UseClasses_ProfanityEditor/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=QUERY")
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity alert!")
    elif "false" in output:
        print("This doc has no curse words")
    else:
        print("Could not scan doc")

read_text()
