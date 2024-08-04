import os

def get_size(path):
    size = 0
    if os.path.isfile(path):
        size = os.path.getsize(path)
    else:
        for dirpath, dirname, filenames in os.walk(path):
            for filename in filenames:
                fp = os.path.join(dirpath, filename)
                if os.path.isfile(fp):
                    size += os.path.getsize(fp)

    return size

def human_readable_size(size):
    for unit in ['B', 'KB', 'MB', 'GB','TB']:
        if size < 1024:
            break
        size /= 1024
    return "{:.1f}{}".format(size,unit)

def next10():
    answer = input("Next 10 items enter - 'y' : ")
    for unit in ['Y', 'y', 'yes', 'Yes']:
        if answer == unit:
            return True
    return False

def main():
    pwd = os.getcwd()
    items = os.listdir(pwd)
    size_list = []

    for item in items:
        full_path = os.path.join(pwd, item)
        size = get_size(full_path)
        size_list.append((size,item))
        #print("{} {}".format(human_readable_size(size), item))

    size_list.sort(key=lambda x: x[0], reverse=True)
    count_item=0
    for size, item in size_list:
        if count_item < 10:
            count_item+=1
        else:
            if next10():
                count_item = 1
            else:
                break

        print("{} {}".format(human_readable_size(size), item))

if __name__ == "__main__":
    main()