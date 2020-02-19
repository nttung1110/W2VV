# Steps to plug-in own data for training/validating/testing using w2vv++ model
## Usage

Change environment variables to desired folder and create folder storing dataset(VisualSearch)
```
export HOME=/path/to/desired/folder
cd $HOME
mkdir VisualSearch
```

## Extract features with ResNet152

1. Make sure ```~/VisualSearch/${data_name}/FeatureData/``` folder exists

2. Create a folder dataset inside the repository.(storing all image and caption data inside this folder)
3. Run resnext_152_extract.py script with parameters(--data_path $path/to/image/folder -- feature_path $output/features/to/txt/file/path

## Convert features txt file to bin file format 

Run txt2bin.py script with parameters(nDims: feature dimensions(1000 if using the given extracted script), inputTextfile:path to features txt file, isFileList, resultDir:

```
# set resultDir as following
resultDir = ~/VisualSearch/${data_name}/mean_resnext101_resnet152
```

## Building vocabulary for caption file

Saving image caption file with format: [image-name] [text_catption] inside folder ```~/VisualSearch/${data_name}/TextData/${data_name}.caption.txt/```
```
cd ~/W2VV-/w2vvpp
./do_build_vocab /VisualSearch/${data_name}/TextData/${data_name}.caption.txt
```
After previous steps, your dataset folder will have following format
```shell
${subset_name}
├── FeatureData
│   └── ${feature_name}
│       ├── feature.bin
│       ├── shape.txt
│       └── id.txt
└── TextData
    └── ${subset_name}.caption.txt

```

* `FeatureData`: extracted image feature. 
* `${subset_name}.txt`: all video IDs in the specific subset, one video ID per line.
* `${subset_name}.caption.txt`: caption data. The file structure is as follows, in which the video and sent in the same line are relevant.
```
image_id_1#1 sentence_1
image_id_1#2 sentence_2
...
image_id_n#1 sentence_k
...
```
