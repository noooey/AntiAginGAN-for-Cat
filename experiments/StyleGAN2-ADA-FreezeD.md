# StyleGAN2 ADA + FreezeD
Fine-tuning StyleGAN2 ADA with FreezeD  
[Original Code](https://github.com/NVlabs/stylegan2-ada)  
```
메인 이미지
```

## Requirements
- TensorFlow 1.15
- CUDA 10.0

[Setting Up  for StyleGAN2](https://github.com/noooey/AntiAginGAN-for-Cat/blob/main/setup/SettingUp_for_StyleGAN2_tf.ipynb)

## Dataset
Prepare custom dataset in TFRecords form  

| Dataset |
| ------- |
| &ensp;&ensp;&boxvr;&nbsp; kitten-datasets-r02.tfrecords |
| &ensp;&ensp;&boxvr;&nbsp; kitten-datasets-r03.tfrecords |
| &ensp;&ensp;&boxvr;&nbsp; ... |
| &ensp;&ensp;&boxur;&nbsp; kitten-datasets-r07.tfrecords |

## Pretrained Model
Prepare pretrained Model  Learned with the ahfq dataset  


![image](https://user-images.githubusercontent.com/66217855/211147695-8abe6ea6-f656-4bd4-86ee-40c1add4b555.png)

[afhqcat.pkl](https://nvlabs-fi-cdn.nvidia.com/stylegan2-ada/pretrained/afhqcat.pkl)

## Train

| Training Options |  
| ----------  |
| &ensp;&ensp;&boxvr;&nbsp; --resume=snapshot.pkl  |
| &ensp;&ensp;&boxvr;&nbsp; --freezed=4  |
| &ensp;&ensp;&boxvr;&nbsp; --res=128  |
| &ensp;&ensp;&boxvr;&nbsp; --metrics='fid50k_full'  |
| &ensp;&ensp;&boxvr;&nbsp; --metricdata=my_dataset  |
| &ensp;&ensp;&boxvr;&nbsp; --cfg='stylegan2' |
| &ensp;&ensp;&boxvr;&nbsp; --gpus=1  |
| &ensp;&ensp;&boxvr;&nbsp; --kimg=5000  |
| &ensp;&ensp;&boxur;&nbsp; --snap=10  |


Select discriminator layers to freeze. `--freezed`  
Due to limited computing resources, `--kimg` should be set as low as 5000.  
Since there is only one gpu available in the colab environment, set it to `--gpus` = 1.  

## Result
