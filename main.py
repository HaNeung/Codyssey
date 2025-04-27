import pickle

# 1. CSV 파일 읽기 (split 이용)
filename = 'Mars_Base_Inventory_List.csv'
inventory = []

with open(filename, mode='r', encoding='utf-8') as file:
    lines = file.readlines()
    header = lines[0].strip().split(',')  # 첫 줄은 헤더
    for line in lines[1:]:  # 나머지는 데이터
        values = line.strip().split(',')
        item = dict(zip(header, values))
        # 인화성 지수 float 변환
        item['Flammability'] = float(item['Flammability'])
        inventory.append(item)

# 2. 출력: 원본 목록
print("=== 전체 화물 목록 ===")
for item in inventory:
    print(item)

# 3. 인화성 순 정렬 (내림차순)
inventory_sorted = sorted(inventory, key=lambda x: x['Flammability'], reverse=True)

print("\n=== 인화성 기준 정렬 목록 ===")
for item in inventory_sorted:
    print(item)

# 4. 인화성 0.7 이상 필터링
danger_items = [item for item in inventory_sorted if item['Flammability'] >= 0.7]

print("\n=== 인화성 0.7 이상 위험 물품 목록 ===")
for item in danger_items:
    print(item)

# 5. 위험 물품 목록을 새로운 CSV로 저장
output_filename = 'Mars_Base_Inventory_danger.csv'
with open(output_filename, mode='w', encoding='utf-8') as file:
    file.write(','.join(danger_items[0].keys()) + '\n')  # 헤더 작성
    for item in danger_items:
        row = [str(item[key]) for key in item.keys()]
        file.write(','.join(row) + '\n')

print(f"\n위험 물품 목록이 '{output_filename}' 파일로 저장되었습니다.")

# 보너스: 정렬된 데이터를 이진 파일로 저장
binary_filename = 'Mars_Base_Inventory_List.bin'
with open(binary_filename, 'wb') as binfile:
    pickle.dump(inventory_sorted, binfile)

print(f"\n인화성 순으로 정렬된 데이터가 '{binary_filename}' 이진 파일로 저장되었습니다.")

# 보너스: 이진 파일에서 데이터 읽기
with open(binary_filename, 'rb') as binfile:
    loaded_inventory = pickle.load(binfile)

print("\n=== 이진 파일에서 로드된 화물 목록 ===")
for item in loaded_inventory:
    print(item)
