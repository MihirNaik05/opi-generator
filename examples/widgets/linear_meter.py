from opigen import Renderer
from opigen.widgets import LinearMeter 
from opigen.contrib import Display 
from opigen.colors import Color
# faster opening  
import argparse
import subprocess

def main():
    meter = LinearMeter(x=40, y=40, 
                        width=400,height=100,
                        pv_name="sim://sine(0,100,1.0)",# define local variable for CS studio
                        enable_gradient=True,
                        highlight_active_region=False)

    # set warning colors
    meter.set_major_color(Color((198,34,15))) 
    meter.set_minor_color(Color((253,137,36)))
    
    screen = Display(600,400,name="Meter Widget")

    screen.add_child(meter)

    r = Renderer(screen, auto_resize=True)
    r.to_bob("examples/widgets/linear_meter.bob")  


if __name__=="__main__":
    main()

    parser = argparse.ArgumentParser()

    parser.add_argument('-open', action='store_true')
    OPEN = parser.parse_args().open
    if OPEN:
        print("Opening Phoebus...")
        subprocess.Popen(['/usr/bin/phoebus', "-resource", 'examples/widgets/linear_meter.bob'])
        
