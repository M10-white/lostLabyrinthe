import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class MazeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu de Labyrinthe")

        self.cell_size = 80  # Taille de chaque case (80x80 pixels)
        self.canvas = tk.Canvas(self.root, width=800, height=800, bg='black')  # Fond noir
        self.canvas.pack()

        self.load_maze()
        self.player_pos = [2, 1]  # Position initiale du joueur
        self.light_radius = 2  # Rayon de la lumière (en cellules)
        
        # Charger les images des sprites
        self.sprites = {
            'up': Image.open('assets/player_up.png').resize((self.cell_size, self.cell_size), Image.LANCZOS),
            'down': Image.open('assets/player_down.png').resize((self.cell_size, self.cell_size), Image.LANCZOS),
            'left': Image.open('assets/player_left.png').resize((self.cell_size, self.cell_size), Image.LANCZOS),
            'right': Image.open('assets/player_right.png').resize((self.cell_size, self.cell_size), Image.LANCZOS),
        }
        self.player_photo = ImageTk.PhotoImage(self.sprites['down'])  # Par défaut, l'image du joueur fait face vers le bas

        self.draw_maze()  # Dessiner le labyrinthe initialement
        self.draw_player()  # Dessiner le joueur initialement
        self.reveal_maze()  # Révéler le labyrinthe initialement

        self.root.bind("<Key>", self.on_key_press)

    def load_maze(self):
        with open('maze.txt', 'r') as f:
            self.maze = [list(line.strip()) for line in f]

    def draw_maze(self):
        # Initialement, ne dessine pas les murs
        pass

    def reveal_maze(self):
        # Effacer les murs précédemment dessinés
        self.canvas.delete('maze')

        # Révéler uniquement les murs qui touchent le joueur
        for y in range(len(self.maze)):
            for x in range(len(self.maze[0])):
                if self.maze[y][x] == '#':  # Vérifie si c'est un mur
                    if self.is_wall_adjacent_to_light(x, y):
                        x1 = x * self.cell_size
                        y1 = y * self.cell_size
                        x2 = x1 + self.cell_size
                        y2 = y1 + self.cell_size
                        # Dessiner les murs uniquement s'ils sont adjacents au joueur
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='white', tags='maze')

    def draw_player(self):
        # Effacer le joueur précédemment dessiné pour éviter les doublons
        self.canvas.delete('player')
        
        # Dessiner le joueur centré dans sa case
        x, y = self.player_pos
        self.canvas.create_image((y * self.cell_size) + self.cell_size // 2, (x * self.cell_size) + self.cell_size // 2, image=self.player_photo, tags='player')

    def on_key_press(self, event):
        # Vérifier si le mouvement est valide avant de mettre à jour la position
        new_pos = self.player_pos.copy()  # Copie de la position actuelle

        # Gérer le mouvement selon la touche pressée
        if event.keysym == 'Up':
            new_pos[0] -= 1
            self.player_photo = ImageTk.PhotoImage(self.sprites['up'])
        elif event.keysym == 'Down':
            new_pos[0] += 1
            self.player_photo = ImageTk.PhotoImage(self.sprites['down'])
        elif event.keysym == 'Left':
            new_pos[1] -= 1
            self.player_photo = ImageTk.PhotoImage(self.sprites['left'])
        elif event.keysym == 'Right':
            new_pos[1] += 1
            self.player_photo = ImageTk.PhotoImage(self.sprites['right'])
        else:
            # Si ce n'est pas une touche de direction, ne pas changer la position
            self.draw_player()  # Redessiner le joueur pour éviter qu'il disparaisse
            return

        # Vérifier si le mouvement est valide avant de mettre à jour la position
        if self.is_move_valid(new_pos):
            self.player_pos = new_pos

        self.reveal_maze()  # Révèle le labyrinthe dans la zone de lumière
        self.draw_player()  # Redessiner le joueur
        self.check_win()

    def is_move_valid(self, new_pos):
        if (0 <= new_pos[0] < len(self.maze)) and (0 <= new_pos[1] < len(self.maze[0])):  # Vérifie que la nouvelle position est dans les limites
            return self.maze[new_pos[0]][new_pos[1]] != '#'
        return False

    def is_wall_adjacent_to_light(self, x, y):
        # Vérifie si un mur est adjacent à la lumière
        player_x, player_y = self.player_pos

        # Vérifie les cases autour du joueur dans le rayon de lumière
        for dx in range(-self.light_radius, self.light_radius + 1):
            for dy in range(-self.light_radius, self.light_radius + 1):
                if abs(dx) + abs(dy) <= self.light_radius:  # Vérifie si le mur est dans le rayon de lumière
                    if (player_x + dx == y) and (player_y + dy == x):  # Si le mur est adjacent au joueur
                        return True
        return False

    def check_win(self):
        if self.maze[self.player_pos[0]][self.player_pos[1]] == 'S':  # Sortie
            messagebox.showinfo("Gagné !", "Vous avez atteint la sortie !")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = MazeGame(root)
    root.mainloop()
