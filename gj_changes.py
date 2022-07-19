import datetime

change_dict = {
    '8.00 - смена Прохорова\n20:00 - смена Кондратьева': datetime.datetime.strptime(f"19.7.2022", "%d.%m.%Y").date(),
    '8.00 - смена Тищенко\n20:00 - смена Прохорова': datetime.datetime.strptime(f"20.7.2022", "%d.%m.%Y").date(),
    '8.00 - смена Исрафилова\n20:00 - смена Тищенко': datetime.datetime.strptime(f"21.7.2022", "%d.%m.%Y").date(),
    '8.00 - смена Кондратьева\n20:00 - смена Исрафилова': datetime.datetime.strptime(f"22.7.2022", "%d.%m.%Y").date(),
}
