import json


tweet = {'positive':2, 'negative':0, 'neutral':1}
pstance = {'favor': 'FAVOR', 'against': 'AGAINST', 'neutral': 'NEUTRAL'}

def scores_sentiment(f,key_label,key_predction, predict2label, method='acc'):
    INPUT = f
    test_file = open(INPUT, 'r', encoding='utf-8')
    test_data = json.load(test_file)
    correct=0
    ret=[]
    f_=0
    a_=0
    n_=0
    for idx, task_json in enumerate(test_data):
        if 'positive' in task_json[key_predction].lower() and not 'negative' in task_json[key_predction].lower():
            predict = 'positive'
            f_+=1
        elif 'negative' in task_json[key_predction].lower() and not 'positive' in task_json[key_predction].lower():
            predict = 'negative'
            a_+=1
        else:
            # print(task_json[key_predction])
            predict = 'neutral'
            n_+=1

        if task_json[key_label] == predict2label[predict]:
            correct+=1
            ret.append(True)
        else:
            ret.append(False)
    print(f)
    print(correct/len(test_data))
    print(f_,a_,n_)
    return ret


def scores_pstance(f,key_label,key_predction, predict2label, method='acc'):
    INPUT = f
    test_file = open(INPUT, 'r', encoding='utf-8')
    test_data = json.load(test_file)
    correct=0
    f_=0
    a_=0
    n_=0
    ret=[]
    for idx, task_json in enumerate(test_data):
        if 'favor' in task_json[key_predction].lower() and not 'against' in task_json[key_predction].lower():
            predict = 'favor'
            f_+=1
        elif 'against' in task_json[key_predction].lower() and not 'favor' in task_json[key_predction].lower():
            predict = 'against'
            a_+=1
        else:
            # print(task_json[key_predction])
            predict = 'neutral'
            n_+=1

        if task_json[key_label] == predict2label[predict]:
            correct+=1
            ret.append(True)
        else:
            ret.append(False)
    
    print(f)
    print(correct/len(test_data))
    print(f_,a_,n_)
    return ret

gpt4 = scores_sentiment('tweet-sentiment-2way/prediction2_gpt4.json','label','response', tweet)
s2l = scores_sentiment('tweet-sentiment-2way/final6.json','label','response', tweet)

print('---')
gpt4 = scores_sentiment('tweet-sentiment-2way-35/prediction2_gpt4.json','label','response', tweet)
s2l = scores_sentiment('tweet-sentiment-2way-35/final6.json','label','response', tweet)
