import random
class Batch:
    def __init__(self, quantity, cost_per_unit):
        self.quantity = quantity
        self.cost_per_unit = cost_per_unit
    def __str__(self):
        return f"Batch(quantity={self.quantity}, cost_per_unit={self.cost_per_unit})"
class Product:
    def __init__(self, product_name, holding_cost, stockout_penalty):
        self.product_name = product_name
        self.holding_cost = holding_cost
        self.stockout_penalty = stockout_penalty
        self.batches = []
    def add_batch(self, quantity, cost_per_unit):
        self.batches.append(Batch(quantity, cost_per_unit))
    def fulfill_demand(self, demand):
        while len(self.batches) > 0 and demand > 0:
            if self.batches[-1].quantity >= demand:
                self.batches[-1].quantity -= demand
                demand = 0
                if self.batches[-1].quantity == 0:
                    self.batches.pop(-1)
                    demand = 0
            else:
                demand -= self.batches[-1].quantity
                self.batches.pop()
        if demand > 0:
            return self.stockout_penalty * demand
        return 0
    def calculate_holding_cost(self):
        total = 0
        for batch in self.batches:
            total += self.holding_cost*batch.quantity
        return total
    def __str__(self):
        result = f"Product: [{self.product_name}]\n"
        for batch in self.batches:
            result += f"Batch: {batch}\n"
        return result
class Inventory_Manager:
    def __init__(self):
        self.products = {}
    def add_product(self, product_name, holding_cost, stockout_penalty):
        if product_name not in self.products:
            self.products[product_name] = Product(product_name, holding_cost, stockout_penalty)
        else:
            print(f"Product {product_name} already exists.")
    def restock_product(self, product_name, quantity, cost_per_unit):
        if product_name in self.products:
            self.products[product_name].add_batch(Batch(quantity, cost_per_unit))
        else:
            print(f"Product {product_name} not found.")
    def simulate_demand(self,min_demand, max_demand):
        demands = {}
        for product_name in self.products:
            demands[product_name] = random.randint(min_demand, max_demand)
        return demands
    def simulate_day(self, demands):
        total = 0
        for product_name, product in self.products.items():
            demand = demands[product_name]
            stockout = product.fulfill_demand(demand)
            holding = product.calculate_holding_cost()
            total += stockout + holding
        return total
    def save_to_csv(self, filename):
        with open(filename, "w") as file:
            file.write("product_name,quantity,cost_per_unit\n")
            for product_name, product in self.products.items():
                for batch in product.batches:
                    file.write(f"{product_name}, {batch.quantity}, {batch.cost_per_unit}\n")
    def load_from_csv(self, filename):
        with open(filename, "r") as file:
            next(file) #niet vergeten!!
            for line in file:
                parts = line.strip().split(",")
                product_name = parts[0].strip()
                batch_quantity = int(parts[1].strip())
                batch_cost_per_unit = float(parts[2].strip())
                if product_name not in self.products:
                    self.add_product(product_name, holding_cost=1, stockout_penalty=5)
                self.products[product_name].add_batch(batch_quantity, batch_cost_per_unit)

    def print_inventory(self):
        print("Current Inventory:")
        for product_name, product in self.products.items():
            print(f"Product: {product_name}")
            for batch in product.batches:
                print(f"  {batch}")
def main():
    inv = Inventory_Manager()

    # Voeg producten toe
    inv.add_product("Widget", holding_cost=1.5, stockout_penalty=5)
    inv.add_product("Gadget", holding_cost=2.0, stockout_penalty=7)

    # Restock
    inv.restock_product("Widget", 100, 2.5)
    inv.restock_product("Widget", 50, 2.0)

    inv.restock_product("Gadget", 70, 3.0)
    inv.restock_product("Gadget", 30, 2.8)

    # Vraag simuleren
    demand_dict = inv.simulate_demand(0, 20)

    # Dag simuleren
    total_cost = inv.simulate_day(demand_dict)
    print("Total cost:", total_cost)

    # Print inventaris
    inv.print_inventory()

    # CSV opslaan
    inv.save_to_csv("inventory.csv")











