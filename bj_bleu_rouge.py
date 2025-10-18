import csv
import pickle
import nltk
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from rouge import Rouge
rouge = Rouge()

def compute_bleu_scores(reference_text_list, candidate_text_list):
    bleu1, bleu2, bleu4 = 0, 0, 0
    for item1 in range(len(reference_text_list)):
        reference = [reference_text_list[item1].split()]   # 参考译文（二维列表）
        candidate = candidate_text_list[item1].split()     # 待比较文本
        smooth = SmoothingFunction().method1
        bleu1 += sentence_bleu(reference, candidate, weights=(1, 0, 0, 0), smoothing_function=smooth)
        bleu2 += sentence_bleu(reference, candidate, weights=(0.5, 0.5, 0, 0), smoothing_function=smooth)
        bleu4 += sentence_bleu(reference, candidate, weights=(0.25, 0.25, 0.25, 0.25), smoothing_function=smooth)
    bleu1 /= len(reference_text_list)
    bleu2 /= len(reference_text_list)
    bleu4 /= len(reference_text_list)
    return bleu1, bleu2, bleu4

path1 = "G:/d_ctr/SupQA_enhance/lw/SupQA_enhance_v1/temp/g_t_a_dataset.csv"
path2 = "G:/d_ctr/SupQA_enhance/lw/SupQA_enhance_v1/temp/result_g_t_a_deepseek-r1_70b_noemo.csv"


src_list = []
output = []
from tqdm import tqdm   

with open(path1, "r", encoding="gbk") as f1, \
     open(path2, "r", encoding="gbk") as f2:

    reader1 = csv.DictReader(f1)
    reader2 = csv.DictReader(f2)
    n = 0
    for row1, row2 in tqdm(zip(reader1, reader2)):
        n += 1

        val1 = row1['raw_dis_template']
        val2 = row2['Generated Response']
        src_list.append(val1)
        output.append(val2)

        if n == 29:
            break


b1, b2, b4 = compute_bleu_scores(src_list, output)
print("BLEU-1:", b1)
print("BLEU-2:", b2)
print("BLEU-4:", b4)

rouge_score = rouge.get_scores(hyps=output, refs=src_list, avg=True)
print("rouge-1:{}".format(rouge_score["rouge-1"]['r']))
print("rouge-2:{}".format(rouge_score["rouge-2"]['r']))
print("rouge-l:{}".format(rouge_score["rouge-l"]['r']))

