# StyleGAN2 ADA
Using StyleGAN2 ADA  
[Original Code](https://github.com/NVlabs/stylegan2-ada)  
```
메인 이미지
```

## Requirements
- TensorFlow 1.15
- CUDA 10.0

[Setting Up  for StyleGAN2](https://github.com/BOAZ-bigdata/17th_Conference_AntiAginGAN-for-Cat/blob/main/setup/SETUP_StyleGAN2-tf.ipynb)

## Dataset
Prepare custom dataset in TFRecords form  

| Dataset |
| ------- |
| &ensp;&ensp;&boxvr;&nbsp; kitten-datasets-r02.tfrecords |
| &ensp;&ensp;&boxvr;&nbsp; kitten-datasets-r03.tfrecords |
| &ensp;&ensp;&boxvr;&nbsp; ... |
| &ensp;&ensp;&boxur;&nbsp; kitten-datasets-r07.tfrecords |

## Train

| Training Options |  
| ----------  |
| &ensp;&ensp;&boxvr;&nbsp; --res=256  |
| &ensp;&ensp;&boxvr;&nbsp; --metrics=none  |
| &ensp;&ensp;&boxvr;&nbsp; --cfg='stylegan2' |
| &ensp;&ensp;&boxvr;&nbsp; --gpus=1  |
| &ensp;&ensp;&boxvr;&nbsp; --kimg=2000  |
| &ensp;&ensp;&boxur;&nbsp; --snap=10  |


Due to limited computing resources, `--kimg` should be set as low as 2000.  
Since there is only one gpu available in the colab environment, set it to `--gpus` = 1.  

## Result
The learning time took about an average of _sec/tick 329_.   

<table>
  <tr>
      <td align="center" ><img src="" width="200" height="100"></td>
     </tr>
     <tr>
     <td align="center" ><img src="" width="200" height="100"></td>
     </tr>
</table>

```
결과물에 대한 설명 및 아쉬운 점
```
