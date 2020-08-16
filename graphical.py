

import csv
import collections
import numpy as np

fan=collections.defaultdict(int)
radiator=collections.defaultdict(int)
engine=collections.defaultdict(int)
temp=collections.defaultdict(int)
starts=collections.defaultdict(int)
low_oil=collections.defaultdict(int)
oil_light=collections.defaultdict(int)

"""
"""
dic_list=[fan,radiator,engine,temp,starts,low_oil,oil_light]

"""
Experiment 1 and 2 are for some test purpose
"""
def experiment1():
    flag=0
    with open('garage.csv','r',encoding='utf-8') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            if flag==1:
                for ele in row:
                    tmp=ele.split()
                    for i in range(len(tmp)):
                        if i==0:
                            continue
                        else:
                            dic_list[i-1][tmp[i]]+=1
            flag=1

    for j in range(len(dic_list)):
        print(dic_list[j])

"""
Experiment 1 and 2 are for some test purpose
"""
def experiment2():
    cnt=0
    flag = 0
    with open('garage.csv','r',encoding='utf-8') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            if flag==1:
                for ele in row:
                    tmp=ele.split()
                    if tmp[1]=='1' and tmp[2]=='1' and tmp[3]=='1' and tmp[4]=='1' and tmp[5]=='1' and tmp[6]=='1' and tmp[7]=='1':
                        cnt+=1
            flag=1
    print(cnt)

