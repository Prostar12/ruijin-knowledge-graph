import logging, sys, argparse

en = []
def str2bool(v):
    # copy from StackOverflow
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def get_entity(tag_seq, char_seq):
    #PER = get_PER_entity(tag_seq, char_seq)
    #LOC = get_LOC_entity(tag_seq, char_seq)
    #ORG = get_ORG_entity(tag_seq, char_seq)
	
    global en
    get_Disease_entity(tag_seq, char_seq)
    get_Reason_entity(tag_seq, char_seq)
    get_Symptom_entity(tag_seq, char_seq)
    get_Test_entity(tag_seq, char_seq)
    get_Test_Value_entity(tag_seq, char_seq)
    get_Drug_entity(tag_seq, char_seq)
    get_Frequency_entity(tag_seq, char_seq)
    get_Amount_entity(tag_seq, char_seq)
    get_Method_entity(tag_seq, char_seq)
    get_Treatment_entity(tag_seq, char_seq)
    get_Operation_entity(tag_seq, char_seq)
    get_SideEff_entity(tag_seq, char_seq)
    get_Anatomy_entity(tag_seq, char_seq)
    get_Level_entity(tag_seq, char_seq)
    get_Duration_entity(tag_seq, char_seq)
    en_p = en
    en = []
    return en_p
 

def get_Disease_entity(tag_seq, char_seq):
    length = len(char_seq)
    start = []
    Disease = []
    poi_start = -1
    #print(list(enumerate(zip(char_seq, tag_seq)))) 
    #print(locals())
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        #if tag == 'I-Disease':
            #continue
        poi_start += 1
        
        if tag == 'B-Disease':
            #en_dict['start'] = poi_start
            start.append(poi_start)
            #print(start)
            if 'disease' in locals().keys():
                print(disease)
                Disease.append(disease)
                del disease
            disease = char
            if i+1 == length:
                Disease.append(disease)
        if tag == 'I-Disease':
            if 'disease' in locals().keys():
                disease += char
                if i+1 == length:
                    Disease.append(disease)
            #else:
        if tag not in ['I-Disease', 'B-Disease']:
            if 'disease' in locals().keys():
                Disease.append(disease)
                del disease
            continue
    for k in range(len(start)):
        en_dict = {}
        en_dict['word'] = Disease[k]
        en_dict['start'] = start[k]
        en_dict['end'] = len(Disease[k]) + start[k]
        
        en_dict['type'] = 'Disease'
        en.append(en_dict)
    return en

def get_Reason_entity(tag_seq, char_seq):
    length = len(char_seq)
    start = []
    Reason = []
    poi_start = -1
    
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        poi_start += 1
        if tag == 'B-Reason':
            #en_dict['start'] = poi_start
            start.append(poi_start)
            #print(start)
            if 'reason' in locals().keys():
                Reason.append(reason)
                del reason
            reason = char
            if i+1 == length:
                Reason.append(reason)
        if tag == 'I-Reason':
            if 'reason' in locals().keys():
                reason += char
                if i+1 == length:
                    Reason.append(reason)
        if tag not in ['I-Reason', 'B-Reason']:
            if 'reason' in locals().keys():
                Reason.append(reason)
                del reason
            continue
    for k in range(len(start)):
        en_dict = {}
        en_dict['word'] = Reason[k]
        en_dict['start'] = start[k]
        en_dict['end'] = len(Reason[k]) + start[k]
        
        en_dict['type'] = 'Reason'
        en.append(en_dict)
    return en

def get_Symptom_entity(tag_seq, char_seq):
    length = len(char_seq)
    start = []
    Symptom = []
    poi_start = -1
    
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        poi_start += 1
        if tag == 'B-Symptom':
            #en_dict['start'] = poi_start
            start.append(poi_start)
            #print(start)
            if 'symptom' in locals().keys():
                Symptom.append(symptom)
                del symptom
            symptom = char
            if i+1 == length:
                Symptom.append(symptom)
        if tag == 'I-Symptom':
            if 'symptom' in locals().keys():
                symptom += char
                if i+1 == length:
                    Symptom.append(symptom)
        if tag not in ['I-Symptom', 'B-Symptom']:
            if 'symptom' in locals().keys():
                Symptom.append(symptom)
                del symptom
            continue
    for k in range(len(start)):
        en_dict = {}
        en_dict['word'] = Symptom[k]
        en_dict['start'] = start[k]
        en_dict['end'] = len(Symptom[k]) + start[k]
        
        en_dict['type'] = 'Symptom'
        en.append(en_dict)
    return en

