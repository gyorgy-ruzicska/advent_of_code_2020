import pandas as pd
import csv
import re


#Day_1
with open('Day1/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    list_of_numbers=[]
    for row in reader:
        list_of_numbers.extend(row)
    for i in range(len(list_of_numbers)):
        for j in range(i, len(list_of_numbers)):
            total1=int(list_of_numbers[i])+int(list_of_numbers[j])
            if total1==2020:
                print("The product of the two numbers: "+str(int(list_of_numbers[i])\
                *int(list_of_numbers[j])))
            for k in range(j, len(list_of_numbers)):
                total2=int(list_of_numbers[i])+int(list_of_numbers[j])\
                      +int(list_of_numbers[k])
                if total2==2020:
                    print("The product of the three numbers: "+str(int(list_of_numbers[i])\
                    *int(list_of_numbers[j])*int(list_of_numbers[k])))

#Day_2
with open('Day2/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    valid1=0
    valid2=0
    for row in reader:
        number, letter, text = row[0].split(" ")
        min, max = number.split("-")
        letter = letter.strip(":")
        letter_count=0
        for i in text:
            if i==letter:
                letter_count+=1
        if (int(min)<=letter_count) & (letter_count<=int(max)):
            valid1+=1
        if (letter==text[int(min)-1]) & (letter!=text[int(max)-1]):
            valid2+=1
        if (letter!=text[int(min)-1]) & (letter==text[int(max)-1]):
            valid2+=1
    print("Number of valid password by policy 1: "+ str(valid1))
    print("Number of valid password by policy 2: "+ str(valid2))

#Day_3
def split(word):
    return [char for char in word]

with open('Day3/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    list_of_numbers=[11,31,51,71,12]
    for i in list_of_numbers:
        locals()["location" + str(i)] = 0
        locals()["trees" + str(i)] = 0
    for row in reader:
        mylist=split(row[0])
        for i in list_of_numbers[:-1]:
            if mylist[locals()["location" + str(i)]%31]=="#":
                locals()["trees" + str(i)]+=1
        if (mylist[location12%31]=="#")&(location11%2==0):
            trees12+=1
        for i in list_of_numbers[:-1]:
            locals()["location" + str(i)]+=int(str(i)[0])
        if location11%2==0:
            location12+=1
    print("We pass %d number of trees by going 1 down and 3 right!"%trees31)
    print("The product for the second part: "+str(trees11*trees31*trees51*trees71*trees12))

#Day_4
with open('Day4/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    passport_dict={}
    valid1=0
    valid2=0
    for row in reader:
        try:
            list=row[0].split(" ")
            for i in list:
                key, value= i.split(":")
                passport_dict[key]=value
        except:
            try:
                key, value= row[0].split(":")
                passport_dict[key]=value
            except:
                keys=passport_dict.keys()
                if "byr" in keys and "iyr" in keys and "eyr" in keys and "hgt" in keys and\
                "hcl" in keys and "ecl" in keys and "pid" in keys:
                    valid1+=1
                    valid_height=False
                    valid_hair=False
                    valid_eye=False
                    valid_pid=False
                    eyes=["amb","blu","brn","gry","grn","hzl","oth"]
                    height=re.match(r"([0-9]+)([a-z]+)",passport_dict["hgt"],re.I)
                    hair=re.match(r"(#)([0-9a-f]{6})",passport_dict["hcl"],re.I)
                    if height:
                        if (height.groups()[1]=="cm") & (150<=int(height.groups()[0])) &\
                        (int(height.groups()[0])<=193):
                            valid_height=True
                        elif (height.groups()[1]=="in") & (59<=int(height.groups()[0])) &\
                             (int(height.groups()[0])<=76):
                             valid_height=True
                    if hair:
                        valid_hair=True
                    if passport_dict["ecl"] in eyes:
                        valid_eye=True
                    if (len(passport_dict["pid"])==9) & (passport_dict["pid"].isnumeric()):
                        valid_pid=True
                    if (len(passport_dict["byr"])==4) & (1920<=int(passport_dict["byr"])) &\
                       (int(passport_dict["byr"])<=2002) & (len(passport_dict["iyr"])==4) &\
                       (2010<=int(passport_dict["iyr"])) & (int(passport_dict["iyr"])<=2020) &\
                       (len(passport_dict["eyr"])==4) & (2020<=int(passport_dict["eyr"])) &\
                       (int(passport_dict["eyr"])<=2030)& valid_height & valid_hair&\
                       valid_eye & valid_pid:
                        valid2+=1
                passport_dict={}
    print("There are %d valid passports"%valid1)
    print("There are %d strongly valid passports"%valid2)

#Day_5
with open('Day5/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    ids=[]
    for line in reader:
        row=line[0][:7]
        column=line[0][7:]
        list_of_rows=[i for i in range(128)]
        list_of_columns=[i for i in range(8)]
        for i in row:
            if i=="F":
                list_of_rows=list_of_rows[:int(len(list_of_rows)/2)]
            else:
                list_of_rows=list_of_rows[int(len(list_of_rows)/2):]
        for i in column:
            if i=="L":
                list_of_columns=list_of_columns[:int(len(list_of_columns)/2)]
            else:
                list_of_columns=list_of_columns[int(len(list_of_columns)/2):]
        id=list_of_rows[0]*8+list_of_columns[0]
        ids.append(id)
    for i in ids[:-1]:
        if i+1 not in ids:
            my_id=i+1
    print("The highest ID is: "+str(max(ids)))
    print("My ID is: "+str(my_id))


#Day_6
def split(word):
    return [char for char in word]
def length_calculator(answers,any_unique,all_unique):
    letters=''.join(answers)
    any_unique.append(len(set(letters)))
    all_answered=split(answers.pop(0))
    for i in answers:
        for j in all_answered:
            if j not in i:
                all_answered=[k for k in all_answered if k != j]
    all_unique.append(len(all_answered))
    return any_unique,all_unique
with open('Day6/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    answers=[]
    any_unique=[]
    all_unique=[]
    for line in reader:
        if line==[]:
            any_unique,all_unique=length_calculator(answers,any_unique,all_unique)
            answers=[]
        else:
            answers.extend(line)
    any_unique,all_unique=length_calculator(answers,any_unique,all_unique)
    print("The number of questions anyone answered 'yes': "+ str(sum(any_unique)))
    print("The number of questions everyone answered 'yes': "+ str(sum(all_unique)))
