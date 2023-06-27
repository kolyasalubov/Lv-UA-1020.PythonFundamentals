import random


class Cell:
    """ 
    Class of cells in the gamefield
    """

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.rowID = str(self.row) if self.row >= 10 else '0' + str(self.row)
        self.colID = str(self.col) if self.col >= 10 else '0' + str(self.col)
        self.fullID = self.rowID + self.colID
        self.neighbs = []
        self.mines_around = None
        self.mined = False
        self.flagged = False


def populate(grid):
    """
    Function populates cells, randomly
    assignes mines amongst cells and 
    for each unmined cell records number of 
    mines around it.
    """

    # Populate cells
    global rows, cols
    global mines_total
    global cells
    cells = []
    rows, cols = grid[0], grid[1]
    mines_total = grid[2]
    for r in range(rows):
        for c in range(cols):
            cell = Cell(r, c)
            cells.append(cell)

    # For each cell, define list of 'neighbours'
    for cell in cells:
        r, c = cell.row, cell.col
        neib_inds = [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1),
                     (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]
        for x in range(len(neib_inds)):
            if 0 <= neib_inds[x][0] < rows and 0 <= neib_inds[x][1] < cols:
                neib = [obj for obj in cells if obj.row == neib_inds[x]
                        [0] and obj.col == neib_inds[x][1]][0]
                cell.neighbs.append(neib)

    # Randomly assign mineas amongst cells
    mines_left = mines_total
    while mines_left > 0:
        clean_cells = [x for x in cells if not x.mined]
        clean_cells[random.randint(0, len(clean_cells) - 1)].mined = True
        mines_left -= 1

    # Set attribute "mines around" for each unmined cell
    for cell in cells:
        if cell.mined:
            continue
        else:
            cell.mines_around = sum(x.mined for x in cell.neighbs)


def setFlag(cellID):
    """
    Function marks a cell as 'flagged' if respective 
    widget is clicked on the gamefield by rightclick
    """
    flagged_cell = [cell for cell in cells if cell.fullID == cellID][0]
    flagged_cell.flagged = True


def unflag(cellID):
    """
    Function reverses 'flagged' attribute for rightclicked cell
    which was previously marked as 'flagged'
    """
    flagged_cell = [cell for cell in cells if cell.fullID == cellID][0]
    flagged_cell.flagged = False


def play(cellID):
    """ 
    This function is the main game engine.
    It is called from main.py when player leftclicks on a cell 
    in the GUI.
    """
    game_status = 0
    # find object containing info aout clicked cell
    clicked_cell = [cell for cell in cells if cell.fullID == cellID][0]
    # If player clicks on cell which has mine, return set of attributes
    # to reveal all mines on the field and end game (game is lost)
    if clicked_cell.mined:
        all_mines = [(x.fullID, 9)
                     for x in cells if x.mined and x != clicked_cell]

        all_mines.append((cellID, 12))
        game_status = -1
        all_mines.append(game_status)
        for cell in cells:
            del cell
        return all_mines
    else:
        # Start collection of cels to open on the gamefield in GUI.
        # First on the list is the clicked cell.
        cells_to_reveal = [clicked_cell]

        # If player opens cell which has NO mines nearby,
        # add to the list (i) all neighbouring cells,
        # (ii) all neighbours of neighbours etc. which have
        #  no mines around, and (iii) neighbours of cells mentioned
        # in section (ii) above which have mined neighbours
        if not clicked_cell.mines_around:
            # step(i) per above description
            for i in clicked_cell.neighbs:
                if i.mines_around == False and i.flagged == False:
                    if i not in cells_to_reveal:
                        cells_to_reveal.append(i)
            # step(ii)
            while True:
                takeout = []
                for i in cells_to_reveal:
                    for j in i.neighbs:
                        if j.mines_around == False and j.flagged == False:
                            if j not in cells_to_reveal:
                                takeout.append(j)
                if not takeout:
                    break
                for k in takeout:
                    if k not in cells_to_reveal:
                        cells_to_reveal.append(k)
            # step (iii)
            takeout_2 = []
            for j in cells_to_reveal:
                if len(j.neighbs) > 0:
                    for w in j.neighbs:
                        if w.flagged == False and w.mined == False:
                            takeout_2.append(w)
            for q in takeout_2:
                if q not in cells_to_reveal:
                    cells_to_reveal.append(q)

        # I. Create list of IDs of cells - this has to be sent to main.py
        #    (can not send the objects themselves)
        # II. Delete respective cells from population
        items_to_reveal = []
        for i in cells_to_reveal:
            item = (i.fullID, i.mines_around)
            items_to_reveal.append(item)
            for j in i.neighbs:
                j.neighbs.remove(i)
            cells.remove(i)
            del i

        # Check if the game is won. If so, delete of cell objects
        if sum(cell.mined for cell in cells) == len(cells):
            game_status = 1
            for cell in cells:
                del cell
        items_to_reveal.append(game_status)
        return items_to_reveal


def quickStart():
    """
    Function randomly selects a cell which has no mines around
    and returns result to main.py for the purposes of Quick Start
    scenario.
    """
    clean_cells = [x for x in cells if not x.mines_around]
    clean_cell = random.choice(clean_cells)
    clean_ID = clean_cell.fullID
    return clean_ID
