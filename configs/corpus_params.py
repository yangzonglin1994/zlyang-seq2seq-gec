import os
import sys

from configs import base_params


class CorpusParams:
    def __init__(self):
        self.current_classname = self.__class__.__name__

        self.open_file_encoding = 'utf-8'
        self.save_file_encoding = 'utf-8'

        self.corpus_root = os.path.join(base_params.PROJECT_ROOT, 'data', 'parallel-corpus')
        self.raw_url = None
        self.processed_url = None
        self.train_url = None
        self.val_url = None
        self.test_url = None

    def __str__(self):
        ret_info = list()
        ret_info.append("open file encoding: " + self.open_file_encoding + '\n')
        ret_info.append("save file encoding: " + self.save_file_encoding + '\n\n')

        ret_info.append("raw url: " + str(self.raw_url) + '\n')
        ret_info.append("processed url: " + str(self.processed_url) + '\n')
        ret_info.append("train url: " + str(self.train_url) + '\n')
        ret_info.append("val url: " + str(self.val_url) + '\n')
        ret_info.append("test url: " + str(self.test_url) + '\n\n')

        return ''.join(ret_info)


class JustForTest(CorpusParams):
    def __init__(self):
        super(JustForTest, self).__init__()

        # just for test
        just_for_test = os.path.join(self.corpus_root, 'just_for_test')
        self.raw_url = just_for_test
        self.processed_url = just_for_test
        self.train_url = just_for_test
        self.val_url = just_for_test
        self.test_url = just_for_test

    def __str__(self):
        ret_info = list()
        ret_info.append('================== ' + self.current_classname + ' ==================\n')
        super_str = super(JustForTest, self).__str__()
        return ''.join(ret_info) + super_str


class NLPCC2018GEC(CorpusParams):
    def __init__(self):
        super(NLPCC2018GEC, self).__init__()

        nlpcc_2018_gec_dir = os.path.join(self.corpus_root, 'NLPCC-2018-GEC')
        self.raw_data_dir = os.path.join(nlpcc_2018_gec_dir, 'raw_data')
        self.processed_data_dir = os.path.join(nlpcc_2018_gec_dir, 'processed_data')

        # raw, processed, train, val, test
        self.raw_url = os.path.join(self.raw_data_dir, 'data.train')
        self.processed_url = os.path.join(self.processed_data_dir, 'data.processed')
        self.train_url = os.path.join(self.processed_data_dir, 'gec_train')
        self.val_url = os.path.join(self.processed_data_dir, 'gec_val')
        self.test_url = os.path.join(self.processed_data_dir, 'gec_test')

    def __str__(self):
        ret_info = list()
        ret_info.append('================== '+self.current_classname+' ==================\n')
        ret_info.append("raw data dir: " + self.raw_data_dir + '\n')
        ret_info.append("processed data dir: " + self.processed_data_dir + '\n\n')

        super_str = super(NLPCC2018GEC, self).__str__()
        return ''.join(ret_info) + super_str


corpus_name_abbr_full = {'just-for-test': JustForTest().__class__.__name__,
                         'nlpcc-2018-gec': NLPCC2018GEC().__class__.__name__}
corpus_name_full_abbr = {v: k for k, v in corpus_name_abbr_full.items()}
available_corpus = ['just-for-test', 'nlpcc-2018-gec']


def get_corpus_params(corpus_name):
    if corpus_name == available_corpus[0]:
        return JustForTest()
    elif corpus_name == available_corpus[1]:
        return NLPCC2018GEC()
    else:
        raise ValueError('In ' + sys._getframe().f_code.co_name +
                         '() func, corpus_name value error.')


if __name__ == '__main__':
    print(CorpusParams())
    print(JustForTest())
    print(NLPCC2018GEC())
