# AntiAginGAN for Cat
Cat Anti-aging Project based StyleGAN2  
```
메인 이미지
```

## Introduction
```
😼 We will make a childhood image of the cat for you who adopted an abandoned cat!
```  
### Background of topic
설명 ...
### Project Objectives
설명 ...

## Problem Definition
Considering the problems below,  
various experiments were conducted with various models to transform Cat into kitten.  
- The cat's species must not change.
- The resulting product should resemble the cat in the input image.
- The result should look young.

## Environment
- OS : Ubuntu 18.04 or Colab
- GPU : Tesla V100-32GB

## Data Preparation
- Web crawling ([Crawler](https://github.com/BOAZ-bigdata/17th_Conference_AntiAginGAN-for-Cat/tree/main/utils/crawler))  
- Resizing images to 256*256  
- Image cleaning ([Cleaner](https://github.com/BOAZ-bigdata/17th_Conference_AntiAginGAN-for-Cat/tree/main/utils/cleaner))  

## StyleGAN2 ADA
Training StyleGAN2 ADA tf model with custom dataset.   

[Detail](https://github.com/BOAZ-bigdata/17th_Conference_AntiAginGAN-for-Cat/blob/main/experiments/StyleGAN2-ADA.md)  
![project11](https://user-images.githubusercontent.com/66217855/211796487-e4419e8f-9e46-4baa-bbaa-0362e1666a45.gif)  

## StyleGAN2 ADA + FreezeD
Fine-tuning the StyleGAN2-ADA tf model pre-trained with afhq cat as custom dataset.  

[Detail](https://github.com/BOAZ-bigdata/17th_Conference_AntiAginGAN-for-Cat/blob/main/experiments/StyleGAN2-ADA-FreezeD.md)  
![project3](https://user-images.githubusercontent.com/66217855/211782101-54235c62-8f94-42ef-a872-6c1c5d1e1f6e.gif)  

## StyleMixing
Disentangled features can be identified through the result that changes according to the layer being swapped.

![ezgif com-gif-maker](https://user-images.githubusercontent.com/66217855/212104286-82cbe6d9-9118-4bc2-b43e-c61dc3b0a113.gif)  

## GANSpace
PCA for Latent Space Exploration  
[Detail]()  

```
결과 이미지
```

## StyleCLIP
설명 ...  
[Detail]()  

```
결과 이미지
```

## Conclusion
```
어쩌구...
```

## Contributors
<table>
  <tr>
      <td align="center"><a href="https://github.com/noooey"><img src="https://avatars.githubusercontent.com/u/66217855?v=4" width="100" height="100"><br /><sub><b>박규연</b></sub></td>
      <td align="center"><a href="https://github.com/GGrite"><img src="https://avatars.githubusercontent.com/u/102473690?v=4" width="100" height="100"><br /><sub><b>김가영</b></sub></td>
      <td align="center"><a href="https://github.com/EUNYUGNYU"><img src="https://avatars.githubusercontent.com/u/64732835?v=4" width="100" height="100"><br /><sub><b>서은유</b></sub></td>
      <td align="center"><a href="https://github.com/Lee-Kiwon"><img src="https://avatars.githubusercontent.com/u/78652810?v=4" width="100" height="100"><br /><sub><b>이기원</b></sub></td>
     </tr>
</table>
