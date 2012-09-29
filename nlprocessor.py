import nltk
from nltk.corpus import wordnet
tokenizer = None
tagger = None

def init_nltk():
    global tokenizer
    global tagger
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+|[^\w\s]+')
    tagger = nltk.UnigramTagger(nltk.corpus.brown.tagged_sents())

def tag(text):
    global tokenizer
    global tagger
    if not tokenizer:
        init_nltk()
    tokenized = tokenizer.tokenize(text)
    tagged = tagger.tag(tokenized)
    tagged.sort(lambda x,y:cmp(x[1],y[1]))
    return tagged


def simple_path(path):
    return [s.lemmas[0].name for s in path]

def nl_process(string, logfile, module_keys):
    string = tag(string)
    location = ""
    search_term = ""
    text = ""
    for word in string:
        if word[1] is None:
            location = word[0]
        elif word[1] == "NN":
            search_term = word[0]
            text += word[0]
        else:
            continue
    
    word = wordnet.synset('%s.n.01' % search_term)
    paths = word.hypernym_paths()
    
    for path in paths:
        for line in simple_path(path):
            for key, value in module_keys.items():
                if line in value.split(", "):
                    module = key
                    break
            else:
                continue
            break
        else:
            continue
        break
    
    return(location,module,text)