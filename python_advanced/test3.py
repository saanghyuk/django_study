# 파일 IO과정만 따로 분리해서 실행시키고,
# 이후에 그걸 가지고 멀티스레드에서 활용시키는 방식

# Chapter06-03-02
# Future 동시성
# 비동기 작업 실행



# 지연시간(Block) CPU 및 리소스 낭비 방지. -> Network I/O 관련 작업 동시성 활용 권장함
# 인터넷에 요청하고 리스폰스 하고, 그런 경우에서 이런 블록에 딱 걸리면 모든게 다 멈춤('블록 걸렸다' 라고 말함)


# 이런 경우는 파일을 읽는 작업을 하나로 따로 분리를 해서 이미 분리를 해놓고, 9개의 스레드로 따로 작업을 시키면 훨씬 빠른 속도가 나옴.
# 그러면 어떻게 나오는지 실험.



# 실습 대상 3가지 경우

import os
import time
import sys
import csv
from concurrent import futures
import pandas as pd
# concurrent.futures 방법1(ThreadPoolExcuter라는 것을 사용해 보자, ProcessPoolExecuter 활용)
# map()
# 서로 다른 스레드 또는 프로세스에서 실행 가능.
# 내부 과정에서 알 필요 없으며, 고수준으로 인터페이스 제공
# 지금까지는 9개 국가를 하나씩 읽고 쓰고 했으면, 지금부터는 일꾼 9명을 보내서 각자 하고 오라고 하는 거야.
# 근데 그러면 17.83s를 9로 나눠서 대충 2초 걸리겠거나 할수 있는데 그건 또 아님. Why? python Global Interpreter Lock때문
# Google Pythoon GIL(Global Interpreter Lock)
# GIL은 한번에 하나의 스레드만을 수행할 수 있게 인터프리터 자체에서 락을 거는 것(안전하게 하고 싶기 때문. 충돌 등을 없애기 위해 언어에서 제약 걸어 둔 것).
# https://wangin9.tistory.com/entry/pythonthreadGIL

# 국가정보
NATION_LS = ('Singapore Germany Israel Norway Italy Canada France Spain Mexico').split()
# 초기 CSV 위치
TARGET_CSV = './resources/nations.csv' # 본인 경로 변경
# 저장 폴더 위치
DEST_DIR = './resources/csvs/' # 본인 경로 변경
# CSV 헤더 기초 정보
HEADER = ['Region','Country','Item Type','Sales Channel','Order Priority','Order Date','Order ID','Ship Date','Units Sold','Unit Price','Unit Cost','Total Revenue','Total Cost','Total Profit']



# 국가별 CSV 파일 저장
def save_csv(data, filename):
    # 최종 경로 생성
    path = os.path.join(DEST_DIR, filename)

    with open(path, 'w', newline='') as fp:
        writer = csv.DictWriter(fp, fieldnames=HEADER)
        # Header Write
        writer.writeheader()
        # Dict to CSV Write
        for row in data:
            writer.writerow(row)

# def get_csv(file, nation_list):
#     with open(file, 'r') as f:
#         reader = csv.DictReader(f)
#         for r in reader:

#             for i in len(nation_list):


# 국가별 분리
def get_sales_data(nt):
    with open(TARGET_CSV, 'r') as f:
        reader = csv.DictReader(f)
        # Dict을 리스트로 적재
        data = []
        # Header 확인
        # print(reader.fieldnames)
        for r in reader:
            # OrderedDict 확인
            # print(r)
            # 조건에 맞는 국가만 삽입
            if r['Country'] == nt:
                data.append(r)
    return data

# 중간 상황 출력
def show(text):
    print(text, end=' ')
    # 중간 출력(버퍼 비우기)
    sys.stdout.flush()


# 국가 별 분리 함수 실행
def separate_many(nt):

    # 분리 데이터
    data = get_sales_data(nt)
    # 상황 출력
    show(nt)
    # 파일 저장
    save_csv(data, nt.lower() + '.csv')

    return len(nt)


# 시간 측정 및 메인함수
def main(separate_many):
    worker = min(20, len(NATION_LS))
    # 시작 시간
    start_tm = time.time()
    # 결과 건수
    with futures.ThreadPoolExecutor(worker) as executer:
      result_cnt = executer.map(separate_many, sorted(NATION_LS))
      # map -> 작업 순서 유지, 즉시 실행, 갯수만큼 map에 동시에 풀리는 것. 리스트의 갯수만큼 실행됨.
      # 위에 separate_many에서 for문 없애줘야함.
    # 종료 시간
    end_tm = time.time() - start_tm

    msg = '\n{} csv separated in {:.2f}s'
    # 최종 결과 출력
    print(msg.format(list(result_cnt), end_tm))




# 국가별 분리


# 실행
if __name__ == '__main__':

    def get_csv_and_divide():
      df = pd.read_csv('./resources/nations.csv')

      print(df.head())
      for i in HEADER:
        i+'df'=df[df['Country']==i]
        print((i+'df').head())
    get_csv_and_divide()
    # main(separate_many)
    # test()

    # 지금 보면 3만건의 데이터를 7번을 읽고 쓰고 한거야.
    # 국가마다 읽고 쓰고를 IO작업을 하는 것.
    # 읽고 쓰는거는 운영체제가 관여를 함.


# 18.44s