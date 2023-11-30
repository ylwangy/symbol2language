import json

bace={'no':'0','yes':'1'}

def scores(f,key_label,key_predction,method='acc'):
    INPUT = f
    test_file = open(INPUT, 'r', encoding='utf-8')
    test_data = json.load(test_file)
    correct=0
    for idx, task_json in enumerate(test_data):
        if task_json[key_predction].lower().strip() in ['yes','no']:
            if task_json[key_label].lower().strip() == bace[task_json[key_predction].lower().strip()]:
                correct+=1
        else:
            print(task_json[key_predction].lower().strip() )

    
    print(f)
    print(correct/len(test_data))

def scores_tox(f,key_label,key_predction,method='acc'):
    INPUT = f
    test_file = open(INPUT, 'r', encoding='utf-8')
    test_data = json.load(test_file)
    correct=0
    for idx, task_json in enumerate(test_data):
        if task_json["NR-AR"]=="0" and task_json["NR-AR-LBD"]=="0" and task_json["NR-AhR"]=="0" and task_json["NR-Aromatase"]=="0" and task_json["NR-ER"]=="0" and task_json["NR-ER-LBD"]=="0" and task_json["NR-PPAR-gamma"]=="0" and task_json["SR-ARE"]=="0" and task_json["SR-ATAD5"]=="0" and task_json["SR-HSE"]=="0" and task_json["SR-MMP"]=="0" and task_json["SR-p53"]=="0":
            label='0'
        else:
            label='1'
        if task_json[key_predction].lower().strip() in ['yes','no']:
            if label.lower().strip() == bace[task_json[key_predction].lower().strip()]:
                correct+=1
        else:
            print(task_json[key_predction].lower().strip())
            # correct+=1
    print(f)
    print(correct/len(test_data))



scores('./BBBP_prediction_gpt4_random.json','p_np','response')
scores('./BBBP_prediction_gpt4_random_s2l.json','p_np','response')

