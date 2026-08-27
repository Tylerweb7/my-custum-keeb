import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

# Initialize keyboard object
keyboard = KMKKeyboard()

# Configure your physical GPIO connection pins (Adjust to match your wiring)
# Raspberry Pi Pico GPIO mapping layout
keyboard.row_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4)
keyboard.col_pins = (board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18)

# Define diode direction: COL2ROW means Cathode black stripe points toward the row wires
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Core 60% ANSI Keymap layout matrix (61 Keys total)
keyboard.keymap = [
    [
        # Row 1 (14 keys)
        KC.ESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC,
        # Row 2 (14 keys)
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS,
        # Row 3 (13 keys)
        KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT,          KC.ENT,
        # Row 4 (12 keys)
        KC.LSFT,          KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH,          KC.RSFT,
        # Row 5 (8 keys configured across matrix layout positions)
        KC.LCTL, KC.LGUI, KC.LALT,                            KC.SPC,                             KC.RALT, KC.RGUI, KC.APP,  KC.RCTL
    ]
]

if __name__ == '__main__':
    keyboard.go()
