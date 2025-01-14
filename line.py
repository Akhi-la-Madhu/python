def read_file(file_name):
    with open(file_name)as f:
        content_list=f.readlines()
    print(content_list)
read_file('file1.txt')    
