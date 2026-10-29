def linear_ticks(vmin: float, vmax: float, nbins: int = 4) -> list[float]:
    step = (vmax - vmin) / nbins
    return [round(vmin + i * step, 6) for i in range(nbins + 1)]
