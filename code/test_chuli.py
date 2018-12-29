import os
import re

def file_name(file_dir):
	for root, dirs, files in os.walk(file_dir):
		return files
#这个是为了把原始数据的换行去掉
def write_clean():
	#wr = 'E:\\ruijin\\wordvec\\final.txt'
	#fw2 = open(wr, 'w', encoding = 'utf-8')
	#total_text = ''
	file_name_list = file_name('../data/test')
	for name in file_name_list:
		#total_text = ''
		if 'txt' in name:
			name_dir = '../data/test/' + name
			#write_dir = '../data/test1/' + name
			output_path = '../data/test1'
			if not os.path.exists(output_path): os.makedirs(output_path)
			write_dir = output_path + '/' + name
			#print(write_dir)
			#write_dir = output_path = os.path.join('.', '../data', 'test1')
			
			f = open(name_dir, 'r', encoding = 'utf-8')
			fw = open(write_dir, 'w', encoding = 'utf-8')
			text = ''
			
			text_write = ''
			while True:
				line = f.readline()
				if line == '':
					break
				line = line.strip('\n')
				line = line.strip()
				#line = line.split('。', '\n')
				#text.append(line)
				text = text + line
			#total_text = total_text + text
			fw.write(text)
			f.close()
			fw.close()
	#fw2.write(total_text)	
	#fw2.close()
	
def cutspace():
	file_name_list = file_name('../data/test1')
	output_path = '../data/test2'
	if not os.path.exists(output_path): os.makedirs(output_path)
	for name in file_name_list:
		f = open('../data/test1/'+name, 'r', encoding = 'utf-8')
		fw = open('../data/test2/'+name, 'w', encoding = 'utf-8')
		text = ''
		while True:
			line = f.readline()
			if line == '':
				break
			for word in line:
				if word == ' ':
					continue
				else:
					text = text + word
		fw.write(text)
		f.close()
		fw.close()
		
#这个是为了获得测试集字符与对应位置的函数

def loc_word():
	file_name_list = file_name('../data/test')
	output_path = '../data/test3'
	if not os.path.exists(output_path): os.makedirs(output_path)
	for name in file_name_list:
		#name_dir = '../data/test/' + name
		#write_dir = '..data/test_position/loc_' + name
		f = open('../data/test/'+name, 'r', encoding = 'utf-8')
		fw = open('../data/test3/loc_'+name, 'w', encoding = 'utf-8')
		position = 0
		while True:
			line = f.readline()
			if line == '':
				break
			for word in line:
				fw.write(word + ' ' + str(position) + '\n')
				position += 1
		f.close()
		fw.close()

'''		
cutspace()
file_name_list = file_name('E:\\ruijin\\ruijin_round1_test_b_20181112\\')		
loc_word(file_name_list)'''
			
#file_name = file_name('../data/test')
#print(file_name)
#write_clean(file_name)
#write_clean()
#cutspace()
#loc_word()
#print(os.path.abspath('..'))