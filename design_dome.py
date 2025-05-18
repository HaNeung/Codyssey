import numpy as np

def load_csv_file(filename):
    '''
    CSV 파일을 문자열 타입으로 읽어오는 함수.
    헤더(첫 줄)는 건너뛰고 모든 값을 문자열로 읽음.
    '''
    return np.genfromtxt(filename, delimiter=',', skip_header=1, dtype=str)

def extract_numeric_data(arr):
    '''
    문자열 배열에서 숫자 데이터만 추출하여 float 형으로 변환.
    첫 번째 열(문자열 데이터)은 제외하고 숫자 데이터만 반환.
    '''
    return arr[:, 1:].astype(float)

def main():
    # 세 개의 CSV 파일을 불러와 배열로 저장
    arr1 = load_csv_file('mars_base_main_parts-001.csv')
    arr2 = load_csv_file('mars_base_main_parts-002.csv')
    arr3 = load_csv_file('mars_base_main_parts-003.csv')

    # 모든 데이터를 하나의 배열로 결합
    combined = np.vstack((arr1, arr2, arr3))

    # 숫자 데이터만 추출하여 평균 계산
    numeric_data = extract_numeric_data(combined)
    averages = np.mean(numeric_data, axis=1)

    # 평균이 50 미만인 데이터만 필터링
    filtered = combined[averages < 50]

    # 결과를 새로운 CSV 파일로 저장 (예외 처리 포함)
    try:
        with open('parts_to_work_on.csv', 'w', encoding='utf-8') as f:
            for row in filtered:
                f.write(','.join(row) + '\n')
    except IOError as e:
        print('파일 저장 중 오류:', e)

if __name__ == '__main__':
    main()
