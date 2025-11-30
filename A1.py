import xml.etree.ElementTree as et

def load_users_data(filename):
    try:
        tree = et.parse(filename)
        root = tree.getroot()
        users = []
        for user in root.findall("user"):
            users.append({
                'user_id': user.find("user_id").text,
                'name': user.find('name').text,
                'age': int(user.find('age').text),
                'weight': float(user.find('weight').text),
                'fitness_level': user.find('fitness_level').text
            })
        return users
    except FileNotFoundError:
        print("Файл не найден")
        return []

def load_workouts_data(filename):
    try:
        tree = et.parse(filename)
        root = tree.getroot()
        workouts = []
        for workout in root.findall("workout"):
            workouts.append({
                'workout_id': workout.find("workout_id").text,
                'user_id': workout.find("user_id").text,
                'date': workout.find('date').text,
                'type': workout.find('type').text,
                'duration': float(workout.find('duration').text),
                'distance': float(workout.find('distance').text),
                'calories': float(workout.find('calories').text),
                'avg_heart_rate': float(workout.find('avg_heart_rate').text),
                'intensity': workout.find('intensity').text
            })
        return workouts
    except FileNotFoundError:
        print("Файл не найден")
        return []


def get_stats(users, workouts):
    print("ОБЩАЯ СТАТИСТИКА")
    print(30*"-")
    print(f"Всего тренировок: {len(workouts)}")
    print(f"Всего пользователей: {len(users)}")

    sum_calor = 0
    for workout in workouts:
        sum_calor += workout['calories']
    print(f"Сожжено калорий: {int(sum_calor)}")

    sum_duration = 0
    for workout in workouts:
        sum_duration += workout['duration']
    h = int(sum_duration // 60)
    m = int(sum_duration % 60)
    print(f"Общее время: {h}.{m}") #задать вопрос по этой строчке(не сходится время)

    sum_distance = 0
    for workout in workouts:
        sum_distance += workout['distance']
    print(f"Пройдено дистанции: {sum_distance:.1f}") #задать вопрос по этой строчке(дахера выводится знаков)

users = load_users_data('users.xml')
workouts = load_workouts_data('workouts.xml')
get_stats(users, workouts)



