class Border:

    def __init__(self, style, width, color, alarm: bool):
        # style: only applies to BOY
        # alarm refers to 'Alarm Sensitive' in 'Border' section (BOY),
        # and 'Alarm Border' in 'Behavior' section (BOB)
        self.alarm = alarm
        self.color = color
        self.style = style
        self.width = width
