import re
from collections import Counter
import numpy as np

def word_frequencies(text):
    words = re.findall(r'\b\w+\b', text.lower()) 
    total_words = len(words)
    word_counts = Counter(words)
    return {word: count / total_words for word, count in word_counts.items()}

def kl_divergence(p, q):
    vocab = set(p.keys()).union(set(q.keys()))  
    p_dist = np.array([p.get(word, 1e-10) for word in vocab])  
    q_dist = np.array([q.get(word, 1e-10) for word in vocab])
    return np.sum(p_dist * np.log(p_dist / q_dist))  

file_path = "jest_vek.txt"  
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

split_pattern = r'\n\s*(II|III)\s*\n'
sections = re.split(split_pattern, text)

chapter_I = sections[0] 
chapter_II = sections[2]  
chapter_III = sections[4] if len(sections) > 4 else ""  

freq_I = word_frequencies(chapter_I)
freq_II = word_frequencies(chapter_II)
freq_III = word_frequencies(chapter_III)

kl_12 = kl_divergence(freq_I, freq_II)
kl_13 = kl_divergence(freq_I, freq_III)
kl_23 = kl_divergence(freq_II, freq_III)

print(f"KL(I || II) = {kl_12:.4f}")
print(f"KL(I || III) = {kl_13:.4f}")
print(f"KL(II || III) = {kl_23:.4f}")
