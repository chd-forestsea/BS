import os
path = './Colorization/'
my_file = '_epoch_color_test_'
lastname = '.png'
for i in range(1,500):
    for j in range(0,20):
        file_name = path + str(i) + my_file + str(j) + lastname
        if os.path.exists(file_name):  # 如果文件存在
            # 删除文件，可使用以下两种方法。
            os.remove(path)
            #os.unlink(path)
        else:
            print('no such file:%s'%my_file)  # 则返回文件不存在