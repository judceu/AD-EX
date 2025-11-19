class Player:
    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number
    def __eq__(self, other):
        if isinstance(other, Player) and self.name == other.name:
            return True
        return False
    def __lt__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        if self.number < other.number:
            return True
        return False
    def __str__(self):
        return f"{self.name} ({self.number})"
def main():
    player1 = Player("Player1", 1)
    player2 = Player("Player2", 2)
    player3 = Player("Player3", 3)

    print(player1)
    print(player1 == Player("Player1", 99)) #eq
    lst = [player1, player2, player3]
    for p in sorted(lst):
        print (p)
class Pass:
    def __init__(self, sender, receiver, nr_of_times):
        self.sender = sender
        self.receiver = receiver
        self.nr_of_times = nr_of_times
    def get_weight(self, nr_of_times):
        return self.nr_of_times
    def get_start(self):
        return self.sender
    def get_end(self):
        return self.receiver
    def __eq__(self, other):
        if isinstance(other, Pass) and self.sender == other.sender and self.receiver == other.receiver:
            return True
        return False
def main():
    player1 = Player("Player1", 1)
    player2 = Player("Player2", 2)
    player3 = Player("Player3", 3)
    pass1 = Pass(player1, player2, 2)
    pass2 = Pass(player2, player3, 3)
    pass3 = Pass(player1, player2, 9)
    print(pass1)
    print(pass2 == pass3)
    print(pass2.get_weight())
class PassGraph:
    def __init__(self):
        self.players = []
        self.adj = {}
    def add_player(self, player):
        if player not in self.players:
            self.players.append(player)
            self.adj[player.name] = [] #playerNAME
    def has_player(self, player):
        return player in self.players
    def get_player(self, name):
        for player in self.players:
            if player.name == name:
                return player
        return None
    def add_pass(self, sender, receiver, times):
        if sender.name not in self.players or receiver.name not in self.players:
            raise ValueError
        if times <= 0:
            raise ValueError
        nr_of_times = 0
        for p in self.adj[sender.name]:
            if p.receiver == receiver:
                nr_of_times += times
            self.adj[sender] = Pass(sender, receiver, nr_of_times)
    def get_pass(self, sender_name, receiver_name):
        if sender_name not in self.adj:
            return None
        for p in self.adj[sender_name]:
            if p.receiver.name == receiver_name:
                return passes
        return None
    def neighbors(self, sender_name):
        if sender_name not in self.adj:
            return []
        return self.adj[sender_name]
    def total_weight(self, subset):
        if subset is None:
            subset = [p.name for p in self.players]

        total = 0
        for sender_name in subset:
            if sender_name not in self.adj:
                continue
            for p in self.adj[sender_name]:
                if p.receiver.name in subset:
                    total += p.nr_of_times
        return total
    def top_pairs(self, k=5):
        all_passes = []
        for plist in self.adj.values():
            all_passes.extend(plist)

        all_passes.sort(key=lambda p: p.nr_of_times, reverse=True)

        return all_passes[:k]

    def distribution_from(self, sender_name):
        if sender_name not in self.adj:
            return []

        counts = {}  # receiver_name → sum

        for p in self.adj[sender_name]:
            r = p.receiver.name
            counts[r] = counts.get(r, 0) + p.nr_of_times

        # maak lijst van tuples
        result = list(counts.items())

        # sorteer dalend
        result.sort(key=lambda x: x[1], reverse=True)

        return result











