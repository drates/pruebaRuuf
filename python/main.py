#Función para calcular máximo de paneles que caben por techo
#Compara unidades que caben en distintas orientaciones (llenando espacio sobrante)
def calculate_panels(a: int, b: int, x: int, y: int) -> int:
    """
    a, b: dimensiones del panel
    x, y: dimensiones del techo
    """
    
    def solve(a, b, x, y):
        # Validación interna de datos, si el panel no cabe en ninguna orientación, retornamos 0
        if a > x or b > y:
            if b > x or a > y:
                return 0

        # 1. Llenado en grilla (Orientación por defecto)
        # Cuántos enteros caben a lo ancho (x) y a lo alto (y)
        horizontal_count = x // a
        vertical_count = y // b
        total_grid = horizontal_count * vertical_count

        if total_grid == 0:
            return 0

        # 2. Cálculo de espacios sobrantes
        # Sobrante horizontal (tira a la derecha)
        remainder_x = x % a
        # Sobrante vertical (tira abajo)
        remainder_y = y % b

        # 3. Intentar meter paneles rotados en los espacios sobrantes
        # En el área sobrante lateral (remainder_x por el alto total y)
        extra_in_x = calculate_panels(b, a, remainder_x, y)
        
        # En el área sobrante inferior (el ancho que ya cubrió la grilla por remainder_y)
        # Usamos (x - remainder_x) para no contar dos veces la esquina
        extra_in_y = calculate_panels(b, a, x - remainder_x, remainder_y)

        return total_grid + extra_in_x + extra_in_y

    # Comparamos si conviene más empezar con el panel orientado por defecto (a, b) 
    # o rotado (b, a) desde el inicio
    return max(solve(a, b, x, y), solve(b, a, x, y))
