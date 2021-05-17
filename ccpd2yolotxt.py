import cv2
import os
import func

name_list = os.listdir("../CCPD2019/CCPD2019/ccpd_base/")

for n in name_list:

    img = cv2.imread("../CCPD2019/CCPD2019/ccpd_base/" + n)
    sp = img.shape
    height = sp[0]
    width = sp[1]

    lu_1 = func.getBiggerRec(n)[0]
    lu_2 = func.getBiggerRec(n)[1]
    rb_1 = func.getBiggerRec(n)[2]
    rb_2 = func.getBiggerRec(n)[3]

    # 0 中心点（归一化宽） 中心点（归一化长） 框宽度（归一化） 框长度（归一化）
    mid_x = (rb_1 + lu_1) / 2 / width
    mid_y = (rb_2 + lu_2) / 2 / height
    dis_x = (rb_1 - lu_1) / width
    dic_y = (rb_2 - lu_2) / height

    res = "0 " + str(mid_x) + " " + str(mid_y) + " " + str(dis_x) + " " + str(dic_y)
    print(res)

    if not os.path.exists("../result/CCPD2019/ccpd_base/"):
        os.makedirs("../result/CCPD2019/ccpd_base/")
    f = open("../result/CCPD2019/ccpd_base/" + n.split(".")[0] + ".txt", 'a')
    f.write(res)
    f.close()