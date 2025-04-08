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
         # Initialize Pygame
        pygame.init()

        # Set up the display
        self.screen = pygame.display.set_mode((1000, 1000), pygame.FULLSCREEN)
        set_window_icon('./MARKUPLOGO.png')
        pygame.display.set_caption("Draw")

        # Initialize attributes
        self.isFullscreen, self.radius, self.color = True, 15, (0, 0, 255)  # Default color is blue
        self.clock, self.drawing, self.last_pos = pygame.time.Clock(), False, None

        # Create a blank canvas
        self.canvas = pygame.Surface(self.screen.get_size())
        self.canvas.fill((0, 0, 0))  # Start with a black canvas

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
            #fill with black
            self.screen.fill((0, 0, 0))

            # Blit the canvas (which contains drawings) 
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