"""
1. Begin by defining the base class `Sport` with the `__init__()` method. This method should initialize the `name` attribute.

2. Implement the `__str__()` method in the `Sport` class. It should return a formatted string that describes the sport.

3. Define the `__eq__()` method in the `Sport` class to compare the name of the sport with another object of the same class. Return `True` if they match; otherwise, return `False`.

4. Create a derived class `Football` that inherits from the `Sport` class. Add an additional attribute, `team`, in the `__init__()` method of the `Football` class.

5. Implement the `__str__()` method in the `Football` class to return a formatted string that describes a football match and lists the teams involved.

6. Define the `__eq__()` method in the `Football` class to compare the name and teams of the football matches.

7. Implement the `__sub__()` method in the `Football` class. If the other object is also a `Football` match, find the common teams between the two matches. If there are shared teams, create a new `Football` object representing the rivalry with those teams. If there are no common teams, return a message indicating the absence of shared teams. If the other object is not a `Football` match, return an error message stating that subtraction cannot be performed between different sports.

8. Create another derived class `Basketball` that also inherits from the `Sport` class. In the `__init__()` method of the `Basketball` class, add an additional attribute, `team`.

9. Implement the `__str__()` method in the `Basketball` class to return a formatted string that describes a basketball game and lists the teams involved.

10. Define the `__eq__()` method in the `Basketball` class to compare the name and teams of the basketball games.

11. Implement the `__sub__()` method in the `Basketball` class similar to the `Football` class, finding common teams and returning a new `Basketball` object representing the rivalry, or an appropriate error message.

12. In the usage example section, create instances of the `Sport`, `Football`, and `Basketball` classes with different attributes.

13. Test the code by printing the objects using `print()`, comparing their equality using the `==` operator, and performing subtraction operations using the `-` operator.

By following these steps, your students should be able to understand the concepts behind the special methods (`__str__()`, `__eq__()`, and `__sub__()`) used in the classes and complete the code accordingly.
"""


class Sport:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"This is {self.name}"

    def __add__(self, other):
        raise TypeError("Not Possible")

    def __sub__(self, other):
        raise TypeError("Not Possible")


class Football(Sport):
    def __init__(self, name, team):
        Sport.__init__(self, name)
        self.team = team

    def __str__(self):
        return f"This is {self.name} team, matched with teams: {', '.join(self.team)}"

    def __eq__(self, other):
        if isinstance(other, Football):
            return self.name == other.name and self.team == other.team
        return False

    def __sub__(self, other):
        if isinstance(other, Football):
            shared_teams = list(set(self.team) & set(other.team))
            if shared_teams:
                return Football(f"{self.name}: ", shared_teams)
            else:
                return f"No common teams between them"
        return "Not Possible"


class Basketball(Sport):
    def __init__(self, name, team):
        Sport.__init__(self, name)
        self.team = team

    def __str__(self):
        return f"This is {self.name} team, matched with teams: {', '.join(self.team)}"

    def __eq__(self, other):
        if isinstance(other, Basketball):
            return self.name == other.name and self.team == other.team
        return False

    def __sub__(self, other):
        if isinstance(other, Basketball):
            shared_teams = list(set(self.team) & set(other.team))
            if shared_teams:
                return Basketball(f"{self.name}: ", shared_teams)
            else:
                return f"No common teams between them"
        return "Not Possible"


basic = Sport("super basic!")


football1 = Football("Football", ["Team A", "Team B"])
football2 = Football("Football", ["Team A", "Team B"])

basketball1 = Basketball("Basketball", ["Kingss", "Rockets"])
basketball2 = Basketball("Basketball", ["Jazz", "Kings"])

print(basic)
print(football1)
print(basketball1)

print(football1 == football2)
print(basketball1 == football1)


print(basketball1 - basketball2)
