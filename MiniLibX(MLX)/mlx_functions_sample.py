import pygame
import sys

# --- Core MLX Structures Mockup ---


class MLXContext:
    def __init__(self):
        pygame.init()
        self.windows = []
        self.loop_hook = None
        self.hooks = {}


class MLXWindow:
    def __init__(self, width, height, title):
        self.surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.width = width
        self.height = height
        self.hooks = {}


class MLXImage:
    def __init__(self, width, height, surface=None):
        if surface:
            self.surface = surface
        else:
            self.surface = pygame.Surface((width, height))
        self.width = width
        self.height = height

# --- MLX Functions Refactored ---


def mlx_init():
    """Initializes Pygame and returns a context object."""
    return MLXContext()


def mlx_new_window(mlx, width, height, title="MLX Window"):
    """Creates a new window."""
    win = MLXWindow(width, height, title)
    mlx.windows.append(win)
    return win


def mlx_clear_window(mlx, win):
    """Clears the window (fills with black)."""
    win.surface.fill((0, 0, 0))
    pygame.display.flip()


def mlx_destroy_window(mlx, win):
    """Closes the window."""
    if win in mlx.windows:
        mlx.windows.remove(win)
    pygame.quit()


def mlx_pixel_put(mlx, win, x, y, color):
    """Puts a pixel on the window."""
    # Convert hex color (e.g., 0xFF0000) to RGB tuple
    r = (color >> 16) & 0xFF
    g = (color >> 8) & 0xFF
    b = color & 0xFF
    win.surface.set_at((x, y), (r, g, b))


def mlx_new_image(mlx, width, height):
    """Creates a new empty image (Surface)."""
    return MLXImage(width, height)


def mlx_put_image_to_window(mlx, win, img, x, y):
    """Blits the image to the window."""
    win.surface.blit(img.surface, (x, y))
    pygame.display.update((x, y, img.width, img.height))


def mlx_xpm_file_to_image(mlx, filename):
    """
    Loads an image file (Pygame supports many formats,
    replacing XPM).
    """
    try:
        surf = pygame.image.load(filename).convert_alpha()
        return MLXImage(surf.get_width(), surf.get_height(), surf)
    except pygame.error as e:
        print(f"Error loading image: {e}")
        return None


def mlx_string_put(mlx, win, x, y, color, string):
    """Renders text to the window."""
    pygame.font.init()
    font = pygame.font.SysFont(None, 24)
    r = (color >> 16) & 0xFF
    g = (color >> 8) & 0xFF
    b = color & 0xFF
    text_surface = font.render(string, True, (r, g, b))
    win.surface.blit(text_surface, (x, y))
    pygame.display.update(
        (x, y, text_surface.get_width(), text_surface.get_height()))


def mlx_key_hook(win, funct, param=None):
    """Registers a key release hook."""
    win.hooks['keyup'] = (funct, param)


def mlx_mouse_hook(win, funct, param=None):
    """Registers a mouse click hook."""
    win.hooks['mousebuttondown'] = (funct, param)


def mlx_hook(win, event_type, event_mask, funct, param=None):
    """Generic event hook."""
    win.hooks[event_type] = (funct, param)


def mlx_loop_hook(mlx, funct, param=None):
    """Registers a hook that triggers on every loop iteration."""
    mlx.loop_hook = (funct, param)


def mlx_loop(mlx):
    """The main event loop."""
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Dispatch window specific hooks
            for win in mlx.windows:
                if event.type == pygame.KEYUP and 'keyup' in win.hooks:
                    funct, param = win.hooks['keyup']
                    funct(event.key, param)

                elif (
                    event.type == pygame.MOUSEBUTTONDOWN and
                    'mousebuttondown' in win.hooks
                ):
                    funct, param = win.hooks['mousebuttondown']
                    funct(event.button, event.pos[0], event.pos[1], param)

        if mlx.loop_hook:
            funct, param = mlx.loop_hook
            funct(param)

        pygame.display.flip()
        pygame.time.Clock().tick(60)
        # Cap at 60 FPS to avoid 100% CPU usage

    pygame.quit()
    sys.exit()


# ========================================== #
#                SAMPLE TEST                 #
# ========================================== #

def my_key_funct(keycode, param):
    print(f"Key released: {keycode}")
    if keycode == pygame.K_ESCAPE:  # ESC key
        print("Exiting...")
        pygame.quit()
        sys.exit()


def my_mouse_funct(button, x, y, param):
    print(f"Mouse clicked at ({x}, {y}) with button {button}")
    # Draw a red pixel where the user clicks
    mlx, win = param
    mlx_pixel_put(mlx, win, x, y, 0xFF0000)
    pygame.display.flip()


def main():
    # 1. mlx_init
    mlx = mlx_init()

    # 2. mlx_new_window
    win = mlx_new_window(mlx, 800, 600, "MLX Refactored in Pygame")

    # 3. mlx_string_put
    mlx_string_put(
        mlx, win, 300, 300, 0x00FF00,
        "Hello from Python MLX! Click or press ESC.")

    # 4. mlx_new_image / mlx_put_image_to_window
    img = mlx_new_image(mlx, 100, 100)
    img.surface.fill((0, 0, 255))  # Fill image with blue
    mlx_put_image_to_window(mlx, win, img, 50, 50)

    # 5. Hooks
    mlx_key_hook(win, my_key_funct, param=None)
    mlx_mouse_hook(win, my_mouse_funct, param=(mlx, win))

    # 6. mlx_loop
    mlx_loop(mlx)


if __name__ == '__main__':
    main()
