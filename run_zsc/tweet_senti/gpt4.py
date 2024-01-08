import json
import openai

INPUT = 'test_2way.json'
INPUT = 'prediction2_gpt4.json'
OUTPUT = 'prediction2_gpt4.json'
test_file = open(INPUT, 'r', encoding='utf-8')
test_data = json.load(test_file)
for idx, task_json in enumerate(test_data):
    if 'response' in task_json.keys():
        continue
    else:
        print(idx, len(test_data))
        # prompt = "what is the sentiment of the tweet:\"" + task_json['text'].strip() + "\" please answer with only Positive or Negative."
        prompt = "Sentiment classification, please answer with only Positive or Negative.\n"
        prompt += task_json['text'].strip() # predict2

        prompt += "\n\nLet's think step by step.\n"
        
        print(prompt)
        try:
            responses = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=256,
                temperature=0
            )
            print(responses['choices'][0]['message']['content'])
            task_json['response'] = responses['choices'][0]['message']['content']
        except:
            pass
        print('---'*10)
with open(OUTPUT, 'w') as f:
    json.dump(test_data, f, indent=4, ensure_ascii=False)