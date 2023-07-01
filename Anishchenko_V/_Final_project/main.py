import tkinter as tk
import time
from PIL import Image, ImageTk
import util as ut


class Btn:
    """
    Class of buttons in the gamefield
    """

    def __init__(self, label, row, col):
        self.label = label
        self.id = row + col
        self.stateL = 1
        self.stateR = 1


# Create main window and window title
root = tk.Tk()
root.title("Minesweeper")

# Resize required images
images = ("imgs/0.png",
          "imgs/1.png",
          "imgs/2.png",
          "imgs/3.png",
          "imgs/4.png",
          "imgs/5.png",
          "imgs/6.png",
          "imgs/7.png",
          "imgs/8.png",
          "imgs/bomb.png",
          "imgs/flag.png",
          "imgs/none.png",
          "imgs/bomb_explod.png")
icons = []
for x in range(len(images)):
    image = Image.open(images[x])
    resize_image = image.resize((20, 20))
    icon = ImageTk.PhotoImage(resize_image)
    icons.append(icon)

emojis_raw_file = ("imgs/emo_smily.png",
                   "imgs/emo_sungl.png",
                   "imgs/emo_sad.png")
icons_emo = []
for emoji_raw in emojis_raw_file:
    emo = Image.open(emoji_raw)
    resize_emo = emo.resize((60, 60))
    icon_emo = ImageTk.PhotoImage(resize_emo)
    icons_emo.append(icon_emo)

# Create favicon
root.iconphoto(False, icons[9])

# Initialize variables
frames_list = []
level = tk.IntVar()
field_and_mines = ((9, 9, 10), (16, 16, 40), (16, 30, 99))
field_sizes = ('230x340', '400x510', '735x510')
grid = field_and_mines[0]
is_running = False
game_started = False


def setupField():
    """
    Function renders gamefield of required
    size and calls a function from util.py
    which initialized objects of class Cell
    """
    global grid
    global btns
    global lvl
    lvl = level.get()
    grid = field_and_mines[lvl]

    # Initialize objects of class Cell
    ut.populate(grid)

    # Set window size depending on selected
    # level of the game
    root.geometry(field_sizes[lvl])

    # Update various labels and list of buttons
    mines_counter.config(text=field_and_mines[lvl][2])
    stopwatch.config(text="000")
    btns = []

    # Remove any previously renderred frames
    if frames_list:
        for frame in frames_list:
            frame.destroy()

    # Create frames for each row on gamefield.
    # Create labels representing cells on gamefield,
    # bind to the lbels click- event listeners.
    for r in range(grid[0]):
        row = str(r) if r >= 10 else '0'+str(r)
        frame = tk.Frame(root)
        frame.pack()
        frames_list.append(frame)
        for c in range(grid[1]):
            col = str(c) if c >= 10 else '0'+str(c)
            label = tk.Label(
                frame, image=icons[11], height=20, width=20, bd=2, relief="raised")
            label.pack(side=tk.LEFT)
            label.bind("<Button-1>", leftClick)
            label.bind("<Button-3>", rightClick)
            btn = Btn(label, row, col)
            btns.append(btn)
    emo_icon.config(image=icons_emo[0])
    emo_icon.unbind("<Button-1>")


def restart(e):
    """
    Function performs role of event listener
    to restart game by a click on emoji icon
    """
    setupField()


def quickStart():
    """
    Function allows avoid annoying situations
    when on very first click of he game the player
    catches a mine.
    """
    setupField()
    to_call_from = ut.quickStart()
    revealCells(to_call_from)


def manageTime():
    """
    Function starts / stops stopwatch
    """
    global is_running
    global start_time
    if not is_running:
        is_running = True
        start_time = time.time()
        updateTime()
    else:
        is_running = False


def updateTime():
    """
    Function updates time on stopwatch
    """
    if is_running:
        elapsed_time = time.time() - start_time
        if elapsed_time > 999:
            stopwatch.config(text="999")
        elif elapsed_time < 9.5:
            placeholder = "00"
        elif elapsed_time < 99.5:
            placeholder = "0"
        elif elapsed_time < 999.5:
            placeholder = ""
        stopwatch.config(text="{}{:.0f}".format(
            placeholder, elapsed_time))
        stopwatch.after(50, updateTime)


def leftClick(e):
    """
    Function handles events on leftclick on the gamefield
    """
    caller = e.widget
    calledBtn = list(filter(lambda x: x.label == caller, btns))[0]

    # If game is won or lost, the leftclick should be disabled,
    # otherwise function 'revealCells' is called
    if calledBtn.stateL == 1:
        revealCells(calledBtn.id)


