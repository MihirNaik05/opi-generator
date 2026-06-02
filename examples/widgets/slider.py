from opigen import Renderer
from opigen.widgets import ScaledSlider 
from opigen.contrib import Display 
# faster opening  
import argparse
import subprocess

def main():
    slider = ScaledSlider(x=40, y=40, 
                        width=400,height=100,
                        pv_name="loc://slider(0)",# define local variable for CS studio
                        limits_from_pv=True # inherit value limits from the process var 
                        ) 

    screen = Display(1200,800,name="Slider Widget")

    screen.add_child(slider)

    r = Renderer(screen, auto_resize=True)
    r.to_bob("examples/widgets/slider.bob")  

if __name__=="__main__":
    main()

    parser = argparse.ArgumentParser()

    parser.add_argument('-open', action='store_true')
    OPEN = parser.parse_args().open
    if OPEN:
        print("Opening Phoebus...")
        subprocess.Popen(['/usr/bin/phoebus', "-resource", 'examples/widgets/slider.bob'])
