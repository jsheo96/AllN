# input: 뉴스 content (string)
# output: list of string
class Separator:
    def __call__(self, content):
        return content.split('.')

