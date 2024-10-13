import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class MazeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu de Labyrinthe")

        self.cell_size = 80  # Taille de chaque case (80x80 pixels)
        self.canvas_width = 800
        self.canvas_height = 800
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg='black')  # Fond noir
        self.canvas.pack()

        self.level = 1  # Niveau de départ
        self.player_pos = [1, 1]  # Position initiale du joueur
        self.light_radius = 1  # Rayon de la lumière (en cellules)
        self.score = 1  # Initialiser le score

        # Charger les images des sprites
        self.sprites = {
            'up': Image.open('assets/player_up.png').resize((self.cell_size, self.cell_size), Image.LANCZOS),
            'down': Image.open('assets/player_down.png').resize((self.cell_size, self.cell_size), Image.LANCZOS),
            'left': Image.open('assets/player_left.png').resize((self.cell_size, self.cell_size), Image.LANCZOS),
            'right': Image.open('assets/player_right.png').resize((self.cell_size, self.cell_size), Image.LANCZOS),
        }
        self.player_photo = ImageTk.PhotoImage(self.sprites['down'])  # Par défaut, l'image du joueur fait face vers le bas

        # Ajouter une étiquette pour le score
        self.score_label = self.canvas.create_text(10, 10, anchor='nw', fill='red', font=('Helvetica', 16), text=f'Niveau : {self.score}')

        # Charger l'image de la porte
        self.door_image = ImageTk.PhotoImage(Image.open('assets/door.png').resize((self.cell_size, self.cell_size), Image.LANCZOS))

        self.generate_maze(self.level)  # Générer un labyrinthe pour le niveau 1
        self.reveal_maze()  # Révéler le labyrinthe initialement
        self.draw_player()  # Dessiner le joueur initialement
        
        self.root.bind("<Key>", self.on_key_press)

    def generate_maze(self, level):
        # Générer un labyrinthe aléatoire avec une difficulté croissante
        width, height = (self.canvas_width // self.cell_size), (self.canvas_height // self.cell_size)  # Adapter la taille du labyrinthe
        self.maze = [['#'] * width for _ in range(height)]
        
        # Algorithme de génération de labyrinthe (Depth-First Search)
        def carve_passages_from(cx, cy, grid):
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = cx + dx * 2, cy + dy * 2
                if 1 <= nx < width-1 and 1 <= ny < height-1 and grid[ny][nx] == '#':
                    grid[cy + dy][cx + dx] = ' '
                    grid[ny][nx] = ' '
                    carve_passages_from(nx, ny, grid)

        # Commence à la position [1,1]
        self.maze[1][1] = ' '
        carve_passages_from(1, 1, self.maze)

        # Placer la sortie aléatoirement
        while True:
            self.exit_pos = [random.randint(1, height-2), random.randint(1, width-2)]
            if self.maze[self.exit_pos[0]][self.exit_pos[1]] == ' ' and self.exit_pos != [1, 1]:
                if not self.is_intersection(self.exit_pos):  # Vérifie que ce n'est pas une intersection
                    self.maze[self.exit_pos[0]][self.exit_pos[1]] = 'S'
                    break

    def is_intersection(self, pos):
        # Vérifie si la position est une intersection
        x, y = pos
        count = 0
        if self.maze[x][y-1] == ' ': count += 1  # Haut
        if self.maze[x][y+1] == ' ': count += 1  # Bas
        if self.maze[x-1][y] == ' ': count += 1  # Gauche
        if self.maze[x+1][y] == ' ': count += 1  # Droite
        return count > 1  # Plus d'un chemin => intersection

    def reveal_maze(self):
        # Effacer les murs et la porte précédemment dessinés
        self.canvas.delete('maze')
        self.canvas.delete('door')

        # Révéler uniquement les murs visibles
        for y in range(len(self.maze)):
            for x in range(len(self.maze[0])):
                if self.maze[y][x] == '#':
                    # Vérifie si le mur est adjacent à la lumière
                    if self.is_adjacent_to_light(x, y):
                        x1 = x * self.cell_size
                        y1 = y * self.cell_size
                        x2 = x1 + self.cell_size
                        y2 = y1 + self.cell_size
                        # Dessiner les murs uniquement s'ils sont adjacents au joueur
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='white', tags='maze')
                elif self.maze[y][x] == 'S':
                    # Vérifie si la sortie est éclairée
                    if self.is_adjacent_to_light(x, y):
                        self.canvas.create_image((x * self.cell_size) + self.cell_size // 2,
                                                  (y * self.cell_size) + self.cell_size // 2,
                                                  image=self.door_image, tags='door')
        
        # S'assurer que le score est au-dessus de tous les autres éléments
        self.canvas.tag_raise(self.score_label)  # Place le score au-dessus des murs et de la porte

    def update_score(self):
        # Mettre à jour l'affichage du score
        self.canvas.itemconfig(self.score_label, text=f'Niveau : {self.score}')

    def is_adjacent_to_light(self, x, y):
        # Vérifie si la cellule est à l'intérieur du rayon de lumière
        player_x, player_y = self.player_pos

        dx = abs(player_x - y)
        dy = abs(player_y - x)

        return (dx <= self.light_radius and dy <= self.light_radius) and (dx + dy != 0)

    def draw_player(self):
        # Effacer le joueur précédemment dessiné pour éviter les doublons
        self.canvas.delete('player')

        # Dessiner le joueur centré dans sa case
        x, y = self.player_pos
        self.canvas.create_image((y * self.cell_size) + self.cell_size // 2, (x * self.cell_size) + self.cell_size // 2, image=self.player_photo, tags='player')

    def on_key_press(self, event):
        new_pos = self.player_pos.copy()

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

        # Vérifier si le nouveau mouvement est possible
        if self.is_move_valid(new_pos):
            self.player_pos = new_pos
            self.reveal_maze()  # Révéler le labyrinthe à chaque mouvement
            self.draw_player()  # Dessiner le joueur à sa nouvelle position

            # Vérifier si le joueur a atteint la sortie
            if self.player_pos == self.exit_pos:
                self.score += 1  # Augmenter le score de 1 à chaque sortie
                self.update_score()
                messagebox.showinfo("Victoire!", "Vous avez trouvé la sortie!")
                self.level += 1  # Passer au niveau suivant
                self.generate_maze(self.level)  # Générer un nouveau labyrinthe
                self.player_pos = [1, 1]  # Réinitialiser la position du joueur
                self.reveal_maze()  # Révéler le nouveau labyrinthe
                self.draw_player()  # Dessiner le joueur dans le nouveau labyrinthe
        else:
            # Si le mouvement est invalide, redessiner le joueur à sa position actuelle
            self.draw_player()  # Redessiner le joueur à sa position actuelle

    def is_move_valid(self, pos):
        # Vérifier si le mouvement est valide
        x, y = pos
        return 0 <= x < len(self.maze) and 0 <= y < len(self.maze[0]) and self.maze[x][y] != '#'

if __name__ == "__main__":
    root = tk.Tk()
    game = MazeGame(root)
    root.mainloop()
