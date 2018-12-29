f = open('E:\\ruijin\\zh-NER-TF-master\\data_path\\t_label2.txt', 'r', encoding = 'utf-8')
fw = open('E:\\ruijin\\zh-NER-TF-master\\data_path\\t_label3.txt', 'w', encoding = 'utf-8')
flag = 0
while True:
	line = f.readline()
	if line == '':
		break
	flag += 1
	if flag == 100:
		flag = 0
		fw.write(line+' '+'\n')
	else:
		fw.write(line)
	if line == ' \n':
		flag = 0
f.close()
fw.close()