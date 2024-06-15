import glfw

# a function to get the resolution of display system
def display_resolution():
    # Initialize GLFW
    glfw.init()

    # Get the primary monitor
    monitor = glfw.get_primary_monitor()
    
    # Get the video mode of the primary monitor
    mode = glfw.get_video_mode(monitor)
    width, height = mode.size
    glfw.terminate()
    return width, height

def main():
    # Get the display resolution
    width, height = display_resolution()
    print("The resolution of my display system is:", width, "x", height)

if __name__ == "__main__":
    main()




