def fruits(fruit_list: tuple) -> dict:
    new_dict = {}
    for item in fruit_list:
        name = item.get('name')
        shape = item.get('shape')
        mass = item.get('mass')
        volume = item.get('volume')
        if (shape == 'sphere') and (300 <= mass <= 600) and (100 <= volume <= 500):
            new_dict[name] = new_dict.get(name, 0) + 1
    return new_dict
