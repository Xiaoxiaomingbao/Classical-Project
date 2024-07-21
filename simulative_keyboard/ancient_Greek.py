import pyperclip
import keyboard

# 本程序自带纠错功能，特别突出了鲁棒性
basic_dict = {'a': 'α', 'b': 'β', 'g': 'γ', 'd': 'δ', 'e': 'ε', 'z': 'ζ', 'j': 'η', 'i': 'ι', 'k': 'κ', 'l': 'λ',
              'm': 'μ', 'n': 'ν', 'o': 'ο', 'p': 'π', 'r': 'ρ', 's': 'σ', 't': 'τ', 'y': 'υ', 'f': 'φ', 'x': 'χ',
              'w': 'ω', 'A': 'Α', 'B': 'Β', 'G': 'Γ', 'D': 'Δ', 'E': 'Ε', 'Z': 'Ζ', 'J': 'Η', 'I': 'Ι', 'K': 'Κ',
              'L': 'Λ', 'M': 'Μ', 'N': 'Ν', 'O': 'Ο', 'P': 'Π', 'R': 'Ρ', 'S': 'Σ', 'T': 'Τ', 'Y': 'Υ', 'F': 'Φ',
              'X': 'Χ', 'W': 'Ω'}

endswith_h_dict = {'τ': 'θ', 'Τ': 'Θ', 'ρ': 'ῥ', 'Ρ': 'Ῥ'}

endswith_s_dict = {'κ': 'ξ', 'Κ': 'Ξ', 'π': 'ψ', 'Π': 'Ψ'}
# 气符 先于 扬抑符 先于 iota subscript/分音符
rough_dict = {'A': 'Ἁ', 'a': 'ἁ', 'E': 'Ἑ', 'e': 'ἑ', 'J': 'Ἡ', 'j': 'ἡ', 'I': 'Ἱ', 'i': 'ἱ', 'O': 'Ὁ', 'o': 'ὁ',
              'Y': 'Ὑ', 'y': 'ὑ', 'W': 'Ὡ', 'w': 'ὡ'}

smooth_dict = {'A': 'Ἀ', 'a': 'ἀ', 'E': 'Ἐ', 'e': 'ἐ', 'J': 'Ἠ', 'j': 'ἠ', 'I': 'Ἰ', 'i': 'ἰ', 'O': 'Ὀ', 'o': 'ὀ',
               'y': 'ὐ', 'W': 'Ὠ', 'w': 'ὠ'}

acute_dict = {'Α': 'Ά', 'α': 'ά', 'Ε': 'Έ', 'ε': 'έ', 'Η': 'Ή', 'η': 'ή', 'Ι': 'Ί', 'ι': 'ί', 'Ο': 'Ό', 'ο': 'ό',
              'Υ': 'Ύ', 'υ': 'ύ', 'Ω': 'Ώ', 'ω': 'ώ', 'Ἀ': 'Ἄ', 'ἀ': 'ἄ', 'Ἁ': 'Ἅ', 'ἁ': 'ἅ', 'Ἐ': 'Ἔ', 'ἐ': 'ἔ',
              'Ἑ': 'Ἕ', 'ἑ': 'ἕ', 'Ἠ': 'Ἤ', 'ἠ': 'ἤ', 'Ἡ': 'Ἥ', 'ἡ': 'ἥ', 'Ἰ': 'Ἴ', 'ἰ': 'ἴ', 'Ἱ': 'Ἵ', 'ἱ': 'ἵ',
              'Ὀ': 'Ὄ', 'ὀ': 'ὄ', 'Ὁ': 'Ὅ', 'ὁ': 'ὅ', 'Ὑ': 'Ὕ', 'ὐ': 'ὔ', 'ὑ': 'ὕ', 'Ὠ': 'Ὤ', 'ὠ': 'ὤ', 'Ὡ': 'Ὥ',
              'ὡ': 'ὥ'}

grave_dict = {'Α': 'Ὰ', 'α': 'ὰ', 'Ε': 'Ὲ', 'ε': 'ὲ', 'Η': 'Ὴ', 'η': 'ὴ', 'Ι': 'Ὶ', 'ι': 'ὶ', 'Ο': 'Ὸ', 'ο': 'ὸ',
              'Υ': 'Ὺ', 'υ': 'ὺ', 'Ω': 'Ὼ', 'ω': 'ὼ', 'Ἀ': 'Ἂ', 'ἀ': 'ἂ', 'Ἁ': 'Ἃ', 'ἁ': 'ἃ', 'Ἐ': 'Ἒ', 'ἐ': 'ἒ',
              'Ἑ': 'Ἓ', 'ἑ': 'ἓ', 'Ἠ': 'Ἢ', 'ἠ': 'ἢ', 'Ἡ': 'Ἣ', 'ἡ': 'ἣ', 'Ἰ': 'Ἲ', 'ἰ': 'ἲ', 'Ἱ': 'Ἳ', 'ἱ': 'ἳ',
              'Ὀ': 'Ὂ', 'ὀ': 'ὂ', 'Ὁ': 'Ὃ', 'ὁ': 'ὃ', 'Ὑ': 'Ὓ', 'ὐ': 'ὒ', 'ὑ': 'ὓ', 'Ὠ': 'Ὢ', 'ὠ': 'ὢ', 'Ὡ': 'Ὣ',
              'ὡ': 'ὣ'}