def revealCells(cellID):
    """
    Function handles events on leftclick on the gamefield
    and on pressing 'Quick Start' button
    """
    global game_started
    global is_running
    # Start stopwatch on the fery first click of a label
    # in the gamefield
    if not game_started:
        game_started = True
        manageTime()
        # Disable possibility to change game level whilst
        # the current gme sesson is in progress
        for r in radios:
            radios[r].config(state="disabled")
        qs.config(state="disabled")
    # Get from util.py data about which cells should be revealed
    click_result = ut.play(cellID)
    game_status = click_result[-1]
    labels_to_open = click_result[:-1]
    # Reveal cells on the gamefield based on data collected above,
    # disable click events for all revealed cells
    for x in labels_to_open:
        btn = list(filter(lambda i: i.id == x[0], btns))[0]
        btn.label.config(image=icons[x[1]])
        btn.label.config(relief="ridge")
        btn.stateL = 0
        btn.stateR = 0
    # End game if it is won or lost
    if game_status != 0:
        # Disable click events for all cells
        for btn in btns:
            btn.stateL = 0
            btn.stateR = 0
        # Enable possibility to select game level
        for r in radios:
            radios[r].config(state="normal")
        qs.config(state="normal")
        # Enable possibility to restart same level
        # by a click on emoji icon
        emo_icon.bind("<Button-1>", restart)
        # Update emoji icon depending on whether game is lost or won
        emo_icon.config(image=icons_emo[1]) if game_status == 1 else emo_icon.config(
            image=icons_emo[2])
        # Stop stopwatch
        is_running = False
        game_started = False


def rightClick(e):
    """
    Function handles events on rightclick on
    the gamefield
    """
    caller = e.widget
    calledBtn = list(filter(lambda i: i.label == caller, btns))[0]
    # If clicked label was not flagged or revealed previously
    if calledBtn.stateR == 1:
        ut.setFlag(calledBtn.id)
        # Display flag on the label
        caller.config(image=icons[10])
        # Toggle right click event listener indicator for the label,
        # disable left click event listener
        calledBtn.stateR *= -1
        calledBtn.stateL *= 0
        # Update quantity of remaining mines shown on the counter label
        counter_current = int(mines_counter.cget("text"))
        counter_new = max(counter_current - 1, 0)
        insertion = '0' + str(counter_new) if counter_new < 10 else counter_new
        mines_counter.config(text=insertion)

    # If clicked cell was flagged before (but is not yet revealed)
    elif calledBtn.stateR == -1:
        ut.unflag(calledBtn.id)
        # Remove flag from the label
        caller.config(image=icons[11])
        # Toggle right click event listener indicator for the label,
        # enable left click event listener
        calledBtn.stateR *= -1
        calledBtn.stateL *= 1
        # Update quantity of remaining mines shown on the counter label
        mines_total = field_and_mines[lvl][2]
        flags_remain = len(list(filter(lambda x: x.stateR == -1, btns)))
        if mines_total - flags_remain > 0:
            counter_current = int(mines_counter.cget("text"))
            counter_new = counter_current + 1
            insertion = '0' + \
                str(counter_new) if counter_new < 10 else counter_new
            mines_counter.config(text=insertion)


# Create frame to place radiobuttons for game level selection
frame_0 = tk.Frame(root)
frame_0.pack()

# Create a dict of radiobuttons
radios = {}
radio_text = ["easy", "normal", "expert"]
for r in range(3):
    r_btn = tk.Radiobutton(frame_0, text=radio_text[r], font=("Fixedsys"), variable=level,
                           value=r, state="normal", command=setupField)
    r_btn.pack(side=tk.LEFT)
    radios[r] = r_btn

# Create frame for Quick Start button
frame_qs = tk.Frame(root)
frame_qs.pack()

# Cretate Quick Start button
qs = tk.Button(frame_qs, text="Quick Start",
               font=("Fixedsys"), bd=2, relief="raised", command=quickStart)
qs.pack()

# Create frame to place mines counter, emoji and stopwatch
frame_m = tk.Frame(root, bd=1)
frame_m.pack()

# Create mines counter label
mines_counter = tk.Label(frame_m, text="00", width=3, font=(
    "Fixedsys", 20), fg="darkred", bd=3, relief="sunken", background="grey")
mines_counter.pack(side=tk.LEFT)

placeholder1 = tk.Label(frame_m, text="    ")
placeholder1.pack(side=tk.LEFT)

# Create emoji label
emo_icon = tk.Label(
    frame_m, image=icons_emo[0], height=60, width=60)
emo_icon.pack(side=tk.LEFT)

placeholder2 = tk.Label(frame_m, text="  ")
placeholder2.pack(side=tk.LEFT)

# Create stopwatch label
stopwatch = tk.Label(frame_m, text="000", font=(
    "Fixedsys", 20), fg="darkred", bd=3, relief="sunken", background="grey")
stopwatch.pack(side=tk.LEFT)

# Prepare field at easy level on the program start
setupField()

# Disallow the window resize
root.resizable(False, False)

# Run the main loop
root.mainloop()
