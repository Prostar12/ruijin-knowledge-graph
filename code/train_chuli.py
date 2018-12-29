import re
import os

def file_name(file_dir):   
    for root, dirs, files in os.walk(file_dir):  
       # print(root) #当前目录路径  
        #print(dirs) #当前路径下所有子目录  
        #print(files) #当前路径下所有非目录子文件
        return files
   
def readfile1(file_name):
    lines = ''
    f = open(file_name, 'r', encoding = 'utf-8')
    while True:
        line = f.readline()
        #line = line.strip('\n')
        lines = lines + line
        if line == '':
            break
    #file_name.close()
    return lines

def readfile2(file_name):
    tag_temp = []
    tag = []
    f = open(file_name, 'r', encoding = 'utf-8')
    while True:
        line = f.readline()
        if line == '':
            break
        line = line.split('\t')
        line_1 = line[1].split()
        #print(len(line_1))
        if len(line_1) == 3:
            tag_temp.append(line[0])
            tag_temp.append(line_1[0])
            tag_temp.append(line_1[1])
            tag_temp.append(line_1[2])
            tag_temp.append(line[2].strip())
            #print(tag_temp)
            tag.append(tag_temp)
            tag_temp = []
        else:
            if ';' not in line_1[3]:
                tag_temp.append(line[0])
                tag_temp.append(line_1[0])
                tag_temp.append(line_1[1])
                tag_temp.append(line_1[3])
                tag_temp.append(line[2].strip())
                tag.append(tag_temp)
                tag_temp = []
        
    return tag

def biaozhu(file_name_txt, file_name_ann, file_name_write):
    f_txt = readfile1(file_name_txt)
    f_ann = readfile2(file_name_ann)
    #print(f_ann)
    num1 = []
    num2 = []
    cla = []
    i = 0
    for num in f_ann:
        i += 1
        if len(num) != 5:
            continue
        num1.append(int(num[2]))#起始位置
        
        num2.append(int(num[3]))#结束位置   
        cla.append(num[1])
    #print(len(cla))
    #print(i)
    index = sorted(range(len(num1)), key=lambda k: num1[k],reverse=False)
    num1 = sorted(num1,reverse=False)
    num2 = [num2[i] for i in index]
    cla = [cla[i] for i in index]
    #print(num1.index(2686))
    #print(num2)
    tt = -2
    fw = open(file_name_write, 'w', encoding = 'utf-8')
    i_list = []
    for num_chara in range(len(f_txt)):
        if f_txt[num_chara] == ' ':
            continue
        if f_txt[num_chara] != '\n': 
            if num_chara in num1:
                #print(num_chara)
                tt += 1
                if tt < len(num1) and tt >= 0:
                    if num_chara < min(num2[num1.index(num_chara) - 1], num2[num1.index(num_chara) - 2]):
                       
                        print(f_txt[num_chara])
                        continue
                    #if num_chara < num2[num1.index(num_chara) - 2] and tt>= 0:
                        #print(f_txt[num_chara])
                        #continue
                b_label = f_txt[num_chara] + ' ' +'B-' + cla[num1.index(num_chara)] + '\n'
                fw.write(b_label)
                for i in range(num_chara + 1, num2[num1.index(num_chara)]):
                    i_list.append(i)
                    if f_txt[i] == '\n':
                        continue
                    else:
                        i_label = f_txt[i] + ' ' +'I-' + cla[num1.index(num_chara)] + '\n'
                        fw.write(i_label)
            else:
                if num_chara not in i_list:
                    
                    if f_txt[num_chara] == '。':
                        o_label = f_txt[num_chara] + ' ' +'O' + '\n' + ' ' + '\n'
                    else:
                        o_label = f_txt[num_chara] + ' ' +'O' + '\n'
                    fw.write(o_label)
    fw.close()
#biaozhu('E:\\Data\\ruijin\\ruijin_round1_train2_20181022\\ruijin_round1_train2_20181022\\2.txt','E:\\Data\\ruijin\\ruijin_round1_train2_20181022\\ruijin_round1_train2_20181022\\2.ann','E:\\Data\\ruijin\\2.txt')
#print(t)

file_name_list = file_name('E:\\Data\\ruijin\\ruijin_round1_train2_20181022\\ruijin_round1_train2_20181022')     
file_name_ann_list = []
file_name_txt_list = []           
for name in list(file_name_list):
    if 'ann' in name:
        file_name_ann_list.append(name)
    else:
        file_name_txt_list.append(name)
#print(file_name_ann) 
for num_name in range(len(file_name_ann_list)):
    #print(file_name_ann[num_name])
    file_name_write = 'E:\\Data\\ruijin\\ruijin_label\\' +  file_name_ann_list[num_name].replace('.ann', '_label.txt')
    file_name_ann = 'E:\\Data\\ruijin\\ruijin_round1_train2_20181022\\ruijin_round1_train2_20181022\\' + file_name_ann_list[num_name]
    #print(file_name_ann)
    file_name_txt = 'E:\\Data\\ruijin\\ruijin_round1_train2_20181022\\ruijin_round1_train2_20181022\\' + file_name_txt_list[num_name]
    biaozhu(file_name_txt, file_name_ann, file_name_write)
    
    
file_name_list2 = []
#test_list = ['0.ann', '6.ann', '9.ann', '10.ann', '123_3_1.ann', '123_12.ann', '126_1.ann', '126_6.ann', '126_24.ann', '131_24.ann']
test_list = []
for num_name in range(len(file_name_ann_list)):
        if file_name_ann_list[num_name] not in test_list:
            file_name = 'E:\\Data\\ruijin\\ruijin_label\\' +  file_name_ann_list[num_name].replace('.ann', '_label.txt')
            file_name_list2.append(file_name)    
fw = open('E:\\Data\\ruijin\\ruijin_round1_train1_20181010\\t_test01.txt', 'w', encoding = 'utf-8')
for i in file_name_list2:
    #print(i)
    #file_name2 = 'E:\\Data\\ruijin\\ruijin_round1_train1_20181010\\' + str(i) + '_test.txt'
    
    f = open(i, 'r', encoding = 'utf-8')
    while True:
        line = f.readline()
        fw.write(line)
        if line == '':
            break
f.close()
fw.close()



