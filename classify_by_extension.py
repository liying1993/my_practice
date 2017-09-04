import os
import itertools
import shutil

origin_ext = set()
src_path = ""
def classify_by_extension(path):
    '''
    首先传进来一个路径名,遍历里面的文件和文件夹。按照文件的扩展名进行分类，并且把分好的文件放进按照扩展名命令的文件夹里面
    如果路径下面有文件夹，就把文件夹里面的文件分类，并存进之前规定的文件夹里面，以此类推
    :param path: "/Users/liying/Documents/backend"
    :return: 
    '''
    #将所有的文件夹名字放在这里
    # import pdb
    # pdb.set_trace()
    src_path = path
    file_lists = os.listdir(path)
    is_dir_list = [i for i in file_lists if os.path.isdir(os.path.abspath(os.path.join(path, i)))]  # 该路径下面所有文件夹
    is_file_list = [i for i in file_lists if os.path.isfile(os.path.abspath(os.path.join(path, i)))]  # 该路径下面所有文件
    # 先处理该路径下面的文件，把文件放到对应的文件夹里面
    # 然后再进到该路径下面的文件夹里面，再处理里面的文件，放到刚刚在外面创建的文件夹里面
    for i in is_file_list:
        first_position = i.find(".")
        ext = i[first_position + 1:]
        origin_ext.add(ext)
        # 以后缀名为文件名的文件夹是否存在，如果不存在的话，就创建一个,然后把对应的文件移动到对应的文件夹里面
        if not os.path.exists(os.path.join(path, ext)):
            os.mkdir(os.path.join(path, ext))
            if os.path.exists(os.path.join(os.path.join(path,ext), i)):
                print("ssss")
            else:
                shutil.move(os.path.join(path, i), os.path.join(path, ext))
        else:
            # 把相对应的文件放到对应的文件夹里面
            if os.path.exists(os.path.join(os.path.join(path,ext), i)):
                print("ssss")
            else:
                shutil.move(os.path.join(path, i), os.path.join(path, ext))
    for i in is_dir_list:
        classify_by_new_directory(src_path, path, i)

def classify_by_new_directory(srcpath, path, dir):
    # import pdb
    # pdb.set_trace()
    new_path = os.path.join(path, dir)
    new_file_lists = os.listdir(new_path)
    new_is_dir_list = [i for i in new_file_lists if os.path.isdir(os.path.abspath(os.path.join(new_path, i)))]
    new_is_file_list = [i for i in new_file_lists if os.path.isfile(os.path.abspath(os.path.join(new_path, i)))]
    for i in new_is_file_list:
        new_first_position = i.find(".")
        new_ext = i[new_first_position + 1:]
        origin_ext.add(new_ext)
        if not os.path.exists(os.path.join(srcpath, new_ext)):
            os.mkdir(os.path.join(srcpath, new_ext))
            if os.path.exists(os.path.join(os.path.join(srcpath,new_ext), i)):
                print("ssss")
            else:
                shutil.move(os.path.join(new_path, i), os.path.join(srcpath, new_ext))
        else:
            if os.path.exists(os.path.join(os.path.join(srcpath,new_ext), i)):
                print("ssss")
            else:
                shutil.move(os.path.join(new_path, i), os.path.join(srcpath, new_ext))
        for i in new_is_dir_list:
            classify_by_new_directory(srcpath, new_path, i)


if __name__ == "__main__":
    classify_by_extension("/Users/liying/Documents/backend/celery_demo")


