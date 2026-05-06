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

# this measures straight line distance based on the pixel per cm calculated above
def measure_from_points(target_p1, target_p2,
                        pixels_per_cm,
                        tree=None, points_xy=None,
                        snapping=True):

    if snapping:
        target_p1 = snap_point_kdtree(target_p1, tree, points_xy)
        target_p2 = snap_point_kdtree(target_p2, tree, points_xy)

    p3, p4 = np.array(target_p1), np.array(target_p2)

    px_dist_target = np.linalg.norm(p3 - p4)

    return px_dist_target / pixels_per_cm