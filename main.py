import pyvrp
import json

from models import Scenario, Depot, Weights, Order

# Парсинг инпута в модели для работы
def parse(path: str) -> Scenario:
    with open(path) as f:
        raw = json.load(f)

    depot = Depot(**raw["depot"])
    weights = Weights(**raw["weights"])

    orders = []
    for i in range(len(raw["orders"])):
        orders.append(Order(**raw["orders"][i]))

    return Scenario(
        depot=depot,
        weights=weights,
        orders=orders,
        vehicle_capacity=raw["vehicle_capacity"],
        vehicle_speed=raw["vehicle_speed"],
        loader_speed=raw["loader_speed"],
        vehicle_shift_size=raw["vehicle_shift_size"],
        loader_shift_size=raw["loader_shift_size"]
    )

if __name__ == "__main__":
    scenario = parse("data/input.json")

    print(scenario)