import os

def predictor(img):
    source = os.path.join('yolov5/images', img)
    os.system(f'python yolov5/detect.py --weights yolov5/best.pt --source {source}')
    output_img = f'yolov5\\runs\\detect\\exp\\{img}'
    return output_img