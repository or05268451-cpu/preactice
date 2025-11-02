def main():
    records = []
    
    with open(r"C:\Users\donle\Desktop\python.py\scores.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            records.append(parts)
            print(parts)

        for record in records:
            name = record[0].strip()
            game = record[1].strip()
            score = record[2].strip()
            print(f"Player: {name} | Game: {game} | Score: {score}")

        game_choice = input("Enter the game you want to check: ").strip()

        print(f"n\nPlayers who play {game_choice}:")
        for record in records:
            if record[1].strip().lower() == game_choice.lower():
                print(f"{record[0]} - Score: {record[2]}")


main()
