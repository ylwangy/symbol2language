import json

pstance = {'favor': 'FAVOR', 'against': 'AGAINST', 'neutral': 'NEUTRAL'}
def scores_stance_text(f,key_label,key_predction, predict2label, method='acc'):
    INPUT = f
    test_file = open(INPUT, 'r', encoding='utf-8')
    test_data = json.load(test_file)
    correct=0
    ret=[]
    f_=0
    a_=0
    n_=0
    for idx, task_json in enumerate(test_data):
        task_json[key_predction] = task_json[key_predction].lower().strip().split('\n')[-1].strip()
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

gpt4 = scores_stance_text('tweet-pstance_zsc/prediction2_gpt4.json','Answer','response', pstance)
s2l = scores_stance_text('tweet-pstance_zsc/final2.json','Answer','response', pstance)


print('---')
gpt4 = scores_stance_text('tweet-pstance_35_zsc/prediction2_gpt4.json','Answer','response', pstance)
s2l = scores_stance_text('tweet-pstance_35_zsc/final2_2.json','Answer','response', pstance)
