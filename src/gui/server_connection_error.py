import customtkinter as ctk

def server_connection_error_page(root):

    error_frame = ctk.CTkFrame(root, fg_color="transparent")
    error_frame.place(relx=0.5, rely=0.5, anchor="center")

    error_label = ctk.CTkLabel(error_frame, text="Unable to connect to server.", font=("Arial", 30), fg_color="transparent")
    error_label.pack(pady=(0, 40))

    error_message_label = ctk.CTkLabel(error_frame, text=root.database.connection_error, font=("Arial", 20), fg_color="transparent", wraplength=700)
    error_message_label.pack(pady=(0, 0))