"""
this function generates the entire covariance matrix
"""
def covMatrix():
    print('Covariance matrix')
    print('because the matrix is symmetric, I only print out the upper triangular matrix')
    flag = 0
    """
    deal with the data first using csv.reader
    """
    with open('garage.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if flag == 1:
                for ele in row:
                    tmp = ele.split()
                    for i in range(len(tmp)):
                        if i == 0:
                            continue
                        else:
                            dic_list[i - 1][tmp[i]] += 1
            flag = 1

    """
    Main idea here is 
    Cov(X, X)=Var(X)=E(X**2)-[E(X)]**2
    Cov(X,Y)=E(XY)-E(X)E(Y)
    """
    for i in range(1,len(tmp)):
        print()
        for j in range(i,len(tmp)):
            """
            when i==j, we need to calculate Cov(X,X)
            """
            if i==j:
                print(float(dic_list[i-1]['1'])/10000-float(dic_list[i-1]['1']**2)/100000000,end='')
                print('  ',end='')
                continue
            """
            when i!=j, we need to calculate Cov(X,Y)
            """
            zeroOne=0
            oneZero=0
            oneOne=0
            flag = 0
            with open('garage.csv','r',encoding='utf-8') as csvfile:
                reader=csv.reader(csvfile)
                for row in reader:
                    if flag==1:
                        for ele in row:
                            tmp=ele.split()
                            if tmp[i]=='0' and tmp[j]=='1':
                                zeroOne+=1
                            elif tmp[i]=='1' and tmp[j]=='0':
                                oneZero+=1
                            elif tmp[i]=='1' and tmp[j]=='1':
                                oneOne+=1
                    flag=1
            print(float(oneOne)/10000-float(oneZero+oneOne)/10000*float(zeroOne+oneOne)/10000,end='')
            print('  ',end='')
    print()
    print()

"""
In this method, I use a dictionary to count all the times each event occurs
I use collections.defaultdict(int) as my dictionary
I use string.split() method to preprocess the data
"""
def completeJointTable():
    dic=collections.defaultdict(int)
    flag = 0
    with open('garage.csv','r',encoding='utf-8') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            if flag==1:
                for ele in row:
                    array=ele.split()
                    tmp=' '.join(array[1:])
                    dic[tmp]+=1
            flag=1
    """
    convert the numbers to the probability
    """
    for key in dic.keys():
        dic[key]=dic[key]/10000
    print('complete joint probability mass function table')
    print()
    """
    sort the dictionary in ascending order
    """
    order=sorted(dic.items(),key=lambda kv:kv[0])
    print(order)
    # print(dic['1 1 1 1 1 1 1'])
    print()

    """
    the code below is the process of calculating the question (d)
    """
    print('The answer of question 1(d)')
    res=0.0
    for key in dic.keys():
        tmp=key.split()
        if tmp[0]=='1' and tmp[4]=='0' and tmp[5]=='1':
            res+=dic[key]/float(10000.0)
    ans=0.0
    for key in dic.keys():
        tmp = key.split()
        if tmp[4] == '0' and tmp[5] == '1':
            ans += dic[key] / float(10000.0)
    print('P(fan=1,low_oil=1,starts=0)= ',end='')
    print(res)
    print('P(low_oil=1,starts=0)= ',end='')
    print(ans)
    print('P(fan=1 | low_oil=1,starts=0)= ', end='')
    print(res/ans)

"""
All the code of generating contingency table are shown below
If there is only one variable, the solution is simple , just count
If there are two variables which conditional probability should be included
Then we can use two dictionaries to store values
"""
def fanbeltTable():
    cnt = 0
    flag = 0
    with open('garage.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if flag == 1:
                for ele in row:
                    tmp = ele.split()
                    if tmp[1] == '1':
                        cnt += 1
            flag = 1
    print()
    print('fan belt table')
    print('T: '+str(cnt/10000))
    print('F: '+str(1-cnt/10000))
    print()

def radiatorleakTable():
    cnt = 0
    flag = 0
    with open('garage.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if flag == 1:
                for ele in row:
                    tmp = ele.split()
                    if tmp[2] == '1':
                        cnt += 1
            flag = 1
    print()
    print('radiator leak table')
    print('T: ' + str(cnt / 10000))
    print('F: ' + str(1 - cnt / 10000))
    print()


def engineoverheatTable():
    joint=[collections.defaultdict(int)]*8
    condition=[collections.defaultdict(int)]*4
    flag = 0
    with open('garage.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if flag == 1:
                for ele in row:
                    tmp = ele.split()
                    if tmp[1] == '1' and tmp[2]=='1' and tmp[3]=='1':
                        joint[0]['111']+=1
                        condition[0]['11']+=1
                    elif tmp[1] == '1' and tmp[2]=='1' and tmp[3]=='0':
                        joint[1]['110']+=1
                        condition[0]['11'] += 1
                    elif tmp[1] == '1' and tmp[2]=='0' and tmp[3]=='1':
                        joint[2]['101']+=1
                        condition[1]['10'] += 1
                    elif tmp[1] == '1' and tmp[2]=='0' and tmp[3]=='0':
                        joint[3]['100']+=1
                        condition[1]['10'] += 1
                    elif tmp[1] == '0' and tmp[2]=='1' and tmp[3]=='1':
                        joint[4]['011']+=1
                        condition[2]['01'] += 1
                    elif tmp[1] == '0' and tmp[2]=='1' and tmp[3]=='0':
                        joint[5]['010']+=1
                        condition[2]['01'] += 1
                    elif tmp[1] == '0' and tmp[2]=='0' and tmp[3]=='1':
                        joint[6]['001']+=1
                        condition[3]['00'] += 1
                    elif tmp[1] == '0' and tmp[2]=='0' and tmp[3]=='0':
                        joint[7]['000']+=1
                        condition[3]['00'] += 1
            flag = 1
    print()
    print('engine overheat table')
    print('TTT: '+str(float(joint[0]['111'])/condition[0]['11']))
    print('TTF: '+str(float(joint[1]['110']) / condition[0]['11']))
    print('TFT: '+str(float(joint[2]['101']) / condition[1]['10']))
    print('TFF: '+str(float(joint[3]['100']) / condition[1]['10']))
    print('FTT: '+str(float(joint[4]['011']) / condition[2]['01']))
    print('FTF: '+str(float(joint[5]['010']) / condition[2]['01']))
    print('FFT: '+str(float(joint[6]['001']) / condition[3]['00']))
    print('FFF: '+str(float(joint[7]['000']) / condition[3]['00']))
    print()

def templightTable():
    joint = [collections.defaultdict(int)] * 4
    condition = [collections.defaultdict(int)] * 2
    flag = 0
    with open('garage.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if flag == 1:
                for ele in row:
                    tmp = ele.split()
                    if tmp[3] == '1' and tmp[4] == '1':
                        joint[0]['11'] += 1
                        condition[0]['1'] += 1
                    elif tmp[3] == '1' and tmp[4] == '0':
                        joint[1]['10'] += 1
                        condition[0]['1'] += 1
                    elif tmp[3] == '0' and tmp[4] == '1':
                        joint[2]['01'] += 1
                        condition[1]['0'] += 1
                    elif tmp[3] == '0' and tmp[4] == '0':
                        joint[3]['00'] += 1
                        condition[1]['0'] += 1
            flag = 1
    print()
    print('temp light table')
    print('TT: '+str(float(joint[0]['11']) / condition[0]['1']))
    print('TF: '+str(float(joint[1]['10']) / condition[0]['1']))
    print('FT: '+str(float(joint[2]['01']) / condition[1]['0']))
    print('FF: '+str(float(joint[3]['00']) / condition[1]['0']))
    print()

def startsTable():
    joint = [collections.defaultdict(int)] * 4
    condition = [collections.defaultdict(int)] * 2
    flag = 0
    with open('garage.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if flag == 1:
                for ele in row:
                    tmp = ele.split()
                    if tmp[3] == '1' and tmp[5] == '1':
                        joint[0]['11'] += 1
                        condition[0]['1'] += 1
                    elif tmp[3] == '1' and tmp[5] == '0':
                        joint[1]['10'] += 1
                        condition[0]['1'] += 1
                    elif tmp[3] == '0' and tmp[5] == '1':
                        joint[2]['01'] += 1
                        condition[1]['0'] += 1
                    elif tmp[3] == '0' and tmp[5] == '0':
                        joint[3]['00'] += 1
                        condition[1]['0'] += 1
            flag = 1
    print()
    print('starts table')
    print('TT: '+str(float(joint[0]['11']) / condition[0]['1']))
    print('TF: '+str(float(joint[1]['10']) / condition[0]['1']))
    print('FT: '+str(float(joint[2]['01']) / condition[1]['0']))
    print('FF: '+str(float(joint[3]['00']) / condition[1]['0']))
    print()

def lowoilTable():
    cnt = 0
    flag = 0
    with open('garage.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if flag == 1:
                for ele in row:
                    tmp = ele.split()
                    if tmp[6] == '1':
                        cnt += 1
            flag = 1
    print()
    print('low oil table')
    print('T: ' + str(cnt / 10000))
    print('F: ' + str(1 - cnt / 10000))
    print()

def oillightTable():
    joint = [collections.defaultdict(int)] * 4
    condition = [collections.defaultdict(int)] * 2
    flag = 0
    with open('garage.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if flag == 1:
                for ele in row:
                    tmp = ele.split()
                    if tmp[6] == '1' and tmp[7] == '1':
                        joint[0]['11'] += 1
                        condition[0]['1'] += 1
                    elif tmp[6] == '1' and tmp[7] == '0':
                        joint[1]['10'] += 1
                        condition[0]['1'] += 1
                    elif tmp[6] == '0' and tmp[7] == '1':
                        joint[2]['01'] += 1
                        condition[1]['0'] += 1
                    elif tmp[6] == '0' and tmp[7] == '0':
                        joint[3]['00'] += 1
                        condition[1]['0'] += 1
            flag = 1
    print()
    print('oil light table')
    print('TT: '+str(float(joint[0]['11']) / condition[0]['1']))
    print('TF: '+str(float(joint[1]['10']) / condition[0]['1']))
    print('FT: '+str(float(joint[2]['01']) / condition[1]['0']))
    print('FF: '+str(float(joint[3]['00']) / condition[1]['0']))
    print()


covMatrix()

completeJointTable()

fanbeltTable()
radiatorleakTable()
engineoverheatTable()
templightTable()
startsTable()
lowoilTable()
oillightTable()

