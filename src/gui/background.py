import CTkGradient as ctkg

def background(root):

    gradient_frame = ctkg.GradientFrame(
    master = root,
    colors = ("#645552", "#AF9590"),
    direction = "horizontal",
    height = 1280,
    width = 720
    )

    gradient_frame.pack(fill = "both", expand = True)