def get_Test_entity(tag_seq, char_seq):
    length = len(char_seq)
    start = []
    Test = []
    poi_start = -1
    
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        poi_start += 1
        if tag == 'B-Test':
            #en_dict['start'] = poi_start
            start.append(poi_start)
            #print(start)
            if 'test' in locals().keys():
                Test.append(test)
                del test
            test = char
            if i+1 == length:
                Test.append(test)
        if tag == 'I-Test':
            if 'test' in locals().keys():
                test += char
                if i+1 == length:
                    Test.append(test)
        if tag not in ['I-Test', 'B-Test']:
            if 'test' in locals().keys():
                Test.append(test)
                del test
            continue
    for k in range(len(start)):
        en_dict = {}
        en_dict['word'] = Test[k]
        en_dict['start'] = start[k]
        en_dict['end'] = len(Test[k]) + start[k]
        
        en_dict['type'] = 'Test'
        en.append(en_dict)
    return en

def get_Test_Value_entity(tag_seq, char_seq):
    length = len(char_seq)
    start = []
    Test_Value = []
    poi_start = -1
    
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        poi_start += 1
        if tag == 'B-Test_Value':
            #en_dict['start'] = poi_start
            start.append(poi_start)
            #print(start)
            if 'test_value' in locals().keys():
                Test_Value.append(test_value)
                del test_value
            test_value = char
            if i+1 == length:
                Test_Value.append(test_value)
        if tag == 'I-Test_Value':
            if 'test' in locals().keys():
                test_value += char
                if i+1 == length:
                    Test_Value.append(test_value)
        if tag not in ['I-Test_Value', 'B-Test_Value']:
            if 'test_value' in locals().keys():
                Test_Value.append(test_value)
                del test_value
            continue
    for k in range(len(start)):
        en_dict = {}
        en_dict['word'] = Test_Value[k]
        en_dict['start'] = start[k]
        en_dict['end'] = len(Test_Value[k]) + start[k]
        
        en_dict['type'] = 'Test_Value'
        en.append(en_dict)
    return en

def get_Drug_entity(tag_seq, char_seq):
    length = len(char_seq)
    start = []
    Drug = []
    poi_start = -1
    
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        poi_start += 1
        if tag == 'B-Drug':
            #en_dict['start'] = poi_start
            start.append(poi_start)
            #print(locals().keys())
            if 'drug' in locals().keys():
                Drug.append(drug)
                del drug
            drug = char
            if i+1 == length:
                Drug.append(drug)
        if tag == 'I-Drug':
            if 'drug' in locals().keys():
                drug += char
                if i+1 == length:
                    Drug.append(drug)
        if tag not in ['I-Drug', 'B-Drug']:
            if 'drug' in locals().keys():
                Drug.append(drug)
                del drug
            continue
    for k in range(len(start)):
        en_dict = {}
        en_dict['word'] = Drug[k]
        en_dict['start'] = start[k]
        en_dict['end'] = len(Drug[k]) + start[k]
        
        en_dict['type'] = 'Drug'
        en.append(en_dict)
    return en

def get_Frequency_entity(tag_seq, char_seq):
    length = len(char_seq)
    start = []
    Frequency = []
    poi_start = -1
    
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        poi_start += 1
        if tag == 'B-Frequency':
            #en_dict['start'] = poi_start
            start.append(poi_start)
            #print(start)
            if 'frequency' in locals().keys():
                Frequency.append(frequency)
                del frequency
            frequency = char
            if i+1 == length:
                Frequency.append(frequency)
        if tag == 'I-Frequency':
            if 'frequency' in locals().keys():
                frequency += char
                if i+1 == length:
                    Frequency.append(frequency)
        if tag not in ['I-Frequency', 'B-Frequency']:
            if 'frequency' in locals().keys():
                Frequency.append(frequency)
                del frequency
            continue
    for k in range(len(start)):
        en_dict = {}
        en_dict['word'] = Frequency[k]
        en_dict['start'] = start[k]
        en_dict['end'] = len(Frequency[k]) + start[k]
        
        en_dict['type'] = 'Frequency'
        en.append(en_dict)
    return en

