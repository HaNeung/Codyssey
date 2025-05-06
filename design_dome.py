# design_dome.py

# 전역변수
material = ''
diameter = 0.0
thickness = 1.0
area = 0.0
weight = 0.0

def sphere_area(diameter, material='유리', thickness=1.0):
    global area, weight

    # 반구의 표면적 = 2 * pi * r^2
    radius = diameter / 2
    pi = 3.141592653589793
    area = 2 * pi * radius * radius  # m^2

    # 재질 밀도 (g/cm^3)
    density = 0.0
    if material == '유리':
        density = 2.4
    elif material == '알루미늄':
        density = 2.7
    elif material == '탄소강':
        density = 7.85
    else:
        print('지원하지 않는 재질입니다. 기본값(유리)로 계산합니다.')
        density = 2.4
        material = '유리'

    # m^2 * cm => 10000(cm^2) * 두께(cm) = cm^3 단위로 변환
    volume_cm3 = area * 10000 * thickness  # cm^3
    mass_g = volume_cm3 * density  # g

    # 무게를 kg으로 변환, 화성 중력 적용 (지구 중력 기준 * 0.38)
    mass_kg = (mass_g / 1000) * 0.38
    weight = round(mass_kg, 3)
    area = round(area, 3)

    # 전역변수 업데이트
    globals()['material'] = material
    globals()['diameter'] = diameter
    globals()['thickness'] = thickness

    # 결과 출력
    print(f'재질 ⇒ {material}, 지름 ⇒ {diameter}, 두께 ⇒ {thickness}, 면적 ⇒ {area}, 무게 ⇒ {weight} kg')


# 반복 실행
while True:
    print('\n돔 계산기를 시작합니다. 종료하려면 "종료"를 입력하세요.')

    d_input = input('지름을 입력하세요 (단위: m): ')
    if d_input == '종료':
        break

    try:
        d = float(d_input)
        if d <= 0:
            print('지름은 0보다 커야 합니다.')
            continue
    except ValueError:
        print('지름은 숫자로 입력해야 합니다.')
        continue

    m_input = input('재질을 입력하세요 (유리, 알루미늄, 탄소강) [기본값: 유리]: ')
    if m_input == '종료':
        break
    if m_input == '':
        m_input = '유리'

    t_input = input('두께를 입력하세요 (단위: cm) [기본값: 1]: ')
    if t_input == '종료':
        break
    if t_input == '':
        t = 1.0
    else:
        try:
            t = float(t_input)
            if t <= 0:
                print('두께는 0보다 커야 합니다.')
                continue
        except ValueError:
            print('두께는 숫자로 입력해야 합니다.')
            continue

    # 계산
    sphere_area(d, m_input, t)

print('프로그램을 종료합니다.')
