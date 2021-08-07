# 한국어 위키백과
# 3강
# 참고: https://omicro03.medium.com/%EC%9E%90%EC%97%B0%EC%96%B4%EC%B2%98%EB%A6%AC-nlp-14%EC%9D%BC%EC%B0%A8-word2vec-%EC%8B%A4%EC%8A%B5-a4e7767a1e66

# 1. 위키피디아 한국어 덤프 파일 다운로드
# 다운로드 : https://dumps.wikimedia.org/kowiki/latest/
# 2. 위키피디아 익스트랙터 다운로드 : 위키 범프에서 위키 문서의 제목과 본문만 추출한다.
# https://github.com/attardi/wikiextractor
# 3. 위키피디아 한국어 덤프 파일 변환
# 4. 훈련 데이터 만들기
# 5. Word2Vec 작업

# ----------------------------------------------------------------
# 라이브러리
from gensim.corpora import WikiCorpus, Dictionary
from gensim.utils import to_unicode
import re

# ----------------------------------------------------------------
# 전처리할 덤프 파일 경로
in_f = 'D:/pseudo_data/raw/kowiki-latest-pages-articles.xml.bz2'
# 저장할 텍스트 경로
out_f = 'D:/pseudo_data/processed/processed_wiki_ko.txt'



# -------------------------------------------------------------
# 말뭉치 만드는 함수 정의
def make_corpus(in_f, out_f):
    """위키피디아 xml 덤프를 test 형식으로 변환"""
    output = open(out_f, 'w', encoding = 'utf-8')
    wiki = WikiCorpus(in_f, tokenizer_func=tokenize, dictionary=Dictionary())
    i = 0
    for text in wiki.get_texts():
        output.write(bytes(' '.join(text), 'utf-8'.decode('utf-8') + '\n'))
        i = i + 1
        if (i % 10000 == 0) :
            print('Processed' + str(i) + 'articles')
    output.close()
    print('Processing complete!')

# ----------------------------------------------------------------
# 사용자 정의 tokenize 정의
# 특수문자, 공백, 이메일주소, 웹 페이지 주소 등을 제거한다.

WIKI_REMOVE_CHARS = re.compile("'+|.{2,30}=+)|__TOC__|(ファイル:).+|:(en|de|it|fr|es|kr|zh|no|fi):|\n", re.UNICODE)
# re.compile
# "'+|.{2,30}=+)|__TOC__|(ファイル:).+|:(en|de|it|fr|es|kr|zh|no|fi):|\n"
# e.UNICODE
WIKI_SPACE_CHARS = re.compile("(\\s|゙|゚|　)+", re.UNICODE)
EMAIL_PATTERN = re.compile("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", re.UNICODE)
URL_PATTERN = re.compile("(ftp|http|https)?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", re.re.UNICODE)
WIKI_REMOVE_TOKEN_CHARS = re.compile("(\\*$|:$|^파일:.+|^;)", re.UNICODE)
MULTIPLE_SPACE = re.compile(' +', re.re.UNICODE)

def tokenize(content, token_min_len = 2, token_max_len=100, lower=True):
    content = re.sub(EMAIL_PATTERN, ' ', cotent)
    content = re.sub(URL_PATTERN, ' ', cotent)
    content = re.sub(WIKI_REMOVE_CHARS, ' ', cotent)
    content = re.sub(WIKI_SPACE_CHARS, ' ', cotent)
    content = re.sub(MULTIPLE_SPACE, ' ', cotent)
    tokens = content.replace(", )", "").split(" ")
    result = []
    for token in tokens:
        if not token.startswith('_'):
            token_candidate = to_unicode(re.sub(WIKI_REMOVE_TOKEN_CHARS, '', token))
        else :
            token_candidate = ""
        if len(token_candidate) > 0 :
            result.append(token_candidate)
    return result
