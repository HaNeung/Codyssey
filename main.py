# 1. CSV 파일 읽기 (split 사용)
def read_csv(filename):
    inventory = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            lines = file.readlines()
            header = lines[0].strip().split(',')  # 첫 줄은 헤더
            for line in lines[1:]:
                values = line.strip().split(',')
                if len(values) != len(header):
                    continue  # 컬럼 수 안 맞는 경우 건너뜀
                item = dict(zip(header, values))
                try:
                    item['Flammability'] = float(item['Flammability'])  # 인화성 지수 변환
                    inventory.append(item)
                except ValueError:
                    continue  # 변환 안 되는 값은 무시
    except FileNotFoundError:
        print(f'파일 "{filename}"을 찾을 수 없습니다.')
    except Exception as e:
        print(f'파일을 읽는 중 오류 발생: {e}')
    return inventory

# 2. CSV 저장
def write_csv(filename, data, header_keys):
    try:
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(','.join(header_keys) + '\n')  # 헤더
            for item in data:
                row = [str(item[key]) for key in header_keys]
                file.write(','.join(row) + '\n')
    except Exception as e:
        print(f'파일 저장 중 오류 발생: {e}')

# 3. 메인 로직
def main():
    input_file = 'Mars_Base_Inventory_List.csv'
    output_file = 'Mars_Base_Inventory_danger.csv'

    inventory = read_csv(input_file)
    if not inventory:
        return

    print('=== 전체 화물 목록 ===')
    for item in inventory:
        print(item)

    # 인화성 기준 정렬
    inventory_sorted = sorted(inventory, key=lambda x: x['Flammability'], reverse=True)

    print('\n=== 인화성 기준 정렬 목록 ===')
    for item in inventory_sorted:
        print(item)

    # 인화성 0.7 이상 필터링
    danger_items = [item for item in inventory_sorted if item['Flammability'] >= 0.7]

    print('\n=== 인화성 0.7 이상 위험 물품 목록 ===')
    for item in danger_items:
        print(item)

    # 위험 물품 CSV 저장
    if danger_items:
        header_keys = list(danger_items[0].keys())
        write_csv(output_file, danger_items, header_keys)
        print(f'\n위험 물품 목록이 "{output_file}" 파일로 저장되었습니다.')

if __name__ == '__main__':
    main()
