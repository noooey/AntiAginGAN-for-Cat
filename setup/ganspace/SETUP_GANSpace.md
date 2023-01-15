# Setting for GANSpace

## setting
mount google drive and clone the ganspace repository   
then run under the script  
```shell
from IPython.display import Javascript
display(Javascript('''google.colab.output.setIframeHeight(0, true, {maxHeight: 200})'''))
!git submodule update --init --recursive
!python -c "import nltk; nltk.download('wordnet')"

# Custom OPs no longer required
#!pip install Ninja
#%cd models/stylegan2/stylegan2-pytorch/op
#!python setup.py install
#!python -c "import torch; import upfirdn2d_op; import fused; print('OK')"
#%cd "/content/ganspace"
```

## install
install packages  
```shell
!pip install requirements.txt
```
