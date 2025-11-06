from copy import deepcopy

# -------------------------------
# 1) کلاس State = وضعیت برج‌ها
# -------------------------------

class State:
    def __init__(self, pegs):
        # pegs مثل [ [3,2,1], [], [] ] هست
        self.pegs = pegs

    def __str__(self):
        # وضعیت فعلی برج‌ها رو برمی‌گردونه
        return str(self.pegs)


# -------------------------------
# 2) کلاس Problem =تعریف کلی
# -------------------------------

class Problem:
    def __init__(self, start_state):
        self.start_state = start_state

    def is_goal(self, state):
        # بررسی می‌کنه که آیا رسیدیم به هدف یا نه
        pass

    def get_moves(self, state):
        # حرکات ممکن رو برمی‌گردونه
        pass

    def do_move(self, state, move):
        # بعد از یه حرکت، وضعیت جدید رو می‌سازه
        pass


# -------------------------------
# 3) کلاس TowerOfHanoi = خود بازی
# -------------------------------

class TowerOfHanoi(Problem):
    def __init__(self, disks):
        # حالت شروع (همه دیسک‌ها روی میله اول)
        start = State([list(range(disks, 0, -1)), [], []])
        super().__init__(start)
        self.disks = disks

    def is_goal(self, state):
        # هدف: همه دیسک‌ها روی میله سوم باشن
        return len(state.pegs[2]) == self.disks

    def get_moves(self, state):
        moves = []
        for i in range(3):
            if not state.pegs[i]:
                continue
            top = state.pegs[i][-1]
            for j in range(3):
                if i != j and (not state.pegs[j] or top < state.pegs[j][-1]):
                    moves.append((i, j))
        return moves

    def do_move(self, state, move):
        new_pegs = deepcopy(state.pegs)
        i, j = move
        disk = new_pegs[i].pop()
        new_pegs[j].append(disk)
        return State(new_pegs)


# -------------------------------
# 4) حل بازگشتی برج هانوی
# -------------------------------

def solve_hanoi(n, source, target, helper, moves):
    if n == 1:
        moves.append((source, target))
    else:
        solve_hanoi(n - 1, source, helper, target, moves)
        moves.append((source, target))
        solve_hanoi(n - 1, helper, target, source, moves)
    return moves


# -------------------------------
# 5) اجرای برنامه
# -------------------------------
if __name__ == "__main__":
    game = TowerOfHanoi(3)

    print("=== Tower of Hanoi Game ===")
    print("Initial State:", game.start_state)

    moves = solve_hanoi(game.disks, 0, 2, 1, [])
    state = game.start_state

    for step, move in enumerate(moves, 1):
        state = game.do_move(state, move)
        print(f"Step {step}: {state}")

    print("*** Goal Reached?", game.is_goal(state))
    print("Total Moves:", len(moves))


