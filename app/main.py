class Distance:
    def __init__(self, km: int | float):
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Distance(km=self.km * other)
        else:
            return None

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            rounded_km = round(self.km / other, 2)
            return Distance(km=rounded_km)
        else:
            return None

    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other
