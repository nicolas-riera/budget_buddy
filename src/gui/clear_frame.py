def clear_frame(root):
    for widget in root.winfo_children():
        widget.destroy()