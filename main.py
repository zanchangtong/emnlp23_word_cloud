# 导入所需的库
import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from collections import Counter
import string

def generate_wordcloud_from_list(titles_list, max_words=100, additional_stopwords=set()):
    """
    Generate a word cloud with specific filters.

    Args:
    filename (str): The file containing the text.
    max_words (int): Maximum number of words to be included in the word cloud.
    additional_stopwords (set): Additional stopwords to be excluded from the word cloud.

    Returns:
    None: Displays the word cloud.
    """
    # 将标题列表转换为单个字符串
    titles = ' '.join(titles_list)

    # Combine default and additional stopwords
    stopwords = set(STOPWORDS).union(additional_stopwords)

    # Create word cloud object
    wordcloud = WordCloud(width=800, height=800, 
                          background_color='white', 
                          stopwords=stopwords, 
                          max_words=max_words,
                          min_font_size=10).generate(titles)

    # Display the word cloud image
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()

def generate_cooccurrence_wordcloud(titles_list, target_phrase="large language model", window_size=5, max_words=100):
    """
    Generate a word cloud based on words co-occurring with a target phrase.

    Args:
    filename (str): The file containing the text.
    target_phrase (str): The target phrase to look for co-occurrences.
    window_size (int): The number of words around the target phrase to consider for co-occurrences.
    max_words (int): Maximum number of words to be included in the word cloud.

    Returns:
    None: Displays the word cloud.
    """
    # 将标题列表转换为单个字符串
    text = ' '.join(titles_list).lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the text
    words = text.split()

    words = [word for word in words if word not in STOPWORDS]

    # Find co-occurring words
    target_phrase_tokens = target_phrase.split()
    cooccurring_words = []
    for i in range(len(words) - len(target_phrase_tokens) + 1):
        if words[i:i+len(target_phrase_tokens)] == target_phrase_tokens:
            window_words = words[max(i - window_size, 0):i] + words[i + len(target_phrase_tokens):i + len(target_phrase_tokens) + window_size]
            cooccurring_words.extend(window_words)

    # Count frequencies
    word_counts = Counter(cooccurring_words)

    # Create word cloud object
    wordcloud = WordCloud(width=800, height=800, 
                          background_color='white', 
                          max_words=max_words,
                          min_font_size=10).generate_from_frequencies(word_counts)

    # Display the word cloud image
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()

def extract_titles_from_bib_file(file_path):
    """
    Extracts titles from a BibTeX file.

    Args:
    file_path (str): The path to the BibTeX file.

    Returns:
    list: A list of titles extracted from the file.
    """
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        bib_data = file.read()

    # Define the regex pattern for extracting titles
    title_pattern = re.compile(r' title\s*=\s*\"([^\"]+)\"')

    # Find all matches of the pattern in the BibTeX data
    titles = title_pattern.findall(bib_data)

    return titles

files = ["bib/findings.bib", "bib/main.bib"]
titles = []
for file in files:
    extracted_titles = extract_titles_from_bib_file(file)
    titles += extracted_titles
generate_wordcloud_from_list(titles, 100)
# generate_cooccurrence_wordcloud(titles, target_phrase="machine translation")

