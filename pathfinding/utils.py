from PIL import Image
from IPython.display import display, HTML
from JSAnimation.IPython_display import display_animation

def render_image(img_array, display_size=(1000, 500)):
    return display(Image.fromarray(img_array, 'RGB').resize(display_size))

def render_anim(ani, **kwargs):
    return display_animation(ani)

def render_anim_to_video(ani):
    return HTML(ani.to_html5_video())
