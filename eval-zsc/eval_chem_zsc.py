import json

bace={'no':'0','yes':'1'}


def transfer(all_res):
    if 'yes' in all_res.split('\n')[-1] and not 'no' in all_res.split('\n')[-1]:
        return 'yes'
    elif 'no' in all_res.split('\n')[-1] and not 'yes' in all_res.split('\n')[-1]:
        return 'no'
    else:
        # print(all_res.split('\n')[-1])
        # aa=input()
        return 'nan'
        

def scores(f,key_label,key_predction,method='acc'):
    INPUT = f
    test_file = open(INPUT, 'r', encoding='utf-8')
    test_data = json.load(test_file)
    correct=0
    for idx, task_json in enumerate(test_data):
        if transfer(task_json[key_predction].lower().strip()) in ['yes','no']:
            if task_json[key_label].lower().strip() == bace[transfer(task_json[key_predction].lower().strip())]:
                correct+=1
        else:
            # print(task_json[key_predction].lower().strip() )
            pass

    
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
        if transfer(task_json[key_predction].lower().strip()) in ['yes','no']:
            if label.lower().strip() == bace[transfer(task_json[key_predction].lower().strip())]:
                correct+=1
        else:
            # print(task_json[key_predction].lower().strip())
            # correct+=1
            pass
    print(f)
    print(correct/len(test_data))


# scores('chem_1107_400/BACE_prediction_gpt4_random.json','Class','response')
# scores('chem_1107_400/BACE_prediction_gpt4_random_s2l.json','Class','response')

# scores('chem_1107_400/BBBP_prediction_gpt4_random.json','p_np','response')
# scores('chem_1107_400/BBBP_prediction_gpt4_random_s2l.json','p_np','response')

# scores_tox('chem_1107_400/Tox21_prediction_gpt4_random.json','','response')
# scores_tox('chem_1107_400/Tox21_prediction_gpt4_random_s2l.json','','response')


# scores('chem_1107_35_400/BACE_prediction_gpt4_random.json','Class','response')
# scores('chem_1107_35_400/BACE_prediction_gpt4_random_s2l.json','Class','response')

# scores('chem_1107_35_400/BBBP_prediction_gpt4_random.json','p_np','response')
# scores('chem_1107_35_400/BBBP_prediction_gpt4_random_s2l.json','p_np','response')

# scores_tox('chem_1107_35_400/Tox21_prediction_gpt4_random.json','','response')
# scores_tox('chem_1107_35_400/Tox21_prediction_gpt4_random_s2l.json','','response')
# scores('chem_1110/BACE_prediction_gpt4_random.json','Class','response')
# scores('chem_1110/BACE_prediction_gpt4_random_s2l.json','Class','response')

# scores('chem_1110/BBBP_prediction_gpt4_random.json','p_np','response')
# scores('chem_1110/BBBP_prediction_gpt4_random_s2l.json','p_np','response')

# scores_tox('chem_1110/Tox21_prediction_gpt4_random.json','','response')
# scores_tox('chem_1110/Tox21_prediction_gpt4_random_s2l.json','','response')

# scores('chem_1110_35/BACE_prediction_gpt4_random.json','Class','response')
# scores('chem_1110_35/BACE_prediction2_gpt4_random.json','Class','response')
# scores('chem_1110_35/BACE_prediction_gpt4_random_s2l.json','Class','response')
# scores('chem_1110_35/BACE_prediction3_gpt4_random_s2l.json','Class','response')
# scores('chem_1110_35/BACE_prediction_gpt4_random_s2l_2.json','Class','response')
# scores('chem_1110_35/BACE_prediction2_gpt4_random_s2l_2.json','Class','response')
# scores('chem_1110_35/BACE_prediction_gpt4_random_s2l_3.json','Class','response')
# print('---')

# scores('chem_1110_35/BBBP_prediction_gpt4_random.json','p_np','response')
# scores('chem_1110_35/BBBP_prediction2_gpt4_random.json','p_np','response')
# scores('chem_1110_35/BBBP_prediction_gpt4_random_s2l.json','p_np','response')
# scores('chem_1110_35/BBBP_prediction3_gpt4_random_s2l.json','p_np','response')
# scores('chem_1110_35/BBBP_prediction_gpt4_random_s2l_2.json','p_np','response')
# scores('chem_1110_35/BBBP_prediction2_gpt4_random_s2l_2.json','p_np','response')
# scores('chem_1110_35/BBBP_prediction_gpt4_random_s2l_3.json','p_np','response')
# print('---')

# scores_tox('chem_1110_35/Tox21_prediction_gpt4_random.json','','response')
# scores_tox('chem_1110_35/Tox21_prediction2_gpt4_random.json','','response')
# scores_tox('chem_1110_35/Tox21_prediction_gpt4_random_s2l.json','','response')
# scores_tox('chem_1110_35/Tox21_prediction3_gpt4_random_s2l.json','','response')
# scores_tox('chem_1110_35/Tox21_prediction_gpt4_random_s2l_2.json','','response')
# scores_tox('chem_1110_35/Tox21_prediction2_gpt4_random_s2l_2.json','','response')
# scores_tox('chem_1110_35/Tox21_prediction_gpt4_random_s2l_3.json','','response')
# print('---')

