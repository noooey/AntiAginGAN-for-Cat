<h1 align="center">Anti-AginGAN for CAT</h1>
<h3 align="center">Cat Anti-aging Project based StyleGAN2</h3>

![image](https://user-images.githubusercontent.com/66217855/213877139-57529be7-6940-4e6d-9d15-dd85e183e278.png)

## Introduction
```
😼 We will make a childhood image of the cat for you who adopted an abandoned cat!
```  
### Background of topic
Recently, pet shops have emerged as a big social problem in the concept of buying and selling living things for money.  
We want to prevent this phenomenon and encourage adoption of abandoned cats.  
If a cat is adopted from an abandoned cat center, there are no childhood photos of the cat, u_u  
I think we can make that memory for them!  

### Project Objectives
Encouraging adoption of abandoned cats

## Problem Definition
- The cat's species must not change.
- The resulting product should resemble the cat in the input image.
- The result should look young.

Considering the above problems ,  
various experiments were conducted to transform cat into kitten.  

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

![project11](https://user-images.githubusercontent.com/102473690/212834598-93d5ced1-1bfb-4649-b62e-d16eb1752fbf.gif)  

## StyleGAN2 ADA + FreezeD
Fine-tuning the StyleGAN2-ADA tf model pre-trained with afhq cat using custom dataset.

[Detail](https://github.com/BOAZ-bigdata/17th_Conference_AntiAginGAN-for-Cat/blob/main/experiments/StyleGAN2-ADA-FreezeD.md)  

![project3](https://user-images.githubusercontent.com/66217855/211782316-3f30000d-1396-4e73-b0be-b2bec91a9d83.gif)  

## StyleMixing
Disentangled features can be identified through the result that changes according to the layer being swapped.

![ezgif com-gif-maker](https://user-images.githubusercontent.com/66217855/212104286-82cbe6d9-9118-4bc2-b43e-c61dc3b0a113.gif)  

## PCA
PCA for Latent Space Exploration  

[Detail](https://github.com/BOAZ-bigdata/17th_Conference_AntiAginGAN-for-Cat/blob/main/experiments/PCA.md)  

<table>
  <tr>
      <td align="center"><img src="https://user-images.githubusercontent.com/66217855/213487974-ce67fb70-deb2-4547-bad5-3f7fab89f6ca.gif" width="180" height="180"><br /><sub><b>eyes</b></sub></td>
      <td align="center"><img src="https://user-images.githubusercontent.com/66217855/213407569-9e2913b9-d0de-43e2-9829-34f5c46f7a22.gif" width="180" height="180"><br /><sub><b>ears</b></sub></td>
      <td align="center"><img src="https://user-images.githubusercontent.com/66217855/213407592-f1af0bb0-1048-4111-86c9-1c5e272953f2.gif" width="180" height="180"><br /><sub><b>mouth</b></sub></td>
      <td align="center"><img src="https://user-images.githubusercontent.com/66217855/213410488-d95a2a36-cc47-4c76-acb3-9aa71c328f03.gif" width="180" height="180"><br /><sub><b>face features</b></sub></td>
  </tr>
</table>

## Apply to real image
Partially adjust latent vector of Images projected into the latent space, with components found through PCA.  

[Detail](https://github.com/BOAZ-bigdata/17th_Conference_AntiAginGAN-for-Cat/blob/main/experiments/ApplytoRealImage.md)

<table>
  <tr>
      <td align="center"><img src="https://user-images.githubusercontent.com/66217855/213456137-46320d43-045d-4201-952f-79c779a81dbf.jpg" width="180" height="180"><br /><sub><b>cat image</b></sub></td>
      <td align="center"><img src="https://user-images.githubusercontent.com/66217855/213457118-3b9d70e5-aa27-4f7c-93e3-162df4933346.gif" width="180" height="180"><br /><sub><b>projected image</b></sub></td>
      <td align="center"><img src="https://user-images.githubusercontent.com/66217855/213464059-3d016d81-b972-4e50-aaf3-b3c6d5f971fe.gif" width="180" height="180"><br /><sub><b>adjust latent vector</b></sub></td>
  </tr>
</table>


## Conclusion
We created a kitten generate model through the Stylegan2-ada model.  
We explored the latent space to find a latent vector that affects a specific feature.  
Using this vector, the projected latent vector was further adjusted to generate the desired images.  

In conclusion, we can convert cat into a kitten by combining and applying the components.  

## References
https://github.com/NVlabs/stylegan2-ada  
https://github.com/harskish/ganspace  
https://github.com/orpatashnik/StyleCLIP   

---

[@BOAZ-bigdata](https://github.com/BOAZ-bigdata) 17th Big Data Conference
