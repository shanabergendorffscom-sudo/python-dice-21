from game_classes import Game

def main():
    game = Game()
    print("Välkommen till Tärningsspelet 21!")

    while True:
        game.player.reset()
        game.dealer.reset()

        # Spelarens tur
        while True:
            print(f"Din poäng: {game.player.total}")
            choice = input("Vill du [r]ulla eller [s]tanna? ").strip().lower()
            if choice == "r":
                roll = game.player.roll()
                print(f"Du slog {roll}, total: {game.player.total}")
                if game.player.busted:
                    print("Du gick över 21! Du förlorar.")
                    game.scores["Dealer"] += 1
                    break
            elif choice == "s":
                break
            else:
                print("Ogiltigt val. Välj 'r' eller 's'.")

        # Dealerns tur om spelaren inte bustat
        if not game.player.busted:
            dealer_total = game.play_dealer_turn()
            print(f"Dealerns total: {dealer_total}")
            if game.dealer.busted:
                print("Dealern gick över 21! Du vinner.")
                game.scores["Player"] += 1
            else:
                if dealer_total > game.player.total:
                    print("Dealern vinner.")
                    game.scores["Dealer"] += 1
                elif dealer_total < game.player.total:
                    print("Du vinner!")
                    game.scores["Player"] += 1
                else:
                    print("Oavgjort.")

        print(f"Ställning: Spelare {game.scores['Player']} - Dealer {game.scores['Dealer']}")
        game.save_scores()

        again = input("Vill du spela igen? (j/n): ").strip().lower()
        if again != "j":
            print("Tack för att du spelade!")
            break

if __name__ == "__main__":
    main()