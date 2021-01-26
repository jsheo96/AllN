import torch
from transformers.modeling_bert import BertPreTrainedModel, BertModel, BertConfig
from transformers import BertTokenizer
import pickle
from utils import Config, PadSequence, PreProcessor
class Encoder(BertPreTrainedModel):
    def __init__(self, ptr_config_path='pretrained/config_subchar12367_bert.json'):
        self.ptr_config = Config(ptr_config_path)
        self.config = BertConfig(self.ptr_config.config)
        super(Encoder, self).__init__(self.config)
        f = open(self.ptr_config.vocab, mode='rb')
        vocab = pickle.load(f)
        self.ptr_tokenizer = BertTokenizer.from_pretrained(self.ptr_config.tokenizer, do_lower_case=False)
        self.pad_sequence = PadSequence(length=128, pad_val=vocab.to_indices(vocab.padding_token))
        self.preprocessor = PreProcessor(vocab=vocab, split_fn=self.ptr_tokenizer.tokenize, pad_fn=self.pad_sequence,
                                    subchar=True)
        self.vocab = self.preprocessor.vocab
        self.bert = BertModel(self.config)
        self.init_weights()

    def forward(self, sentences):
        with torch.no_grad():
            input_ids = self.sentences2indices(sentences)
            attention_mask = input_ids.ne(self.vocab.to_indices(self.vocab.padding_token)).float()
            _, pooled_output = self.bert(input_ids=input_ids, attention_mask=attention_mask)
            return pooled_output

    def sentences2indices(self, sentences):
        indices = torch.tensor([self.preprocessor.preprocess(sentence) for sentence in sentences])
        return indices

if __name__ == '__main__':
    encoder = Encoder()
    sentences =['안녕 나는 허지성','안녕하세요']
    output = encoder(sentences)
    print(output.shape)