circumflex_dict = {'α': 'ᾶ', 'η': 'ῆ', 'ω': 'ῶ', 'υ': 'ῦ', 'Ἀ': 'Ἆ', 'ἀ': 'ἆ', 'Ἁ': 'Ἇ', 'ἁ': 'ἇ', 'Ἠ': 'Ἦ', 'ἠ': 'ἦ',
                   'Ἡ': 'Ἧ', 'ἡ': 'ἧ', 'Ἰ': 'Ἶ', 'ἰ': 'ἶ', 'Ἱ': 'Ἷ', 'ἱ': 'ἷ', 'Ὑ': 'Ὗ', 'ὐ': 'ὖ', 'ὑ': 'ὗ', 'Ὠ': 'Ὦ',
                   'ὠ': 'ὦ', 'Ὡ': 'Ὧ', 'ὡ': 'ὧ'}

iota_dict = {'Α': 'ᾼ', 'α': 'ᾳ', 'Ἀ': 'ᾈ', 'ἀ': 'ᾀ', 'Ἁ': 'ᾉ', 'ἁ': 'ᾁ', 'Ἂ': 'ᾊ', 'ἂ': 'ᾂ', 'Ἃ': 'ᾋ', 'ἃ': 'ᾃ',
             'Ἄ': 'ᾌ', 'ἄ': 'ᾄ', 'Ἅ': 'ᾍ', 'ἅ': 'ᾅ', 'Ἆ': 'ᾎ', 'ἆ': 'ᾆ', 'Ἇ': 'ᾏ', 'ἇ': 'ᾇ', 'ὰ': 'ᾲ', 'ᾶ': 'ᾷ',
             'ά': 'ᾴ', 'Η': 'ῌ', 'η': 'ῃ', 'Ἠ': 'ᾘ', 'ἠ': 'ᾐ', 'Ἡ': 'ᾙ', 'ἡ': 'ᾑ', 'Ἢ': 'ᾚ', 'ἢ': 'ᾒ', 'Ἣ': 'ᾛ',
             'ἣ': 'ᾓ', 'Ἤ': 'ᾜ', 'ἤ': 'ᾔ', 'Ἥ': 'ᾝ', 'ἥ': 'ᾕ', 'Ἦ': 'ᾞ', 'ἦ': 'ᾖ', 'Ἧ': 'ᾟ', 'ἧ': 'ᾗ', 'ὴ': 'ῂ',
             'ή': 'ῄ', 'Ω': 'ῼ', 'ω': 'ῳ', 'Ὠ': 'ᾨ', 'ὠ': 'ᾠ', 'Ὡ': 'ᾩ', 'ὡ': 'ᾡ', 'Ὢ': 'ᾪ', 'ὢ': 'ᾢ', 'Ὣ': 'ᾫ',
             'ὣ': 'ᾣ', 'Ὤ': 'ᾬ', 'ὤ': 'ᾤ', 'Ὥ': 'ᾭ', 'ὥ': 'ᾥ', 'Ὦ': 'ᾮ', 'ὦ': 'ᾦ', 'Ὧ': 'ᾯ', 'ὧ': 'ᾧ', 'ὼ': 'ῲ',
             'ῶ': 'ῷ', 'ώ': 'ῴ'}

diaeresis_dict = {'ῖ': 'ῗ', 'ὶ': 'ῒ', 'ί': 'ΐ', 'ῦ': 'ῧ', 'ὺ': 'ῢ', 'ύ': 'ΰ'}

special_punctuation = {';': '·', '?': ';'}


def on_key_event(e):
    global last_char
    # 检查事件是否为按键事件
    if e.event_type == keyboard.KEY_DOWN:
        if e.name == 'esc':
            exit(0)
        if len(e.name) == 1 and ('a' <= e.name <= 'z' or 'A' <= e.name <= 'Z'):
            if e.name in ['h', 's', 'H', 'S']:
                double_letter(e.name)
            elif e.name in ['u', 'v', 'c', 'U', 'V', 'C']:
                acu_gra_cir(e.name)
            else:
                basic_letter(e.name)
        elif e.name == 'space' or e.name == 'enter':
            lowercase_sigma(e.name)
        elif e.name == 'shift':
            pass
        elif e.name == '/':
            iota_diaeresis()
        elif e.name in [',', '.', ';', '?']:
            punctuate(e.name)
        else:
            last_char = ''


