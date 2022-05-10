import sys
sys.path.append('.')
from chatbot.utils.Preprocess import Preprocess
from chatbot.models.ner.NerModel import NerModel

p = Preprocess(word2index_dic='chatbot/train_tools/dict/chatbot_dict.bin',
               userdic = 'chatbot/utils/user_dic.tsv')


ner = NerModel(model_name='chatbot/models/ner/ner_model.h5', proprocess=p)
query = '라면 정보 궁금해요'
predicts = ner.predict(query)
tags = ner.predict_tags(query)
print(predicts)
print(tags)

