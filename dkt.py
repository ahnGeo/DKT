import csv
from pickle import EMPTY_TUPLE

number_list = []
question_list = []
answer_list = []

with open("./dkt-public/data/assistments/builder_test.csv", 'r') as f :
    test_reader = csv.reader(f)
    for i, row in enumerate(test_reader) :
        if i % 3 == 0 :
            number_list.append(row)
        if i % 3 == 1 :
            question_list.append(row)
        if i % 3 == 2 :
            answer_list.append(row)
        
qna_list = []
for idx1 in range(len(question_list)) :
    empty_row = []
    for idx2 in range(len(question_list[idx1])) :
        empty_tuple = []
        empty_tuple.append(question_list[idx1][idx2])
        empty_tuple.append(answer_list[idx1][idx2])
        empty_row.append(empty_tuple)
    qna_list.append(empty_row)

print(qna_list[1])