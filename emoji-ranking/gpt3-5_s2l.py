import json
import openai

# INPUT = 'prediction_gpt3-5_s2l_cot.json'
INPUT = 'emoji_tag_s2l.json'
OUTPUT = 'prediction_gpt3-5_s2l_cot.json'
test_file = open(INPUT, 'r', encoding='utf-8')
test_data = json.load(test_file)
for idx, task_json in enumerate(test_data):
    if 'response' in task_json.keys():
        continue
    else:
        print(idx, len(test_data))
        prompt = "As a social scientist, Your task is to analyze eight emotions (anger, anticipation, disgust, fear, joy, sadness, surprise, trust) of the emoji. For each emotion, please assign a score from 0 to 1 according to the emoji. Please provide your best estimation of the emotion scores with two decimal places:\n"
        prompt += task_json['emoji']
        prompt += ' (' + task_json['s2l'] + ')'
        print(prompt)
        try:
            responses = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
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
    json.dump(test_data, f, indent=4, ensure_ascii=False)