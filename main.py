# 导入所需的库
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 定义一个函数来生成词云
def generate_wordcloud(titles):
    # 创建词云对象
    wordcloud = WordCloud(width=800, height=800, 
                          background_color ='white', 
                          stopwords = set(), 
                          min_font_size = 10).generate(titles)

    # 显示词云图像
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 
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
    title_pattern = re.compile(r'title\s*=\s*\"([^\"]+)\"')

    # Find all matches of the pattern in the BibTeX data
    titles = title_pattern.findall(bib_data)

    return titles

files = ["bib/findings.bib", "bib/main.bib"]
titles = []
for file in files:
    extracted_titles = extract_titles_from_bib_file('path_to_your_bib_file.bib')
    titles += extracted_titles
generate_wordcloud(titles)