'''def get_Amount_entity(tag_seq, char_seq):
    length = len(char_seq)
    start = []
    Amount = []
    poi_start = -1
    
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        poi_start += 1
        if tag == 'B-Amount':
            #en_dict['start'] = poi_start
            start.append(poi_start)
            #print(start)
            if 'amount' in locals().keys():
                Amount.append(amount)
                del amount
            amount = char
            if i+1 == length:
                Amount.append(amount)
        if tag == 'I-Amount':
            amount += char
            if i+1 == length:
                Amount.append(amount)
        if tag not in ['I-Amount', 'B-Amount']:
            if 'amount' in locals().keys():
                Amount.append(amount)
                del amount
            continue
    for k in range(len(start)):
        en_dict = {}
        en_dict['word'] = Amount[k]
        en_dict['start'] = start[k]
        en_dict['end'] = len(Amount[k]) + start[k]
        
        en_dict['type'] = 'Amount'
        en.append(en_dict)
    return en'''
	
def get_Amount_entity(tag_seq, char_seq):
    length = len(char_seq)
    start = []
    Amount = []
    poi_start = -1
    
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        #print(i)
        poi_start += 1
        if tag == 'B-Amount':
            #en_dict['start'] = poi_start
            start.append(poi_start)
            #print(locals().keys())
            if 'amount' in locals().keys():
                
                Amount.append(amount)
                #print(Amount)
                del amount
            amount = char
            
            if i+1 == length:
                Amount.append(amount)
        #amount1 = amount
        if tag == 'I-Amount':
            if 'amount' in locals().keys():
                amount += char
                if i+1 == length:
                    Amount.append(amount)
        if tag not in ['I-Amount', 'B-Amount']:
            if 'amount' in locals().keys():
                Amount.append(amount)
                del amount
            continue
    for k in range(len(start)):
        en_dict = {}
        en_dict['word'] = Amount[k]
        en_dict['start'] = start[k]
        en_dict['end'] = len(Amount[k]) + start[k]
        
        en_dict['type'] = 'Amount'
        en.append(en_dict)
    return en

def get_Method_entity(tag_seq, char_seq):
    length = len(char_seq)
    start = []
    Method = []
    poi_start = -1
    
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        poi_start += 1
        if tag == 'B-Method':
            #en_dict['start'] = poi_start
            start.append(poi_start)
            #print(start)
            if 'method' in locals().keys():
                Method.append(method)
                del method
            method = char
            if i+1 == length:
                Method.append(method)
        if tag == 'I-Method':
            if 'method' in locals().keys():
                method += char
                if i+1 == length:
                    Method.append(method)
        if tag not in ['I-Method', 'B-Method']:
            if 'method' in locals().keys():
                Method.append(method)
                del method
            continue
    for k in range(len(start)):
        en_dict = {}
        en_dict['word'] = Method[k]
        en_dict['start'] = start[k]
        en_dict['end'] = len(Method[k]) + start[k]
        
        en_dict['type'] = 'Method'
        en.append(en_dict)
    return en

def get_Treatment_entity(tag_seq, char_seq):
    length = len(char_seq)
    start = []
    Treatment = []
    poi_start = -1
    
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        poi_start += 1
        if tag == 'B-Treatment':
            #en_dict['start'] = poi_start
            start.append(poi_start)
            #print(start)
            if 'treatment' in locals().keys():
                Treatment.append(treatment)
                del treatment
            treatment = char
            if i+1 == length:
                Treatment.append(treatment)
        if tag == 'I-Treatment':
            if 'treatment' in locals().keys():
                treatment += char
                if i+1 == length:
                    Treatment.append(treatment)
        if tag not in ['I-Treatment', 'B-Treatment']:
            if 'treatment' in locals().keys():
                Treatment.append(treatment)
                del treatment
            continue
    for k in range(len(start)):
        en_dict = {}
        en_dict['word'] = Treatment[k]
        en_dict['start'] = start[k]
        en_dict['end'] = len(Treatment[k]) + start[k]
        
        en_dict['type'] = 'Treatment'
        en.append(en_dict)
    return en

def get_Operation_entity(tag_seq, char_seq):
    length = len(char_seq)
    start = []
    Operation = []
    poi_start = -1
    
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        poi_start += 1
        if tag == 'B-Operation':
            #en_dict['start'] = poi_start
            start.append(poi_start)
            #print(start)
            if 'operation' in locals().keys():
                Operation.append(operation)
                del operation
            operation = char
            if i+1 == length:
                Operation.append(operation)
        if tag == 'I-Operation':
            if 'operation' in locals().keys():
                operation += char
                if i+1 == length:
                    Operation.append(operation)
        if tag not in ['I-Operation', 'B-Operation']:
            if 'operation' in locals().keys():
                Operation.append(operation)
                del operation
            continue
    for k in range(len(start)):
        en_dict = {}
        en_dict['word'] = Operation[k]
        en_dict['start'] = start[k]
        en_dict['end'] = len(Operation[k]) + start[k]
        
        en_dict['type'] = 'Operation'
        en.append(en_dict)
    return en

