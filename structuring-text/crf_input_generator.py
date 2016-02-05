import sys
import nltk
import json

with open("token_pos.txt", "w") as f:
    for line in sys.stdin:
        data = json.loads(line)
        for ingredient in data['ingredients']:
            tokens = nltk.word_tokenize(ingredient.strip())
            tagged_tokens = nltk.pos_tag(tokens)
            for token, pos in tagged_tokens:
                try:
                    f.write("%s %s\n" % (token.encode('utf8'), pos))
                except:
                    print token
            f.write("\n")
f.close()
