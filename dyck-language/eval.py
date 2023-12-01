import json
for NAME in ['gpt4','gpt4_s2l']:
    for N in [1,2,3,4,5]:
        INPUT = './demos_' +str(N)+ '_'+NAME + '.json'
        OUTPUT = './demos_' +str(N)+ '_'+NAME + '.json'
        
        # print(INPUT)
        test_file = open(INPUT, 'r', encoding='utf-8')
        test_data = json.load(test_file)
        total = 0
        correct = 0
        partial = 0
        for idx, task_json in enumerate(test_data):
            if not 'response' in task_json.keys():
                continue
            # print(task_json['response'])
            ans = task_json['response'].split('\n')[0].strip()
            if ans == task_json['label']:
                correct += 1
                task_json['eval'] = 1
                total+=1
            else:
                task_json['eval'] = 0
                total+=1
            task_json['label_'] = ans

        with open(OUTPUT, 'w') as f:
            json.dump(test_data, f, indent=4)

for NAME in ['gpt4','gpt4_s2l']:
    print('---'*10)
    print(NAME)
    for N in [1,2,3,4,5]:
        INPUT = './demos_' +str(N)+ '_'+NAME + '.json'
        test_file = open(INPUT, 'r', encoding='utf-8')
        test_data = json.load(test_file)
        print(INPUT)
        c=0
        for idx, task_json in enumerate(test_data):
            if not 'eval' in task_json.keys():
                break
            c+=1
        if c==500:
            correct = 0
            for idx, task_json in enumerate(test_data):
                if task_json['eval'] ==1 :
                    correct+=1

            print(correct/500)            
