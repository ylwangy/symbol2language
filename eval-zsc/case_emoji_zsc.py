import json

emoji_text = {'neutral': 'neutral', 'positive': 'positive', 'negative': 'negative'}
def scores_emoji_text(f,key_label,key_predction, predict2label, method='acc'):
    INPUT = f
    test_file = open(INPUT, 'r', encoding='utf-8')
    test_data = json.load(test_file)
    correct=0
    ret=[]
    f_=0
    a_=0
    n_=0
    for idx, task_json in enumerate(test_data):
        task_json[key_predction] = task_json[key_predction].strip().split('\n')[-1].strip()
        if 'positive' in task_json[key_predction].lower() and not 'negative' in task_json[key_predction].lower() and not 'neutral' in task_json[key_predction].lower():
            predict = 'positive'
            f_+=1
        elif 'negative' in task_json[key_predction].lower() and not 'positive' in task_json[key_predction].lower() and not 'neutral' in task_json[key_predction].lower():
            predict = 'negative'
            a_+=1
        elif 'neutral' in task_json[key_predction].lower() and not 'positive' in task_json[key_predction].lower() and not 'negative' in task_json[key_predction].lower():
            predict = 'neutral'
            n_+=1
        else:
            # print(task_json[key_predction])
            predict = 'neutral'

        if task_json[key_label] == predict2label[predict]:
            correct+=1
            ret.append(True)
        else:
            ret.append(False)
    
    print(f)
    print(correct/len(test_data))
    print(f_,a_,n_)
    return ret

gpt4 = scores_emoji_text('emoji_text/prediction2_gpt4.json','label','response', emoji_text)


s2l = scores_emoji_text('emoji_text/final4.json','label','response', emoji_text)


print('------')
gpt4 = scores_emoji_text('emoji_text_35_zsc/prediction2_gpt4.json','label','response', emoji_text)

s2l = scores_emoji_text('emoji_text_35_zsc/final8.json','label','response', emoji_text)

