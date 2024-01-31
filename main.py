import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import re
import streamlit as st


greetings_BoW = [
    'hello',
    'how',
    'are',
    'you',
    'hi',
    'hey',
    'howdy',
    'greetings',
    'good morning',
    'morning',
    'good afternoon',
    'afternoon',
    'good evening',
    'evening',
    'hi there',
    'hello there',
    'hey there',
    'hiya',
    'yo',
    'hola',
    'salut',
    'ciao',
    'bonjour',
    'hallo',
    'namaste',
    'what’s up',
    'sup',
    'how’s it going',
    'how are you',
    'how do you do',
    'what\'s going on',
    'what\'s new',
    'what\'s happening',
    'how\'s everything',
    'how\'s life',
    'hi friend',
    'hello friend',
    'hey friend',
    'hi buddy',
    'hello buddy',
    'hey buddy',
    'hi pal',
    'hello pal',
    'hey pal',
    'hi mate',
    'hello mate',
    'hey mate',
    'hi dear',
    'hello dear',
    'hey dear',
    'hi love',
    'hello love',
    'hey love',
    'hi sweetie',
    'hello sweetie',
    'hey sweetie',
    'hi darling',
    'hello darling',
    'hey darling',
    'hi sunshine',
    'hello sunshine',
    'hey sunshine',
    'hi beautiful',
    'hello beautiful',
    'hey beautiful',
    'hi handsome',
    'hello handsome',
    'hey handsome',
    'hi cutie',
    'hello cutie',
    'hey cutie',
    'hi gorgeous',
    'hello gorgeous',
    'hey gorgeous',
    'hi princess',
    'hello princess',
    'hey princess',
    'hi champ',
    'hello champ',
    'hey champ',
    'hi superstar',
    'hello superstar',
    'hey superstar',
    'hi rockstar',
    'hello rockstar',
    'hey rockstar',
    'hi genius',
    'hello genius',
    'hey genius',
    'hi maestro',
    'hello maestro',
    'hey maestro',
    'hi wizard',
    'hello wizard',
    'hey wizard',
    'hi legend',
    'hello legend',
    'hey legend',
    'hi hero',
    'hello hero',
    'hey hero',
    'hi warrior',
    'hello warrior',
    'hey warrior',
    'hi explorer',
    'hello explorer',
    'hey explorer',
    'hi adventurer',
    'hello adventurer',
    'hey adventurer',
    'hi traveler',
    'hello traveler',
    'hey traveler',
    'hi pioneer',
    'hello pioneer',
    'hey pioneer',
    'hi innovator',
    'hello innovator',
    'hey innovator',
    'hi creator',
    'hello creator',
    'hey creator',
    'hi artist',
    'hello artist',
    'hey artist',
    'hi poet',
    'hello poet',
    'hey poet',
    'hi dreamer',
    'hello dreamer',
    'hey dreamer',
    'hi visionary',
    'hello visionary',
    'hey visionary',
    'hi thinker',
    'hello thinker',
    'hey thinker',
    'hi philosopher',
    'hello philosopher',
    'hey philosopher',
    'hi intellect',
    'hello intellect',
    'hey intellect',
    'hi scholar',
    'hello scholar',
    'hey scholar',
    'hi mentor',
    'hello mentor',
    'hey mentor',
    'hi guide',
    'hello guide',
    'hey guide',
    'hi teacher',
    'hello teacher',
    'hey teacher',
    'hi professor',
    'hello professor',
    'hey professor',
    'hi coach',
    'hello coach',
    'hey coach',
    'hi instructor',
    'hello instructor',
    'hey instructor',
    'hi trainer',
    'hello trainer',
    'hey trainer',
    'hi leader',
    'hello leader',
    'hey leader',
    'hi boss',
    'hello boss',
    'hey boss',
    'hi captain',
    'hello captain',
    'hey captain',
    'hi commander',
    'hello commander',
    'hey commander',
    'hi chief',
    'hello chief',
    'hey chief',
    'hi director',
    'hello director',
    'hey director',
    'hi manager',
    'hello manager',
    'hey manager',
    'hi supervisor',
    'hello supervisor',
    'hey supervisor',
    'hi colleague',
    'hello colleague',
    'hey colleague',
    'hi team',
    'hello team',
    'hey team',
    'hi crew',
    'hello crew',
    'hey crew',
    'hi staff',
    'hello staff',
    'hey staff',
    'hi everyone',
    'hello everyone',
    'hey everyone',
    'hi all',
    'hello all',
    'hey all',
    'hi world',
    'hello world',
    'hey world',
    'hi universe',
    'hello universe',
    'hey universe',
]


observe_point = '''

ObservePoint agent

Tools available:
WebAuditReader: Fetches data from the API endpoint and prints names, IDs, and starting URLs of web audits.
WebAuditRunReader: Uses data from Class 1 to fetch data for a specific runID and prints webAuditId and runID.
WebAuditTagPresenceReader: Uses data from Class 1 and Class 2 to fetch tag information based on a specific auditID and runID.
PageSummaryFetcher: Fetches data from the API endpoint and prints page ID, page url and page titles 
CookieFetcher: This tool extracts and displays information about cookies used on audited web pages, helping you understand tracking and user data management.
InitiatorExtractor: Tool to get all tags, inititators and extract initiator data using a POST request to the given endpoint. 
updatestartingurl: This tool allows you to update the starting URL for an audit, enabling you to customize the audit process as needed.
ConsoleLogFetcher: It captures and presents data from the browser's console logs, giving you insights into any errors or messages generated during the audit.
Tag Searcher: Tool to search tags by ID or tag name and retrieve tag details the identifier is the tag id or name
newrun: Tool to create a new run in an observepoint audit.
how many visits did we get via referal and direct traffic in october? how do they compare?
Auditchecker: Tool to periodically check for new audits by making requests to the specified endpoint every 8 minutes. It detects a new audit if one has been included in the last 8 minutes.Run this tool on startup.

Questions
Can you tell me which tags and cookies are currently present on the shop page of the Royal Mail website?
Are there any Reddit tags that are not present on our website, and if so, which ones are missing?
Is there a difference in the tags and cookies present on the privacy page compared to the previous audit runs?
How can I change the starting URL for our audits to ensure we are monitoring the right pages?
I would like to initiate a new run for our audit? 
Can you provide details about the most recent web audit run, including its webAuditID and runID?
How can I fetch information about all the web audits we've conducted, including their names and starting URLs?
What insights can you provide from the browser's console logs regarding any errors or messages generated during the last two runs on the help page?
Can you help me identify the resource initiators on our website help page?

The name of the audit has to be specified Royal Mail


'''

