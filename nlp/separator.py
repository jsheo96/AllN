
# input: 뉴스 content (string)
# output: list of string
class Separator:
    # TODO: 문장을 좀 더 정확하게 나누기
    def __call__(self, content):
        return content.split('.')


if __name__ == '__main__':
    from db_reader import DBReader
    db_reader = DBReader('/home/jsheo/AllN/news.db')
    raws = db_reader.contains('content','에코프로비엠')
    content = raws[0][3]
    separator = Separator()
    sentences = separator(content)
    print(len(sentences))