def get_SideEff_entity(tag_seq, char_seq):
    length = len(char_seq)
    start = []
    SideEff = []
    poi_start = -1
    
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        poi_start += 1
        if tag == 'B-SideEff':
            #en_dict['start'] = poi_start
            start.append(poi_start)
            #print(start)
            if 'sideeff' in locals().keys():
                SideEff.append(sideeff)
                del sideeff
            sideeff = char
            if i+1 == length:
                SideEff.append(sideeff)
        if tag == 'I-SideEff':
            if 'sideeff' in locals().keys():
                sideeff += char
                if i+1 == length:
                    SideEff.append(sideeff)
        if tag not in ['I-SideEff', 'B-SideEff']:
            if 'sideeff' in locals().keys():
                SideEff.append(sideeff)
                del sideeff
            continue
    for k in range(len(start)):
        en_dict = {}
        en_dict['word'] = SideEff[k]
        en_dict['start'] = start[k]
        en_dict['end'] = len(SideEff[k]) + start[k]
        
        en_dict['type'] = 'SideEff'
        en.append(en_dict)
    return en

def get_Anatomy_entity(tag_seq, char_seq):
    length = len(char_seq)
    start = []
    Anatomy = []
    poi_start = -1
    
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        poi_start += 1
        if tag == 'B-Anatomy':
            #en_dict['start'] = poi_start
            start.append(poi_start)
            #print(start)
            if 'anatomy' in locals().keys():
                Anatomy.append(anatomy)
                del anatomy
            anatomy = char
            if i+1 == length:
                Anatomy.append(anatomy)
        if tag == 'I-Anatomy':
            if 'anatomy' in locals().keys():
                anatomy += char
                if i+1 == length:
                    Anatomy.append(anatomy)
        if tag not in ['I-Anatomy', 'B-Anatomy']:
            if 'anatomy' in locals().keys():
                Anatomy.append(anatomy)
                del anatomy
            continue
    for k in range(len(start)):
        en_dict = {}
        en_dict['word'] = Anatomy[k]
        en_dict['start'] = start[k]
        en_dict['end'] = len(Anatomy[k]) + start[k]
        
        en_dict['type'] = 'Anatomy'
        en.append(en_dict)
    return en

def get_Level_entity(tag_seq, char_seq):
    length = len(char_seq)
    start = []
    Level = []
    poi_start = -1
    
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        poi_start += 1
        if tag == 'B-Level':
            #en_dict['start'] = poi_start
            start.append(poi_start)
            #print(start)
            if 'level' in locals().keys():
                #print(level)
                Level.append(level)
                del level
            level = char
            if i+1 == length:
                Level.append(level)
        if tag == 'I-Level':
            if 'level' in locals().keys():
                level += char
                if i+1 == length:
                    Level.append(level)
            #else:
                
        if tag not in ['I-Level', 'B-Level']:
            if 'level' in locals().keys():
                Level.append(level)
                del level
            continue
    for k in range(len(start)):
        en_dict = {}
        en_dict['word'] = Level[k]
        en_dict['start'] = start[k]
        en_dict['end'] = len(Level[k]) + start[k]
        
        en_dict['type'] = 'Level'
        en.append(en_dict)
    return en

def get_Duration_entity(tag_seq, char_seq):
    length = len(char_seq)
    start = []
    Duration = []
    poi_start = -1
    
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        poi_start += 1
        if tag == 'B-Duration':
            #en_dict['start'] = poi_start
            start.append(poi_start)
            #print(start)
            if 'duration' in locals().keys():
                Duration.append(duration)
                del duration
            duration = char
            if i+1 == length:
                Duration.append(duration)
        if tag == 'I-Duration':
            if 'duration' in locals().keys():
                duration += char
                if i+1 == length:
                    Duration.append(duration)
        if tag not in ['I-Duration', 'B-Duration']:
            if 'duration' in locals().keys():
                Duration.append(duration)
                del duration
            continue
    for k in range(len(start)):
        en_dict = {}
        en_dict['word'] = Duration[k]
        en_dict['start'] = start[k]
        en_dict['end'] = len(Duration[k]) + start[k]
        
        en_dict['type'] = 'Duration'
        en.append(en_dict)
    return en

def get_logger(filename):
    logger = logging.getLogger('logger')
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    handler = logging.FileHandler(filename)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s: %(message)s'))
    logging.getLogger().addHandler(handler)
    return logger
