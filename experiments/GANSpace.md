# GANSpace
PCA for Latent Space Exploration  
[Original Code](https://github.com/harskish/ganspace)  

```
image
```

## Requirements
- PyTorch 1.3
- Python 3.7

[Setting Up  for GANSpace](https://github.com/harskish/ganspace/blob/master/SETUP.md)

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

| Visualize Options |  
| ----------  |
| &ensp;&ensp;&boxvr;&nbsp; --model='StyleGAN2'  |
| &ensp;&ensp;&boxvr;&nbsp; --class='anti-cat'  |
| &ensp;&ensp;&boxvr;&nbsp; --layer='style'  |
| &ensp;&ensp;&boxvr;&nbsp; --use_w |
| &ensp;&ensp;&boxvr;&nbsp; --inputs  |
| &ensp;&ensp;&boxvr;&nbsp; --sigma  |
| &ensp;&ensp;&boxvr;&nbsp; -n  |
| &ensp;&ensp;&boxvr;&nbsp; -b  |
| &ensp;&ensp;&boxur;&nbsp; -c  |


## Result


```
결과물에 대한 설명 및 아쉬운 점
```
