import gpt2
import model_window

window = model_window.ModelWindow()
window.make_window(800, 600)
'''
window.display_image("image/surface0000.png", 300, 400, 500,200)
window.display_image("image/surface0010.png", 300, 400, 0,320)
window.display_image("image/balloonk0.png", 326, 96, 220,250)
window.display_image("image/balloonk1.png", 326, 96, 180,500)
'''

window.display_image("image/kyun_egao_kotti.png", 300, 400, 500,200)
window.display_image("image/main2.png", 300, 400, 30,420)

window.display_image("image/balloonk0.png", 326, 96, 220,250)
window.display_image("image/balloonk1.png", 326, 96, 180,500)


window.display_exit_button(750,550)

window.display_window()

