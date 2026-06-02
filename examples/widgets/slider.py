from opigen import Renderer
from opigen.widgets import ScaledSlider 
from opigen.contrib import Display 

slider = ScaledSlider(x=40, y=40, 
                      width=400,height=100,
                      pv_name="loc://slider(0)",# define local variable for CS studio
                      limits_from_pv=True # inherit value limits from the process var 
                      ) 

screen = Display(1200,800,name="Slider Widget")

screen.add_child(slider)

r = Renderer(screen, auto_resize=True)
r.to_bob("examples/widgets/slider.bob")  

