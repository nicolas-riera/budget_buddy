section_frames = {}
sections = {}

def setup_refresh(sections_dict, frames):
    global sections, section_frames
    sections = sections_dict
    section_frames = frames


def refresh_section(root, name):
    # Re-render section to ensure latest data is displayed
    sections[name](root, section_frames[name])
    
    # Instantly bring the chosen frame to the absolute front (Z-index top)
    # This completely hides the others without doing costly geometry recalculations!
    section_frames[name].tkraise()