def basic_letter(letter):
    global last_char
    global basic_dict
    if last_char == 'h':
        add_breathing(letter, True)
        return 0
    if last_char == ' ':
        add_breathing(letter, False)
        return 0
    if letter not in list(basic_dict.keys()):
        keyboard.press_and_release('backspace')
        return 0
    character = basic_dict[letter]
    last_char = character
    pyperclip.copy(character)
    keyboard.press_and_release('backspace')
    keyboard.press_and_release('ctrl+v')


def double_letter(ends):
    global last_char
    global endswith_s_dict
    global endswith_h_dict
    if ends == 'h':
        if last_char == ' ':
            last_char = 'h'
            return 0
        if last_char not in list(endswith_h_dict.keys()):
            keyboard.press_and_release('backspace')
            return 0
        character = endswith_h_dict[last_char]
    elif ends == 'H':
        keyboard.press_and_release('backspace')
        return 0
    elif ends == 'S':
        basic_letter(ends)
        return 0
    else:
        if last_char not in list(endswith_s_dict.keys()):
            basic_letter(ends)
            return 0
        character = endswith_s_dict[last_char]
    last_char = character
    pyperclip.copy(character)
    keyboard.press_and_release('backspace')
    keyboard.press_and_release('backspace')
    keyboard.press_and_release('ctrl+v')


def add_breathing(letter, order):
    # order为真，rough breathing；为假，smooth breathing
    global last_char
    global rough_dict
    global smooth_dict
    if order:
        if letter in list(rough_dict.keys()):
            character = rough_dict[letter]
            last_char = character
            pyperclip.copy(character)
            keyboard.press_and_release('backspace')
            keyboard.press_and_release('backspace')
            keyboard.press_and_release('ctrl+v')
        else:
            keyboard.press_and_release('backspace')
            keyboard.press_and_release('backspace')
            last_char = ''
    else:
        if letter in list(smooth_dict.keys()):
            character = smooth_dict[letter]
            last_char = character
            pyperclip.copy(character)
            keyboard.press_and_release('backspace')
            keyboard.press_and_release('ctrl+v')
        else:
            last_char = ''
            basic_letter(letter)


def acu_gra_cir(letter):
    global last_char
    if letter in ['U', 'V', 'C']:
        keyboard.press_and_release('backspace')
        return 0
    if letter == 'u':
        if last_char not in list(acute_dict.keys()):
            keyboard.press_and_release('backspace')
            return 0
        character = acute_dict[last_char]
        last_char = character
    elif letter == 'v':
        if last_char not in list(grave_dict.keys()):
            keyboard.press_and_release('backspace')
            return 0
        character = grave_dict[last_char]
        last_char = character
    else:
        if last_char not in list(circumflex_dict.keys()):
            keyboard.press_and_release('backspace')
            return 0
        character = circumflex_dict[last_char]
        last_char = character
    pyperclip.copy(character)
    keyboard.press_and_release('backspace')
    keyboard.press_and_release('backspace')
    keyboard.press_and_release('ctrl+v')


def iota_diaeresis():
    global last_char
    global iota_dict
    global diaeresis_dict
    if last_char in list(iota_dict.keys()):
        character = iota_dict[last_char]
    elif last_char in list(diaeresis_dict.keys()):
        character = diaeresis_dict[last_char]
    else:
        keyboard.press_and_release('backspace')
        return 0
    last_char = character
    pyperclip.copy(character)
    keyboard.press_and_release('backspace')
    keyboard.press_and_release('backspace')
    keyboard.press_and_release('ctrl+v')


def lowercase_sigma(order):
    global last_char
    if last_char != 'σ':
        last_char = ' '
        return 0
    keyboard.press_and_release('backspace')
    keyboard.press_and_release('backspace')
    character = 'ς'
    last_char = character
    pyperclip.copy(character)
    keyboard.press_and_release('ctrl+v')
    keyboard.press_and_release(order)


def punctuate(punctuation):
    global last_char
    global special_punctuation
    if punctuation in [',', '.']:
        last_char = ''
    else:
        last_char = ''
        character = special_punctuation[punctuation]
        pyperclip.copy(character)
        keyboard.press_and_release('backspace')
        keyboard.press_and_release('ctrl+v')


# 控制和调用last_character是关键
last_char = ''
print('希腊语键盘已启动！')

# 绑定监听器到按键事件
keyboard.hook(on_key_event)

# 阻塞程序，等待按键事件
keyboard.wait('esc')