# scores('chem_1112_35/BACE_prediction2_gpt4_random.json','Class','response')
# scores('chem_1112_35/BACE_prediction_gpt4_random_s2l.json','Class','response')

# scores('chem_1112_35/BBBP_prediction2_gpt4_random.json','p_np','response')
# scores('chem_1112_35/BBBP_prediction_gpt4_random_s2l.json','p_np','response')

# scores_tox('chem_1110_35/Tox21_prediction2_gpt4_random.json','','response')
# scores_tox('chem_1110_35/Tox21_prediction3_gpt4_random.json','','response')
# scores_tox('chem_1110_35/Tox21_prediction4_gpt4_random.json','','response')
# scores_tox('chem_1112_35/Tox21_prediction2_gpt4_random.json','','response')

# scores_tox('chem_1112_35/Tox21_prediction_gpt4_random_s2l.json','','response')
# scores_tox('chem_1112_35/Tox21_prediction2_gpt4_random_s2l.json','','response')


scores('chem_final_zsc/BACE_prediction_gpt4_random.json','Class','response')
scores('chem_final_zsc/BACE_prediction_gpt4_random_s2l.json','Class','response')
scores('chem_final_zsc/BACE_prediction_gpt4_random_s2l_description.json','Class','response')
scores('chem_final_zsc/BACE_prediction_gpt4_random_s2l_description2.json','Class','response')

scores('chem_final_zsc/BBBP_prediction_gpt4_random.json','p_np','response')
scores('chem_final_zsc/BBBP_prediction_gpt4_random_s2l.json','p_np','response')
scores('chem_final_zsc/BBBP_prediction_gpt4_random_s2l_description.json','p_np','response')

scores_tox('chem_final_zsc/Tox21_prediction_gpt4_random.json','','response')
scores_tox('chem_final_zsc/Tox21_prediction_gpt4_random_s2l.json','','response')
scores_tox('chem_final_zsc/Tox21_prediction_gpt4_random_s2l_description.json','','response')

# scores('chem_final_35_zsc/BACE_prediction_gpt4_random.json','Class','response')
# scores('chem_final_35_zsc/BACE_prediction_gpt4_random_s2l.json','Class','response')
# scores('chem_final_35_zsc_2/BACE_prediction_gpt4_random.json','Class','response')
# scores('chem_final_35_zsc_2/BACE_prediction_gpt4_random_s2l.json','Class','response')
# scores('chem_final_35_zsc_3/BACE_prediction_gpt4_random.json','Class','response')
# scores('chem_final_35_zsc_3/BACE_prediction_gpt4_random_s2l.json','Class','response')
# scores('chem_final_35_zsc_4/BACE_prediction_gpt4_random.json','Class','response')
# scores('chem_final_35_zsc_4/BACE_prediction_gpt4_random_s2l.json','Class','response')
# scores('chem_final_35_zsc_4/BACE_prediction2_gpt4_random.json','Class','response')
# scores('chem_final_35_zsc_4/BACE_prediction2_gpt4_random_s2l.json','Class','response')
# scores('chem_final_35_zsc_4/BACE_prediction3_gpt4_random_s2l.json','Class','response')
# scores('chem_final_35_zsc_4/BACE_prediction4_gpt4_random_s2l.json','Class','response')

# scores('chem_final_35_zsc/BBBP_prediction_gpt4_random.json','p_np','response')
# scores('chem_final_35_zsc/BBBP_prediction_gpt4_random_s2l.json','p_np','response')

# scores_tox('chem_final_35_zsc/Tox21_prediction_gpt4_random.json','','response')
# scores_tox('chem_final_35_zsc/Tox21_prediction_gpt4_random_s2l.json','','response')

scores('chem_1122_35_zsc/BACE_prediction_gpt4_random.json','Class','response')
scores('chem_1122_35_zsc/BACE_prediction_gpt4_random_s2l.json','Class','response')
scores('chem_1122_35_zsc/BACE_prediction_gpt4_random_s2l_description.json','Class','response')
scores('chem_1122_35_zsc/BACE_prediction_gpt4_random_s2l_description2.json','Class','response')

scores('chem_1122_35_zsc/BBBP_prediction_gpt4_random.json','p_np','response')
scores('chem_1122_35_zsc/BBBP_prediction_gpt4_random_s2l.json','p_np','response')
scores('chem_1122_35_zsc/BBBP_prediction_gpt4_random_s2l_description.json','p_np','response')

scores_tox('chem_1122_35_zsc/Tox21_prediction_gpt4_random.json','','response')
scores_tox('chem_1122_35_zsc/Tox21_prediction_gpt4_random_s2l.json','','response')
scores_tox('chem_1122_35_zsc/Tox21_prediction_gpt4_random_s2l_description.json','','response')
scores_tox('chem_1122_35_zsc/Tox21_prediction_gpt4_random_s2l_description2.json','','response')