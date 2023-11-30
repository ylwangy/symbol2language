import json
import numpy as np
from sklearn.metrics import f1_score
from sklearn.metrics import precision_recall_fscore_support

LABEL2IDX={'FAVOR':1,'AGAINST':0}
cannot_ans = 0
def extract(pred,f):
    pred=pred.lower().strip().split('\n')[-1]
    # print(pred)
    global cannot_ans

    if 'favor' in pred and not 'against' in pred:
        return 'FAVOR'
    elif 'against' in pred  and not 'favor' in pred:
        return 'AGAINST'
    elif 'against Trump' in pred:
        return 'AGAINST'
    else:
        cannot_ans += 1
        return 'FAVOR'


PATH='./'


#ok
FILES=[ './prediction2_gpt4.json',
        './final2.json', ]



for f in FILES:
    print(f)
    labels=[]
    predicts=[]
    test_file = open(PATH + f, 'r', encoding='utf-8')
    test_data = json.load(test_file)
    for idx, test_case in enumerate(test_data):
        # print(test_case['Answer'])
        # print(test_case['Predict'])
        labels.append(LABEL2IDX[test_case['Answer']])
        predicts.append(LABEL2IDX[extract(test_case['response'],f)])

    # print(f1_score(labels,predicts,average='macro'))
    # print(f1_score(labels,predicts,average='micro'))
    result = precision_recall_fscore_support(np.array(labels), np.array(predicts), average=None, labels=[0,1])
    print((result[2][0]+result[2][1])/2) # average F1 score of Favor and Against


