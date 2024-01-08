import json
import openai

INPUT = 'tablefact_500_s2l_3.json'
INPUT = 'final2.json'
OUTPUT = 'final2.json'
test_file = open(INPUT, 'r', encoding='utf-8')
test_data = json.load(test_file)
for idx, task_json in enumerate(test_data):
    if 'response' in task_json.keys():
        continue
    else:
        print(idx, len(test_data))
        prompt = "Your task is to judge whether the statement is true or false based on the table. Please answer by true or false only.\n\n"
        prompt += 'Table:\n' + task_json['table'].strip() + '\n\n'
        prompt += 'Table Description:\n' + task_json['s2l'].strip() + '\n\n'
        prompt += 'Statement:\n' + task_json['statement'].strip() + '\n\n'
        prompt += "\n\nLet's think step by step.\n"
        print(prompt)
        try:
            responses = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1024,
                temperature=0
            )
            print(responses['choices'][0]['message']['content'])
            task_json['response'] = responses['choices'][0]['message']['content']
        except:
            pass
        print('---'*10)
with open(OUTPUT, 'w') as f:
    json.dump(test_data, f, indent=4)