from kiwipiepy import Kiwi

def main():
    kiwi = Kiwi()
    print(kiwi.tokenize("안녕하세요 형태소 분석기 키위입니다."))

if __name__ == "__main__":
    main()