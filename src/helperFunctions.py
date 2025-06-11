import matplotlib.pyplot as plt


def draw_pitch(ax=None, pitch_length=120, pitch_width=80):
    """Function to draw a football pitch with specified dimensions."""
    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 8))
    
    # Pitch Outline & Centre Line
    ax.plot([0, 0, pitch_length, pitch_length, 0], [0, pitch_width, pitch_width, 0, 0], color="black")
    ax.plot([pitch_length/2, pitch_length/2], [0, pitch_width], color="black")
    
    # Left Penalty Area
    ax.plot([18, 18, 0, 0, 18], [62, 18, 18, 62, 62], color="black")
    # Right Penalty Area
    ax.plot([pitch_length, pitch_length, pitch_length-18, pitch_length-18, pitch_length], 
            [62, 18, 18, 62, 62], color="black")
    
    # Left 6-yard Box
    ax.plot([6, 6, 0, 0, 6], [50, 30, 30, 50, 50], color="black")
    # Right 6-yard Box
    ax.plot([pitch_length, pitch_length, pitch_length-6, pitch_length-6, pitch_length],
            [50, 30, 30, 50, 50], color="black")
    
    # Centre Circle
    centre_circle = plt.Circle((pitch_length/2, pitch_width/2), 10, color="black", fill=False)
    ax.add_patch(centre_circle)
    
    # Penalty Spots
    ax.plot([12, pitch_length-12], [pitch_width/2, pitch_width/2], marker='o', color='black', linestyle='None')
    
    # Remove axis labels and ticks
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Set limits to the pitch size
    ax.set_xlim(0, pitch_length)
    ax.set_ylim(0, pitch_width)
    
    ax.set_aspect('equal')
    return ax