adobeanalytics = '''
"metadata": {
    "_id": "6540f59dc57a310fee66f236",
    "source": "adobeanalytics",
    "profile_id": "6lijgqaxow5n9f8br5sbclc51",
    "dataset_uri": "rmgroyalmailcom",
    "metrics": [
      "metrics/visits",
      "metrics/pageevents",
      "metrics/revenue"
    ],
    "dimensions": [
      "variables/marketingchannel"
    ],
    "date_columns": [
      "date"
    ],
    "date_range": [
      "2023-10-01",
      "2023-10-30"
    ],
    "time_unit": "D",
    "dimensions_variables": 
    [
      {
        "dimension": "variables/marketingchannel",
        "items": [
          "Direct Traffic",
          "Organic Search",
          "Referral Traffic",
          "Email Marketing (EM)",
          "Paid Search (SM)",
          "Internal Traffic",
          "Door Drops (DL)",
          "Other",
          "Organic Social",
          "Social Media (SB)",
          "Sponsorship (SS)",
          "Public Relations (PR)",
          "Digital Display (DD)",
          "Direct Mail (DM)",
          "Affiliate Network (AF)",
          "None"]
      }
    ]
  }
'''


stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves",
    "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their",
    "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was",
    "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and",
    "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between",
    "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on",
    "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all",
    "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same",
    "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "d", "ll", "m", "o", "re",
    "ve", "y", "ain", "aren", "couldn", "didn", "doesn", "hadn", "hasn", "haven", "isn", "ma", "mightn", "mustn", "needn",
    "shan", "shouldn", "wasn", "weren", "won", "wouldn"]


input_format = {
    'input': 'hello'
}


def tokenize_text(text):
    words = word_tokenize(text)
    return words

def list_tokenizer(sentence_list):
    # Initialize the tokenizer
    tokenizer = nltk.RegexpTokenizer(r"\w+")

    # Tokenize each sentence in the list
    tokenized_list = [tokenizer.tokenize(sentence) for sentence in sentence_list]

    return tokenized_list



#is the list nested
def is_nested(input_list):
    return any(isinstance(i, list) for i in input_list)

# flattener
def flatten_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list

def intersection(list1, list2):

    if is_nested(list1):
        list1 = flatten_list(list1)
    else:
        pass

    if is_nested(list2):
        list2 = flatten_list(list2)
    else:
        pass

    
    # Convert lists to sets and find the intersection
    common_elements = set(list1) & set(list2)

    # Convert the result back to a list if needed
    common_elements_list = list(common_elements)

    num_of_common_elements = len(common_elements_list)

    return (num_of_common_elements)


# splitting adobe analytics strings into words
def word_split(text):
    clean = text.split(' ')
    cleaning = ' '.join(clean).split(' ')
    cleaning = [words.strip() for words in cleaning]
    words = [w for w in cleaning if len(w) > 0]
    combined = ' '.join(words)
    return combined

# process adobe analytics text
def remove_special_characters(text):
    # Use regular expression to remove non-alphabetic characters (keeping spaces)
    cleaned_text = re.sub('[^a-zA-Z\s]', '', text)
    processed = word_split(cleaned_text)
    return processed

# stopwords remover
def remove_stopwords(text):

    # Split the text into a list of words
    words = word_tokenize(text)

    # Filter out the stop words from the list of words
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Join the filtered words into a new text
    clean_text = " ".join(filtered_words)

    return clean_text



# Logic to solve the problem
def processors(text):
    # step1 - remove the stopwords
    step1 = remove_stopwords(text)

    # step2 - remove remove_special_characters
    step2 = remove_special_characters(step1)

    # step 3 - tokenize the result in step2 using word tokenizer
    step3 = tokenize_text(step2)

    #  remove special characters in the observepoint text
    obsp = tokenize_text(remove_stopwords(observe_point))

    # process the adobe analytics
    adobeAnalytics = tokenize_text(remove_special_characters(word_split(adobeanalytics)))

    # do the comparisons here. for eachone seperately seperately, 

    # for greetings
    greetings = intersection(step3, flatten_list(greetings_BoW))

    # for observe point
    observeP = intersection(step3, flatten_list(obsp))

    # for adobe analytics
    adobe = intersection(step3, adobeAnalytics)

    reuslt = {
        'Greetings':greetings,
        'Observe Point':observeP,
        'Adobe Analytics':adobe
    }

    return reuslt



# streamlit testing model
st.title('Context Switching Tester')
inputs = st.text_area('Query')

tester = st.button('Test')


if tester:
    processed = processors(inputs)
    st.write(processed)

    def this_engine(dictionary):
    # Find the key with the highest value
        max_key = max(dictionary, key=dictionary.get)
        return max_key
    
    this_engine = this_engine(processed)
    st.write(f'this question is coming from {this_engine}')


    

