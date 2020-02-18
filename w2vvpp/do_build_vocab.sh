
# train_collection='tgif-msrvtt10k'
train_collection=$1
overwrite=1

for encoding in bow bow_nsw gru
do
    python build_vocab.py $train_collection --encoding $encoding --overwrite $overwrite
done


