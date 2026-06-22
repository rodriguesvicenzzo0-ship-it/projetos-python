print("--- MUSIC PLAYER ---")
playlist = ["musica 1-rock", "musica 2-pop", "musica 3-RAP"]
atual = int(input("Digite o número da música que deseja ouvir (1, 2 ou 3): "))
print(f"Reproduzindo: {playlist[atual]}")
print(f"musica anterior: {playlist[atual-1]}")
print("=" * 40)