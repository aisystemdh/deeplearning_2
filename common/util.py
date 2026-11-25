import numpy as np
#말뭉치를 단어로 변환한 뒤 id로 저장 , 전처리
def preprocess(text):
    text = text.lower()
    text = text.replace('.',' .')
    words = text.split(' ')
    word_to_id = {}
    id_to_word = {}
    for word in words:
            if word not in word_to_id:
                  new_id = len(word_to_id)
                  word_to_id[word] = new_id
                  id_to_word[new_id] = word

    corpus = np.array([word_to_id[w] for w in words])

    return corpus, word_to_id, id_to_word

#동시 발생 행렬 <파라미터> 1: 원소의 id 2:어휘 수 3:윈도우 크기
def create_co_matrix(corpus, vocab_size , window_size=1):
      corpus_size = len(corpus)
      co_matrix = np.zeros((vocab_size,vocab_size),dtype = np.int32)
      for idx, word_id in enumerate(corpus):
            for i in range(1,window_size +1):
                left_idx = idx - i
                right_idx = idx + i

                if left_idx >=0:
                      left_word_id = corpus[left_idx]
                      co_matrix[word_id, left_word_id] += 1

                if right_idx < corpus_size : 
                      right_word_id = corpus[right_idx]
                      co_matrix[word_id,right_word_id] += 1
      return co_matrix

#벡터의 내적를 통한 코사인 유사도
def cos_similarity(x,y,eps = 1e-8):
      nx = x /(np.sqrt(np.sum(x**2)) + eps)
      ny = y /(np.sqrt(np.sum(y**2)) + eps)
      return np.dot(nx, ny)

#단어를 유사도 순으로 나열 query -> 검색 단어 top -> 상위 몇단어까지 출력 할지 결정
def most_similarity(query,word_to_id,id_to_word,word_matrix,top =5):
      #1: 검색어를 꺼낸다.
      if quert not in word_to_id:
            print('%s를 찾을 수 없습니다.' %query)
            return
      print('\n[query]'+ query)
      query_id = word_to_id[query]
      #해당 단어의 인접행 제공
      query_vec = word_matrix[query_id]

      #코사인 유사도 계산
      vocab_size = len(id_to_word)
      similarity = np.zeros(vocab_size)
      for i in range(vocab_size):
            similarity[i] = cos_similarity(word_matrix[i],query_vec)

    #코사인 유사도를 기준으로 내림차순 출력
      count = 0
      for i in (-1 * similarity).argsort():
            if id_to_word[i] = query:
                continue
            print(' %s:%s' %(id_to_word[i],similarity[i]))
            count += 1
            if count >= top:
                  return 
            

#동시 벌생 행렬을 PPMI 행렬로 변환, C는 동시 발생 행렬이다. verbose는 진행 상황 출력 여부
def ppmi(C , verbose = False ,eps = 1e -8):
      M = np.zeros_like(C,dtype = np.float32)
      N = np.sum(C) #전체 등장 횟수
      S = np.sum(C , axis=0)
      total = C.shape[0] * C.shape[1]
      cnt = 0
      #행 수와 열 수를 샌다.
      for i in range(C.shape[0]):
            for j in range(C.shape[1]):
                  pmi = np.log2(C[i,j]*N / (S[j]*S[i]) + eps)
                  M[i,j] = max(0,pmi)

                  if verbose:
                        cnt+=1
                        if cnt % (total//100 +1) == 0:
                              print ('%.1f%% 완료' %(100*cnt / total))
      return M

                  
            


      


            
            




                  