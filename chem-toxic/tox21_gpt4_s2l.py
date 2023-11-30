import json
import openai

INPUT = 'Tox21_random_500_s2l.json'
INPUT = 'Tox21_prediction_gpt4_random_s2l.json'
OUTPUT = 'Tox21_prediction_gpt4_random_s2l.json'
test_file = open(INPUT, 'r', encoding='utf-8')
test_data = json.load(test_file)
for idx, task_json in enumerate(test_data):
    if 'response' in task_json.keys():
        continue
    else:
        print(idx, len(test_data))
        prompt = "You are an expert chemist, your task is to predict the property of molecule using your experienced chemical property prediction knowledge. Given the SMILES string of a molecule, the task focuses on predicting molecular properties, specifically wether a molecule is toxic(Yes) or Not toxic(No), please answer with only Yes or No.\n"
        # prompt += f"SMILES: {task_json['smiles']}\ntoxic: "
        prompt += f"SMILES: {task_json['smiles']}\n{task_json['s2l-2'].strip()}\ntoxic: "
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