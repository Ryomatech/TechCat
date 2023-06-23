import csv
import re
import os
import sys


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def csv_to_dictionary(filename):
    dictionary = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            key = row[0]
            value = row[1]
            dictionary[key] = value
    return dictionary

def atwei():
    file_path = 'statics/AtomicWeight.csv'
    AtomicWeight = csv_to_dictionary(file_path)
    return AtomicWeight

def split_string(string):
    pattern = r'(\(|\)|[A-Za-z]|\d)'  # `(`、`)`、英語の単語の1文字、数字の1文字にマッチする正規表現パターン
    result = re.findall(pattern, string)
    return result

def expand_formula(string):
    if '(' not in string:
        return string
    else:
        splited_string=split_string(string)
        right_parent_index=splited_string.index('(')
        left_parent_times=0
        for j in range (right_parent_index+1,len(splited_string)-1):
            if splited_string[j]==')':
                if  left_parent_times==0:
                    if j==len(splited_string)-2:
                        return ''.join(splited_string[0:right_parent_index])+(''.join(splited_string[right_parent_index+1:j])*int(splited_string[j+1]))
                    else:
                        return ''.join(splited_string[0:right_parent_index])+(''.join(splited_string[right_parent_index+1:j])*int(splited_string[j+1]))+''.join(splited_string[j+2:])
                else:
                    left_parent_times-=1
            if splited_string[j]=='(':
                left_parent_times+=1

def resplit_string(string):
    pattern = r'([A-Z][a-z]*)|(\d+)'
    result = re.findall(pattern, string)
    splits = [item for sublist in result for item in sublist if item]
    final_splits = []
    current_number = ''
    for split in splits:
        if split.isdigit():
            current_number += split
        else:
            if current_number:
                final_splits.append(current_number)
                current_number = ''
            final_splits.append(split)
    if current_number:
        final_splits.append(current_number)
    return final_splits

def molcalcal(input_string):
    while '(' in input_string:
        input_string=expand_formula(input_string)
    split_result = resplit_string(input_string)
    ChemicalFormula=['0']
    for i in range(len(split_result)):
        if split_result[i].isdigit() or ChemicalFormula[-1].isdigit():
            ChemicalFormula.append(split_result[i])
        else:
            ChemicalFormula.append('1')
            ChemicalFormula.append(split_result[i])
    if not ChemicalFormula[-1].isdigit():
        ChemicalFormula.append('1')
    ChemicalFormula.pop(0)

    MolecularWeight=0
    AtomicWeight = atwei()
    for i in range(len(ChemicalFormula)//2):
        MolecularWeight+=float(AtomicWeight[ChemicalFormula[2*i]])*int(ChemicalFormula[2*i+1])
    return str(format(MolecularWeight, '.4f'))

