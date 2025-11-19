from operator import truediv


class BankLening:
    def __init__(self, bank_id, bedrag):
        self.bank_id = bank_id
        self.bedrag = bedrag

    def __eq__(self, other):
        return isinstance(other, BankLening) and \
               self.bank_id == other.bank_id and \
               self.bedrag == other.bedrag

    def __hash__(self):
        return hash((self.bank_id, self.bedrag))

class Bank:
    def __init__(self, id, naam, balans):
        self.id = id
        self.naam = naam
        self.balans = balans
        self.bankleningen = set()

    def toevoegen_lening(self, bank_id_ontlener, bedrag):
        if self.balans >= bedrag:
            self.balans -= bedrag
            self.bankleningen.add(BankLening( bank_id_ontlener, bedrag)) #banklening bij uitlener!
            return True
        else:
            return False
    def ontvangen_terugbetaling(self,bank_id_ontlener, bedrag):
        lening = None
        for l in self.bankleningen:
            if l.bank_id == bank_id_ontlener:
                lening = l
                break
        if bedrag > lening.bedrag:
            return False
        if lening is None:
            return False
        if bedrag == lening.bedrag:
            self.bankleningen.remove(lening)
            self.balans += bedrag
            return True
        lening.bedrag -= bedrag
        self.balans += bedrag
        return True
    def __eq__(self, other):
        return isinstance(other, Bank) and self.id == other.id
    def __hash__(self):
        return hash(self.id)
    def __str__(self):
        totaal = sum(l.bedrag for l in self.bankleningen)
        return f"{self.naam} - {self.balans} - {len(self.bankleningen)} - {totaal}"

def parse_bank(s):
    parts = s.split(";")

    # Basisinfo
    id = parts[0]
    naam = parts[1]
    balans = float(parts[2])
    aantal = int(parts[3])

    # Nieuwe bank aanmaken
    bank = Bank(id, naam, balans)

    # Leningen lezen
    index = 4
    for i in range(aantal):
        bank_id_ontlener = parts[index]
        bedrag = float(parts[index + 1])

        bank.bankleningen.add(BankLening(bank_id_ontlener, bedrag))

        index += 2  # volgende lening


class BankNetwerk:
    def __init__(self, bestandsnaam):
        self.banken = {}

        with open(bestandsnaam, "r") as f: #constructor
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                bank = Bank.parse_bank(line)
                self.banken[bank.id] = bank
    def toevoegen_bank(self, bank_id, naam, balans):
        self.banken[bank_id] = Bank(id, naam, balans)
    def aanpassenBalansBank(self, bank_id, bedrag):
        self.banken[bank_id].balans += bedrag #bank = self.banken[bank_id]; bank.balans += bedrag
    def aangaan_banklening(self, bank_id_uitlener, bank_id_ontlener, bedrag):
        uitlener = self.banken[bank_id_uitlener]
        ontlener = self.banken[bank_id_ontlener]

        if uitlener.toevoegen_lening(ontlener, bedrag):
            ontlener.balans += bedrag
            return True
        return False
    def terugBetalenLening(self, bank_id_uitlener, bank_id_ontlener, bedrag):
        if self.banken[bank_id_ontlener].balans < bedrag:
            return False
        elif self.banken[bank_id_uitlener].ontvangen_terugbetaling(bank_id_ontlener, bedrag):
            self.banken[bank_id_ontlener].balans -= bedrag
            return True
        return False











