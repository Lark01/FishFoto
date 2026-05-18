def get_histogram_data(image):

    min_val, max_val = get_absolute_limits(image)
    #if it is grayscale only return one histogram
    if len(image.shape) == 2:
        hist = np.histogram(
            image.ravel(),
            bins=256,
            range=(min_val, max_val)
        )[0]

        return {"gray": hist.tolist()}

    # if rgb/rgba return three/four histograms
    channels = image.shape[2]
    names = ["b", "g", "r", "a"]
    result = {}

    for i in range(channels):
        name = names[i] if i < len(names) else f"{i}"
        hist = np.histogram(image[:, :, i].ravel(),bins=256,range=(min_val, max_val))[0]
        result[name] = hist.tolist()
    return result