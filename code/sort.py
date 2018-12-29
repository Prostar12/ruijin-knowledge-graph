import re
import os

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files
		
		
#识别出来的实体不是按位置排序的，所以要把它们按位置排

file_name_list = file_name('E:\\ruijin\\test_chuli\\test_b_ori')	
for name in file_name_list:	
	f = open('E:\\ruijin\\test_chuli\\test_b_ori\\'+name, 'r', encoding = 'utf-8')
	fw = open('E:\\ruijin\\test_chuli\\test_b_ori_sort\\'+name, 'w', encoding = 'utf-8')
	lines = []
	while True:
		line = f.readline()
		if line == '':
			break
		line = line.split('\t')
		lines.append(line)

	t = sorted(lines,key=(lambda x:int(x[0])))
	for item in t:
		fw.write(item[0]+'\t'+item[1]+'\t'+item[2]+'\t'+item[3]+'\n')


	f.close()
	fw.close()







#这一步是和原始文本位置对应，但没有对应分号
file_name_list2 = file_name('E:\\ruijin\\ruijin_round1_test_b_20181112')
#file_name_list2 = ['128_20_6.txt']
print(file_name_list2)
for name in file_name_list2:
    f1 = open('E:\\ruijin\\test_chuli\\loc_word_b\\loc_'+name, 'r', encoding = 'utf-8')#这个是读取对应测试集的字符和位置
    f2 = open('E:\\ruijin\\test_chuli\\test_b_ori_sort\\rec_'+name, 'r', encoding = 'utf-8')#读取上一步排好序的测试集预测文件
    fw = open('E:\\ruijin\\test_chuli\\rec_text9_b\\'+name, 'w', encoding = 'utf-8') #写入到这个文件
    loc_list = []
    lines = []
    while True:
        line = f2.readline()
        if line == '':
            break
        rr = line
        line = line.split('\t')
        #print(rr.split())
        if len(rr.split())>3:
            #print(line)
            if len(line) != 1:
                lines.append(line)
    #print(lines)
    a2=[]
    for item in lines:
        a1 =[]
        for t in item:
            s = re.sub('[\r\n\t]', '', t)
            a1.append(s)
        a2.append(a1)
    #print(a2)
    while True:
        line = f1.readline()
        if line == '':
            break
        line = line.split()
        loc_list.append(line)
        for item in loc_list:
            if item == []:
                loc_list.remove(item)
        for item in range(len(loc_list)):
            if len(loc_list[item]) == 1:
                loc_list[item] = [' ', loc_list[item][0]]
    print(loc_list)
    f1.close()
    #print(a2)
    j = int(a2[0][0])
    f_list = []
    for item in a2:
        #print(j)
        if item[0] in f_list:
            break
        else:
            f_list.append(item[0]) 
            #print(item)
            #if item[3][0] == ' ':
                #item[0] = str(int(item[0]) - 1)
                #item[3][0] = ''
            for i in range(j, j+len(loc_list)):
                #print(j)
                flag = 0
                flag2 = 0
                reg = 0
                for k in range(len(item[3])):
                    #print(item[3]
                    if i+k < len(loc_list)-1:
                        
                        if k == 0:
                            if item[3][k] == loc_list[i+k][0]:
                                flag += 1
                            else:
                                break
                            #if item[3][k] == ' ':
                                #print(item[3])
                                #flag += 1
                                        
                        if k != 0:
                            if loc_list[i+k+reg][0] == ' ':
                                reg += 1
                                flag2 += 1
                            if item[3][k] != loc_list[i+k][0] and item[3][k] != loc_list[i+k+reg][0]:
                                break
                            else:
                                if item[3][k] == loc_list[i+k][0]:
                                    flag += 1
                                if item[3][k] == loc_list[i+k+reg][0]:
                                    flag += 1
                                    
                                    #reg += 1
                                #print(flag2)
                                
                if flag >= len(item[3]):
                    if flag2 == 0:
                        #print(item)
                        if item[3][0] == ' ':
                            item[0] = int(loc_list[i][1]) + 1
                        else:
                            item[0] = int(loc_list[i][1])
                        item[1] = int(loc_list[i][1]) + len(item[3])
                        j = int(item[1])
                        #print(j)
                    else:
                        print(item)
                        if item[3][0] == ' ':
                            item[0] = int(loc_list[i][1]) + 1
                        else:
                            item[0] = int(loc_list[i][1])
                        item[1] = int(loc_list[i][1]) + len(item[3])+ flag2
                        #print(item['end'])
                        j = int(item[1])
                        #print(j)
            
                    break
    i = 0
    for en in a2:
	    en_write1 = en[0]
	    en_write2 = en[1]
	    en_write3 = en[2]
	    en_write4 = en[3]
	    i += 1
	    fw.write('T' +str(i)+'\t' + str(en_write1)+'\t'+str(en_write2)+'\t'+en_write3+'\t'+en_write4+'\n')
    fw.close()
    f1.close()
    f2.close()