import pygame

class Timer:
    def __init__(self, duration):
        self.duration = duration  # Set duration of the timer in seconds
        self.current_time = 0     # Timer starts at 0
        self.running = False      # Timer state

    def start(self):
        self.start_time = pygame.time.get_ticks()  # Start time for reference
        self.running = True            # Timer is now running

    def update(self):
        if self.running:
            self.current_time = pygame.time.get_ticks() - self.start_time  # Calculate elapsed time
            if self.current_time >= self.duration:             # Check if time's up
                self.stop()

    def stop(self):
        self.running = False  # Stop the timer
        self.current_time = 0
        # print("Timer finished!")

    # def reset(self):
    #     self.current_time = 0  # Reset the timer back to 0
    #     self.running = False    # Timer stops