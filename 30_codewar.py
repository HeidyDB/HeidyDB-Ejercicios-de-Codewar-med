def sumIntervals(intervals):
    """Suma la longitud de los intervalos, considerando las superposiciones."""
    if not intervals:
        return 0

    # Ordenar los intervalos por el inicio
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    merged_intervals = []
    current_start, current_end = sorted_intervals[0]

    for start, end in sorted_intervals[1:]:
        if start <= current_end:  # Hay superposición
            current_end = max(current_end, end)
        else:
            merged_intervals.append((current_start, current_end))
            current_start, current_end = start, end

    # Añadir el último intervalo
    merged_intervals.append((current_start, current_end))

    # Calcular la suma de las longitudes de los intervalos fusionados
    total_length = sum(end - start for start, end in merged_intervals)
    return total_length