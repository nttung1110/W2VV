# Usage

Change environment variables to desired folder and create folder storing dataset(VisualSearch)
```
export HOME=/path/to/desired/folder
cd $HOME
mkdir VisualSearch
git clone https://github.com/0902338471/W2VV-.git
```

## Extract features with ResNet152
1.Run following code, replace ${your_data_name} variable by your own data name
```
mkdir ~/${your_data_name}   
mkdir ~/VisualSearch/${your_data_name}/FeatureData/
mkdir ~/VisualSearch/${your_data_name}/TextData/
```
2. Download all your dataset inside folder ```~/${your_data_name}```.(storing images and captions data in separate subfolder)
3. Saving image caption file with format: [image-name] [text_catption] inside folder ```~/VisualSearch/${data_name}/TextData/${data_name}.caption.txt/```
4. Run following code, replace ```${image_folder}``` ```${output_features_name}``` with your folder image dataset and desired txt file storing extracted features respectively
```
python resnext_152_extract.py --data_path ${image_folder} -- feature_path ${output_features_name}.txt
```

## Convert features txt file to bin file format 
Run following code, replace ```${output_features_name}``` and ```${data_name}```
```
python txt2bin.py --nDims 1000, --inputTextfile ~/${output_features_name},
--resultDir ~/VisualSearch/${data_name}/FeatureData/mean_resnext101_resnet152
```
After previous steps, your dataset folder will have following format
```shell
${your_data_name}
├── FeatureData
│   └── mean_resnext101_resnet152
│       ├── feature.bin
│       ├── shape.txt
│       └── id.txt
└── TextData
    └── ${your_data_name}.caption.txt

```

* `FeatureData`: extracted image feature. 
* `feature.bin`: extracted features in binary format
* `${your_data_name}.caption.txt`: caption data. The file structure is as follows, in which the image and sentence in the same line are relevant.
```
image_id_1#1 sentence_1
image_id_1#2 sentence_2
...
image_id_n#1 sentence_k
...
```

## Training

### Building vocabulary for caption file

Run following code
```
cd ~/W2VV-/w2vvpp
./do_build_vocab /VisualSearch/${data_name}/TextData/${data_name}.caption.txt
```
