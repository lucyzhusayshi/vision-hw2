from uwimg import *
sys.settrace
def draw_corners():
    im = load_image("data/Rainier1.png")
    detect_and_draw_corners(im, 2, 50, 3)
    save_image(im, "corners1")
    

def draw_matches():
    a = load_image("data/Rainier1.png")
    b = load_image("data/Rainier2.png")
    m = find_and_draw_matches(a, b, 2, 50, 3)
    save_image(m, "matches1")

def easy_panorama():
    im1 = load_image("data/Rainier1.png")
    im2 = load_image("data/Rainier2.png")
    pan = panorama_image(im1, im2, thresh=50)
    save_image(pan, "easy_panorama")

def rainier_panorama():
    im1 = load_image("data/Rainier1.png")
    im2 = load_image("data/Rainier2.png")
    im3 = load_image("data/Rainier3.png")
    im4 = load_image("data/Rainier4.png")
    im5 = load_image("data/Rainier5.png")
    im6 = load_image("data/Rainier6.png")
    pan = panorama_image(im1, im2, thresh=5)
    save_image(pan, "rainier_panorama_1")
    # m = find_and_draw_matches(pan, im5,2,5,3)
    # save_image(m, "match_rainier_2")
    pan2 = panorama_image(pan, im5, thresh=5)
    save_image(pan2, "rainier_panorama_2")
    # m = find_and_draw_matches(pan2, im6,2,5,3)
    # save_image(m, "match_rainier_3")
    pan3 = panorama_image(pan2, im6, thresh=5)
    save_image(pan3, "rainier_panorama_3")
    pan4 = panorama_image(pan3, im3, thresh=5)
    save_image(pan4, "rainier_panorama_4")
    pan5 = panorama_image(pan4, im4, thresh=5)
    save_image(pan5, "rainier_panorama_5")
    # im1 = load_image("rainier_panorama_2.jpg")
    # pan = panorama_image(im1, im6, thresh=5)
    # save_image(pan, "inliers_pan3")

def field_panorama():
    im1 = load_image("data/field1.jpg")
    im2 = load_image("data/field2.jpg")
    im3 = load_image("data/field3.jpg")
    im4 = load_image("data/field4.jpg")
    im5 = load_image("data/field5.jpg")
    im6 = load_image("data/field6.jpg")
    im7 = load_image("data/field7.jpg")
    im8 = load_image("data/field8.jpg")

    im1 = cylindrical_project(im1, 1200)
    im2 = cylindrical_project(im2, 1200)
    im3 = cylindrical_project(im3, 1200)
    im4 = cylindrical_project(im4, 1200)
    im5 = cylindrical_project(im5, 1200)
    im6 = cylindrical_project(im6, 1200)
    im7 = cylindrical_project(im7, 1200)
    im8 = cylindrical_project(im8, 1200)
    save_image(im1, "cylindrical_projection")

    pan = panorama_image(im5, im6, thresh=2, iters=50000, inlier_thresh=3)
    save_image(pan, "field_panorama_1")
    pan2 = panorama_image(pan, im7, thresh=2, iters=50000, inlier_thresh=3)
    save_image(pan2, "field_panorama_2")
    pan3 = panorama_image(pan2, im8, thresh=2, iters=50000, inlier_thresh=3)
    save_image(pan3, "field_panorama_3")
    pan4 = panorama_image(pan3, im4, thresh=2, iters=50000, inlier_thresh=3)
    save_image(pan4, "field_panorama_4")
    pan5 = panorama_image(pan4, im3, thresh=2, iters=50000, inlier_thresh=3)
    save_image(pan5, "field_panorama_5")

def helens_panorama():
    im1 = load_image("data/helens1.jpg")
    im2 = load_image("data/helens2.jpg")
    im3 = load_image("data/helens3.jpg")
    im4 = load_image("data/helens4.jpg")
    im5 = load_image("data/helens5.jpg")
    im6 = load_image("data/helens6.jpg")
    pan = panorama_image(im4, im3, thresh=5)
    save_image(pan, "helens_panorama_1")
    pan2 = panorama_image(pan, im5, thresh=5)
    save_image(pan2, "helens_panorama_2")
    # pan3 = panorama_image(pan2, im6)
    # save_image(pan3, "helens_panorama_3")
    # pan4 = panorama_image(pan, im2, thresh=5, inlier_thresh=1, iters=50000)
    # save_image(pan4, "helens_panorama_4")
    # pan5 = panorama_image(im6, pan4, thresh=5)
    # save_image(pan5, "helens_panorama_5")

def sun_panorama():
    im1 = load_image("data/sun1.jpg")
    im2 = load_image("data/sun2.jpg")
    im3 = load_image("data/sun3.jpg")
    im4 = load_image("data/sun4.jpg")
    im5 = load_image("data/sun5.jpg")
    pan3 = panorama_image(im3, im4, thresh=5)
    save_image(pan3, "sun_panorama_1")
    pan5 = panorama_image(pan3, im5, thresh=5)
    save_image(pan5, "sun_panorama_2")
    pan = panorama_image(im2, im1, thresh=5)
    save_image(pan, "sun_panorama_3")
    pan2 = panorama_image(pan5, pan, thresh=5)
    save_image(pan2, "sun_panorama_4")
    pan4 = panorama_image(pan5, im2, thresh=5)
    save_image(pan4, "sun_panorama_5")

# draw_corners()
# draw_matches()
# easy_panorama()
rainier_panorama()
helens_panorama()
sun_panorama()
#field_panorama()

