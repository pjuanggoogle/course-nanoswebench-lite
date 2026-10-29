from mpl_transforms.bbox import bbox_union

def test_non_empty_bboxes():
    assert bbox_union([(1, 2, 3, 4), (2, 1, 5, 6)]) == (1, 1, 5, 6)

def test_skips_degenerate_bboxes():
    assert bbox_union([(0, 0, 0, 0), (2, 3, 5, 7)]) == (2, 3, 5, 7)
    assert bbox_union([(0, 0, 0, 0)]) is None
