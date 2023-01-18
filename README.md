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
Recently, pet shops have emerged as a big social problem in the concept of buying and selling living things for money.  
If a cat is adopted from an abandoned cat center, there are no childhood photos of the cat!  

### Project Objectives
Encouraging adoption of abandoned cats

## Problem Definition
- The cat's species must not change.
- The resulting product should resemble the cat in the input image.
- The result should look young.

Considering the above problems ,  
various experiments were conducted with various models to transform Cat into kitten.  

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

![project11](https://user-images.githubusercontent.com/102473690/212833511-99ed675c-dd6c-4336-afa8-80b03a26ec0a.gif)  

## StyleGAN2 ADA + FreezeD
Fine-tuning the StyleGAN2-ADA tf model pre-trained with afhq cat as custom dataset.  

[Detail](https://github.com/BOAZ-bigdata/17th_Conference_AntiAginGAN-for-Cat/blob/main/experiments/StyleGAN2-ADA-FreezeD.md)  

![project3](https://user-images.githubusercontent.com/66217855/211782101-54235c62-8f94-42ef-a872-6c1c5d1e1f6e.gif)  

## StyleMixing
Disentangled features can be identified through the result that changes according to the layer being swapped.

![ezgif com-gif-maker](https://user-images.githubusercontent.com/66217855/212104286-82cbe6d9-9118-4bc2-b43e-c61dc3b0a113.gif)  

## GANSpace
PCA for Latent Space Exploration  

[Detail](https://github.com/BOAZ-bigdata/17th_Conference_AntiAginGAN-for-Cat/blob/main/experiments/GANSpace.md)  

```
결과 이미지
```

## Conclusion
We created a kitten generate model through the Stylegan2-ada model.  
We explored the latent space to find a latent vector that affects a specific feature.  
Using this vector, the projected late vector was further adjusted to generate the desired image.  
