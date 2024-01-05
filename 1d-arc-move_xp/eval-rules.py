import json
for NAME in ['all_1d_move_1p','all_1d_move_2p','all_1d_move_3p']:
    for N in [3,4]:
        INPUT = './004/' + NAME + '_demos_' + str(N) + '_s2l_rules.json'
        OUTPUT = './004/' + NAME + '_demos_' + str(N) + '_s2l_rules.json'
        test_file = open(INPUT, 'r', encoding='utf-8')
        test_data = json.load(test_file)
        total = 0
        correct = 0
        partial = 0
        for idx, task_json in enumerate(test_data):
            if not 'response' in task_json.keys():
                continue
            # print(task_json['response'])
            if '(' in task_json['response']:
                ans = task_json['response'].strip().split('\n')[0].split('(')[0].strip().replace(':','')
            else:
                ans = task_json['response'].strip().split('\n')[0].strip().replace(':','')
            # if ans == task_json['label'] or ans in task_json['label'] or task_json['label'] in ans:
            if ans == task_json['s2l_label_tools']:
                correct += 1
                task_json['eval'] = 1
            # elif ans in task_json['label'] or task_json['label'] in ans:
            #     print(ans)
                # aa=input()
                # partial +=1
                total+=1
            else:
                task_json['eval'] = 0
                total+=1
            task_json['label_'] = ans

        with open(OUTPUT, 'w') as f:
            json.dump(test_data, f, indent=4)


for NAME in ['all_1d_move_1p','all_1d_move_2p','all_1d_move_3p']:
    print('---'*10)
    # NAME = NAME+'_123'
    # for N in [3,5,8,10,12,15]:
    for N in [3,4]:
        INPUT = './004/' + NAME + '_demos_' + str(N) + '_s2l_rules.json'
        test_file = open(INPUT, 'r', encoding='utf-8')
        test_data = json.load(test_file)
        print(INPUT)
        c=0
        for idx, task_json in enumerate(test_data):
            if not 'eval' in task_json.keys():
                break
            c+=1
        if c==60:
            correct = 0
            for idx, task_json in enumerate(test_data):
                if task_json['eval'] ==1 :
                    correct+=1

            print(correct/60)     