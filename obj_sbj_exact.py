import subprocess
import csv
iprompts = ["1+1 = ?","1+2=?"]
import pickle

pk_path = "G:/d_ctr/SupQA_enhance/lw/SupQA_enhance_v1/Amazon_Subjective_test_set.pk"

with open(pk_path, 'rb') as f:
    data = pickle.load(f)

nn = 0



with open('results_obj_sbj.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['ID', 'Generated Response']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 写入CSV的表头
    writer.writeheader()
    for num,item in enumerate(data):
        obj_reference = item['objective_answer']['answer_text'].strip()
        sbj_reference = item['subjective_answer'].strip()
        print(obj_reference)
        print("-----")
        print(sbj_reference)





#         # 写入输出到文件
        
        writer.writerow({'obj_reference': obj_reference, 'sbj_reference': sbj_reference})

