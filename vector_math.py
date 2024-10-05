def final_velocities(v1, v2, r1, r2, m1, m2):
    
    def dot_product(v1, v2):
        return v1[0] * v2[0] + v1[1] * v2[1]

    def magnitude_squared(v):
        return v[0] ** 2 + v[1] ** 2

    def scalar_multiply(scalar, v):
        return [scalar * v[0], scalar * v[1]]

    def vector_subtract(v1, v2):
        return [v1[0] - v2[0], v1[1] - v2[1]]

    def vector_add(v1, v2):
        return [v1[0] + v2[0], v1[1] + v2[1]]

    # relative position and velocity vectors
    r_rel = vector_subtract(r1, r2)
    v_rel = vector_subtract(v1, v2)

    # dot product of v_rel and r_rel, and the magnitude squared of r_rel
    dot = dot_product(v_rel, r_rel)
    mag_sq = magnitude_squared(r_rel)

    # same positions give zero div errors
    if mag_sq == 0:
        return v1, v2

    # final velocity of asteroid 1
    scalar = (2 * m2 / (m1 + m2)) * (dot / mag_sq)
    change_in_v1 = scalar_multiply(scalar, r_rel)
    v1_final = vector_subtract(v1, change_in_v1)

    # final velocity of asteroid 2
    scalar = (2 * m1 / (m1 + m2)) * (dot_product(vector_subtract(v2, v1), vector_subtract(r2, r1)) / magnitude_squared(vector_subtract(r2, r1)))
    change_in_v2 = scalar_multiply(scalar, vector_subtract(r2, r1))
    v2_final = vector_subtract(v2, change_in_v2)

    return v1_final, v2_final