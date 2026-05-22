import string
from collections import Counter

with open("/kaggle/input/datasets/mountsai6/sotu-speech/State of the union.txt", "r") as file:
    content = file.read()

def char_count(content):
    character_count = len(content) 
    return character_count

def sentence_counting(content):
    sentences = content.replace('!', '.').replace('?', '.').split('.')
    sentences = [s.strip() for s in sentences if s.strip()]
    sentence_count = len(sentences)
    return sentence_count

def word_counting(content):
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    cleaned_text = content.translate(translator)
    words = [word.lower() for word in cleaned_text.split()]
    word_count = len(words)
    return words, word_count  

def avg_word_length(words, word_count):
    sum_letters = 0
    for word in words:
        word_length = len(word)
        sum_letters += word_length

    if word_count > 0:
        cal_avg_word_length = sum_letters / word_count
    else:
        cal_avg_word_length = 0
    return cal_avg_word_length

def avg_sent_length(sentence_count, word_count):
    if sentence_count > 0:
        cal_avg_sent_length = word_count / sentence_count
    else:
        cal_avg_sent_length = 0
    return cal_avg_sent_length

def word_distribution(words, word_count):
    word_counts = Counter(words)
    distribution = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return distribution

def top_ten_longest_words(words):
    unique_words = list(set(words))
    longest_words = sorted(unique_words, key=len, reverse=True)
    top_ten_longest = longest_words[:10]
    return top_ten_longest



total_chars = char_count(content)
total_sentences = sentence_counting(content)

words_list, total_words = word_counting(content) 

final_avg_word = avg_word_length(words_list, total_words)
final_avg_sent = avg_sent_length(total_sentences, total_words)
final_distribution = word_distribution(words_list, total_words)
final_top_ten = top_ten_longest_words(words_list)



print("=" * 65)
print(f"{'STATE OF THE UNION SPEECH METRICS':^65}")
print("=" * 65)

print(f"{'Character Count':<40} | {total_chars:<20,}")
print(f"{'Sentence Count':<40} | {total_sentences:<20,}")
print(f"{'Word Count':<40} | {total_words:<20,}")
print(f"{'Average Word Length':<40} | {final_avg_word:<20.2f}")
print(f"{'Average Sentence Length (words)':<40} | {final_avg_sent:<20.2f}")
print("\n" + "=" * 65)

print(f"{'TOP 10 LONGEST WORDS':^65}")
print("=" * 65)
print(f"{'Rank':<8} | {'Word':<40} | {'Length':<10}")
print("-" * 65)
for i, word in enumerate(final_top_ten, 1):
    print(f"{i:<8} | {word:<40} | {len(word):<10}")
print("\n" + "=" * 65)


print(f"{'WORD FREQUENCY DISTRIBUTION (Top 25)':^65}")
print("=" * 65)
print(f"{'Rank':<8} | {'Word':<40} | {'Frequency':<10}")
print("-" * 65)
for i, (word, freq) in enumerate(final_distribution[:10], 1):
    print(f"{i:<8} | {word:<40} | {freq:<10,}")
print("=" * 65)
