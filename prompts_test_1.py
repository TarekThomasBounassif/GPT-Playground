sentiment_extract_prompt = '''
Use the text within double quotes "{}" to evaluate the sentiment expressed towards 
the subject "{}". Output the result in JSON format with the following elements.
First element is the sentiment on a scale of 1 to 10, 1 being most negative 10 being most positive,
Second element is a list of the 3 words in the text used the most to determine the rating.
Third element is your reasoning for why this rating was chosen.
'''

subject_id_prompt = '''
Based on this text between double quotes "{}", identity the overall subject of the text. 
The subject is the entity the text relates to and not the overall topic. 
Response should be 1 or 2 words long and should only contain the subject of the text. 
'''

sub_prompt = '''
Just in case you didn’t already hate Brad Paisley enough for teaming up with Jill Biden to push vaccines, here he is singing in Ukraine with Sen. Joe Manchin
He won’t play any songs in East Palestine, but he’ll play in Kiev?!
'''

sub_prompt = '''
Glory to Ukraine and its soldiers 🇺🇦
'''

tweet = '''
BOYCOTT PHILLIP MORRIS

Did you know that, this year, Phillip Morris 🇺🇸 received a “certificate of merit” for its support of the Armed Forces of Russia 🇷🇺?

Did you know it is also the largest foreign taxpayer in Russia 🇷🇺.
'''

tweet = '''
BREAKING: Elon Musk says Hello to his subscribers. There are rumors that he is going to share exclusive memes in there.

Subscribe 
@elonmusk
 now. One thing’s for sure, it won’t be boring. 🤣
'''