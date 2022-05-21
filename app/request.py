import urllib.request, json

quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'

def random_quotes():
    '''
    method gets the json url request from the quotes API
    '''
    
    with urllib.request.urlopen(quote_url) as url:
        #Use the read() function to read the response and store it in a get_quote_data variable.
        get_quote_data = url.read()

        #Convert the JSON response to a Python dictionary using json.loads function
        get_quote_response = json.loads(get_quote_data)

        quote_result = {}
        
        #Checking if the response contains any data
        if get_quote_response['quote']:
            quote_result['id'] = get_quote_response['id']
            quote_result['author'] = get_quote_response['author']
            quote_result['quote'] = get_quote_response['quote']
            
        return quote_result
    
def generate_quote(times, random_quotes):
    quotes = []
    for i in range(times):
        quote = random_quotes()
        quotes.append(quote)
        
    return quotes