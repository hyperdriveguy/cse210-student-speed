class Point:
    """Represents distance from an origin (0, 0).

    Stereotype:
        Information Holder

    Attributes:
        _x (integer): The horizontal distance.
        _y (Point): The vertical distance.
    """
    
    def __init__(self, x, y):
        """The class constructor.
        
        Args:
            self (Point): An instance of Point.
            x (integer): A horizontal distance.
            y (integer): A vertical distance.
            velocity x (integer): A horizontal velocity.
            velocity y (integer): A vertical velocity.
        """
        self._x = x
        self._y = y
        self._velocity_x = 0
        self._velocity_y = 0

    def add_point(self, other):
        """Gets a new point instance that is the sum of this and the given one.

        Args:
            self (Point): An instance of Point.
            other (Point): The Point to add.

        Returns:
            Point: A new Point that is the sum.
        """
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)

    def equals(self, other):
        """Whether or not this Point is equal to the given one.

        Args:
            self (Point): An instance of Point.
            other (Point): The Point to compare.

        Returns: 
            boolean: True if both x and y are equal; false if otherwise.
        """
        return self._x == other.get_x() and self._y == other.get_y()

    def update_position(self):
        """Changes the position based on the point's velocity.

        Args:
            self (Point): An instance of Point.
        """
        self._x += self._velocity_x
        self._y += self._velocity_y

    @property
    def x_velocity(self):
        return self._velocity_x
    
    @x_velocity.setter
    def x_velocity(self, x_velocity: int):
        self._velocity_x = x_velocity

    @property
    def y_velocity(self):
        return self._velocity_y
    
    @y_velocity.setter
    def y_velocity(self, y_velocity: int):
        self._velocity_y = y_velocity
    
    @property
    def x(self):
        """Gets the horizontal distance.
        
        Args:
            self (Point): An instance of Point.
            
        Returns:
            integer: The horizontal distance.
        """
        return self._x
    
    @x.setter
    def x(self, x: int):
        """Sets the horizontal distance.
        
        Args:
            self (Point): An instance of Point.
            
        Returns:
            integer: The horizontal distance.
        """
        return self._x
        self._x = x
    
    @property
    def y(self):
        """Gets the vertical distance.
        
        Args:
            self (Point): An instance of Point.
            
        Returns:
            integer: The vertical distance.
        """
        return self._y
    
    @y.setter
    def y(self, y: int):
        """Sets the vertical distance.
        
        Args:
            self (Point): An instance of Point.
            
        Returns:
            integer: The vertical distance.
        """
        self._y = y

    def new_reverse(self):
        """Gets a new Point that is the reverse of this one.
        
        Args:
            self (Point): An instance of Point.
            
        Returns:
            Point: A new Point that is reversed.
        """
        x = self._x * -1
        y = self._y * -1
        return Point(x, y)