import os

path = os.path.abspath(os.getcwd())
output_path = r'yolov5\runs\detect\exp'

def predictor(img):
    source = os.path.join('yolov5/images', img)
    os.system(f'python yolov5/detect.py --weights yolov5/best.pt --source {source}')
    output_img = os.path.join(path, output_path) + f'\\{img}'
    return output_img