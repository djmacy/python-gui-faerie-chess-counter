import tkinter as tk
from tkinter import ttk

def calculate_points():
    total_points = (pawn_var.get() or 0) * 1 + (peasant_var.get() or 0) * 2 + (soldier_var.get() or 0) * 3 + \
                   (rook_var.get() or 0) * 9 + (knight_var.get() or 0) * 4 + \
                   (bishop_var.get() or 0) * 6 + (catapult_var.get() or 0) * 3 + \
                   (chamberlain_var.get() or 0) * 6 + (courtesan_var.get() or 0) * 6 + \
                   (herald_var.get() or 0) * 6 + (inquisitor_var.get() or 0) * 8 + \
                   (lancer_var.get() or 0) * 5 + (pontiff_var.get() or 0) * 8 + \
                   (thief_var.get() or 0) * 5 + (tower_var.get() or 0) * 10 + \
                   (queen_var.get() or 0) * 12 + (king_var.get() or 0) * 0 + \
                   (jester_var.get() or 0) * 12 + (regent_var.get() or 0) * 15

    selected_difficulty = difficulty_var.get()

    difficulties = {
        "Beginner": 65,
        "Intermediate": 70,
        "Advanced": 75
    }

    remaining_points = difficulties[selected_difficulty] - total_points

    result_label.config(text=f"Total points: {total_points}\nRemaining points: {remaining_points}")

def update_rank1_pieces(*args):
    total_rank1_pieces = pawn_var.get() + peasant_var.get() + soldier_var.get()
    rank1_label.config(text="Rank I Pieces Left: " + str(8 - total_rank1_pieces))


def update_rank2_pieces(*args):
    total_rank2_pieces = (rook_var.get() + knight_var.get() + bishop_var.get() + catapult_var.get() + chamberlain_var.get()
    + courtesan_var.get() + herald_var.get() + inquisitor_var.get() + lancer_var.get() + pontiff_var.get() + thief_var.get()
    + tower_var.get())
    rank2_label.config(text="Rank I Pieces Left: " + str(6 - total_rank2_pieces))


root = tk.Tk()
root.title("Faerie Chess Counter")

piece_label = tk.Label(root, text="Rank I selection:")
piece_label.grid(row=0, column=0, sticky="w")

pawn_label = tk.Label(root, text="Pawns:")
pawn_label.grid(row=1, column=0, sticky="w")
pawn_var = tk.IntVar(root)
pawn_dropdown = ttk.Combobox(root, textvariable=pawn_var, values=[4, 5, 6, 7, 8], state="readonly")
pawn_dropdown.set(4)
pawn_dropdown.grid(row=1, column=1)

peasant_label = tk.Label(root, text="Peasants:")
peasant_label.grid(row=2, column=0, sticky="w")
peasant_var = tk.IntVar(root)
peasant_dropdown = ttk.Combobox(root, textvariable=peasant_var, values=list(range(3)), state="readonly")
peasant_dropdown.grid(row=2, column=1)

soldier_label = tk.Label(root, text="Soldiers:")
soldier_label.grid(row=3, column=0, sticky="w")
soldier_var = tk.IntVar(root)
soldier_dropdown = ttk.Combobox(root, textvariable=soldier_var, values=list(range(3)), state="readonly")
soldier_dropdown.grid(row=3, column=1)

rank1_label = tk.Label(root, text="Rank I Pieces Left: 4")
rank1_label.grid(row=4, column=0, sticky="w")

#dynamically updates how many pieces the user has left to select from in rank I
pawn_var.trace_add("write", update_rank1_pieces)
peasant_var.trace_add("write", update_rank1_pieces)
soldier_var.trace_add("write", update_rank1_pieces)

piece_label = tk.Label(root, text="Rank II selection:")
piece_label.grid(row=0, column=2, sticky="w")

rook_label = tk.Label(root, text="Rooks:")
rook_label.grid(row=1, column=2, sticky="w")
rook_var = tk.IntVar(root)
rook_dropdown = ttk.Combobox(root, textvariable=rook_var, values=list(range(3)),state="readonly")
rook_dropdown.grid(row=1, column=3)

knight_label = tk.Label(root, text="Knights:")
knight_label.grid(row=2, column=2, sticky="w")
knight_var = tk.IntVar(root)
knight_dropdown = ttk.Combobox(root, textvariable=knight_var, values=list(range(3)),state="readonly")
knight_dropdown.grid(row=2, column=3)

bishop_label = tk.Label(root, text="Bishops:")
bishop_label.grid(row=3, column=2, sticky="w")
bishop_var = tk.IntVar(root)
bishop_dropdown = ttk.Combobox(root, textvariable=bishop_var, values=list(range(3)),state="readonly")
bishop_dropdown.grid(row=3, column=3)

catapult_label = tk.Label(root, text="Catapults:")
catapult_label.grid(row=4, column=2, sticky="w")
catapult_var = tk.IntVar(root)
catapult_dropdown = ttk.Combobox(root, textvariable=catapult_var, values=list(range(2)),state="readonly")
catapult_dropdown.grid(row=4, column=3)

chamberlain_label = tk.Label(root, text="Chamberlain:")
chamberlain_label.grid(row=5, column=2, sticky="w")
chamberlain_var = tk.IntVar(root)
chamberlain_dropdown = ttk.Combobox(root, textvariable=chamberlain_var, values=list(range(2)),state="readonly")
chamberlain_dropdown.grid(row=5, column=3)

