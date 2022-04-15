def fruits(fruit_list):
    new_dict = {}
    for item in fruit_list:
        name = item.get('name')
        shape = item.get('shape')
        mass = item.get('mass')
        volume = item.get('volume')
        if shape == 'sphere':
            if 300 <= mass <= 600:
                if 100 <= volume <= 500:
                    if name in new_dict:
                        new_dict[name] += 1
                    else:
                        new_dict[name] = 1
    return new_dict