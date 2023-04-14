main_prompt = '''
Rate the sentiment of the following phrase enclosed in double quotes on a scale of 1 to 10, 
1 being extremely negative and 10 being extremely positive, "{}". 
Store the result in json format with 4 elements:
The first element is the integer rating assigned to the phrase,
The second element is a list of the top 3 words used to determine your rating,
The third element is the subject of the message summarized in a maximum of 2 words,
The fourth element is short and concise explanation for your reasoning for the rating.
Keep in mind emotional tone and irony
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