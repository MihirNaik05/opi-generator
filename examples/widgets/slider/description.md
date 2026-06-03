# Basic Scaled Slider

This example shows:

- `widgets.Display(1200,800,name="Slider Widget")`
- `widgets.ScaledSlider(x=40, y=40,
                width=400,height=100,
                pv_name="loc://slider(0)",
                limits_from_pv=True)`

The display contains a single scaled slider object.

The only PV is `loc://slider` which stores the value of the slider in a local variable.
