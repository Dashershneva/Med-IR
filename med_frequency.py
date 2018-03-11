import re
from pymystem3 import Mystem
import collections

mystem = Mystem()

file = open('C:\\Users\\DariaLaptop\\PycharmProjects\\firstpy\\Questions_relevant\\questions_original_text_0.txt', 'r', encoding='utf-8')
f = file.read()
f = f.replace('\\n', '')
f = re.sub('\W', ' ', f)


print(f)

lek = "фосфолюгель"

reg = 'PR=|CONJ=|APRO=*|PART='
reg_text = '.?%s' %lek

word_form_dict = {}
if lek in f:
    lek_key = lek in word_form_dict
    if lek_key == False:
        word_form_dict[lek] = {}
        lekarstvo = word_form_dict[lek]
    t = re.search('%s .*' % lek, f.lower())
    p = t.group(0)
    p = p.split(' ')
    p = mystem.analyze(' '.join(p))
    p_clean = []
    print(p)
    i = 0
    for item in p:
        if type(p[i]) == dict:
                analysis_key = 'analysis' in p[i]
                if analysis_key == True:
                    word = p[i]['analysis']
                    if word != [] and not re.search(reg, word[0]['gr']):
                        word_form = word[0]['lex']
                        p_clean.append(word_form)
        i += 1
    p = p_clean[1:16]
    m = mystem.analyze(' '.join(p))
    i = 0
    for item in m:
        if type(m[i]) == dict:
                analysis_key = 'analysis' in m[i]
                if analysis_key == True:
                    word = m[i]['analysis']
                    if word != [] and not re.search(reg, word[0]['gr']):
                        word_form = word[0]['lex']
                        if word_form in lekarstvo:
                            lekarstvo[word_form] += 1
                        else:
                            lekarstvo[word_form] = 1
        i += 1
    l = mystem.lemmatize(t.group(0))
    l = ''.join(l)
    l = l.split(' ')
"""    for word in l:
        q = 0
        if q < 15:
            print(l[q])
        q += 1 """

print(t.group(0))
print(p_clean)
print(len(p))
print(word_form_dict)
#print(l[:14])

"""
f_lem = mystem.lemmatize(f)
f_stem = mystem.analyze(f)
i = 0
word_form_dict = {}
for item in f_stem:
    if type(f_stem[i]) == dict:
        analysis_key = 'analysis' in f_stem[i]
        if analysis_key == True:
            word = f_stem[i]['analysis']
            if word != []: #and not re.search(reg, word[0]['gr']):
                word_form = word[0]['lex']
                if word_form in word_form_dict:
                    word_form_dict[word_form] += 1
                else:
                    word_form_dict[word_form] = 1
    i += 1

"""
"""
def compute_tf(f_lem):
    tf_text = collections.Counter(f_lem)
    for n in tf_text:
        tf_text[n] = tf_text[n]/float(len(f_lem))
    return tf_text

print(compute_tf(f_lem))
"""
"""

print(f)
print(f_lem)
#print(f_stem)
print(word_form_dict)

file.close()

"""