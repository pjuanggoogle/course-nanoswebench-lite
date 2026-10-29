from mpl_transforms.bbox import bbox_union

def test_non_empty_bboxes():
    assert bbox_union([(10, 20, 30, 40), (15, 10, 25, 50)]) == (10, 10, 30, 50)

def test_ignores_degenerate_zero_area_bbox():
    assert bbox_union([(0, 0, 0, 0), (10, 20, 30, 40)]) == (10, 20, 30, 40)
