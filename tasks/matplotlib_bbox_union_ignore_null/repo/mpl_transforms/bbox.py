def bbox_union(bboxes: list[tuple[float, float, float, float]]):
    if not bboxes:
        raise ValueError("bboxes cannot be empty")
    return (
        min(b[0] for b in bboxes),
        min(b[1] for b in bboxes),
        max(b[2] for b in bboxes),
        max(b[3] for b in bboxes),
    )
