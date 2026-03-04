import re
import json


def to_float(money_str):
    # "18 009,00" -> 18009.00
    return float(money_str.replace(" ", "").replace(",", "."))


def parse_receipt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()

    # 1) Date and time
    datetime_match = re.search(r"Время:\s+(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})", data)
    if datetime_match:
        date = datetime_match.group(1)
        time = datetime_match.group(2)
    else:
        date = "Unknown"
        time = "Unknown"

    # 2) Items
    # Match blocks:
    # 1.
    # Name
    # 2,000 x 154,00
    # 308,00
    item_pattern = re.findall(
        r"\d+\.\s*\n"              # item number like "1."
        r"(.+?)\n"                 # product name
        r"(\d+,\d+)\s*x\s*"        # quantity like "2,000"
        r"([\d\s]+,\d{2})\n"       # unit price like "1 200,00"
        r"([\d\s]+,\d{2})",        # total price like "308,00"
        data
    )

    items = []
    for m in item_pattern:
        name = m[0].strip()
        quantity = float(m[1].replace(",", "."))
        unit_price = to_float(m[2])
        total_price = to_float(m[3])

        items.append({
            "product": name,
            "quantity": quantity,
            "unit_price": unit_price,
            "total_price": total_price
        })

    # 3) Grand total (ИТОГО)
    total_match = re.search(r"ИТОГО:\s*\n([\d\s]+,\d{2})", data)
    if total_match:
        grand_total = to_float(total_match.group(1))
    else:
        grand_total = 0.0

    # 4) Payment method + amount
    payment_method = "Unknown"
    payment_amount = 0.0

    pay_card = re.search(r"Банковская карта:\s*\n([\d\s]+,\d{2})", data)
    pay_cash = re.search(r"Наличные:\s*\n([\d\s]+,\d{2})", data)

    if pay_card:
        payment_method = "Банковская карта"
        payment_amount = to_float(pay_card.group(1))
    elif pay_cash:
        payment_method = "Наличные"
        payment_amount = to_float(pay_cash.group(1))

    # 5) Calculate total from items
    total_calculated = 0.0
    for it in items:
        total_calculated += it["total_price"]

    # 6) Extract all prices 
    all_prices = re.findall(r"[\d\s]+,\d{2}", data)

    # 7) JSON result
    receipt_json = {
        "store": "EUROPHARMA",
        "date": date,
        "time": time,
        "items": items,
        "totals": {
            "total_items": len(items),
            "total_calculated": total_calculated,
            "grand_total": grand_total
        },
        "payment": {
            "method": payment_method,
            "amount": payment_amount
        },
        "all_prices_found": all_prices
    }

    return receipt_json


if __name__ == "__main__":
    result = parse_receipt("raw.txt")
    print(json.dumps(result, indent=4, ensure_ascii=False))