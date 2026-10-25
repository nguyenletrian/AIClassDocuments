"""12 synthetic products: list/dictionary/set and CRUD."""
PRODUCTS = [{"id":f"P{i:03}", "name":f"Item {i}","category":("Stationery","Electronics","Household")[i%3],"price":20+i*15,"stock":i} for i in range(1,13)]
def find(items, key):
    return next((x for x in items if x["id"]==key),None)
def add(items, item):
    if find(items,item["id"]): raise ValueError("Duplicate id")
    if item["price"]<0 or item["stock"]<0: raise ValueError("Negative value")
    items.append(dict(item))
def main():
    items = [dict(x) for x in PRODUCTS]
    assert len(items)==12
    print("Categories:",sorted({x["category"] for x in items}))
    add(items, {"id":"P013","name":"Item 13","category":"Stationery","price":60,"stock":3})
    item=find(items,"P013")
    item["stock"]=7
    print("Updated:",item)
    items[:]=[x for x in items if x["id"]!="P001"]
    assert len(items)==12
if __name__ == "__main__":
    main()
