txt_file = '../string/preprocessed/protein.actions.15k.tsv'
inp = txt_file
ofile = 'string_vec_partial.txt'

#train
import logging
import os.path
import sys
import multiprocessing
import time
 
from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models import Phrases
from gensim.models.word2vec import LineSentence
 
if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
 
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
 
    t0 = time.time()
    # check and process input arguments
    sentences = LineSentence(inp)
        

    model = Word2Vec(sentences, vector_size=5, window=10 , min_count=1 , sg=1 , workers=multiprocessing.cpu_count()-1 )

    model.wv.save_word2vec_format("string_vec7.txt", binary=False)
    #vocab_size = len(model.vocab)
    with open(ofile, 'w')as fp:
        # for w in model.wv.vocab:

        for w in list(model.wv.index_to_key):
            fp.write(w + '\t')
            # fp.write(" ".join([str(d) for d in model[w]]) + "\n")
            fp.write(" ".join([str(d) for d in model.wv[w]]) + "\n")
            
    print (time.time()-t0)
