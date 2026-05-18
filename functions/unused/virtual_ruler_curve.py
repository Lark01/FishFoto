# kdtree used for algorithm to snap points to edges
def build_edge_kdtree(image, low=100, high=200):
    edges = cv2.Canny(image, low, high)
    points = np.argwhere(edges > 0)

    if len(points) == 0:
        return None, None
    points_xy = np.array([(x, y) for y, x in points])
    tree = KDTree(points_xy)

    return tree, points_xy
def snap_point_kdtree(point, tree, points_xy):
    if tree is None:
        return point

    x, y = point

    dist, idx = tree.query([x, y])

    nearest = points_xy[idx]

    return (int(nearest[0]), int(nearest[1]))
#this function calculates the pixels per cm 
def compute_pixels_per_cm(ref_p1, ref_p2, ref_size_cm):
    p1, p2 = np.array(ref_p1), np.array(ref_p2)

    px_dist_ref = np.linalg.norm(p1 - p2)

    if px_dist_ref == 0:
        raise ValueError("Reference points must not be identical.")

    return px_dist_ref / ref_size_cm


#this takes three points and turn them into bezier curve points, the second point controls curve shape
def bezier_point(t, p0, p1, p2):
    return ((1 - t)**2 * p0 +2 * (1 - t) * t * p1 + t**2 * p2)

def measure_curve_bezier(p0, p1, p2,
                         pixels_per_cm,
                         tree=None, points_xy=None,
                         snapping=True,
                         samples=200):

    if snapping:
        p0 = snap_point_kdtree(p0, tree, points_xy)
        p1 = snap_point_kdtree(p1, tree, points_xy)
        p2 = snap_point_kdtree(p2, tree, points_xy)

    t_vals = np.linspace(0, 1, samples)

    curve_points = np.array([bezier_point(t,np.array(p0),np.array(p1),np.array(p2)) for t in t_vals])
    diffs = np.diff(curve_points, axis=0)
    segment_lengths = np.sqrt((diffs**2).sum(axis=1))
    px_length = np.sum(segment_lengths)

    return px_length / pixels_per_cm