from opigen import Renderer
from opigen.widgets import ProgressBar 
from opigen.contrib import Display 
from opigen.colors import Color
# faster opening  
import argparse
import subprocess

def main(): 
    bar = ProgressBar(x=40,y=40,width=400,height=100,
                      pv_name="sim://sine(0,100,0.5)") 
    
    screen = Display(600,400,name="Progress Bar Widget")

    screen.add_child(bar)

    r = Renderer(screen, auto_resize=True)
    r.to_bob("examples/widgets/progress_bar.bob")  


if __name__=="__main__":
    main()

    parser = argparse.ArgumentParser()

    parser.add_argument('-open', action='store_true')
    OPEN = parser.parse_args().open
    if OPEN:
        print("Opening Phoebus...")
        subprocess.Popen(['/usr/bin/phoebus', "-resource", 'examples/widgets/progress_bar.bob'])
        
