from keras.applications.resnet import ResNet152
import numpy as np
import os
import json
import argparse
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input
def parse_args():
    parser = argparse.ArgumentParser('W2VVPP extract features script.')
    parser.add_argument('--data_path', type=str,
                        help='image dataset path')
    parser.add_argument('--feature_path', type=str,
                        help='specified path to file to save features')

    args = parser.parse_args()
    return args
def main():
    opt = parse_args()
    print(json.dumps(vars(opt), indent = 2))
    input_path = opt.data_path
    print("Input path:"+str(input_path))
    output_path = opt.feature_path
    print("Output path:"+(output_path))

    #loading pretrain resnet 152
    resnet152_model = ResNet152(ResNet152(include_top=False, weights='imagenet', input_tensor=None, input_shape=None, pooling=None,))
    count = 0

    features_filename = open(output_path,"w")

    for filename in os.listdir(input_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(input_path,filename)
            print("Image path:",image_path)
            img = image.load_img(image_path, target_size=(224, 224))

            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)

            features = resnet152_model.predict(x)[0]
            
            output = filename+" "+" ".join(np.asarray(features, dtype=str))+"\n"
            # filename_features_format = np.insert(features.astype(str), 0, str(filename), axis=0)
            features_filename.write(output)
            # np.savetxt(features_filename,filename_features_format,fmt='%s')

            count += 1
            print("Processing "+str(count)+". Filename: "+filename)
if __name__ == '__main__':
    main()
