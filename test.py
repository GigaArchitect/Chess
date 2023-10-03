from subprocess import check_output
Engine_Path = str()

try: 
    temp = check_output("which stockfish", shell=True)
    Engine_Path = temp.decode("utf-8").replace("\n", "")
except:
    print("Install StockFish First")

print(Engine_Path)
