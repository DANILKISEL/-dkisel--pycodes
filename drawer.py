import pygame
import os
import colors


def set_window_icon(file_path):
    """Set the window icon from a given file path."""
    if os.path.isfile(file_path):
        icon = pygame.image.load(file_path)
        pygame.display.set_icon(icon)
        print(f"Window icon set to {file_path}")
    else:
        print("Icon file not found. Please check the path.")


class DrawingApp:
    def __init__(self):
        # Initialize Pygame and set up the display
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 1000) , pygame.FULLSCREEN)
        set_window_icon('./MARKUPLOGO.png')
        pygame.display.set_caption("Draw")
        self.isFullscreen = True
        self.clock = pygame.time.Clock()
        self.radius = 15
        self.color = (0, 0, 255)  # Default color is blue
        self.drawing = False
        self.last_pos = None

        # Create a surface to draw on (initially blank)
        self.canvas = pygame.Surface(self.screen.get_size())
        self.canvas.fill((0, 0, 0))  # Start with a black canvas

        self.loaded_image = None  # Initialize variable for loaded image

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    self.handle_keydown(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.drawing = True
                        self.last_pos = event.pos

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.drawing = False
                        self.last_pos = None

                if event.type == pygame.MOUSEMOTION:
                    if self.drawing and self.last_pos is not None:
                        # Draw a line from the last position to the current position on the canvas surface.
                        pygame.draw.line(self.canvas, self.color, self.last_pos, event.pos, self.radius)
                        self.last_pos = event.pos

            # Check if the display is still active before blitting
            if not pygame.display.get_init():
                break

            # Blit the loaded image first (if any), then draw on top of it
            if self.loaded_image is not None:
                img_rect = self.loaded_image.get_rect(topleft=(0, 0))
                self.screen.blit(self.loaded_image, img_rect.topleft)
            else:
                # If no image is loaded, fill with black
                self.screen.fill((0, 0, 0))

            # Blit the canvas (which contains drawings) over the loaded image
            self.screen.blit(self.canvas, (0, 0))

            pygame.display.flip()
            self.clock.tick(60)

    def handle_keydown(self, event):
        """Handle key press events."""
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            return
        if event.key == pygame.K_z:  # Clear display when 'Z' is pressed
            # Clear only the drawing canvas; keep the loaded image intact.
            self.canvas.fill((0, 0, 0))
        if event.key == pygame.K_s:  # Save when 'S' is pressed
            filename = input("FILENAME:")
            pygame.image.save(self.canvas, filename)
            print(f"Drawing saved as '{filename}'")

        if event.key == pygame.K_e:  # Toggle eraser when 'E' is pressed
            self.color = (0, 0, 0) if self.color != (0, 0, 0) else (255, 255, 255)

        if event.key == pygame.K_F12:
            if not self.isFullscreen:
                self.screen = pygame.display.set_mode((1000, 1000) , pygame.FULLSCREEN)
                self.isFullscreen = True
            else:
                self.screen = pygame.display.set_mode((1000, 1000))
                self.isFullscreen = False


        # Color selection keys
        color_map = colors.color_map_f()

        if event.key in color_map:
            self.color = color_map[event.key]

if __name__ == "__main__":
    app = DrawingApp()
    app.run()