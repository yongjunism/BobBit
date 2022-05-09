import sys
sys.path.append('.')

from sili.utils.Preprocess import Preprocess
from sili.models.intent.IntentModel import IntentModel

p = Preprocess(word2index_dic='sili/train_tools/dict/chatbot_dict.bin',
               userdic = 'sili/utils/user_dic.tsv')

intent = IntentModel(model_name='sili\models\intent\intent_model.h5', proprocess=p)
query = "오늘 아이스크림 주문 가능한가요?"
predict = intent.predict_class(query)
predict_label = intent.labels[predict]

print(query)
print("의도 예측 클래스 : ", predict)
print("의도 예측 레이블 : ", predict_label)

