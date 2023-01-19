# PCA
Explore the latent space by checking components that affect a specific part through PCA  
We used GANSpace!  
[Original Code](https://github.com/harskish/ganspace)   

<table>
  <tr>
      <td align="center"><img src="https://user-images.githubusercontent.com/66217855/213407552-94a01405-be0e-45e0-ab55-c00a06e27a94.gif" width="100" height="100"><br /><sub><b>eyes</b></sub></td>
      <td align="center"><img src="https://user-images.githubusercontent.com/66217855/213407569-9e2913b9-d0de-43e2-9829-34f5c46f7a22.gif" width="100" height="100"><br /><sub><b>ears</b></sub></td>
      <td align="center"><img src="https://user-images.githubusercontent.com/66217855/213407592-f1af0bb0-1048-4111-86c9-1c5e272953f2.gif" width="100" height="100"><br /><sub><b>mouth</b></sub></td>
      <td align="center"><img src="https://user-images.githubusercontent.com/66217855/213410488-d95a2a36-cc47-4c76-acb3-9aa71c328f03.gif" width="100" height="100"><br /><sub><b>face features</b></sub></td>
  </tr>
</table>

## Requirements
[Setting Up  for GANSpace](https://github.com/BOAZ-bigdata/17th_Conference_AntiAginGAN-for-Cat/blob/main/setup/ganspace/SETUP_GANSpace.md)

## Pretrained Model
Prepare models learned from freezeD experience.  
Convert this pkl model to pt. ([Converter](https://github.com/BOAZ-bigdata/17th_Conference_AntiAginGAN-for-Cat/tree/main/utils/converter))  

## Config
Open models/wrappers.py,  
and edit the stylegan2 configs dict on line 110 to include your model and its corresponding resolution.  

I.E from
```python
# Image widths
configs = {
    'ffhq': 1024,
    'car': 512,
    'cat': 256,
    ...
}
```
to
```python
# Image widths
configs = {
    'anti-cat': 256,
    'ffhq': 1024,
    'car': 512,
    'cat': 256,
    ...
}
```

Then copy your pytorch model over to your drive account or any other hosting platform, and add the direct download link to the checkpoints dict in the download_checkpoint function on line 136.
```python
def download_checkpoint(self, outfile):
    checkpoints = {
        'anti-cat': 'https://drive.google.com/uc?export=download&id=1JxgW_zoVww4hXO0G4PO7e_w3rFtI7jsG',
        'ffhq': 'https://drive.google.com/uc?id=12yYXZymadSIj74Yue1Q7RrlbIqrXggo3',
        'car': 'https://drive.google.com/uc?export=download&id=1iRoWclWVbDBAy5iXYZrQnKYSbZUqXI6y',
        'cat': 'https://drive.google.com/uc?export=download&id=15vJP8GDr0FlRYpE8gD7CdeEz2mXrQMgN',
        ...
    }
```

## Explore Latent Space

| PCA Options |  
| ----------  |
| &ensp;&ensp;&boxvr;&nbsp; --model='StyleGAN2'  |
| &ensp;&ensp;&boxvr;&nbsp; --class='anti-cat'  |
| &ensp;&ensp;&boxvr;&nbsp; --layer='style'  |
| &ensp;&ensp;&boxvr;&nbsp; --use_w |
| &ensp;&ensp;&boxvr;&nbsp; --components=32  |


## Result

<table>
  <tr>
      <td align="center"><img src="https://user-images.githubusercontent.com/66217855/213407552-94a01405-be0e-45e0-ab55-c00a06e27a94.gif" width="200" height="200"><br /><sub><b>eyes</b></sub></td>
      <td align="center"><img src="https://user-images.githubusercontent.com/66217855/213407569-9e2913b9-d0de-43e2-9829-34f5c46f7a22.gif" width="200" height="200"><br /><sub><b>ears</b></sub></td>
  </tr>
  <tr>
      <td align="center"><img src="https://user-images.githubusercontent.com/66217855/213407592-f1af0bb0-1048-4111-86c9-1c5e272953f2.gif" width="200" height="200"><br /><sub><b>mouth</b></sub></td>
      <td align="center"><img src="https://user-images.githubusercontent.com/66217855/213410488-d95a2a36-cc47-4c76-acb3-9aa71c328f03.gif" width="200" height="200"><br /><sub><b>face features</b></sub></td>
  </tr>
</table>


```
We explored the latent space to find a latent vector that affects a specific feature.  
```
