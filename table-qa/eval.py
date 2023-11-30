import json
import sys
import glob
import argparse
import re
import numpy as np
import string
from evaluate import load
squad_metric = load("squad")

parser = argparse.ArgumentParser()
# parser.add_argument("--cutoff", default=-1, type=int)
# parser.add_argument("--inputs", required=True, type=str)


def maybe_normalize_float(span: str):
    if span and (re.match(r"^[+-][0-9]+[.]?[0-9]*$", span)
                 or (re.match(r"^[0-9]*[.]?[0-9]*$", span))) and span != '.':
        # FIXME: We did this(instead of try except) to convert a string into a float
        #  since the try catch will lead to an error when using 8 V100 gpus with cuda 11.0,
        #  and we still don't know why that could happen....
        return str(float(span))
    else:
        return span


def maybe_normalize_number(text: str) -> str:
    units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
    ]
    for index, unit in enumerate(units):
        if text == unit:
            return str(float(index))
    return text


def remove_punc(text: str) -> str:
    exclude = set(string.punctuation)
    return ''.join(ch for ch in text if ch not in exclude)


def remove_articles(text: str) -> str:
    return re.sub(r'\b(a|an|the)\b', ' ', text)


# def eval_ex_match(pred, gold_result):
#     pred = pred.lower()
#     gold_result = gold_result.lower()

#     # Replace and with comma
#     if ' and ' in pred and '|' in gold_result:
#         pred = pred.replace(' and ', ', ')

#     pred = [span.strip() for span in pred.split(', ')]

#     if '|' in gold_result:
#         gold_result = [span.strip() for span in gold_result.split('|')]
#     else:
#         gold_result = [span.strip() for span in gold_result.split(', ')]

#     pred = [maybe_normalize_number(remove_punc(remove_articles(span.strip()))) for span in pred]
#     gold_result = [maybe_normalize_number(remove_punc(remove_articles(span.strip()))) for span in gold_result]

#     # print(pred, ' # ', gold_result)
#     clean_float = True  # TODO
#     if clean_float:
#         pred = [maybe_normalize_float(span) for span in pred]
#         gold_result = [maybe_normalize_float(span) for span in gold_result]
#     print(pred)
#     print(gold_result)
#     aa=input()
#     return sorted(pred) == sorted(gold_result)



def cal_f1(pred, gold_result):
    pred = pred.lower()
    gold_result = gold_result.lower()

    # Replace and with comma
    if ' and ' in pred and '|' in gold_result:
        pred = pred.replace(' and ', ', ')
        gold_result = gold_result.replace('|', ', ')

    pred = [span.strip() for span in pred.split(', ')]

    if '|' in gold_result:
        gold_result = [span.strip() for span in gold_result.split('|')]
    else:
        gold_result = [span.strip() for span in gold_result.split(', ')]

    pred = [maybe_normalize_number(remove_punc(remove_articles(span.strip()))) for span in pred]
    gold_result = [maybe_normalize_number(remove_punc(remove_articles(span.strip()))) for span in gold_result]

    # print(pred, ' # ', gold_result)
    clean_float = True  # TODO
    if clean_float:
        pred = [maybe_normalize_float(span) for span in pred]
        gold_result = [maybe_normalize_float(span) for span in gold_result]

    # if len (gold_result)==1 and gold_result[0].endswith('.0'):
    #     gold_result.append(gold_result[0][:-2])
    # print(pred)
    # print(gold_result)
    predictions = [{'prediction_text': ' '.join(pred), 'id': '56e10a3be3433e1400422b22'}]
    references = [{'answers': {'answer_start': [97], 'text': [' '.join(gold_result)]}, 'id': '56e10a3be3433e1400422b22'}]
    results = squad_metric.compute(predictions=predictions, references=references)
    # print(results['f1'])
    # aa=input()
    return results['f1'],results['exact_match']



if __name__ == "__main__":
    args = parser.parse_args()

    INPUT = 'prediction2_gpt4.json'
    test_file = open(INPUT, 'r', encoding='utf-8')
    test_data = json.load(test_file)
    counter = {}
    f1 = []
    em = []
    for idx, task_json in enumerate(test_data):

        f1.append(cal_f1(task_json['response'], task_json['answer'])[0])
        em.append(cal_f1(task_json['response'], task_json['answer'])[1])

    print(sum(f1)/len(f1))
    print(sum(em)/len(em))
    print('---')
  

    INPUT = 'final3.json'
    test_file = open(INPUT, 'r', encoding='utf-8')
    test_data = json.load(test_file)
    counter = {}
    f1 = []
    em = []
    for idx, task_json in enumerate(test_data):

        f1.append(cal_f1(task_json['response'], task_json['answer'])[0])
        em.append(cal_f1(task_json['response'], task_json['answer'])[1])

    print(sum(f1)/len(f1))
    print(sum(em)/len(em))
    print('---')



