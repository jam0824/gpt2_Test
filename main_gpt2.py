import gpt2
import model_window
import softalk


window = model_window.ModelWindow()
window.make_window(1000, 600)

marisa0 = window.add_image("image/marisa_0.png", 400, 320)
marisa1 = window.add_image("image/marisa_1.png", 400, 320)
reimu0 = window.add_image("image/reimu_0.png", 400, 320)
reimu1 = window.add_image("image/reimu_1.png", 400, 320)
balloon0 = window.add_image("image/balloonk0.png", 326, 96)
balloon1 = window.add_image("image/balloonk1.png", 326, 96)

marisa_dict = window.display_image(marisa1, 600,200, 'marisa')
reimu_dict = window.display_image(reimu1, 0,200, 'reimu')
balloon_dict = window.display_image(balloon1, 350,400, 'balloon')

window.set_marisa_dict(marisa0, marisa1, marisa_dict)
window.set_reimu_dict(reimu0, reimu1, reimu_dict)
window.set_balloon_dict(balloon0, balloon1, balloon_dict)

window.fuwa_fuwa_animation()


window.display_exit_button(750,550)

window.display_window()
