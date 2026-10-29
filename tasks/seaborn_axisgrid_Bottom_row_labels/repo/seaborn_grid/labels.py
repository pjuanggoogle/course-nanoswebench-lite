def visible_axes_labels(nrows: int, ncols: int, share_x: bool = True, share_y: bool = True) -> list[list[tuple[bool, bool]]]:
    grid = []
    for r in range(nrows):
        row = []
        for c in range(ncols):
            x_vis = (not share_x) or (r == 0)
            y_vis = (not share_y) or (c == 0)
            row.append((x_vis, y_vis))
        grid.append(row)
    return grid
