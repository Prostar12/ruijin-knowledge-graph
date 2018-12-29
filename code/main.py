import test_chuli
import pre_chuli

import tensorflow as tf
import numpy as np
import os, argparse, time, random
from model import BiLSTM_CRF
from utils import str2bool, get_logger, get_entity
from data import read_corpus, read_dictionary, tag2label, random_embedding

test_chuli.write_clean()
test_chuli.cutspace()
test_chuli.loc_word()

## Session configuration
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # default: 0
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
config.gpu_options.per_process_gpu_memory_fraction = 0.8  # need ~700MB GPU memory


## hyperparameters
parser = argparse.ArgumentParser(description='BiLSTM-CRF for Chinese NER task')
parser.add_argument('--train_data', type=str, default='../code/train.txt', help='train data source')
parser.add_argument('--test_data', type=str, default='../code/test.txt', help='test data source')
parser.add_argument('--batch_size', type=int, default=64, help='#sample of each minibatch')
parser.add_argument('--epoch', type=int, default=38, help='#epoch of training')
parser.add_argument('--hidden_dim', type=int, default=300, help='#dim of hidden state')
parser.add_argument('--optimizer', type=str, default='Adam', help='Adam/Adadelta/Adagrad/RMSProp/Momentum/SGD')
parser.add_argument('--CRF', type=str2bool, default=True, help='use CRF at the top layer. if False, use Softmax')
parser.add_argument('--lr', type=float, default=0.002, help='learning rate')
parser.add_argument('--clip', type=float, default=5.0, help='gradient clipping')
parser.add_argument('--dropout', type=float, default=0.5, help='dropout keep_prob')
parser.add_argument('--update_embedding', type=str2bool, default=True, help='update embedding during training')
parser.add_argument('--pretrain_embedding', type=str, default='random', help='use pretrained char embedding or init it randomly')
parser.add_argument('--embedding_dim', type=int, default=300, help='random init char embedding_dim')
parser.add_argument('--shuffle', type=str2bool, default=True, help='shuffle training data before each epoch')
parser.add_argument('--mode', type=str, default='demo', help='train/test/demo')
parser.add_argument('--demo_model', type=str, default='154138625', help='model for test and demo')
args = parser.parse_args()

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files
		
## get char embeddings
word2id = read_dictionary('../code/word2id.pkl')
if args.pretrain_embedding == 'random':
    embeddings = random_embedding(word2id, args.embedding_dim)
else:
    embedding_path = 'pretrain_embedding.npy'
    embeddings = np.array(np.load(embedding_path), dtype='float32')


## read corpus and get training data
if args.mode != 'demo':
    train_path = os.path.join('.', args.train_data)
    test_path = os.path.join('.', args.test_data)
    train_data = read_corpus(train_path)
    test_data = read_corpus(test_path); test_size = len(test_data)


## paths setting
paths = {}
timestamp = str(int(time.time())) if args.mode == 'train' else args.demo_model
#output_path = os.path.join('.', args.train_data+"_save", timestamp)
#output_path = os.path.join('.', '../data', model)
output_path = '../data/model'
if not os.path.exists(output_path): os.makedirs(output_path)
summary_path = os.path.join(output_path, "summaries")
paths['summary_path'] = summary_path
if not os.path.exists(summary_path): os.makedirs(summary_path)
model_path = os.path.join(output_path, "checkpoints/")
print(model_path)
if not os.path.exists(model_path): os.makedirs(model_path)
ckpt_prefix = os.path.join(model_path, "model")
paths['model_path'] = ckpt_prefix
result_path = os.path.join(output_path, "results")
paths['result_path'] = result_path
if not os.path.exists(result_path): os.makedirs(result_path)
log_path = os.path.join(result_path, "log.txt")
paths['log_path'] = log_path
get_logger(log_path).info(str(args))


## training model
if args.mode == 'train':
    model = BiLSTM_CRF(args, embeddings, tag2label, word2id, paths, config=config)
    model.build_graph()

    ## hyperparameters-tuning, split train/dev
    # dev_data = train_data[:5000]; dev_size = len(dev_data)
    # train_data = train_data[5000:]; train_size = len(train_data)
    # print("train data: {0}\ndev data: {1}".format(train_size, dev_size))
    # model.train(train=train_data, dev=dev_data)

    ## train model on the whole training data
    print("train data: {}".format(len(train_data)))
    model.train(train=train_data, dev=test_data)  # use test_data as the dev_data to see overfitting phenomena

## testing model
elif args.mode == 'test':
    ckpt_file = tf.train.latest_checkpoint(model_path)
    print(ckpt_file)
    paths['model_path'] = ckpt_file
    model = BiLSTM_CRF(args, embeddings, tag2label, word2id, paths, config=config)
    model.build_graph()
    print("test data: {}".format(test_size))
    model.test(test_data)

## demo
elif args.mode == 'demo':
    ckpt_file = tf.train.latest_checkpoint(model_path)
	#print(ckpt_file)
#    ckpt_file = 'E:/ruijin/zh-NER-TF-master22/data_path_save/1541386253/checkpoints/model-20128'#读取模型 test_b_ori
    #ckpt_file = 'E:/ruijin/zh-NER-TF-master22/data_path_save/1540878231/checkpoints/model-25160'#读取模型 test_b_ori2
    print(ckpt_file)
    paths['model_path'] = ckpt_file
    model = BiLSTM_CRF(args, embeddings, tag2label, word2id, paths, config=config)
    model.build_graph()
    saver = tf.train.Saver()
    with tf.Session(config=config) as sess:
        print('============= demo =============')
        saver.restore(sess, ckpt_file)
        file_name_list = file_name('../data/test2')#读取测试集
        output_path = '../data/test_ori'
        if not os.path.exists(output_path): os.makedirs(output_path)
        for name in file_name_list:
            name_dir =  '../data/test2/' + name
            write_dir = '../data/test_ori/rec_' + name#预测完后写入的文件
            f = open(name_dir, 'r', encoding = 'utf-8')
            fw = open(write_dir, 'w', encoding = 'utf-8')
            while True:
                line = f.readline()
                if line == '':
                    break
                line = list(line.strip())
                demo_data = [(line, ['O'] * len(line))]
                tag = model.demo_one(sess, demo_data)
                result = get_entity(tag, line)
                #result = sorted(result1[0].items(), key=lambda x:x[1], reverse = False)				
            entity_list = result
            #print(entity_list)
            #j_sort = []
            
            i = 0
            for en in entity_list:
                en_write1 = en['start']
                en_write2 = en['end']
                en_write3 = en['type']
                en_write4 = en['word']
                i += 1
                fw.write(str(en_write1)+'\t'+str(en_write2)+'\t'+en_write3+'\t'+en_write4+'\n')
            print(entity_list)
            fw.close()
	


pre_chuli.sort()
pre_chuli.duiying()
pre_chuli.jiafenhao()
pre_chuli.quchong()
