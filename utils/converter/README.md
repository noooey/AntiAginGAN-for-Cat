# Convert pkl model to pt model

## Usage
1. Set up for StyleGAN2 TF model
  [Setting Up for StyleGAN2](https://github.com/BOAZ-bigdata/17th_Conference_AntiAginGAN-for-Cat/blob/main/setup/stylegan2/SETUP_StyleGAN2-tf.ipynb)
2. Install more requirements
  `pip install requirements.txt`
3. Export your pkl model to pt model

## Export
```
$ python export_weights.py my_network.pkl my_network.pt
```
