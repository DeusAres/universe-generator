# universe-generator
Generate a pixel art image in the universe with planets, quasars, stars and black holes
<img src="https://github.com/DeusAres/universe-generator/blob/master/saves/galaxy_1.png?raw=true" width = 300>

# Requirements
python 3+, PIL, numpy, funPIL, PySimpleGUI  
`pip install Pillow numpy funPIL PySimpleGUI`  
Download the this github repo and you are ready to go  


# Usage
The interface is pretty straight forward.  
If you are facing problems, tune down some data, like population, squares sizes and distances.  
I've put a timeout in the generation, if after 5 seconds has yet to be generated, a popup will appear to notice you that you need to tune down the datas  
The last prompted datas for generation is stored in `numbers.json` so you can catch it up later if you need to close the programm  
The images are saved in `./saved/` with name `galaxy_` and an index number  

Happy generation!

