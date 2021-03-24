# with futures.ThreadPoolExecutor(worker) as executer:
      # result_cnt = executer.map(separate_many, sorted(NATION_LS))
# 여기서 근데 map에 하나씩 대응될때마다, 상태를 알 수가 없잖아.
# 어떤 거는 예외가 발생할 수도 있고, 무슨 문제가 있을 수도 있어.
# Reference : https://medium.com/humanscape-tech/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%98-future-%ED%81%B4%EB%9E%98%EC%8A%A4-8b6bc15bd6af
# 실습 대상 3가지 경우

import os
import time
import sys
import csv
from concurrent import futures
# concurrent.futures 방법1(ThreadPoolExcuter[멀티쓰레드] 라는 것을 사용해 보자, ProcessPoolExecuter[멀티프로세서] 활용)
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
    # show(nt) 임시 주석
    # 파일 저장
    save_csv(data, nt.lower() + '.csv')

    return nt


# 시간 측정 및 메인함수
def main(separate_many):
    worker = min(20, len(NATION_LS))
    # 시작 시간
    start_tm = time.time()

    # futures
    futures_list = []
    # 결과 건수
    with futures.ThreadPoolExecutor(worker) as executer:
        # Submit -> Callable 객체 스케쥴링(실행 예약) -> 이후 Future로 반환
        # 일을 스케쥴링 하고, 아래에서 일한 결과들을 받아볼 수 있게 만든 것.
        # future는 result()각각의 결과값, done()각 일꾼이 잘 마무리를 했는지, as_complete() 일 끝난 직원들이 모두 일이 끝날때까지 기다려주는 함수.
        # map은 그냥 일만 시키는 거고, submit은 이렇게 구체적인 상태를 보고 싶을 때 사용함.
        for nt in sorted(NATION_LS):
            # future 반환
            future = executer.submit(separate_many, nt) # submit은 실행 예약
            # 스케쥴링
            futures_list.append(future)
            # Scheduled for Canada : <Future at 0x7f95a7900048 state=running> 이렇게 일꾼들 다 실행되기 시작함.
            print('Scheduled for {} : {}'.format(nt, future))

        for future in futures.as_completed(futures_list):
            result = future.result() # 결과값 위에 separate_many의 return값이 나옴.
            done = future.done() # 일을 제대로 했는지. True or False
            cancelled = future.cancelled #취소가 되진 않았는지
            # print('RESULT : {}'.format(result))
            # print('DONE : {}'.format(done))
            print('Future Result : {}, Done: {}'.format(result, done))
            print('Future Cancelled : {}'.format(cancelled))

    # 종료 시간s
    end_tm = time.time() - start_tm

    msg = '\n{} csv separated in {:.2f}s'
    # 최종 결과 출력
    print(msg.format(list(futures_list), end_tm))


# 실행
if __name__ == '__main__':
    main(separate_many)

    # 지금 보면 3만건의 데이터를 7번을 읽고 쓰고 한거야.
    # 국가마다 읽고 쓰고를 IO작업을 하는 것.
    # 읽고 쓰는거는 운영체제가 관여를 함.


# 18.44s