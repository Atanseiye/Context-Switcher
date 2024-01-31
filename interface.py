from main import tokenizer
from main import greetings



params = {
    'text':"Hello hello"
}

def tokenize(querys):

    # change all the text to small letters
    query = [query.lower() for query in querys]
    query = ''.join(query)

    tokenized = tokenizer(query)

    # returning the set of the tokenized sentence

    print(tokenized)
    tokenized_set = set(tokenized[0])

    return tokenized_set



def tokenize_and_return_set(word_list):
    # Tokenize each element in the list
    print('word_list: ', word_list)
    tokenized_list = [tokenizer(word) for word in word_list]

    print('tokenized_list: ', tokenized_list)

    # Flatten the list of lists into a single list
    flattened_tokens = [token for sublist in tokenized_list for token in sublist]
    print('flattened_tokens: ', flattened_tokens)

    # Convert the list of tokens to a set to get unique tokens
    unique_tokens_set = set(flattened_tokens[0])
    print('unique_tokens_set: ', unique_tokens_set)

    return unique_tokens_set



print(tokenize_and_return_set(greetings))