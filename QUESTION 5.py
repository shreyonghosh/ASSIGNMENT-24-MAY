def word_frequency(sentence):
    
    sentence = sentence.lower()
    
    
    words = sentence.split()
    
    
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
            
    return freq


input_text = "Capgemini Capgemini is good"
print(word_frequency(input_text))