courtesan_label = tk.Label(root, text="Courtesan:")
courtesan_label.grid(row=6, column=2, sticky="w")
courtesan_var = tk.IntVar(root)
courtesan_dropdown = ttk.Combobox(root, textvariable=courtesan_var, values=list(range(2)),state="readonly")
courtesan_dropdown.grid(row=6, column=3)

herald_label = tk.Label(root, text="Herald:")
herald_label.grid(row=7, column=2, sticky="w")
herald_var = tk.IntVar(root)
herald_dropdown = ttk.Combobox(root, textvariable=herald_var, values=list(range(2)),state="readonly")
herald_dropdown.grid(row=7, column=3)

inquisitor_label = tk.Label(root, text="Inquisitor:")
inquisitor_label.grid(row=8, column=2, sticky="w")
inquisitor_var = tk.IntVar(root)
inquisitor_dropdown = ttk.Combobox(root, textvariable=inquisitor_var, values=list(range(2)),state="readonly")
inquisitor_dropdown.grid(row=8, column=3)

lancer_label = tk.Label(root, text="Lancer:")
lancer_label.grid(row=9, column=2, sticky="w")
lancer_var = tk.IntVar(root)
lancer_dropdown = ttk.Combobox(root, textvariable=lancer_var, values=list(range(2)),state="readonly")
lancer_dropdown.grid(row=9, column=3)

pontiff_label = tk.Label(root, text="Pontiff:")
pontiff_label.grid(row=10, column=2, sticky="w")
pontiff_var = tk.IntVar(root)
pontiff_dropdown = ttk.Combobox(root, textvariable=pontiff_var, values=list(range(2)),state="readonly")
pontiff_dropdown.grid(row=10, column=3)

thief_label = tk.Label(root, text="Thief:")
thief_label.grid(row=11, column=2, sticky="w")
thief_var = tk.IntVar(root)
thief_dropdown = ttk.Combobox(root, textvariable=thief_var, values=list(range(2)),state="readonly")
thief_dropdown.grid(row=11, column=3)

tower_label = tk.Label(root, text="Tower:")
tower_label.grid(row=12, column=2, sticky="w")
tower_var = tk.IntVar(root)
tower_dropdown = ttk.Combobox(root, textvariable=tower_var, values=list(range(2)),state="readonly")
tower_dropdown.grid(row=12, column=3)

rank2_label = tk.Label(root, text="Rank I Pieces Left: 6")
rank2_label.grid(row=13, column=2, sticky="w")

#dynamically updates how many pieces the user has left to select from in rank II
rook_var.trace_add("write", update_rank2_pieces)
knight_var.trace_add("write", update_rank2_pieces)
bishop_var.trace_add("write", update_rank2_pieces)
catapult_var.trace_add("write", update_rank2_pieces)
chamberlain_var.trace_add("write", update_rank2_pieces)
courtesan_var.trace_add("write", update_rank2_pieces)
herald_var.trace_add("write", update_rank2_pieces)
inquisitor_var.trace_add("write", update_rank2_pieces)
lancer_var.trace_add("write", update_rank2_pieces)
pontiff_var.trace_add("write", update_rank2_pieces)
thief_var.trace_add("write", update_rank2_pieces)
tower_var.trace_add("write", update_rank2_pieces)

piece_label = tk.Label(root, text="Rank III selection:")
piece_label.grid(row=0, column=4, sticky="w")

queen_label = tk.Label(root, text="Queen:")
queen_label.grid(row=1, column=4, sticky="w")
queen_var = tk.IntVar(root)
queen_dropdown = ttk.Combobox(root, textvariable=queen_var, values=list(range(2)),state="readonly")
queen_dropdown.grid(row=1, column=5)

king_label = tk.Label(root, text="King:")
king_label.grid(row=2, column=4, sticky="w")
king_var = tk.IntVar(root)
king_dropdown = ttk.Combobox(root, textvariable=king_var, values=list(range(2)),state="readonly")
king_dropdown.grid(row=2, column=5)

jester_label = tk.Label(root, text="Jester:")
jester_label.grid(row=3, column=4, sticky="w")
jester_var = tk.IntVar(root)
jester_dropdown = ttk.Combobox(root, textvariable=jester_var, values=list(range(2)),state="readonly")
jester_dropdown.grid(row=3, column=5)

regent_label = tk.Label(root, text="Regent:")
regent_label.grid(row=4, column=4, sticky="w")
regent_var = tk.IntVar(root)
regent_dropdown = ttk.Combobox(root, textvariable=regent_var, values=list(range(2)), state="readonly")
regent_dropdown.grid(row=4, column=5)

difficulty_label = tk.Label(root, text="Difficulty:")
difficulty_label.grid(rows = 15, column=0, sticky="w")
difficulty_var = tk.StringVar(root)
difficulty_dropdown = ttk.Combobox(root, textvariable=difficulty_var, values=["Beginner", "Intermediate", "Advanced"], state="readonly")
difficulty_dropdown.grid(row= 15, columns=1)

difficulty_dropdown.defaultvalue = "Easy"
difficulty_var.set("Beginner")

calculate_button = tk.Button(root, text="Calculate Points", command=calculate_points)
calculate_button.grid(row=16, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=17, column=0, columnspan=2)

root.mainloop()
