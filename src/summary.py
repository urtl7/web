import re

def get_sentences(txt):
    return txt.split('.')

def get_words(txt):
    only_words_text = re.compile(r'[^0-9^a-z^A-Z\s]').sub('',txt)
    return only_words_text.split(' ')

def get_keywords(word_list , min_ratio=0.001, max_ratio=0.5) :
    """ this method takes a word list and returns a set of keywords """
    assert (min_ratio < 1 and max_ratio < 1)    
    count_dict = {}    
    for word in word_list:
        count_dict.setdefault(word , 0)
        count_dict[word] +=1
    keywords = set()
    for word , cnt in count_dict.items():
        word_percentage = count_dict[word]* 1.0 / len (word_list)
        if word_percentage <= max_ratio and word_percentage >=min_ratio:
            keywords.add(word)
    return keywords

def get_sentence_weight (sentence , keywords):
    """ this method takes a sentence string and a set of keywords and returns weight of the sentence """
    sen_list = sentence.split(' ')
    window_start = 0; window_end = -1;
    #calculating window start
    for i in range(len(sen_list)):
        if sen_list[i] in keywords:
            window_start = i
            break
    #calculating window end
    for i in range(len(sen_list) - 1 , 0 , -1) :
        if sen_list[i] in keywords:
            window_end = i
            break
    if window_start > window_end :
        return 0
    window_size = window_end - window_start + 1
    #calculating number of keywords
    keywords_cnt =0
    for w in sen_list :
        if w in keywords:
            keywords_cnt +=1
    return keywords_cnt*keywords_cnt *1.0 / window_size

def summarize(text):
    txt = text.replace('\n','')
    word_list = get_words(txt)
    keywords = get_keywords(word_list , 0.05 , 0.5)
    sentence_list = get_sentences(txt)
    sentence_weight = {}
    for sen in sentence_list:
        sentence_weight[sen] = get_sentence_weight(sen, keywords)
    top_sentences = list(sentence_list)                                # make a copy
    top_sentences.sort(key=lambda x: sentence_weight[x], reverse=True)      # sort by score
    top_sentences = top_sentences[:int(len(sentence_weight)*0.2)] # get a part
    top_sentences.sort(key=lambda x: sentence_list.index(x))           # sort by occurrence
    summary = '. '.join(top_sentences)
    return summary