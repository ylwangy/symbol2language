import json


table_fact = {'true':1, 'false':0}

def transfer(all_res):
    if 'true' in all_res.split('\n')[-1] and not 'false' in all_res.split('\n')[-1]:
        return 'true'
    elif 'false' in all_res.split('\n')[-1] and not 'true' in all_res.split('\n')[-1]:
        return 'false'
    else:
        # print(all_res.split('\n')[-1])
        # aa=input()
        return 'nan'    

def scores_sentiment(f,key_label,key_predction, predict2label, method='acc'):
    INPUT = f
    test_file = open(INPUT, 'r', encoding='utf-8')
    test_data = json.load(test_file)
    correct=0
    ret = []
    for idx, task_json in enumerate(test_data):
        # predict =  task_json[key_predction].lower().strip()
        predict =  transfer(task_json[key_predction].lower().strip())
        if not predict in predict2label.keys():
            # print(predict)
            # predict = 'false'
            ret.append(False)
        else:
            if task_json[key_label] == predict2label[predict]:
                correct+=1
                ret.append(True)
            else:
                ret.append(False)
    
    print(f)
    print(correct/len(test_data))
    return ret

gpt4 = scores_sentiment('table_fact_zsc/prediction_gpt4.json','label','response', table_fact)

s2l = scores_sentiment('table_fact_zsc/final2.json','label','response', table_fact)
s2l = scores_sentiment('table_fact_zsc_rules/final2.json','label','response', table_fact)

print('---')
gpt4 = scores_sentiment('table_fact_35_zsc/prediction_gpt4.json','label','response', table_fact)
s2l = scores_sentiment('table_fact_35_zsc/final1.json','label','response', table_fact)
s2l = scores_sentiment('table_fact_35_rules_zsc/final1.json','label','response', table_fact)