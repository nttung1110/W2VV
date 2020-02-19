# Steps to plug-in own data for training/validating/testing using w2vv++ model

## Extract features with ResNet152

1. Create a folder inside VisualSearch/${data_name}
2. Create a folder dataset inside the repository.(storing all image and caption data inside this folder)
3. Run resnext_152_extract.py script with parameters(--data_path $path/to/image/folder -- feature_path $path/to/txt/file/saving
features

## Convert features txt file to bin file format 

Run txt2bin.py script with parameters(nDims: feature dimensions(1000 if using the given extracted script), inputTextfile:path to features txt file, isFileList, resultDir:
specify path as following VisualSearch/${data_name}/${feature_name}:must be mean_resnext101_resnet152 to match with default model

## Building vocabulary for caption file

Saving image caption file with format: [image-name] [text_catption] inside folder VisualSearch/${data_name}/TextData 

run ./do_build_vocab following the instructions of readme file inside w2vv folder

### Remaining steps follow the same instructions specified in w2vv Readme file
