"""CLI CRUD miniature: track changes to this script with Git."""
INVENTORY={f"P{i:03}":{"name":f"Item {i}","stock":i*2} for i in range(1,13)}
def create(items,key,name,stock):
    if key in items: raise ValueError("Duplicate id")
    if not isinstance(stock,int) or stock<0: raise ValueError("Invalid stock")
    items[key]={"name":name,"stock":stock}
def update(items,key,stock):
    if key not in items: raise KeyError(key)
    if not isinstance(stock,int) or stock<0: raise ValueError("Invalid stock")
    items[key]["stock"]=stock
def delete(items,key):
    if key not in items: raise KeyError(key)
    del items[key]
def main():
    items={k:dict(v) for k,v in INVENTORY.items()}
    assert len(items)==12
    create(items,"P013","Item 13",5)
    update(items,"P013",7)
    delete(items,"P001")
    assert len(items)==12
    for key in sorted(items): print(key,items[key])
    print("Use git status, git diff and at least three commits as part of the lab.")
if __name__ == "__main__":
    main()
