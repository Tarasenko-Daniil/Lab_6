import xml.etree.ElementTree as et

def load_users_data(filename):
    tree = et.parse(filename)
    root = tree.getroot()

    for user in root.findall("user"):
        user_id = user.find("user_id").text
        name = user.find('name').text
        age = user.find('age').text
        weight = user.find('weight').text
        fitness_level = user.find('fitness_level').text

        print(f"id: {user_id}, Имя: {name}, Возраст: {age}, Вес: {weight}, Уровень подготовки: {fitness_level}")

