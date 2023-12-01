import json
import openai

for N in [0,1,2,3,4,5]:
    INPUT = 'demos_' + str(N) + '.json'
    # INPUT = 'demos_' + str(N) + '_gpt4.json'
    OUTPUT = 'demos_' + str(N) + '_gpt4.json'
    test_file = open(INPUT, 'r', encoding='utf-8')
    test_data = json.load(test_file)
    for idx, task_json in enumerate(test_data):
        if 'response' in task_json.keys():
            continue
        else:
            print(idx, len(test_data))
            if N==0:
                prompt="Let's play some puzzles that focus on reasoning and logic. You will get a \"input sequence\", then you must answer the corresponding \"output sequence\".\n"
            else:
                prompt="Let's play some puzzles that focus on reasoning and logic. In each puzzle, you will be provided a few demonstrations of how an \"input sequence\" gets transformed into a corresponding \"output sequence\". At the end, you will get a brand new \"input sequence\", then you must answer the corresponding \"output sequence\".\n"
            prompt += task_json['prompt']
            print(task_json['prompt'])
            try:
                responses = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=128,
                    temperature=0
                )
                print(responses['choices'][0]['message']['content'])
                task_json['response'] = responses['choices'][0]['message']['content']
            except:
                pass
            print('---'*10)
    with open(OUTPUT, 'w') as f:
        json.dump(test_data, f, indent=4, ensure_ascii=False)
