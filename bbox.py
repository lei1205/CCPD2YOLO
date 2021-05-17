import cv2
import os
import func

# 面积比-斜度-左上右下坐标-四个角坐标（右下角开始顺时针）-车牌-亮度-模糊度

dir = "../CCPD2019/CCPD2019/ccpd_base/"
name_list = os.listdir(dir)
for names in name_list:
    img = cv2.imread(dir + names)

    cv2.rectangle(img, (func.getBiggerRec(names)[0], func.getBiggerRec(names)[1]), (func.getBiggerRec(names)[2], func.getBiggerRec(names)[3]), (0, 0, 255), 1)

    AddText = img.copy()
    cv2.putText(AddText, func.getPlateNo(names), (func.getBiggerRec(names)[0], func.getBiggerRec(names)[1]), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 255), 2)

    cv2.imshow(names, AddText)
    cv2.waitKey()
    cv2.destroyAllWindows()