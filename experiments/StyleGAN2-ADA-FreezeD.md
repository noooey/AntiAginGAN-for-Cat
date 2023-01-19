# StyleGAN2 ADA + FreezeD
Fine-tuning StyleGAN2 ADA with FreezeD  
[Original Code](https://github.com/NVlabs/stylegan2-ada)  

![project3](https://user-images.githubusercontent.com/66217855/211782316-3f30000d-1396-4e73-b0be-b2bec91a9d83.gif)

## Requirements
- TensorFlow 1.15
- CUDA 10.0

[Setting Up  for StyleGAN2](https://github.com/BOAZ-bigdata/17th_Conference_AntiAginGAN-for-Cat/blob/main/setup/stylegan2/SETUP_StyleGAN2-tf.ipynb)

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
| &ensp;&ensp;&boxvr;&nbsp; --freezed=2  |
| &ensp;&ensp;&boxvr;&nbsp; --res=256  |
| &ensp;&ensp;&boxvr;&nbsp; --cfg='stylegan2' |
| &ensp;&ensp;&boxvr;&nbsp; --gpus=1  |
| &ensp;&ensp;&boxvr;&nbsp; --kimg=2000  |
| &ensp;&ensp;&boxur;&nbsp; --snap=10  |


Select discriminator layers to freeze. `--freezed`  
Due to limited computing resources, `--kimg` should be set as low as 2000.  
Since there is only one gpu available in the colab environment, set it to `--gpus` = 1.  

## Result

<table>
  <tr>
      <td align="center" ><img src="https://user-images.githubusercontent.com/66217855/211782316-3f30000d-1396-4e73-b0be-b2bec91a9d83.gif" width="400" height="200"></td>
     </tr>
     <tr>
     <td align="center" ><img src="https://user-images.githubusercontent.com/66217855/211782101-54235c62-8f94-42ef-a872-6c1c5d1e1f6e.gif" width="400" height="200"></td>
     </tr>
</table>

```
When fine tuning is performed on a pre-trained model,
It created a more complete image of the same number of classes than it did from the beginning.

However, compared to the goal (did the adult cat turn into a young cat?) the result was disappointing.

We needed to adjust the local area of the cat's face.
```
