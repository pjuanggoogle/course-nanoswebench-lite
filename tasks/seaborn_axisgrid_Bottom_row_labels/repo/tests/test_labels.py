from seaborn_grid.labels import visible_axes_labels

def test_unshared_labels():
    assert visible_axes_labels(2, 2, share_x=False, share_y=False) == [
        [(True, True), (True, True)],
        [(True, True), (True, True)],
    ]

def test_shared_x_bottom_row_and_y_left_col():
    assert visible_axes_labels(2, 2, share_x=True, share_y=True) == [
        [(False, True), (False, False)],
        [(True, True), (True, False)],
    ]
