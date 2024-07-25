import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')

file_path = 'path/to/your/google_forms_responses.csv'
df = pd.read_csv(file_path)


response_column = 'Your_Response_Column_Name'  

keywords = ['keyword1', 'keyword2', 'keyword3']  

def find_keywords(text, keywords):
    words = word_tokenize(text.lower())
    return [word for word in words if word in keywords]

df['keywords_found'] = df[response_column].apply(lambda x: find_keywords(x, keywords))
df['keyword_counts'] = df['keywords_found'].apply(Counter)


keyword_summary = Counter()
for counts in df['keyword_counts']:
    keyword_summary.update(counts)


print("Keyword Summary:")
for keyword, count in keyword_summary.items():
    print(f"{keyword}: {count}")

df.to_csv('path/to/save/keyword_analysis.csv', index=False)
