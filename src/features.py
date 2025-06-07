import numpy as np

class ShotCalculations:
    """Class for calculating shot-related features.
    Attributes:
        x (float): Shot x-coordinate
        y (float): Shot y-coordinate
        goal_x (float): Goal x-coordinate
        goal_y (float): Goal y-coordinate
        goal_width (float): Width of the goal    
    """
    def __init__(self,x,y,goal_x=120,goal_y=40, goal_width=7.32):
        self.x=x
        self.y=y
        self.goal_x=goal_x
        self.goal_y=goal_y
        self.goal_width=goal_width
    

    def calculate_shot_distance(self):
        """Calculate the distance from a shot to the goal.

            Returns: 
            float: Distance from the shot to the goal.
        """
        return np.sqrt((self.goal_x - self.x)**2 + (self.goal_y - self.y)**2)


    def calculate_shot_angle(self):
        """Calculate the angle of a shot relative to the goal.
        Returns:
            float: Angle in radians formed by shot position and goal posts
        
        """
    
        #get the coordinates of the goal's top and bottom edges
        top_y = self.goal_y + (self.goal_width / 2)
        bottom_y = self.goal_y - (self.goal_width / 2)

        # Calculate the lengths of the sides of the triangle formed by the shot and the goal
        a = np.sqrt((self.goal_x - self.x)**2 + (top_y - self.y)**2) 
        b = np.sqrt((self.goal_x - self.x)**2 + (bottom_y - self.y)**2) 
        c = self.goal_width # width of the goal

        # Law of Cosines
        angle = np.arccos((a**2 + b**2 - c**2) / (2 * a * b)) 
        return angle