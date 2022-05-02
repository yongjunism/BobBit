import sys
sys.path.append('.')
from chatbot.utils.Preprocess import Preprocess

sent = "내일 오전 10시에 짬뽕 주문하고 싶어"
p = Preprocess(userdic = 'chatbot/utils/user_dic.tsv')

# tag 유
pos = p.pos(sent)
ret = p.get_keywords(pos, without_tag=False)
print(ret)

# tag 무
ret = p.get_keywords(pos, without_tag=True)
print(ret)

# w2i = p.get_wordidx_sequence(keywords)
# sequences = [w2i]
#
# MAX_SEQ_LEN = 15    # 임베딩 벡터 크기
# padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')
#
# print(keywords)
# print(sequences)
# print(padded_seqs)
