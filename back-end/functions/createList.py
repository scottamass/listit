DEFAULT_items =[]

def create_list(details):
    temp=details
    print(temp)
    processed = [l for l in temp.split('\r\n') if l.split()]
    for i in processed:
        print(f'item:{i}')
        DEFAULT_items.append(i)
    

def get_items():
    items=DEFAULT_items
    print(items)

    return items  