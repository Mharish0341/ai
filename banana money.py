class MonkeyBananaProblem:
    def __init__(self):
        self.room = [
            "#######",
            "#     #",
            "#  M  #",
            "#     #",
            "#  B  #",
            "#     #",
            "#######"
        ]
        self.monkey = (2, 4)
        self.box = None
        self.banana = (4, 4)

    def display_room(self):
        print("\n".join(self.room))

    def move(self, entity, direction):
        row, col = entity
        delta = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
        new_row, new_col = row + delta[direction][0], col + delta[direction][1]

        if 0 <= new_row < len(self.room) and 0 <= new_col < len(self.room[0]) and self.room[new_row][new_col] != '#':
            return new_row, new_col
        return row, col

    def perform_action(self, action):
        if action.startswith("move"):
            self.monkey = self.move(self.monkey, action.split("_")[1])
        elif action.startswith("push") and self.box:
            self.box = self.move(self.box, action.split("_")[1])
        else:
            print("Invalid action.")

    def check_goal(self):
        return self.monkey == self.banana and (not self.box or self.box == self.banana)


if __name__ == "__main__":
    monkey_banana_problem = MonkeyBananaProblem()

    while not monkey_banana_problem.check_goal():
        monkey_banana_problem.display_room()
        action = input("Enter your action: ")
        monkey_banana_problem.perform_action(action)

    print("Congratulations! The monkey reached the banana.")
