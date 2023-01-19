# Apply to real image
Partially adjust latent vector of Images projected into the latent space, with components found through PCA.   
We used **a combination of two components** because we couldn't find one component that transformed into a kitten's form.  

<table>
  <tr>
      <td align="center"><img src="https://user-images.githubusercontent.com/66217855/213456137-46320d43-045d-4201-952f-79c779a81dbf.jpg" width="180" height="180"><br /><sub><b>cat image</b></sub></td>
      <td align="center"><img src="https://user-images.githubusercontent.com/66217855/213457118-3b9d70e5-aa27-4f7c-93e3-162df4933346.gif" width="180" height="180"><br /><sub><b>projected image</b></sub></td>
      <td align="center"><img src="https://user-images.githubusercontent.com/66217855/213464059-3d016d81-b972-4e50-aaf3-b3c6d5f971fe.gif" width="180" height="180"><br /><sub><b>adjust latent vector</b></sub></td>
  </tr>
</table>


## Components
We found a meaningful component out of 32 components. (from PCA)[https://github.com/BOAZ-bigdata/17th_Conference_AntiAginGAN-for-Cat/blob/main/experiments/PCA.md]  
We selected and combined the two components below to create a direction for converting cat into a kitten.  

<table>
  <tr>
      <td align="center"><img src="https://user-images.githubusercontent.com/66217855/213407592-f1af0bb0-1048-4111-86c9-1c5e272953f2.gif" width="200" height="200"><br /><sub><b>mouth</b></sub></td>
      <td align="center"><img src="https://user-images.githubusercontent.com/66217855/213410488-d95a2a36-cc47-4c76-acb3-9aa71c328f03.gif" width="200" height="200"><br /><sub><b>face features</b></sub></td>
  </tr>
</table>

## Result

<table>
  <tr>
      <td align="center"><img src="https://user-images.githubusercontent.com/66217855/213456137-46320d43-045d-4201-952f-79c779a81dbf.jpg" width="200" height="200"><br /><sub><b>cat image</b></sub></td>
      <td align="center"><img src="https://user-images.githubusercontent.com/66217855/213457118-3b9d70e5-aa27-4f7c-93e3-162df4933346.gif" width="200" height="200"><br /><sub><b>projected image</b></sub></td>
      <td align="center"><img src="https://user-images.githubusercontent.com/66217855/213464059-3d016d81-b972-4e50-aaf3-b3c6d5f971fe.gif" width="200" height="200"><br /><sub><b>adjust latent vector</b></sub></td>
  </tr>
</table>

```
We were able to generate the desired image using the additional adjusted latent vector.
Now we can adjust the face area we want anywhere!
```
