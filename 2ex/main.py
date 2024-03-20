
def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')

                cat_id, cat_name, cat_age = parts
                cat_info = {"id": cat_id, "name": cat_name, "age": int(cat_age)}
                cats_info.append(cat_info)

    except:
        print("Error")
    return cats_info

cats_info = get_cats_info("e:\\python\\Homework\\goit-algo-hw-04\\2ex\\cats.txt")
print(cats_info)